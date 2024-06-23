from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

class SDNTopo(Topo):
    def build(self):
        # Add hosts
        hosts = []
        for i in range(10):
            host = self.addHost(f'PC{i}')
            hosts.append(host)

        # Add switches
        sw = []
        for i in range(7):
            switch = self.addSwitch(f'SW{i}')
            sw.append(switch)

        # Add links between hosts and switches
        self.addLink(hosts[0], sw[1])
        self.addLink(hosts[1], sw[1])
        self.addLink(hosts[2], sw[3])
        self.addLink(hosts[3], sw[3])
        self.addLink(hosts[4], sw[4])
        self.addLink(hosts[5], sw[4])
        self.addLink(hosts[6], sw[5])
        self.addLink(hosts[7], sw[5])
        self.addLink(hosts[8], sw[2])
        self.addLink(hosts[9], sw[2])

        # Add links between switches
        self.addLink(sw[0], sw[1])
        self.addLink(sw[0], sw[3])
        self.addLink(sw[0], sw[4])
        self.addLink(sw[0], sw[5])
        self.addLink(sw[0], sw[6])
        self.addLink(sw[1], sw[6])
        self.addLink(sw[2], sw[6])

def run():
    topo = SDNTopo()
    net = Mininet(topo=topo, controller=RemoteController, link=TCLink)

    # Add remote controller
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
