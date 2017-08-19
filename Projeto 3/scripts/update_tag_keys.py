#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:38:21 2017

@author: william2
"""

# -*- coding: utf-8 -*-
import sqlite3
import re

Rnormal = re.compile(r'^([\w\. _])+',re.U) #verifica se tem o formato esperado
Rproblemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')#verifica caracterés problematicos
Ruppercase_incorrect=re.compile(r'[A-Z][A-Z]+',re.U)#verifica as maiúsculas
Rspace = re.compile(r'^([\w\. _])*[ ]',re.U)#olha espaços

def update_problems_keys(name):
    '''Função para corrigir os nomes nas colunas keys'''
    if(Rproblemchars.search(name)!=None):
        if(name==u'Unid.Hab'):
            return u'unidade_habitacional'
        elif(Rspace.search(name)!=None):
            #troca espaços por underlines
            return Rspace.search(name).group()[:-1]+'_'+ name[(Rspace.search(name)).end():]
        else:
            #se tinha um caractére problematico mas não foi achado o defeito printa
            print name+" Problem",Rspace.search(name)
    if(not name.islower()):
        #se não for minúscula
        if(name=='FID' or name=='IBGE' or name=='BR' or name=='CE'):
            return name
        elif(name==u'AProjetada'):
            return u'área_projetada'
        elif(name=='AConst'):
            return u'área_construída'
        elif(name=='GEOCODIGO'):
            return u'geocodigo'    
        elif(name=='UNIDADES_HABITACIONAIS'):
            return u'unidades_habitacionais'        
        else:
            #torna minúscula
            return name.lower()
    return name
db=sqlite3.connect("GrandeFortaleza.db")
c=db.cursor()
QUERY="""SELECT key,value FROM ways_tags;"""
c.execute(QUERY)
rows=c.fetchall()
for key,valor in rows:
    alterado=update_problems_keys(key)
 #   print alterado
    if(key!=alterado):
        #faz a troca de palavras se necessário nos ways
        CHANGE="UPDATE ways_tags SET key = replace(key, %s, %s);" % ("'"+key+"'","'"+alterado+"'")
        print CHANGE
        c.execute(CHANGE)
QUERY="""SELECT key,value FROM nodes_tags;""" 
c.execute(QUERY)
rows=c.fetchall()
for key,valor in rows:
    alterado=update_problems_keys(key)    
    update_problems_keys(key)
    if(key!=alterado):
        #mesma coisa para os nodes. Faz a troca.
        CHANGE="UPDATE nodes_tags SET key = replace(key, %s, %s);" % ("'"+key+"'","'"+alterado+"'")
        print CHANGE
        c.execute(CHANGE)
db.commit()
db.close()