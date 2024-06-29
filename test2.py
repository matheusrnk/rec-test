from mininet.net import Mininet
from mininet.node import Controller, Host, Switch
from mininet.cli import CLI
from mininet.link import Link

def my_network():
    net = Mininet(controller=Controller)

    # Create Switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    # Create Hosts
    h1 = net.addHost('h1', ip='10.0.0.1/24', defaultRoute='yes')  # Assuming specific IP for h1
    h2 = net.addHost('h2', ip='10.0.0.2/24', defaultRoute='yes')  # Assuming specific IP for h2
    h3 = net.addHost('h3', ip='10.0.1.1/24', defaultRoute='yes')  # Assuming specific IP for h3
    h4 = net.addHost('h4', ip='10.0.1.2/24', defaultRoute='yes')  # Assuming specific IP for h4
    pc_pt = net.addHost('pc_pt', ip='10.0.2.1/24', defaultRoute='yes')  # Assuming specific IP for pc_pt

    # Create Links - Refer to your diagram for specific connections
    net.addLink(s1, h1)
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s2, s4)
    net.addLink(s2, s5)
    net.addLink(s3, s6)
    net.addLink(s4, h2)
    net.addLink(s5, h3)
    net.addLink(s6, h4)
    net.addLink(s4, pc_pt)  # Assuming PC_PT connects to s4

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    my_network()
