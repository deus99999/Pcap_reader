import dpkt
from asterix4py import AsterixParser


def convert_hex_to_dec(hexdata):
    output = ""
    for i in range(0, len(hexdata), 2):
        sub_str = hexdata[i] + hexdata[i + 1]
        output += convert_hex_to_dec(sub_str)
    output += chr(int(hex, 16))
    return output

def get_bytes_data_from_xml():
    with open('cat_62_dump.pcap', 'rb') as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                try:
                    data = eth.ip.udp.data
                    # hexdata = ":".join("{:02x}".format(ord(c)) for c in str(data))
                    # print(f'Parsing packet: {hexdata}')
                    print(data)




                    a = AsterixParser(data)
                    print(a.decoded)
                except Exception as e:
                    print(e)
            print("\n#####################\n")
            return data



print(get_bytes_data_from_xml())