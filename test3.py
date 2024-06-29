from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_full_topology():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, link=TCLink)

    # Adding Ryu controller
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    # Adding switches
    switch0 = net.addSwitch('s0', protocols='OpenFlow13')
    switch1 = net.addSwitch('s1', protocols='OpenFlow13')
    switch2 = net.addSwitch('s2', protocols='OpenFlow13')
    switch3 = net.addSwitch('s3', protocols='OpenFlow13')
    switch4 = net.addSwitch('s4', protocols='OpenFlow13')
    switch5 = net.addSwitch('s5', protocols='OpenFlow13')
    switch6 = net.addSwitch('s6', protocols='OpenFlow13')

    # Adding hosts
    hosts = []
    for i in range(10):
        host = net.addHost(f'h{i}')
        hosts.append(host)

    # Adding links between switches
    net.addLink(switch6, switch0)
    net.addLink(switch6, switch1)
    net.addLink(switch6, switch2)
    net.addLink(switch0, switch3)
    net.addLink(switch0, switch4)
    net.addLink(switch0, switch5)
    net.addLink(switch0, switch1)
    net.addLink(switch0, switch2)

    # Adding links between switches and hosts
    net.addLink(switch1, hosts[0])
    net.addLink(switch1, hosts[1])
    net.addLink(switch3, hosts[2])
    net.addLink(switch3, hosts[3])
    net.addLink(switch4, hosts[4])
    net.addLink(switch4, hosts[5])
    net.addLink(switch5, hosts[6])
    net.addLink(switch5, hosts[7])
    net.addLink(switch2, hosts[8])
    net.addLink(switch2, hosts[9])

    # Start the network
    net.start()

    # Enable STP
    for switch in [switch0, switch1, switch2, switch3, switch4, switch5, switch6]:
        switch.cmd('ovs-vsctl set Bridge %s stp_enable=true' % switch.name)

    # Running CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_full_topology()
