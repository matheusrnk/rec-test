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
    net = Mininet(switch=OVSSwitch,controller=RemoteController, autoStaticArp=True)
    
    info('*** Adicionando o Controlador\n' )
    c1 = RemoteController('c1', ip='127.0.0.1', port=6653)
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
    pc0 = net.addHost('PC0', mac='1e:0b:fa:73:69:f1')
    pc1 = net.addHost('PC1', mac='1e:0b:fa:73:69:f2')
    pc2 = net.addHost('PC2', mac='1e:0b:fa:73:69:f3')
    pc3 = net.addHost('PC3', mac='1e:0b:fa:73:69:f4')
    pc4 = net.addHost('PC4', mac='1e:0b:fa:73:69:f5')
    pc5 = net.addHost('PC5', mac='1e:0b:fa:73:69:f6')
    pc6 = net.addHost('PC6', mac='1e:0b:fa:73:69:f7')
    pc7 = net.addHost('PC7', mac='1e:0b:fa:73:69:f8')
    pc8 = net.addHost('PC8', mac='1e:0b:fa:73:69:f9')
    pc9 = net.addHost('PC9', mac='1e:0b:fa:73:69:fa')

        # Add links
    net.addLink(s0, s1)
    net.addLink(s0, s2)
    net.addLink(s0, s3)
    net.addLink(s0, s4)
    net.addLink(s0, s5)
    net.addLink(s0, s6)
    net.addLink(s1, s6)
    net.addLink(s2, s6)
        
    net.addLink(pc0, s1)
    net.addLink(pc1, s1)
    net.addLink(pc2, s3)
    net.addLink(pc3, s3)
    net.addLink(pc4, s4)
    net.addLink(pc5, s4)
    net.addLink(pc6, s5)
    net.addLink(pc7, s5)
    net.addLink(pc8, s2)
    net.addLink(pc9, s2)
    
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
