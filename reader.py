import dpkt
from asterix4py import AsterixParser


def read_pcap():
    with open('cat_62_dump.pcap', 'rb') as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                try:
                    data = eth.ip.udp.data
                   # hexdata = ":".join("{:02x}".format(ord(c)) for c in str(data))
                    a = AsterixParser(data)
                    dict_data = a.decoded
                    #print(dict_data)
                    #json_data = json.dumps(dict_data)
                except Exception as e:
                    print(e)
            return dict_data



