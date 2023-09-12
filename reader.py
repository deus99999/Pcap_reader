import dpkt
from read_xml import get_length
from asterix4py import AsterixParser

with open('cat_62_dump.pcap', 'rb') as pcap_file:
    pcap = dpkt.pcap.Reader(pcap_file)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if isinstance(eth.data, dpkt.ip.IP):
            try:
                data = eth.ip.udp.data
                print("Data:", data)
                hexdata = ":".join("{:02x}".format(ord(c)) for c in str(data))
                #print(f'Parsing packet: {hexdata}')



                a = AsterixParser(data)
                print(a.decoded)
            except Exception as e:
                print(e)

        print("\n#####################\n")



