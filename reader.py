import dpkt
from asterix4py import AsterixParser


def get_bytes_data_from_pcap():
    with open('../Pcap_reader/cat_62_dump.pcap', 'rb') as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                try:
                    data = eth.ip.udp.data
                    hexdata = ":".join("{:02x}".format(ord(c)) for c in str(data))
                except Exception as e:
                    print(e)
            return data


a = AsterixParser(get_bytes_data_from_pcap())
res = a.decoded
print(res)