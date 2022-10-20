def calc_ip_rede(ip, mask):
    numeros_ip_rede = []
    for i in range(4):
        numeros_ip_rede.append(ip[i] & mask[i])
    return numeros_ip_rede


def calc_broadcast(network_ip, mask_not):
    numeros_broadcast = []
    for i in range(4):
        numeros_broadcast.append(network_ip[i] | mask_not[i])
    return numeros_broadcast


def calc_operacao_not(mask_split):
    result_list = []
    for i in range(4):
        result_list.append(~mask_split[i] & 0xFF) # 0xFF (Hexadecimal) == 255 (integer) == 11111111 (binary)
    return result_list


def join_numbers(address_split):
    list_str = [str(valor) for valor in address_split]
    result = '.'.join(list_str)
    return result


def join_binary(address_split):
    list_str = ['{:08b}'.format(valor) for valor in address_split]
    result = '.'.join(list_str)
    return result


def split_endereco_numeros(endereco):
    return [int(valor) for valor in endereco.split('.')]


def calc_first_host(network_ip_numbers):
    first_host_numbers = network_ip_numbers.copy()
    first_host_numbers[3] = first_host_numbers[3] + 1
    return first_host_numbers


def calc_last_host(broadcast_numbers):
    last_host_numbers = broadcast_numbers.copy()
    last_host_numbers[3] =  last_host_numbers[3] - 1
    return last_host_numbers


def count_numbers_bits_host(mask_split):
    quantidade_bits = join_binary(mask_split).count('0')
    return quantidade_bits


def calc_quantidade_hosts(numero_bits_hosts):
    quantidade_hosts = pow(2, numero_bits_hosts)
    return quantidade_hosts


def main():
    str_ip = input('ip: ')  # ex: 192.168.10.100
    str_mask = input('mask: ')  # ex: 255.255.255.192

    ip_split = split_endereco_numeros(str_ip)
    mask_split = split_endereco_numeros(str_mask)

    network_ip = calc_ip_rede(ip_split, mask_split)

    mask_not = calc_operacao_not(mask_split)

    broadcast = calc_broadcast(network_ip, mask_not)

    first_host = calc_first_host(network_ip)

    last_host = calc_last_host(broadcast)

    numero_bits_host = count_numbers_bits_host(mask_split)

    numero_hosts = calc_quantidade_hosts(numero_bits_host)

    print(f'IP (binário): {join_binary(ip_split)}')
    print(f'Máscara (binário): {join_binary(mask_split)}')

    print(f'\n\n------ Resultado ------')
    print(f'Número De Bits De Host Por Sub-Rede: {numero_bits_host}\n')
    
    print(f'Número de Hosts por Sub-Rede: {numero_hosts}\n')


    print(f'Endereço de Rede desta Sub-Rede: {join_numbers(network_ip)}')
    print(f'Endereço de Rede desta Sub-Rede (binário): {join_binary(network_ip)}\n')

    print(f'Máscara (Not - binário): {join_binary(mask_not)}')
    print(f'Máscara (Not): {join_numbers(mask_not)}\n')

    print(f'Endereço IPv4 do Primeiro Host nesta Sub-Rede: {join_numbers(first_host)}')
    print(f'Endereço IPv4 do Primeiro Host nesta Sub-Rede (binário): {join_binary(first_host)}\n')

    print(f'Endereço IPv4 do Último Host nesta Sub-Rede: {join_numbers(last_host)}')
    print(f'Endereço IPv4 do Último Host nesta Sub-Rede (binário): {join_binary(last_host)}\n')

    print(f'Endereço IPv4 de Broadcast nesta Sub-Rede: {join_numbers(broadcast)}')
    print(f'Endereço IPv4 de Broadcast nesta Sub-Rede (binário): {join_binary(broadcast)}\n')


if __name__ == '__main__':
    main()
