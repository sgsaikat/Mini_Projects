import xml.etree.ElementTree as ET
import pandas as pd

xml_file = 'xml_2_df.xml'
data = []

try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for items in root.findall('Results_from_Database_Query_ODBC'):
        tags = dict()
        for item in items:
            tags[item.tag] = item.text
        data.append(tags)
except Exception as err:
    print(err)

data = pd.DataFrame(data)
data.to_csv('xml_2_df.csv', index=None)
print(data.head())
