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
    pc0 = net.addHost('PC0')
    pc1 = net.addHost('PC1')
    pc2 = net.addHost('PC2')
    pc3 = net.addHost('PC3')
    pc4 = net.addHost('PC4')
    pc5 = net.addHost('PC5')
    pc6 = net.addHost('PC6')
    pc7 = net.addHost('PC7')
    pc8 = net.addHost('PC8')
    pc9 = net.addHost('PC9')

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

    # Open Mininet CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
