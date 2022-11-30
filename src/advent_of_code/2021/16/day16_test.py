from day16 import *


def test_hex_conversion():
    assert load_data('D2FE28') == [int(i) for i in '110100101111111000101000']


def test_version_sum_1():
    data = load_data('8A004A801A8002F478')
    assert sum_up_version(parse_n_packets(data, version_sum=True)) == 16


def test_version_sum_operator_ltype1():
    data = load_data('EE00D40C823060')
    assert sum_up_version(parse_n_packets(data, version_sum=True)) == 14


def test_version_sum_3():
    data = load_data('620080001611562C8802118E34')
    assert sum_up_version(parse_n_packets(data, version_sum=True)) == 12


def test_sum():
    data = load_data('C200B40A82')
    assert interpret_content(parse_n_packets(data))[0] == 3


def test_product():
    data = load_data('04005AC33890')
    assert interpret_content(parse_n_packets(data))[0] == 54


def test_maximum():
    data = load_data('CE00C43D881120')
    assert interpret_content(parse_n_packets(data))[0] == 9

def test_greater_than():
    data = load_data('F600BC2D8F')
    assert interpret_content(parse_n_packets(data))[0] == 0


def test_combined():
    data = load_data('9C0141080250320F1802104A08')
    assert interpret_content(parse_n_packets(data))[0] == 1
