def ip_to_octets(ip_address):
    octets = ip_address.split('.')
    return [int(octet) for octet in octets]

def octets_to_ip(octets):
    return '.'.join(str(octet) for octet in octets)

def network_address(ip_address, subnet_mask):
    ip_octets = ip_to_octets(ip_address)
    mask_octets = ip_to_octets(subnet_mask)
    network_octets = [ip_octets[i] & mask_octets[i] for i in range(4)]
    return octets_to_ip(network_octets)

def broadcast_address(ip_address, subnet_mask):
    ip_octets = ip_to_octets(ip_address)
    mask_octets = ip_to_octets(subnet_mask)
    inverted_mask_octets = [255 - octet for octet in mask_octets]
    broadcast_octets = [ip_octets[i] | inverted_mask_octets[i] for i in range(4)]
    return octets_to_ip(broadcast_octets)

def host_count(subnet_mask):
    mask_octets = ip_to_octets(subnet_mask)
    inverted_mask_octets = [255 - octet for octet in mask_octets]
    host_count = 1
    for octet in inverted_mask_octets:
        host_count *= (octet + 1)
    return host_count - 2

print('Calculadora ip Recurso Educativo Digital para la materia Redes de Computadora. ITSSNA')
ip_address = input("Ingrese una direccion ip ejemplo 192.168.0.1: ")
subnet_mask = input("Ingrese la mascara de red ejemplo 255.255.255.0: ")

#ip_address = '192.168.1.1'
#subnet_mask = '255.255.254.0'

print('Dirección IP:', ip_address)
print('Máscara de subred:', subnet_mask)
print('Dirección de red:', network_address(ip_address, subnet_mask))
print('Dirección de difusión:', broadcast_address(ip_address, subnet_mask))
print('Cantidad de direcciones de host disponibles:', host_count(subnet_mask))
