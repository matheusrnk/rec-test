from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        # Add switches
        s0 = self.addSwitch('SW0')
        s1 = self.addSwitch('SW1')
        s2 = self.addSwitch('SW2')
        s3 = self.addSwitch('SW3')
        s4 = self.addSwitch('SW4')
        s5 = self.addSwitch('SW5')
        s6 = self.addSwitch('SW6')

        # Add hosts
        pc0 = self.addHost('PC0', ip='10.0.0.1/24')
        pc1 = self.addHost('PC1', ip='10.0.0.2/24')
        pc2 = self.addHost('PC2', ip='10.0.0.3/24')
        pc3 = self.addHost('PC3', ip='10.0.0.4/24')
        pc4 = self.addHost('PC4', ip='10.0.0.5/24')
        pc5 = self.addHost('PC5', ip='10.0.0.6/24')
        pc6 = self.addHost('PC6', ip='10.0.0.7/24')
        pc7 = self.addHost('PC7', ip='10.0.0.8/24')
        pc8 = self.addHost('PC8', ip='10.0.0.9/24')
        pc9 = self.addHost('PC9', ip='10.0.0.10/24')

        # Add links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s4)
        self.addLink(s0, s5)
        self.addLink(s0, s6)
        self.addLink(s1, s6)
        self.addLink(s2, s6)
        
        self.addLink(pc0, s1)
        self.addLink(pc1, s1)
        self.addLink(pc2, s3)
        self.addLink(pc3, s3)
        self.addLink(pc4, s4)
        self.addLink(pc5, s4)
        self.addLink(pc6, s5)
        self.addLink(pc7, s5)
        self.addLink(pc8, s2)
        self.addLink(pc9, s2)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=RemoteController, link=TCLink)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
