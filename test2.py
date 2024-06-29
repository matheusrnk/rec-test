from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Host, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class MultiSwitchTopology(Topo):
    def build(self):
        # Adding switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')

        # Adding hosts
        host1 = self.addHost('h1', ip='10.0.0.1/24')
        host2 = self.addHost('h2', ip='10.0.0.2/24')
        host3 = self.addHost('h3', ip='10.0.0.3/24')
        host4 = self.addHost('h4', ip='10.0.0.4/24')

        # Creating links between switches
        self.addLink(switch1, switch2, cls=TCLink, bw=10)
        self.addLink(switch1, switch3, cls=TCLink, bw=10)
        self.addLink(switch2, switch3, cls=TCLink, bw=10)

        # Creating links between hosts and switches
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch3)

def run():
    topo = MultiSwitchTopology()
    net = Mininet(topo=topo, controller=None, autoSetMacs=True)

    # Starting the network
    net.start()

    # Open Mininet CLI for testing
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
