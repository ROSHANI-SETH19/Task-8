import json
import xml.etree.ElementTree as ET

def parse_json(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise SyntaxError(f"Invalid JSON: {e}")

def parse_xml(xml_str):
    try:
        root = ET.fromstring(xml_str)
        return {root.tag: parse_xml_element(root)}
    except ET.ParseError as e:
        raise SyntaxError(f"Invalid XML: {e}")

def parse_xml_element(element):
    if len(element) == 0:
        return element.text.strip()
    else:
        return {child.tag: parse_xml_element(child) for child in element}

def to_json(data):
    if isinstance(data, dict):
        return json.dumps(data)
    elif isinstance(data, list):
        return json.dumps(data)
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")

def to_xml(data):
    if isinstance(data, dict):
        root = ET.Element("root")
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        return ET.tostring(root, encoding="unicode")
    elif isinstance(data, list):
        root = ET.Element("root")
        for value in data:
            child = ET.SubElement(root, "item")
            child.text = str(value)
        return ET.tostring(root, encoding="unicode")
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")

def convert(data_str, from_format, to_format):
    if from_format == "json":
        data = parse_json(data_str)
    elif from_format == "xml":
        data = parse_xml(data_str)
    else:
        raise ValueError(f"Unsupported format: {from_format}")

    if to_format == "json":
        return to_json(data)
    elif to_format == "xml":
        return to_xml(data)
    else:
        raise ValueError(f"Unsupported format: {to_format}")

# Example usage:
json_str = '{"name": "John", "age": 30}'
xml_str = convert(json_str, "json", "xml")
print(xml_str)

xml_str = '<root><name>John</name><age>30</age></root>'
json_str = convert(xml_str, "xml", "json")
print(json_str)