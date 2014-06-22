# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 18:43:43 2014

@author: wyh
"""
cities={'CA':'San Franciso','MI':'Detroit','FL':'jacksonville'}

cities['NL']='New York'
cities['OR']='Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"
    
cities['_find']=find_city

while True:
    print "state?enter to qiut",
    state=raw_input(">")

    if not state:
        break
    
    city_found=cities['_find'](cities,state)
    print city_found
        