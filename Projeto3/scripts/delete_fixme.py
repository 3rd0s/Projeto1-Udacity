#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:52:15 2017

@author: william2
"""
import sqlite3

db=sqlite3.connect("GrandeFortaleza.db")
c=db.cursor()
CHANGE="DELETE FROM ways_tags WHERE key='fixme';"
c.execute(CHANGE)
CHANGE="DELETE FROM nodes_tags WHERE key='fixme';"
c.execute(CHANGE)
db.commit()
db.close()