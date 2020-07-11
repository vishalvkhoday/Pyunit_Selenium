import xml.etree.ElementTree as ET

tree = ET.parse("C:/Users/DELL/Desktop/20Micro.xml")
root = tree.getroot()

for child in root:

    tempTag = str(child.tag)
    tempTag = tempTag.strip("}")
    
    tempAttr = str(child.attrib)
    print(child.tag,child.text)