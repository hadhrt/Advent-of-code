import timeit


class Packet_parser:

    def __init__(self, hex_transmission):
        bitlen = len(hex_transmission)*4
        self.transmission = bin(int(hex_transmission, 16))[2:].zfill(bitlen)

    def parse_packet(self):
        version = int(self.readbits(3), 2)
        id = int(self.readbits(3), 2)

        # literal packet
        if id == 4:
            return self.parse_literal_packet(version, id)
        else:
            return self.parse_operator_packet(version, id)

    def parse_literal_packet(self, version, id):
        literal = ""
        # read until bitgroup without "1" prefix
        while self.readbits(1) == "1":
            literal += self.readbits(4)
        # read last bitgroup
        literal += self.readbits(4)
        return Literal_Packet(version, id, int(literal, 2))

    def parse_operator_packet(self, version, id):
        subpackets = []
        lengh_type_id = self.readbits(1)
        if lengh_type_id == "0":
            bit_length = int(self.readbits(15), 2)
            target_transmission_length = len(self.transmission) - bit_length
            while len(self.transmission) > target_transmission_length:
                subpackets.append(self.parse_packet())
            if target_transmission_length != len(self.transmission):
                raise IndexError("Too many bit read from transmission while parsing subpackets")
        elif lengh_type_id == "1":
            num_packets = int(self.readbits(11), 2)
            for i in range(num_packets):
                subpackets.append(self.parse_packet())
        else:
            raise ValueError("Invalid lengh_type_id")
        return Operator_Packet(version, id, subpackets.copy())


    def readbits(self, num_bits):
        if len(self.transmission) < num_bits:
            raise EOFError("EOF reached while reading transmission")
        ret = self.transmission[:num_bits]
        self.transmission = self.transmission[num_bits:]
        return ret


class Packet:
    def __init__(self, version, id):
        self.version = version
        self.id = id
    def get_version_sum(self):
        return self.version
    def get_decoded_value(self):
        raise NotImplementedError("Generic Packets have no decoded value")
        return 0

class Literal_Packet(Packet):
    def __init__(self, version, id, value):
        super().__init__(version, id)
        self.value = value
    def get_decoded_value(self):
        return self.value

class Operator_Packet(Packet):
    def __init__(self, version, id, subpackets):
        super().__init__(version, id)
        self.subpackets = subpackets
    def get_version_sum(self):
        version_sum = self.version
        for packet in self.subpackets:
            version_sum += packet.get_version_sum()
        return version_sum
    def get_decoded_value(self):
        match self.id:
            case 0:
                #sum packet
                return sum([packet.get_decoded_value() for packet in self.subpackets])
            case 1:
                #product packet
                product = 1
                for packet in self.subpackets:
                    product *= packet.get_decoded_value()
                return product
            case 2:
                #minimum packet
                return min([packet.get_decoded_value() for packet in self.subpackets])  
            case 3:
                #maximum packet
                return max([packet.get_decoded_value() for packet in self.subpackets])
            case 5:
                #greater than packet
                if len(self.subpackets) != 2:
                    raise IndexError("Number of subpackets is not 2: {len(self.subpackets)}")
                if self.subpackets[0].get_decoded_value() > self.subpackets[1].get_decoded_value():
                    return 1
                else:
                    return 0    
            case 6:
                #less than packet
                if len(self.subpackets) != 2:
                    raise IndexError("Number of subpackets is not 2: {len(self.subpackets)}")
                if self.subpackets[0].get_decoded_value() < self.subpackets[1].get_decoded_value():
                    return 1
                else:
                    return 0    
            case 7:
                #equal to packet
                if len(self.subpackets) != 2:
                    raise IndexError("Number of subpackets is not 2: {len(self.subpackets)}")
                if self.subpackets[0].get_decoded_value() == self.subpackets[1].get_decoded_value():
                    return 1
                else:
                    return 0    
            case _:
                raise ValueError(f"Unknown Packet ID: {self.id}")
        

def p1(lines):
    values = 0
    for line in lines:
        pp = Packet_parser(line)
        outer_packet = pp.parse_packet()
    return outer_packet.get_version_sum()


def p2(lines):
    values = 0
    for line in lines:
        pp = Packet_parser(line)
        outer_packet = pp.parse_packet()
    return outer_packet.get_decoded_value()


f = open("input16.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
