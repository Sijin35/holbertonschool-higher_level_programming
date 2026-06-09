#!/usr/bin/python3
"""Module that serializes and deserializes with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    with open(filename, "r", encoding="utf-8") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
