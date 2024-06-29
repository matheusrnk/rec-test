from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.1.0.1/24')
        h4 = self.addHost('h4', ip='10.1.0.2/24')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=RemoteController, link=TCLink)
    net.start()
    
    # Add routes for hosts on different subnets to communicate
    h1, h2, h3, h4 = net.get('h1', 'h2', 'h3', 'h4')
    h1.cmd('route add -net 10.1.0.0/24 gw 10.0.0.254')
    h2.cmd('route add -net 10.1.0.0/24 gw 10.0.0.254')
    h3.cmd('route add -net 10.0.0.0/24 gw 10.1.0.254')
    h4.cmd('route add -net 10.0.0.0/24 gw 10.1.0.254')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
