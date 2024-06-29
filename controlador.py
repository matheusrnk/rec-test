#!/usr/bin/env python

import socket
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet

class SimpleForwardingController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SimpleSwitch13, self).__init__(*args, **kwargs)
        # Bind the controller to a specific IP and port
        self.bind_controller()

    def bind_controller(self):
        try:
            # Specify the IP address and port here
            ip_address = '0.0.0.0'  # Listen on all interfaces
            port_number = 6633  # Default OpenFlow port
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((ip_address, port_number))
            server_socket.listen(1)
            print(f'Ryu controller bound to {ip_address}:{port_number}')
        except Exception as e:
            print(f'Failed to bind Ryu controller: {str(e)}')

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, MAIN_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.datapath
        ofproto = datapath.ofproto
        parser = datapath.parser

        # Install the table-miss flow entry.
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=0,
                                commands=parser.OFPFC_ADD, match=match,
                                actions=actions)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.parser
        in_port = msg.match['in_port']
        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocol(ethernet.ethernet)

        if eth is None:
            return

        dst = eth.dst
        src = eth.src

        # Simple forwarding logic: forward to the next hop towards the destination
        # This is a very basic example and might need adjustments based on your topology
        if dst[0] == '10':
            out_port = 1  # Assuming port 1 leads to the next hop towards the destination
        else:
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]
        mod = parser.OFPFlowMod(datapath=datapath, cookie=0,
                                priority=1, match=parser.OFPMatch(in_port=in_port, eth_type=eth.ethertype, eth_dst=dst),
                                actions=actions)
        datapath.send_msg(mod)
