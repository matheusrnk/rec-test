from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Add switches
    s0 = net.addSwitch('SW0')
    s1 = net.addSwitch('SW1')
    s2 = net.addSwitch('SW2')
    s3 = net.addSwitch('SW3')
    s4 = net.addSwitch('SW4')
    s5 = net.addSwitch('SW5')
    s6 = net.addSwitch('SW6')

    # Add hosts with specific IPs
    pc0 = net.addHost('PC0', ip='10.0.1.1/24')
    pc1 = net.addHost('PC1', ip='10.0.1.2/24')
    pc2 = net.addHost('PC2', ip='10.0.2.1/24')
    pc3 = net.addHost('PC3', ip='10.0.2.2/24')
    pc4 = net.addHost('PC4', ip='10.0.3.1/24')
    pc5 = net.addHost('PC5', ip='10.0.3.2/24')
    pc6 = net.addHost('PC6', ip='10.0.4.1/24')
    pc7 = net.addHost('PC7', ip='10.0.4.2/24')
    pc8 = net.addHost('PC8', ip='10.0.5.1/24')
    pc9 = net.addHost('PC9', ip='10.0.5.2/24')

    # Add links
    net.addLink(s0, s1)
    net.addLink(s0, s2)
    net.addLink(s0, s3)
    net.addLink(s0, s4)
    net.addLink(s0, s5)
    net.addLink(s0, s6)
    net.addLink(s1, s6)
    net.addLink(s2, s6)
    
    net.addLink(pc0, s1)
    net.addLink(pc1, s1)
    net.addLink(pc2, s3)
    net.addLink(pc3, s3)
    net.addLink(pc4, s4)
    net.addLink(pc5, s4)
    net.addLink(pc6, s5)
    net.addLink(pc7, s5)
    net.addLink(pc8, s2)
    net.addLink(pc9, s2)

    # Add Ryu controller
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    # Start Mininet
    net.start()

    # Start the Ryu controller
    for switch in net.switches:
        switch.start([c0])

    # Configure default routes for the hosts
    pc0.cmd('ip route add default via 10.0.1.254 dev pc0-eth0')
    pc1.cmd('ip route add default via 10.0.1.254 dev pc1-eth0')
    pc2.cmd('ip route add default via 10.0.2.254 dev pc2-eth0')
    pc3.cmd('ip route add default via 10.0.2.254 dev pc3-eth0')
    pc4.cmd('ip route add default via 10.0.3.254 dev pc4-eth0')
    pc5.cmd('ip route add default via 10.0.3.254 dev pc5-eth0')
    pc6.cmd('ip route add default via 10.0.4.254 dev pc6-eth0')
    pc7.cmd('ip route add default via 10.0.4.254 dev pc7-eth0')
    pc8.cmd('ip route add default via 10.0.5.254 dev pc8-eth0')
    pc9.cmd('ip route add default via 10.0.5.254 dev pc9-eth0')

    # Open Mininet CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
