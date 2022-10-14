def calculate_network_ip(ip, mask):
    result_list = []
    for i in range(4):
        result_list.append(ip[i] & mask[i])
    return result_list


def calculate_broadcast(network_ip, mask_not):
    result_list = []
    for i in range(4):
        result_list.append(network_ip[i] | mask_not[i])
    return result_list


def calculate_not_operation(mask_split):
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


def split_numbers(address):
    return [int(valor) for valor in address.split('.')]


def main():
    str_ip = input('ip: ')  # ex: 192.168.10.100
    str_mask = input('mask: ')  # ex: 255.255.255.192

    ip_split = split_numbers(str_ip)
    mask_split = split_numbers(str_mask)

    network_ip = calculate_network_ip(ip_split, mask_split)

    mask_not = calculate_not_operation(mask_split)

    broadcast = calculate_broadcast(network_ip, mask_not)

    print(f'\n\n------ Resultado ------')
    print(f'IP (binário): {join_binary(ip_split)}')
    print(f'Máscara (binário): {join_binary(mask_split)}\n')

    print(f'IP da rede: {join_numbers(network_ip)}')
    print(f'IP da rede (binário): {join_binary(network_ip)}\n')

    print(f'Máscara (Not - binário): {join_binary(mask_not)}')
    print(f'Máscara (Not): {join_numbers(mask_not)}\n')

    print(f'Broadcast: {join_numbers(broadcast)}')
    print(f'Broadcast (binário): {join_binary(broadcast)}')


if __name__ == '__main__':
    main()
