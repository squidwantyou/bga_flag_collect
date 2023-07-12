#!/usr/bin/env python
import sys,os
from common import *


bag = dict()


ofp = open("all_data.csv",'w')

for line in open("all.csv"):
    items = line.strip().split('\t')
    p_name , o_name, p,o,start,table = items
    flag = open(f"Player_Flag/{o}").read().split(',')[0].lstrip().strip()

    ofp.write( "\t".join([p_name,o_name,p,o,start,table,flag]) )
    ofp.write( "\n" )

    if flag in ("China","Taiwan","Hong Kong","Macao","ERROR"):
        continue



    if p_name in bag:
        bag[p_name].add(flag)
    else:
        bag[p_name] = set()
        bag[p_name].add(flag)

for p_name in bag:
    print(p_name,":")
    tmp = '\n\t'.join( list(bag[p_name] )) 
    print( f"\t{tmp}" )

for p_name in bag:
    print( "%-20s %d"%(p_name,len(bag[p_name])) )

