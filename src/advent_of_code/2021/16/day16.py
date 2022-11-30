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


def parse_n_packets(bit_data, n=1, version_sum=False):
    content = []
    for i in range(n):
        if n != 1:
            print(f'\tparsing packet {i+1}/{n}')
        version, packet_id = parse_header(bit_data)
        if version_sum:
            content.append(version)

        # literal
        if packet_id == 4:
            print(f'literal packet, version {version}')
            literal_bits = ''

            # iterate over chunks
            continue_bit = 1
            while continue_bit:
                continue_bit = bit_data[0]
                for b in bit_data[1:5]:
                    literal_bits += str(b)
                del bit_data[:5]

            if not version_sum:
                content.append(int(literal_bits, 2))

        # operator
        else:
            print(f'operator packet, version {version}')
            if not version_sum:
                content.append(f'o{packet_id}')
            length_type = bit_data[0]
            del bit_data[0]

            if length_type == 0:
                sub_packet_bit_length = bits_to_int(bit_data[:15])
                print(f'\tcontaining {sub_packet_bit_length} bits')
                del bit_data[:15]
                sub_packet_data = bit_data[:sub_packet_bit_length]

                content.append(parse_all_bits(sub_packet_data,
                                              version_sum=version_sum))
                del bit_data[:sub_packet_bit_length]

            else:
                n_sub_packets = bits_to_int(bit_data[:11])
                print(f'\tcontaining {n_sub_packets} packets')
                del bit_data[:11]
                content.append(parse_n_packets(bit_data, n=n_sub_packets,
                                               version_sum=version_sum))

    return content


def parse_all_bits(bit_data, version_sum=False):
    content = []
    while bit_data:
        content.append(parse_n_packets(bit_data, version_sum=version_sum))
    return content


def sum_up_version(content):
    s = 0
    for i in content:
        if type(i) == int:
            s += i
        else:
            s += sum_up_version(i)
    return s


def interpret_content(content):
    literals = []
    while content:
        element = content.pop(0)

        if type(element) == list:
            element = interpret_content(element)[0]

        if type(element) == int:
            literals.append(element)

        else:
            operand_content = content.pop(0)
            operands = interpret_content(operand_content)

            if element == 'o0':
                literals.append(sum(operands))

            elif element == 'o1':
                res = 1
                for i in operands:
                    res *= i
                literals.append(res)

            elif element == 'o2':
                literals.append(min(operands))

            elif element == 'o3':
                literals.append(max(operands))

            elif element == 'o5':
                literals.append(int(operands[0] > operands[1]))

            elif element == 'o6':
                literals.append(int(operands[0] < operands[1]))

            elif element == 'o7':
                literals.append(int(operands[0] == operands[1]))

    return literals


if __name__ == '__main__':
    data = load_data('input.txt')
    n_version = sum_up_version(parse_n_packets(data, version_sum=True))
    print(f'Version sum: {n_version}')

    data = load_data('input.txt')
    c = parse_n_packets(data, version_sum=False)
    interpretation = interpret_content(c)
    print(f'Message content: {interpretation[0]}')
