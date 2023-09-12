import xml.dom.minidom
from xml.dom.minidom import Element


xml_file = "asterix_cat062_1_18.xml"
dom = xml.dom.minidom.parse(xml_file)
root = dom.documentElement
print(root)

for DataItem in root.childNodes:
    #print(DataItem)
    if type(DataItem) is not Element:
        continue

    for DataItemFormats in DataItem.childNodes:
        if type(DataItemFormats) is not Element:
            continue
        if DataItemFormats.nodeName == "DataItemFormat":
            for DataItemFormat in DataItemFormats.childNodes:
                #print(f'DataItemFormat: {DataItemFormat}')
                VariableId = 1
                if type(DataItemFormat) is not Element:
                    continue

                if DataItemFormat.nodeName == "Fixed":
                     print(DataItemFormat.nodeName)
                     Fixed = DataItemFormat
                     for Bits in Fixed.childNodes:
                         if type(Bits) is not Element:
                             continue

                         BitsShortName = ""
                         BitsName = ""
                         for Bit in Bits.childNodes:
                             if type(Bit) is not Element:
                                 continue
                             if Bit.nodeName == "BitsShortName":

                                for text in Bit.childNodes:
                                    BitsShortName = text.nodeValue
                                    print(BitsShortName)

                             if Bit.nodeName == "BitsName":
                                  BitsName = text.nodeValue
                    # VariableId += 1


                """if DataItemFormat.nodeName == "Variable":
                    printVariable(DataItemFormat, DataItemId=DataItemId)
                if DataItemFormat.nodeName == "Compound":
                    printCompound(DataItemFormat, DataItemId=DataItemId)
                if DataItemFormat.nodeName == "Explicit":
                    printExplicit(DataItemFormat, DataItemId=DataItemId)
                        """
# category = root.getElementsByTagName('Category')[0]
# dataItemsCache[category] = category.getElementsByTagName('DataItem')
# uap = category.getElementsByTagName('UAP')[0]
# uapItemsCache[category] = uap.getElementsByTagName('UAPItem')

hex_string = "62:22:3e:5c:78:30:31:3e:5c:78:62:66:5f:5c:78:65:63:5c:78:65:36:5c:78:65:65:5c:78:30:37:52:5c:78:66:31:48:5c:78:30:30:4f:5c:78:62:30:5c:78:30:30:5c:78:30:30:5c:78:39:38:6f:20:5c:78:31:61:34:5c:78:65:37:5c:78:30:65:5c:78:61:62:5c:5c:5c:78:66:64:5c:78:64:63:5c:78:30:33:2c:5c:78:30:63:5c:78:39:36:5c:78:65:66:5c:78:30:37:5c:78:66:31:5c:78:30:65:5c:78:38:39:65:56:5c:78:31:38:40:5c:78:62:37:5c:78:64:31:58:20:5c:78:65:38:3f:5c:78:30:31:5c:78:64:34:5c:78:30:35:5c:78:66:30:5c:78:30:35:5c:78:66:30:5c:78:30:30:5c:78:38:66:5c:78:30:30:5c:78:38:35:5c:78:30:30:5c:78:30:30:5c:78:30:30:5c:78:30:30:5c:78:65:61:60:5c:78:30:38:5c:78:62:66:5c:78:30:30:5c:78:66:63:5c:78:30:30:63:5c:78:30:38:54:5c:78:30:62:5c:78:66:32:5c:78:38:31:5c:78:30:31:5c:78:30:31:49:40:30:5c:78:30:37:5c:78:30:37:5c:78:30:34:5c:78:39:30:5c:78:30:35:5c:78:30:35:5c:78:30:35:5c:78:66:30:5c:78:30:35:5c:78:66:30:5c:78:30:30:5c:78:38:32:5c:78:62:66:5f:5c:78:65:63:5c:78:65:36:5c:78:65:65:5c:78:30:37:52:5c:78:66:31:48:5c:78:30:30:4e:5c:78:30:30:60:5c:78:30:30:5c:78:39:39:5c:78:63:61:5c:78:65:30:5c:78:31:61:7e:5c:5c:5c:78:30:62:5c:78:62:39:76:5c:78:66:63:5c:78:62:37:5c:78:30:32:3f:5c:78:30:63:5c:78:39:35:5c:78:65:37:5c:78:30:37:5c:78:30:31:5c:78:30:65:5c:78:38:39:65:5c:78:62:35:5c:78:31:38:40:5c:78:62:33:5c:78:31:31:5c:78:39:38:20:5c:78:64:38:5c:78:39:66:5c:78:30:35:5c:78:66:30:5c:78:30:35:5c:78:66:30:5c:78:30:30:5c:78:61:65:5c:78:30:30:5c:78:61:34:5c:78:30:30:5c:78:66:62:5c:78:30:30:63:5c:78:30:38:54:5c:78:30:35:24:5c:78:38:31:5c:78:30:31:5c:78:30:31:49:40:30:5c:78:30:36:5c:78:30:36:5c:78:30:34:5c:78:39:30:5c:78:30:35:5c:78:30:35:5c:78:30:35:5c:78:66:31:5c:78:30:35:5c:78:66:32:5c:78:30:30:5f:5c:78:62:66:5f:5c:78:65:63:5c:78:65:36:5c:78:65:65:5c:78:30:37:52:5c:78:66:31:48:5c:78:30:30:4c:5c:78:30:32:5c:78:38:30:5c:78:30:30:5c:78:39:30:5c:78:63:36:5c:78:63:30:5c:78:31:30:42:5c:78:39:31:5c:78:30:37:5c:78:38:30:5c:78:65:63:5c:78:66:63:5c:78:30:62:5c:78:30:31:2d:5c:78:30:31:42:5c:78:63:30:5c:78:38:39:63:5c:78:66:31:54:5c:78:31:31:74:41:5c:78:39:38:20:5c:78:30:65:5c:78:65:37:5c:78:38:31:5c:78:30:31:5c:78:30:31:41:40:34:5c:78:30:36:5c:78:30:36:5c:78:66:66:5c:78:30:30:5c:78:39:30:5c:78:30:33:5c:78:30:33:5c:78:30:35:5c:78:65:62:5c:78:30:35:5c:78:65:61:5c:78:30:30:5c:78:30:30:5c:78:62:66:5f:5c:78:65:63:5c:78:65:36:5c:78:65:65:5c:78:30:37:52:5c:78:66:31:48:5c:78:30:30:4b:5c:78:39:66:5c:78:65:30:5c:78:30:30:5c:78:38:65:27:20:5c:78:31:35:36:75:5c:78:30:34:5c:78:61:30:43:5c:78:30:32:5c:78:64:62:5c:78:66:66:2a:5c:78:30:31:5c:78:63:36:5c:78:65:66:5c:78:30:37:5c:78:66:31:5c:78:30:65:5c:78:38:39:40:5c:78:39:64:5c:78:31:63:60:79:5c:78:64:66:38:20:49:5c:78:64:64:5c:78:30:31:76:5c:78:30:31:5c:78:39:30:5c:78:30:31:5c:78:39:30:5c:78:66:65:5c:78:63:64:5c:78:66:65:5c:78:63:38:5c:78:30:30:5c:78:30:30:5c:78:30:30:5c:78:30:30:4c:5c:78:62:34:5c:78:30:36:5c:78:39:64:5c:78:30:31:5c:78:31:39:5c:78:30:30:49:5c:78:30:38:52:5c:78:30:38:5c:78:38:64:5c:78:38:31:5c:78:30:31:5c:78:30:31:41:40:34:5c:78:30:37:5c:78:30:37:5c:78:66:66:5c:78:30:38:5c:78:39:30:5c:78:30:33:5c:78:30:33:5c:78:30:32:5c:78:62:39:5c:78:30:32:5c:78:62:61:5c:78:66:65:5c:78:62:31:22"
byte_list = hex_string.split(':')

# length_list = get_length()
# print((length_list))


data = b'>\x02\xfe\xbf_\xec\xe6\xee\x00R\xef\x8b\x00A\x18@\x00\x9b\x0b`\x1c\x1c\x16\xf8\x7fE\xfb\xe5\xfe\xcb\x08\x07\xef\x07\xb1\x0eq\x00`M`w\xd7x \xb3\xb0\x01\xf8\x05P\x05P\x00\x00\x00\x00\x00\x00\xb7=\tl\x01&\x00i\x08R\x06\x90\x01\x01\x01I@0\x15\x0e\x00\x90\x15\x12\x05P\x05P\x00\x00\xbf\xdf\xec\xe6\xee\x00R\xef\x8b\x00B\xfa\x80\x00\x9d\x95`#v\x17\xf8\t\xd7\x00\x11\xfc6\xf9\x00\x01v\xef\x07\xf1\x0e\x06\x80\x9bTq4\xd3X \x85\x86\x01\xde\x04\x88\x04\x88\x00W\x00\\\xfc|\x00\xfc\x84\xd0\x08R\x01:\x00_\x08R\t\x08\x01\x01\x01I@0\x15\x0e\x84\x90\x15\x12\x04\x1c\x04\x1b\x00c\xbf\xdf\xec\xe6\xee\x00R\xef\x8b\x00C\xd1\x00\x00\x9d\xd1\xa0"\xc7\xd4\xf9\x11\xc2\xffO\xfc8\x00\x01\x01n\xef\x07\xf1\x0eq|\xfa,\xe1u\xc3( \x87\xa7\x01\xe0\x05\xa0\x05\xa0\x00)\x00R\x00\x00\x00\x00\x8a\x7f\x08\x89\x013\x00`\x08R\x05\x8e\x01\x01\x01I@0\x15\x0e\x04\x90&\x12\x04[\x04[\x00P\xbf_\xec\xe6\xee\x00R\xef\x8b\x00D\xf0\xe0\x00\x9b\xdc\x00\x1c\xe7\xc3\x00\xb3-\xfc\x1d\x01\xec\x082\xef\x07\xb1\x0e\x06\xa1;ED\xb9f\x08 \xd3\xa6\x01\xf4\x05\xa0\x05\xa0\x00\n\x00\x00\x00\x00\xd5\xc7\t\x87\x01\x18\x00i\x08R\x03\x16\x01\x01\x01I@0\x17\x10\x00\x90\x17\x13\x05\xa0\x05\xa0\x00\x00\xbf_\xec\xe6\xee\x00R\xef\x8b\x00Cc\xa0\x00\x9b\xa0@#\xd4\xdb\xfd\x8ch\x02T\x00\xcb\x01/\xc0\x89l\x12\x19,q\xda\x08 \x03\xea\x01\x01\x01I@0\x17\x10\x00\x90\x17\x13\x01\x97\x01\x98\x00\x00\xbf_\xec\xe6\xee\x00R\xef\x8b\x00C\xdf@\x00\x9d\xd0\xa0\x1fZ\xe1\xff\x86\xc8\xfcK\x01\xdd\x07P\xef\x07\xf1\x0ep\xc0\xc4ED\xb6\xdbX \xd4\\\x01\xdc\x05\xf0\x05\xf0\x00\x1a\x00\x05\xff\x9c\x00\x00\xd5\xc7\t\x1a\x01\x01\x00e\x08R\x02\xba\x01\x01\x01I@0\x15\x0e\x00\x90\x15\x12\x05\xf0\x05\xf0\x00\x00\xbf_\xec\xe6\xee\x00R\xef\x8b\x00H\xc4`\x00\x9cF\x00$\xaa\x1c\x00\x9f\xc0\x02\xe3\xfd\xcb\x0b\x1e\xef\x07\xf1\x0e\t\xa0PP#\xb7\xcb\x1d\xe0\\T\x01\xe2\x05x\x05x\x00\x1a\xff\xfb\x00d\x00\x00]\xc0\x07\xf7\x01\x12\x00d\x08R\x05\xb9\x01\x01\x01I@0\x18\x10\x00\x90\x18\x13\x05w\x05x\x00\x00\xbf_\xec\xe6\xee\x00R\xef\x8b\x00F\xc0@\x00\x9b\xe8@%W\t\x01\x9bM\x03\xaa\x00\xd0\x04`\xef\x07\xb1\x0e\x06\xa0\x81ED\xb8\xe7\x0c :\xf3\x01\xee\x05x\x05x\xff\xf1\x00\x05\x00\x00:=\x087\x01\x19\x00h\x08R\x01u\x01\x01\x01I@0\x18\x10\x00\x90\x18\x13\x05x\x05y\x00\x00\xbf\xdf\xec\xe6\xee\x00R\xef\x8b\x00F\x95`\x00\x9c0`\x1f\xb3\xf1\xfdN\x17\xfeg\xfd+\x06\xfd\x01k\xef\x07\xf1\x0eq\x00*M`u\xdbx \x8fw\x01\xa0\x05\xa0\x05\xa0\x00\x80\x00\x8a\x00d\x00\x00\x95&\x07/\x011\x00O\x08R\x0c\xc7\x01\x01\x01I@0\x18\x10D\x90\x18\x13\x02\xc8\x02\xc7\x00\xd8'

p = 6
_from = 16
_to = 9
def decode_fixed(data):
    result = {}
    length = 2
    _bytes = data[p : p + length]
    print(_bytes)

    # DataItem Fixed
    bitslist = root.getElementsByTagName('Bits')

    """сдвигает двоичную цифру 1 влево на определенное количество позиций"""
    mask = (1 << (_from - _to + 1)) - 1
   # print(f'Mask: {mask}')
    """данные из _bytes преобразуются в целое число data. int.from_bytes преобразует последовательность байтов в целое 
    число. byteorder='big': Этот параметр указывает, что байты в последовательности должны интерпретироваться как 
    "большой порядок байтов" (big-endian), что означает, что старший байт идет первым. signed=False: указывает, что 
    число должно быть беззнаковым (то есть, только положительным или нулевым)"""
    data = int.from_bytes(_bytes, byteorder='big', signed=False)
    print(f"Data: {data}")

    fieldBits = ((data >> (_to - 1)) & mask)

    print("fieldBits: ", fieldBits)

decode_fixed(data)




