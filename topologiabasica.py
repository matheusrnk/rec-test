#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class Topologia(Topo):
    def build(self, **_opts):
        
        # routers
        r0 = self.addHost('R0', cls=LinuxRouter, ip='10.0.0.1/24')
        r1 = self.addHost('R1', cls=LinuxRouter, ip='10.1.0.1/24')
        r2 = self.addHost('R2', cls=LinuxRouter, ip='10.2.0.1/24')
        r3 = self.addHost('R3', cls=LinuxRouter, ip='10.3.0.1/24')
        r4 = self.addHost('R4', cls=LinuxRouter, ip='10.4.0.1/24')
        r5 = self.addHost('R5', cls=LinuxRouter, ip='10.5.0.1/24')
        r6 = self.addHost('R6', cls=LinuxRouter, ip='10.6.0.1/24')
        
        # switches
        s0 = self.addSwitch('SW0')
        s1 = self.addSwitch('SW1')
        s2 = self.addSwitch('SW2')
        s3 = self.addSwitch('SW3')
        s4 = self.addSwitch('SW4')
        s5 = self.addSwitch('SW5')
        s6 = self.addSwitch('SW6')
        
        # adding switch to router
        self.addLink(s0, r0, params2={'ip': '10.0.0.1/24'})
        self.addLink(s1, r1, params2={'ip': '10.1.0.1/24'})
        self.addLink(s2, r2, params2={'ip': '10.2.0.1/24'})
        self.addLink(s3, r3, params2={'ip': '10.3.0.1/24'})
        self.addLink(s4, r4, params2={'ip': '10.4.0.1/24'})
        self.addLink(s5, r5, params2={'ip': '10.5.0.1/24'})
        self.addLink(s6, r6, params2={'ip': '10.6.0.1/24'})
        
        # adding route-to-router connection
        self.addLink(r0, r1, params1={'ip': '10.100.0.1/24'}, params2={'ip': '10.100.0.2/24'})
        self.addLink(r0, r3, params1={'ip': '10.101.0.1/24'}, params2={'ip': '10.101.0.2/24'})
        self.addLink(r0, r4, params1={'ip': '10.102.0.1/24'}, params2={'ip': '10.102.0.2/24'})
        self.addLink(r0, r5, params1={'ip': '10.103.0.1/24'}, params2={'ip': '10.103.0.2/24'})
        self.addLink(r0, r6, params1={'ip': '10.104.0.1/24'}, params2={'ip': '10.104.0.2/24'})
        self.addLink(r1, r6, params1={'ip': '10.105.0.1/24'}, params2={'ip': '10.105.0.2/24'})
        self.addLink(r2, r6, params1={'ip': '10.106.0.1/24'}, params2={'ip': '10.106.0.2/24'})

        # Hosts
        pc0 = self.addHost('PC0', ip='10.1.0.250/24', defaultRoute='via 10.1.0.1')
        pc1 = self.addHost('PC1', ip='10.1.0.251/24', defaultRoute='via 10.1.0.1')
        pc2 = self.addHost('PC2', ip='10.3.0.250/24', defaultRoute='via 10.3.0.1')
        pc3 = self.addHost('PC3', ip='10.3.0.251/24', defaultRoute='via 10.3.0.1')
        pc4 = self.addHost('PC4', ip='10.4.0.250/24', defaultRoute='via 10.4.0.1')
        pc5 = self.addHost('PC5', ip='10.4.0.251/24', defaultRoute='via 10.4.0.1')
        pc6 = self.addHost('PC6', ip='10.5.0.250/24', defaultRoute='via 10.5.0.1')
        pc7 = self.addHost('PC7', ip='10.5.0.251/24', defaultRoute='via 10.5.0.1')
        pc8 = self.addHost('PC8', ip='10.2.0.250/24', defaultRoute='via 10.2.0.1')
        pc9 = self.addHost('PC9', ip='10.2.0.251/24', defaultRoute='via 10.2.0.1')

        # Links
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
    topo = Topologia()
    net = Mininet(topo=topo)

    info(net['R0'].cmd("ip route add 10.1.0.0/24 via 10.100.0.2 dev R0-eth1"))
    info(net['R0'].cmd("ip route add 10.3.0.0/24 via 10.101.0.2 dev R0-eth2"))
    info(net['R0'].cmd("ip route add 10.4.0.0/24 via 10.102.0.2 dev R0-eth3"))
    info(net['R0'].cmd("ip route add 10.5.0.0/24 via 10.103.0.2 dev R0-eth4"))
    info(net['R0'].cmd("ip route add 10.6.0.0/24 via 10.104.0.2 dev R0-eth5"))
    info(net['R1'].cmd("ip route add 10.6.0.0/24 via 10.105.0.2 dev R1-eth2"))
    info(net['R2'].cmd("ip route add 10.6.0.0/24 via 10.106.0.2 dev R2-eth2"))

    net.start()
    CLI(net)
    net.stop()

#topos = {'topo_basica': (lambda: Topologia())}
if __name__ == '__main__':
    setLogLevel('info')
    run()