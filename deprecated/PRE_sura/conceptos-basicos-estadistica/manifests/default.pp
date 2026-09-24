##
## Los paquetes listados abajo son instalados usando
##
##    apt-get install  nombre-paquete
##

package {['python3-pip']:
    ensure => present,
}

##
## Los paquetes de Python listados abajo son instalados usando
##
##    pip3 install nombre-paquete
##
package {['jupyter',
          'jupyterlab']:
    ensure   => present,
    provider => 'pip3',
}
