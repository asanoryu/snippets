from lxml import etree
from sys import argv, exit
"""
    xml format
    <functions>
        <xml_tag1>function_arg</xml_tag1>
        <xml_tag2>function_arg2</xml_tag2>
    </functions>
"""
xml_file = 'funcs.xml'
def function_for_xml_tag_1(xml_tag1_value):
    pass

def function_for_xml_tag_2(xml_tag2_value):
    pass

_mapping = {
    'xml_tag1' : function_for_xml_tag_1,
    'xml_tag2' : function_for_xml_tag_2,
  }


map_xml = etree.parse(xml_file)
for func in map_xml.iter():
    if not func.tag  == 'functions' and func.tag is not etree.Comment:
        print('Call {} with {} '.format(func.tag, func.text), end='')
        try:
            _mapping[func.tag](func.text)
        except KeyError as e:
            print(': Don\'t know what to call: {}'.format(func.tag))
        except Exception as e:
            print('\nError {}'.format(e))
        