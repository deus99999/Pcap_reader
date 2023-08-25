import dpkt
from read_xml import get_length


with open('cat_62_dump.pcap', 'rb') as pcap_file:
    pcap = dpkt.pcap.Reader(pcap_file)

    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)

        #  contains the payload of the Ethernet frame
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            tcp = ip.data
            # tcp must be <class 'dpkt.udp.UDP'> not bytes
            if not isinstance(tcp, bytes):
                tcp_payload = tcp.data
                print(f"Payload: {tcp_payload}")
                data_parts = ["{:02X}".format(ord(b)) for b in str(tcp_payload)]  # byte to hex
                hex_string = ":".join(data_parts)
                print(hex_string)

                # import binascii
                # hex_string = binascii.hexlify(tcp_payload).decode("utf-8")
                # print(hex_string)


        print("\n#####################\n")



