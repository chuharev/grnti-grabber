#!python3

import re
import xml.etree.ElementTree as etree
import xml.dom.minidom
import sys



FILENAME = sys.argv[1]

def make_xml_node(feed, number, desc, parent_id, dep='TRUE', lang='ru'):
    subject = etree.SubElement(new_feed, 'subject')

    subjectid  = etree.SubElement(subject, 'subjectid')
    subjectid.text = number

    name  = etree.SubElement(subject, 'name')
    name_item  = etree.SubElement(name, 'item')
    name_item_name  = etree.SubElement(name_item, 'name')
    name_item_name.text = desc

    name_item_lang  = etree.SubElement(name_item, 'lang')
    name_item_lang.text = lang

    parents  = etree.SubElement(subject, 'parents')
    parents_item = etree.SubElement(parents, 'item')
    parents_item.text = parent_id

    depositable = etree.SubElement(subject, 'depositable')
    depositable.text = dep


def parse_line ( line ):
    p = re.compile('\s*(\d{2})\.?(\d{2})?\.?(\d{2})?.*')
    m = p.match(line)
    indx = [m.group(i) for i in range(0, len(m.groups() ) + 1  )  ]

    level = 3 
    if indx[3] == None:
        indx[3] =  '00'
        level = 2 

    if indx[2] == None:
        indx[2] =  '00'
        level = 1 


    return indx, level



new_feed = etree.Element('subjects', encoding="utf-8")

with open(FILENAME, 'r') as f:
    lst = f.readlines()

    make_xml_node(new_feed, 'subjects', u'ГРНТИ' , 'ROOT', 'FALSE')

    for i, line in  enumerate (lst[:]):
        line1 = line.lstrip()
        if  line1.startswith("#"):
            continue

        indx, level = parse_line( line1  )

        parent_id = ''
        if indx[2] == '00' and indx[3]=='00':
            parent_id = 'subjects'
        elif indx[2] != '00' and indx[3]=='00':
            parent_id = '{0}.{1}.{2}'.format(indx[1],'00','00')
        elif indx[2] != '00' and indx[3]!='00':
            parent_id = '{0}.{1}.{2}'.format(indx[1], indx[2], '00')

        number = '{0}.{1}.{2}'.format(indx[1], indx[2], indx[3])
            
        desc = indx[0]

        dep = 'TRUE'
#        dep = 'FALSE'
#        try:
#            _, lv = parse_line ( lst[i+1])
#            #print(level, lv) 
#            if lv <= level:
#                dep = 'TRUE'
#        except:
#            pass
#
#        if indx[2] != '00' and indx[3] != '00':
#            dep = 'TRUE'

        make_xml_node(new_feed, number, desc, parent_id, dep)

    make_xml_node(new_feed, 'other', u'Другое' , 'subjects', 'TRUE')

    xml = xml.dom.minidom.parseString( etree.tostring(new_feed) )
    pretty_xml_as_string = xml.toprettyxml()
    print(pretty_xml_as_string )


