from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(controller=RemoteController)

    # Adding controller
    c0 = net.addController('c0', port=6633)

    # Adding switches
    switch0 = net.addSwitch('s0')
    switch1 = net.addSwitch('s1')
    switch2 = net.addSwitch('s2')
    switch3 = net.addSwitch('s3')
    switch4 = net.addSwitch('s4')
    switch5 = net.addSwitch('s5')
    switch6 = net.addSwitch('s6')

    # Adding hosts
    hosts = []
    for i in range(10):
        host = net.addHost(f'h{i}')
        hosts.append(host)

    # Adding links between switches
    net.addLink(switch6, switch0)
    net.addLink(switch6, switch1)
    net.addLink(switch6, switch2)
    net.addLink(switch0, switch3)
    net.addLink(switch0, switch4)
    net.addLink(switch0, switch5)
    net.addLink(switch0, switch1)
    net.addLink(switch0, switch2)

    # Adding links between switches and hosts
    net.addLink(switch1, hosts[0])
    net.addLink(switch1, hosts[1])
    net.addLink(switch3, hosts[2])
    net.addLink(switch3, hosts[3])
    net.addLink(switch4, hosts[4])
    net.addLink(switch4, hosts[5])
    net.addLink(switch5, hosts[6])
    net.addLink(switch5, hosts[7])
    net.addLink(switch2, hosts[8])
    net.addLink(switch2, hosts[9])

    net.build()
    c0.start()
    switch0.start([c0])
    switch1.start([c0])
    switch2.start([c0])
    switch3.start([c0])
    switch4.start([c0])
    switch5.start([c0])
    switch6.start([c0])

    net.startTerms()

    CLI(net)

    net.stop()

if __name__ == '__main__':
    #setLogLevel('info')
    create_topology()
