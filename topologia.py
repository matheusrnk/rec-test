from miniself.topo import Topo
from miniself.link import TCLink


class Topologia(Topo):

    def build(self):

         # Add switches
        s0 = self.addSwitch('SW0')
        s1 = self.addSwitch('SW1')
        s2 = self.addSwitch('SW2')
        s3 = self.addSwitch('SW3')
        s4 = self.addSwitch('SW4')
        s5 = self.addSwitch('SW5')
        s6 = self.addSwitch('SW6')

        # Add hosts with specific IPs
        pc0 = self.addHost('PC0')
        pc1 = self.addHost('PC1')
        pc2 = self.addHost('PC2')
        pc3 = self.addHost('PC3')
        pc4 = self.addHost('PC4')
        pc5 = self.addHost('PC5')
        pc6 = self.addHost('PC6')
        pc7 = self.addHost('PC7')
        pc8 = self.addHost('PC8')
        pc9 = self.addHost('PC9')

        # Add links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s4)
        self.addLink(s0, s5)
        self.addLink(s0, s6)
        self.addLink(s1, s6)
        self.addLink(s2, s6)
        
        self.addLink(pc0, s1, cls=TCLink)
        self.addLink(pc1, s1, cls=TCLink)
        self.addLink(pc2, s3, cls=TCLink)
        self.addLink(pc3, s3, cls=TCLink)
        self.addLink(pc4, s4, cls=TCLink)
        self.addLink(pc5, s4, cls=TCLink)
        self.addLink(pc6, s5, cls=TCLink)
        self.addLink(pc7, s5, cls=TCLink)
        self.addLink(pc8, s2, cls=TCLink)
        self.addLink(pc9, s2, cls=TCLink)
            
topos = {
    'topologia': (lambda: Topologia()),
}