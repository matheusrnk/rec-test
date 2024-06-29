from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import TCLink
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        h5 = self.addHost('h5', ip='10.1.0.1/24')
        h6 = self.addHost('h6', ip='10.1.0.2/24')
        h7 = self.addHost('h7', ip='10.1.0.3/24')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s2)
        self.addLink(h6, s3)
        self.addLink(h7, s3)
        self.addLink(s1, s2)
        self.addLink(s2, s3)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=Controller, link=TCLink)
    net.start()
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
