import xmltodict
import json


def dict_from_sml(xml_file):
    with open(xml_file, 'r') as xml_file:
        xml_data = xml_file.read()
        xml_dict = xmltodict.parse(xml_data)
        # json_data = json.dumps(xml_dict, indent=4)

    return xml_dict


def get_length():
    json = dict_from_sml('asterix_cat062_1_18.xml')
    item_dict = (json["Category"]["DataItem"])

    byte_length = []

    for item in item_dict:
        data_item_format = item["DataItemFormat"]
        print(data_item_format)

        if 'Variable' in data_item_format:
            fixed = data_item_format['Variable']['Fixed']
            if isinstance(fixed, dict):
                length = fixed['@length']
                print('___ ', length)
                byte_length.append(length)
            if isinstance(fixed, list):
                length = fixed[0]['@length']
                print("=== ", length)
                byte_length.append(length)

        if 'Fixed' in data_item_format:
            length = data_item_format['Fixed']['@length']
            print("%%% ", length)
            byte_length.append(length)

        if 'Compound' in data_item_format:
            variable = data_item_format['Compound']['Variable']

            if isinstance(variable, dict):
                fixed = variable['Fixed']
                if isinstance(fixed, dict):
                    length = fixed['@length']
                    print("--- ", length)
                    byte_length.append(length)
                if isinstance(fixed, list):
                    length = fixed[0]['@length']
                    print("--- ", length)
                    byte_length.append(length)

            if isinstance(variable, list):
                fixed = variable[0]
                if isinstance(fixed, dict):
                    length = fixed['Fixed']
                    length = length[0]['@length']
                    print("---- ", length)
                    byte_length.append(length)

        if 'Explicit' in data_item_format:
            ixplicit = data_item_format['Explicit']
            if 'Compound' in ixplicit:
                compound = ixplicit['Compound']
                variable = compound['Variable']
                fixed = variable['Fixed']
                length = fixed['@length']
                print("... ", length)
                byte_length.append(length)

            if 'Fixed' in ixplicit:
                fixed = ixplicit['Fixed']
                length = fixed['@length']
                print('+++ ', length)
                byte_length.append(length)

    print(len(byte_length))
    print(byte_length)
    return byte_length

get_length()
