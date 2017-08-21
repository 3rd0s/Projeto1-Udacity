#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:43:08 2017

@author: william2
"""

import pandas as pd
from collections import defaultdict
import re
import sqlite3

#EXPRESSÕES REGULARES PARA O TIPO DE VIA(RUA,AVENIDA... E CARACTÉRES PROBLEMATICOS)
street_type_re = re.compile(r'^\b\S+\.?', re.IGNORECASE)
R2problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\t\r\n]')
#NOMES ESPERADOS, O 4º VÊM DO QUARTO ANÉL VIÁRIO DE FORTALEZA
expected = [u"Rua",u"Avenida",u"Beco",u"Alameda",u"Acesso",u"Travessa", u"CE",u"BR",u"4º",u'Campus',u'Praça','Vila']

#ESSA FUNCAO FOI USADA NO NOTEBOOK PARA CONSEGUIR OS TERMOS DO MAPPING E DO EXPECTED
def audit_street_type(street_types, street_name):
    """Audita para verificar se falta algum prefixo
    args:
        street_types (list): nome dos tipos de rua já vérificados que não estão no expected.
        street_name (str): nome da string pra ser auditada
    return:
        None
    """
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
 #MAPA PARA MUDANÇA DE TERMOS USADOS           
mapping = { u"Av.": u"Avenida",
            u"Av": u"Avenida",
            u"Tv.": u"Travessa",
            u"R.": u"Rua",
            u"Ce": u"CE",
            u"Br": u"BR"
            }
def update_problems_addr(name):
    '''Função para corrigir os nomes nas colunas value do tipo addr
    args:
        name (str): nome a ser verificado por problemas
    return:
        (str) nome corrigido
    
    '''
    name=name.title()
    if(name==u'Costa Barros'):
        return u'Avenida Costa Barros'
    elif(name==u'Barbosa de Freitas'):
        return u'Avenida Barbosa de Freitas'
    elif(name==u'Joaquim Nabuco'):
        return u'Rua Joaquim Nabuco'
    elif(name==u'Eng\xb0 Sandoval S\xe1'):
        return u'Rua Engenheiro Sandoval'
    elif(name==u'2'):
        return u'Rua 2'
    elif(name==u'Alu\xedsio Mamede'):
        return u'Rua Aluísio Mamede'
    elif(name==u'Titan'):
        return u'Rua Titan'
    elif(name==u'Washington Soares'):
        return u'Avenida Washington Soares'    
    elif(name==u'José Severino'):
        return u'Rua José Severino'
    elif(name==u'Rua Nove,'):
        return u'Rua Nove'
    elif(name==u'João Paula Costa'):
        return u'Rua João Paula Costa'
    elif(name==u'Maria Teixeira Joca'):
        return u'Rua Maria Teixeira Joca'
    elif(name==u'Santa Teresinha'):
        return u'Rua Santa Teresinha'
    elif(name==u'Santa Teresinha'):
        return u'Rua Santa Teresinha'
    elif(name==u'Alphaville Fortaleza'):
        return u'Avenida Litorânea'
    elif(street_type_re.search(name).group() not in expected):
        rua = street_type_re.search(name)
        print name
        #EFETUA A MUDANÇA DE PREFIXO COM BASE NO MAPPING
        name= re.sub(street_type_re,mapping[rua.group()],name)
    return name
def audit_street(name_table,database):
    '''Audita uma tabela de um database, procurando erros nos nomes das ruas
    args:
        name_table (str): Nome da tábela analisada
        database (str): Nome do banco de dados
    return:
        None
    '''
    
    db=sqlite3.connect(database)
    QUERY='SELECT * FROM '+name_table
    nodes_tags=pd.read_sql(QUERY,db)
    count=0
    street_types = defaultdict(set)
    for valor,tipo,chave in nodes_tags[['value', 'type','key']].values:
        if(tipo=='addr'and chave=='street'):   
            alterado=update_problems_addr(valor)
            if(valor!=alterado):
                nodes_tags['value'].values[count]=alterado
            audit_street_type(street_types, alterado) 
        count+=1
    #como se nota foi usado pandas para passar as informações, somente para eu
    #poder treina-lo mais#
    nodes_tags.to_sql(name_table,db, if_exists='replace', index=False)
    #print (street_types)
    #print nodes_tags.head()
    db.commit()
    db.close()
#audita os nós    
audit_street(u'nodes_tags','GrandeFortaleza.db')
#audita as vias
audit_street(u'ways_tags','GrandeFortaleza.db')