def load_data(f):
    try:
        with open(f) as file:
            hex_data = file.readline().strip()

    except FileNotFoundError:
        hex_data = f

    bit_data = []
    for h in hex_data:
        decimal = int(h, 16)
        bits = format(decimal, '04b')
        for b in bits:
            bit_data.append(int(b))

    return bit_data


def bits_to_int(bit_data):
    bit_string = ''
    for b in bit_data:
        bit_string += str(b)
    return int(bit_string, 2)


def parse_header(bit_data):
    version = bits_to_int(bit_data[:3])
    packet_id = bits_to_int(bit_data[3:6])
    del bit_data[:6]
    return version, packet_id


def parse_n_packets(bit_data, n=1, return_version_sum=False):
    version_sum = 0
    for i in range(n):
        if n != 1:
            print(f'\tparsing packet {i+1}/{n}')
        version, packet_id = parse_header(bit_data)
        version_sum += version

        # literal
        if packet_id == 4:
            print(f'Literal packet, version {version}')
            literal_bits = ''

            # iterate over chunks
            continue_bit = 1
            while continue_bit:
                continue_bit = bit_data[0]
                for b in bit_data[1:5]:
                    literal_bits += str(b)
                del bit_data[:5]

            # for now: do nothing with it
            literal = int(literal_bits, 2)

        # operator
        else:
            print(f'Operator packet, version {version}')
            length_type = bit_data[0]
            del bit_data[0]

            if length_type == 0:
                sub_packet_bit_length = bits_to_int(bit_data[:15])
                print(f'\tcontaining {sub_packet_bit_length} bits')
                del bit_data[:15]
                sub_packet_data = bit_data[:sub_packet_bit_length]

                version_sum += parse_all_bits(sub_packet_data,
                                              return_version_sum=return_version_sum)
                del bit_data[:sub_packet_bit_length]

            else:
                n_sub_packets = bits_to_int(bit_data[:11])
                print(f'\tcontaining {n_sub_packets} packets')
                del bit_data[:11]
                version_sum += parse_n_packets(bit_data, n=n_sub_packets,
                                               return_version_sum=return_version_sum)

    if return_version_sum:
        return version_sum


def parse_all_bits(bit_data, return_version_sum=False):
    version_sum = 0
    while bit_data:
        version_sum += parse_n_packets(bit_data, return_version_sum=return_version_sum)
    if return_version_sum:
        return version_sum


if __name__ == '__main__':
    data = load_data('input.txt')
    n_version = parse_n_packets(data, return_version_sum=True)
    print(f'Version sum: {n_version}')
