from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    # Create the network with default controller and OVS switches
    net = Mininet(controller=Controller, switch=OVSSwitch, autoStaticArp=True)
    
    info('*** Adding the Controller\n')
    c0 = net.addController('c0')
    
    # Add switches
    s0 = net.addSwitch('s0')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    # Add hosts
    pc0 = net.addHost('pc0')
    pc1 = net.addHost('pc1')
    pc2 = net.addHost('pc2')
    pc3 = net.addHost('pc3')
    pc4 = net.addHost('pc4')
    pc5 = net.addHost('pc5')
    pc6 = net.addHost('pc6')
    pc7 = net.addHost('pc7')
    pc8 = net.addHost('pc8')
    pc9 = net.addHost('pc9')

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
    
    info('*** Starting the Network\n')
    net.build()
    
    info('*** Starting the Controller\n')
    c0.start()

    info('*** Starting the switches\n')
    s0.start([c0])
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])
    s5.start([c0])
    s6.start([c0])
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
