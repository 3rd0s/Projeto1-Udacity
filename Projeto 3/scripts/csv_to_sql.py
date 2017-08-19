#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 18:14:55 2017

@author: william2
"""

import pandas as pd
import sqlite3
import sys
import re
name = sys.argv[1]

db=sqlite3.connect(u"GrandeFortaleza.db")
df = pd.read_csv(name,encoding='utf-8')
name_table = re.sub(u'\.csv$', '', name)
df.to_sql(name_table, db, if_exists='append', index=False)
c=db.cursor()