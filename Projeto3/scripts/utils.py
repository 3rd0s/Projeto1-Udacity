#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:04:28 2017

@author: william2
"""

import os
statinfo=os.stat("GrandeFortaleza.osm")
print "osm: "+str(statinfo.st_size/1024/1024) + "MB"
statinfo=os.stat("GrandeFortaleza.db")
print "database: "+str(statinfo.st_size/1024/1024) + "MB"
statinfo=os.stat("ways_nodes.csv")
print "ways_nodes.csv: "+str(statinfo.st_size/1024/1024) + "MB"
statinfo=os.stat("ways.csv")
print "ways.csv: "+str(statinfo.st_size/1024/1024) + "MB"
statinfo=os.stat("ways_tags.csv")
print "ways_tags.csv: "+str(statinfo.st_size/1024/1024) + "MB"
statinfo=os.stat("nodes_tags.csv")
print "nodes_tags.csv: "+str(statinfo.st_size/1024/1024) + "MB"
statinfo=os.stat("nodes.csv")
print "nodes.csv: "+str(statinfo.st_size/1024/1024) + "MB"