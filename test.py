from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


def myNetwork():
    net = Mininet(switch=OVSSwitch, autoSetMacs=True, autoStaticArp=True)
    
    info('*** Adicionando o Controlador\n' )
    c1 = Controller('c1', ip='10.0.0.1', port=6653)
    net.addController(c1)
 
    # Add switches
    s0 = net.addSwitch('SW0', OVSSwitch)
    s1 = net.addSwitch('SW1', OVSSwitch)
    s2 = net.addSwitch('SW2', OVSSwitch)
    s3 = net.addSwitch('SW3', OVSSwitch)
    s4 = net.addSwitch('SW4', OVSSwitch)
    s5 = net.addSwitch('SW5', OVSSwitch)
    s6 = net.addSwitch('SW6', OVSSwitch)

    # Add hosts
    pc0 = net.addHost('PC0')
    pc1 = net.addHost('PC1')
    pc2 = net.addHost('PC2')
    pc3 = net.addHost('PC3')
    pc4 = net.addHost('PC4')
    pc5 = net.addHost('PC5')
    pc6 = net.addHost('PC6')
    pc7 = net.addHost('PC7')
    pc8 = net.addHost('PC8')
    pc9 = net.addHost('PC9')

        # Add links
    net.addLink(s0, s1, cls=TCLink)
    net.addLink(s0, s2, cls=TCLink)
    net.addLink(s0, s3, cls=TCLink)
    net.addLink(s0, s4, cls=TCLink)
    net.addLink(s0, s5, cls=TCLink)
    net.addLink(s0, s6, cls=TCLink)
    net.addLink(s1, s6, cls=TCLink)
    net.addLink(s2, s6, cls=TCLink)
        
    net.addLink(pc0, s1, cls=TCLink)
    net.addLink(pc1, s1, cls=TCLink)
    net.addLink(pc2, s3, cls=TCLink)
    net.addLink(pc3, s3, cls=TCLink)
    net.addLink(pc4, s4, cls=TCLink)
    net.addLink(pc5, s4, cls=TCLink)
    net.addLink(pc6, s5, cls=TCLink)
    net.addLink(pc7, s5, cls=TCLink)
    net.addLink(pc8, s2, cls=TCLink)
    net.addLink(pc9, s2, cls=TCLink)
    
    info('*** Iniciando a Rede\n')
    net.build()
    
    info('*** Iniciando o Controlador\n')
    c1.start()

    info('*** Iniciando os switches\n')
    s1.start([c1])
    s2.start([c1])
    s3.start([c1])
    s4.start([c1])
    s5.start([c1])
    s6.start([c1])
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
