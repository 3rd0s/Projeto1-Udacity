# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

#função para contagem de tags presentes
def count_tags(filename):
    dicionario=defaultdict(int)
    for event, elem in ET.iterparse(filename):
        dicionario[elem.tag]+=1
    return dicionario


#analisar as tags presentes
tags = count_tags('GrandeFortaleza.osm')
pprint.pprint(tags)
 
