# Compares two XML files and returns true if they have the same elements with the same data and attributes, but not
# necessarily in the same order

import sys
import io
import xml.etree.ElementTree as ET
import xmltodict
import json
import dicttoxml
from xml.dom.minidom import parseString
import xml.etree.cElementTree as ET


# Makes sure all lists in the dictionary are sorted, at all levels of depth
def sort_dict(d):
  for k, v in d.items():
    if isinstance(v, dict):
      d[k] = sort_dict(v)
    elif isinstance(v, list):
      for i in range(len(v)):
        if isinstance(v[i], dict):
          v[i] = sort_dict(v[i])

      d[k] = sorted(v)

  return d



def compare_xml_files(xmlfile1, xmlfile2):
  # Parse files
  xmlstr1 = open(xmlfile1, 'r').read()
  xmlstr2 = open(xmlfile2, 'r').read()

  # Turn the strings into dicts
  xmldict1 = json.loads(json.dumps(xmltodict.parse(xmlstr1, process_namespaces=True)))
  xmldict2 = json.loads(json.dumps(xmltodict.parse(xmlstr2, process_namespaces=True)))

  # Sort the dictionaries for comparison
  xmldict1 = sort_dict(xmldict1)
  # print xmldict1
  xml = pretty_print_xmls(xmldict1)
  create_file("temp1.xml",xml)
  xmldict2 = sort_dict(xmldict2)
  # print xmldict2
  xml = pretty_print_xmls(xmldict2)
  create_file("temp2.xml",xml)
  # dict_diff(xmldict1,xmldict2)
  # Compare the two dictionaries
  

def dict_diff(first, second):
    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    # Check all keys in first dict
    for key in first.keys():
        if (not second.has_key(key)):
            diff[key] = (first[key], KEYNOTFOUND)
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second.keys():
        if (not first.has_key(key)):
            diff[key] = (KEYNOTFOUND, second[key])
    
    for key in diff.keys():
    	print diff[key]
    	print '\n'

def pretty_print_xmls(xmldict):
	xml = dicttoxml.dicttoxml(xmldict, attr_type=False)
	return xml
	# print xml
	# dom = parseString(xml)
	# print(xml.toprettyxml())

def create_file(filename,content):
	with io.FileIO(filename, "w") as file:
    		file.write(content)

if __name__ == "__main__":
  print(compare_xml_files(sys.argv[1], sys.argv[2]))
