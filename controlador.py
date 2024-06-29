#!/usr/bin/env python

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet

class SimpleForwardingController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SimpleForwardingController, self).__init__(*args, **kwargs)

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
