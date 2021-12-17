from day16 import *


def test_hex_conversion():
    assert load_data('D2FE28') == [int(i) for i in '110100101111111000101000']


def test_version_sum_1():
    data = load_data('8A004A801A8002F478')
    assert parse_n_packets(data, return_version_sum=True) == 16


def test_version_sum_operator_ltype1():
    data = load_data('EE00D40C823060')
    assert parse_n_packets(data, return_version_sum=True) == 14


def test_version_sum_3():
    data = load_data('620080001611562C8802118E34')
    assert parse_n_packets(data, return_version_sum=True) == 12

