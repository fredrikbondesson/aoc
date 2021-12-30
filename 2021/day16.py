import util
from operator import add, mul, gt, lt, eq


hex_binary = {
'0' :'0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111',
}

def get_packet_version(binary_str):
    return binary_str[0:3]

def get_packet_type_id(binary_str):
    return binary_str[3:3+3]

def get_packets(binary_str):
    buf=[]

    for i in range(6, len(binary_str), 5):
        print(i, binary_str[i:i+5])
        buf.append(binary_str[i+1:i+5])

        if binary_str[i:i+1] == '0':
            print('The end')
            break

    return ''.join(buf)


def get_packets_as_decimal(packets_str):
    return int(packets_str, 2)

def get_length_type_id(binary_str):
    return binary_str[6:6+1]

def get_sub_packet_length(binary_str):
    return binary_str[7:7+15]

def get_first_sub_packet(binary_str):
    return binary_str[22:22+11]

def get_second_sub_packet(binary_str):
    return binary_str[33:33+16]

def hex_to_binary(hex_str):
    buf = []
    for char in hex_str:
        # print(hex_binary[char])
        buf.append(hex_binary[char])
    return ''.join(buf)

def get_number_of_sub_packets(packet):
    return packet[7:7+11]

def get_literal_sum(binary_str):
    done = False
    start = 6
    buf = []
    while not done:
        ls = binary_str[start:start+5]
        buf.append(ls[1:])

        if ls[0] == '0':
            done = True
        start += 5

    return int(''.join(buf), 2), len(buf)

pos = 0
versions = []

def parse(binary):
    global pos
    global versions
    pos = 0
    versions = []
    print(f'parse {binary}')
    return parse_next(binary)

ops = add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq

def parse_next(binary_str):
    global pos
    global versions
    binary = binary_str[pos:]
    print(f'parse: {binary}')
    print(f'pos={pos}')
    total = 0

    print(f'Version: {get_packet_version(binary)} {int(get_packet_version(binary), 2)}')
    versions.append(int(get_packet_version(binary), 2))
    
    packet_type_id = get_packet_type_id(binary)
    print(f'Packet Type Id: {packet_type_id} {int(packet_type_id, 2)}')
    if packet_type_id == '100': # 4
        literals, nr_of_literals = get_literal_sum(binary)
        pos += 3 + 3 + 5 * nr_of_literals
        total = literals
        # print(f'Total4: {total}')
    else:
        print(f'get_length_type_id: {get_length_type_id(binary)}')
        # if packet_type_id == '000': # 000
        #     print('SUM:')
        # elif packet_type_id == '001': # 001
        #     print('PRODUCT:')
        # elif packet_type_id == '010': # 010
        #     print('MINUMUM:')
        # elif packet_type_id == '011': # 011
        #     print('MAXIMUM:')
        # elif packet_type_id == '101': # 101
        #     print('GT:')
        # elif packet_type_id == '110': # 110
        #     print('LT:')
        # elif packet_type_id == '111': # 111
        #     print('EQUAL:')
        if get_length_type_id(binary) == '0':
            length = int(get_sub_packet_length(binary), 2)
            print(f'Sub Packet Length: {length} int: {length}')
            pos += 22 # 3+3+1+15
            read_until = pos + length
            total = parse_next(binary_str)
            # print(f'Total0->1: {total}')
            while pos < read_until:
                res2 = parse_next(binary_str)
                # print(f'Total0->2: {res2}')
                total = ops[int(packet_type_id, 2)](total, res2)

            # print(f'Total0->3: {total}')

        elif get_length_type_id(binary) == '1':
            nr = get_number_of_sub_packets(binary)
            print(f'Number of sub packets: {nr} {int(nr, 2)}')
            pos += 18 # 3+3+1+11
            total = parse_next(binary_str)
            # print(f'Total1->1: {total}')
            for i in range(int(nr, 2) - 1):
                res2 = parse_next(binary_str)
                # print(f'Total1->2: {res2}')
                total = ops[int(packet_type_id, 2)](total, res2)

            # print(f'Total1->3: {total}')
        else:
            print('Should not happen')
            assert False

    print(f'Returning total: {total}')
    return total

# 38006F45291200
# 00111000000000000110111101000101001010010001001000000000
packet = '00111000000000000110111101000101001010010001001000000000'
assert get_packet_version(packet) == '001'
assert get_packet_type_id(packet) == '110'
assert get_length_type_id(packet) == '0'
assert get_sub_packet_length(packet) == '000000000011011'
assert get_first_sub_packet(packet) == '11010001010'
assert get_second_sub_packet(packet) == '0101001000100100'


# EE00D40C823060
# 11101110000000001101010000001100100000100011000001100000
packet = '11101110000000001101010000001100100000100011000001100000'
assert get_packet_version(packet) == '111'
assert get_packet_type_id(packet) == '011'
assert get_length_type_id(packet) == '1'
nr_of_sub_packets = get_number_of_sub_packets(packet)
assert int(nr_of_sub_packets, 2) == 3


def main():
    global versions
    global pos

    def more_tests():
        # EE00D40C823060
        # 11101110000000001101010000001100100000100011000001100000
        binary = hex_to_binary('EE00D40C823060')
        assert binary == '11101110000000001101010000001100100000100011000001100000'

        # D2FE28 
        # 110100101111111000101000
        # VVVTTTAAAAABBBBBCCCCC
        binary = '110100101111111000101000'
        assert get_packet_version(binary) == '110'
        assert get_packet_type_id(binary) == '100'

        literals,_ = get_literal_sum(binary)
        print(f'Literals: {literals}')
        assert literals == 2021

        total = parse(binary)
        print(versions)
        print(sum(versions))
        assert sum(versions) == 6

        hex = '8A004A801A8002F478'
        print(hex)
        # 100010100000000001001010100000000001101010000000000000101111010001111000
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        assert sum(versions) == 16, f'{sum(versions)} != 16'

        hex = 'C0015000016115A2E0802F182340'
        print(hex)
        binary = hex_to_binary(hex)
        print(binary)

        hex = 'A0016C880162017C3686B18A3D4780'
        print(hex)
        binary = hex_to_binary(hex)
        print(binary)

        hex = '620080001611562C8802118E34'
        # 01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100
        print(hex)
        binary = hex_to_binary(hex)
        assert binary == '01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100'
        total = parse(binary)
        print(versions)
        print(sum(versions))
        assert sum(versions) == 12, f'{sum(versions)} != 12'

        # C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
        hex='C200B40A82'
        print(hex)
        # 1100001000000000101101000000101010000010
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        assert sum(versions) == 14, f'{sum(versions)} != 14'
        print(total)
        assert total == 3, f'{total} != 3'

        hex = '04005AC33890'
        print(hex)
        # 000001000000000001011010110000110011100010010000
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        assert sum(versions) == 8, f'{sum(versions)} != 8'
        print(total)
        assert total == 54, f'{total} != 54'

        hex = '880086C3E88112'
        print(hex)
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        assert sum(versions) == 15, f'{sum(versions)} != 15'
        print(total)
        assert total == 7, f'{total} != 7'

        hex='CE00C43D881120'
        print(hex)
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        #assert sum(versions) == 15, f'{sum(versions)} != 15'
        print(total)
        assert total == 9, f'{total} != 9'

        hex = 'D8005AC2A8F0'
        print(hex)
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        #assert sum(versions) == 15, f'{sum(versions)} != 15'
        print(total)
        assert total == 1, f'{total} != 1'

        hex= '9C0141080250320F1802104A08'
        print(hex)
        binary = hex_to_binary(hex)
        total = parse(binary)
        print(versions)
        print(sum(versions))
        #assert sum(versions) == 15, f'{sum(versions)} != 15'
        print(total)
        assert total == 1, f'{total} != 1'

    more_tests()
    
    data = util.read_data('2021/day16.txt')
    binary = hex_to_binary(data[0])
    total = parse(binary)
    print(f'total: {total}')
    print(versions)
    print(sum(versions))
    assert sum(versions) == 860, f'{sum(versions)} != 860'
    assert total == 470949537659


if __name__ == '__main__':
    main()