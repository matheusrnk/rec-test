from mininet.cli import CLI
from mininet.net import Mininet
import mininet.link
import mininet.log
import mininet.node
import time
import csv
import os

mininet.log.info('\n*** Initialize Mininet\n')

net = Mininet(build=False, controller=mininet.node.RemoteController, link=mininet.link.TCLink, topo=None)
cli = CLI(net, script='/dev/null')

mininet.log.info('\n*** Add nodes\n')

c1 = net.addController('c1', controller=mininet.node.RemoteController, ip='127.0.0.1', port=6653)
PC0 = net.addHost('PC0', ip='127.0.0.2')
PC1 = net.addHost('PC1', ip='127.0.0.3')
PC2 = net.addHost('PC2', ip='127.0.0.4')
PC3 = net.addHost('PC3', ip='127.0.0.5')
PC4 = net.addHost('PC4', ip='127.0.0.6')
PC5 = net.addHost('PC5', ip='127.0.0.7')
PC6 = net.addHost('PC6', ip='127.0.0.8')
PC7 = net.addHost('PC7', ip='127.0.0.9')
PC8 = net.addHost('PC8', ip='127.0.0.10')
PC9 = net.addHost('PC9', ip='127.0.0.11')
sw0 = net.addSwitch('sw0', cls=mininet.node.OVSSwitch)
sw1 = net.addSwitch('sw1', cls=mininet.node.OVSSwitch)
sw2 = net.addSwitch('sw2', cls=mininet.node.OVSSwitch)
sw3 = net.addSwitch('sw3', cls=mininet.node.OVSSwitch)
sw4 = net.addSwitch('sw4', cls=mininet.node.OVSSwitch)
sw5 = net.addSwitch('sw5', cls=mininet.node.OVSSwitch)
sw6 = net.addSwitch('sw6', cls=mininet.node.OVSSwitch)

mininet.log.info('\n*** Add links\n')

net.addLink(sw6, sw0, intfName1='sw6-eth2', intfName2='sw0-eth0')
net.addLink(sw0, sw1, intfName1='sw0-eth1', intfName2='sw1-eth3')
net.addLink(sw0, sw2, intfName1='sw0-eth5', intfName2='sw2-eth1')
net.addLink(sw3, sw0, intfName1='sw3-eth5', intfName2='sw0-eth2')
net.addLink(sw4, sw0, intfName1='sw4-eth0', intfName2='sw0-eth3')
net.addLink(sw5, sw0, intfName1='sw5-eth0', intfName2='sw0-eth4')
net.addLink(PC8, sw2, intfName1='PC8-eth0', intfName2='sw2-eth2')
net.addLink(PC9, sw2, intfName1='PC9-eth0', intfName2='sw2-eth3')
net.addLink(PC2, sw3, intfName1='PC2-eth1', intfName2='sw3-eth1')
net.addLink(PC3, sw3, intfName1='PC3-eth0', intfName2='sw3-eth2')
net.addLink(PC4, sw4, intfName1='PC4-eth1', intfName2='sw4-eth2')
net.addLink(PC5, sw4, intfName1='PC5-eth1', intfName2='sw4-eth4')
net.addLink(PC6, sw5, intfName1='PC6-eth0', intfName2='sw5-eth1')
net.addLink(PC7, sw5, intfName1='PC7-eth0', intfName2='sw5-eth3')
net.addLink(sw1, sw6, intfName1='sw1-eth5', intfName2='sw6-eth0')
net.addLink(sw1, PC0, intfName1='sw1-eth0', intfName2='PC0-eth0')
net.addLink(sw1, PC1, intfName1='sw1-eth4', intfName2='PC1-eth0')
net.addLink(sw2, sw6, intfName1='sw2-eth0', intfName2='sw6-eth8')

mininet.log.info('\n*** Build the network\n')

net.build()

mininet.log.info('\n*** Start controllers\n')

c1.start()

mininet.log.info('\n*** Start switches\n')

sw0.start([])
sw1.start([c1])
sw2.start([c1])
sw3.start([])
sw4.start([])
sw5.start([])
sw6.start([c1])

mininet.log.info('\n*** Run global startup commands\n')

mininet.log.debug('[mininet]> pingall\n')
cli.onecmd('pingall')

def run_ping_tests(net):
    hosts = net.hosts
    with open('ping_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['source', 'destination', 'min_rtt', 'avg_rtt', 'max_rtt', 'mdev_rtt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for src in hosts:
            for dst in hosts:
                if src != dst:
                    ping_result = src.cmd('ping -c 4 %s' % dst.IP())
                    # Parse the ping_result here to extract the desired metrics
                    # This is just an example of the output parsing; adjust as needed
                    min_rtt, avg_rtt, max_rtt, mdev_rtt = ping_result.split('/')[-3:]
                    writer.writerow({
                        'source': src.name,
                        'destination': dst.name,
                        'min_rtt': min_rtt,
                        'avg_rtt': avg_rtt,
                        'max_rtt': max_rtt,
                        'mdev_rtt': mdev_rtt
                    })

def run_iperf_tests(net):
    hosts = net.hosts
    with open('iperf_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['source', 'destination', 'bandwidth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for src in hosts:
            for dst in hosts:
                if src != dst:
                    dst.cmd('iperf -s &')
                    iperf_result = src.cmd('iperf -c %s -t 10' % dst.IP())
                    dst.cmd('kill %iperf')
                    # Parse the iperf_result here to extract the desired metrics
                    # This is just an example of the output parsing; adjust as needed
                    bandwidth = iperf_result.split(' ')[-2]
                    writer.writerow({
                        'source': src.name,
                        'destination': dst.name,
                        'bandwidth': bandwidth
                    })

def run_tshark_tests(net):
    hosts = net.hosts
    if not os.path.exists('tshark_results'):
        os.makedirs('tshark_results')

    for src in hosts:
        for dst in hosts:
            if src != dst:
                capture_file = 'tshark_results/%s_to_%s.pcap' % (src.name, dst.name)
                src.cmd('tshark -i %s-eth0 -w %s &' % (src.name, capture_file))
                time.sleep(1)
                src.cmd('ping -c 10 %s' % dst.IP())
                time.sleep(1)
                src.cmd('kill %tshark')

                tshark_result = src.cmd('tshark -r %s -q -z io,stat,0' % capture_file)
                # Parse the tshark_result here to extract the desired metrics
                # This is just an example of the output parsing; adjust as needed
                packet_loss = tshark_result.split(' ')[-2]
                with open('tshark_results.csv', 'a', newline='') as csvfile:
                    fieldnames = ['source', 'destination', 'packet_loss']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({
                        'source': src.name,
                        'destination': dst.name,
                        'packet_loss': packet_loss
                    })

mininet.log.info('\n*** Run tests\n')

run_ping_tests(net)
run_iperf_tests(net)
run_tshark_tests(net)

mininet.log.info('\n*** Start CLI\n')

CLI(net)

mininet.log.info('\n*** Finish\n')

net.stop()
