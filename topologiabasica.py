from mininet.topo import Topo
from mininet.node import Node

class Topologia(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Hosts
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

        # routers
        r0 = self.addNode('R0', cls=Node, name='router0')
        r1 = self.addNode('R1')
        r2 = self.addNode('R2')
        r3 = self.addNode('R3')
        r4 = self.addNode('R4')
        r5 = self.addNode('R5')
        r6 = self.addNode('R6')

        # Links
        self.addLink(pc0, r1)
        self.addLink(pc1, r1)
        self.addLink(pc2, r3)
        self.addLink(pc3, r3)
        self.addLink(pc4, r4)
        self.addLink(pc5, r4)
        self.addLink(pc6, r5)
        self.addLink(pc7, r5)
        self.addLink(pc8, r2)
        self.addLink(pc9, r2)

        self.addLink(r0, r1)
        self.addLink(r0, r3)
        self.addLink(r0, r4)
        self.addLink(r0, r5)
        self.addLink(r0, r6)
        self.addLink(r1, r6)
        self.addLink(r2, r6)

topos = {'topo_basica': (lambda: Topologia())}