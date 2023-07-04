#!/usr/bin/env python
import sys,os
import json

infile = "player_id.list"

for line in open(infile):
    line = line.strip()
    p_name = " ".join(line.split()[:-1])
    p_id = int( line.split()[-1] )
    os.system(f"touch games_data/{p_id}/beat.list")
    os.system(f"touch 'games_data/{p_id}/0.{p_name}'")

    with open(f"games_data/{p_id}/beat.list",'w') as ofp:
        ofp.write(("\t".join( [ "Win","Lose", "Start at", "Table id"] ) ) )  
        ofp.write("\n")
        i = 1
        while True:
            jsonfile = f"games_data/{p_id}/{i}.json"
            if not os.path.isfile(jsonfile):
                break
            tmp = json.loads( open(jsonfile).read() )

            for table in tmp['data']['tables']:
                if table['normalend'] != '1':
                    continue
                players = table['players']
                ranks = table['ranks']
                names = table['player_names']
                rank = dict()
                name = dict()
                for a,b in zip( players.split(","), ranks.split(",") ):
                    rank[int(a)] = b 
                for a,b in zip( players.split(","), names.split(",") ):
                    name[int(a)] = b 
#                print(table)
                for oppo in rank:
                    if int(oppo) != p_id and int(rank[oppo]) > int(rank[p_id]):
#                        print( names, ranks )
#                        print( p_id, oppo, table['table_id'] )
                        ofp.write(("\t".join( [ name[p_id], name[oppo],  table['start'], table['table_id']] ) ) )  
                        ofp.write("\n")
                    
                
               #{'table_id': '393061428', 'game_name': 'seasons', 'game_id': '30', 'start': '1688357154', 'end': '1688358987', 'concede': '0', 'unranked': '0', 'normalend': '1', 'players': '85409012,85068842', 'player_names': 'zhix,Dagedog', 'scores': '210,150', 'ranks': '1,2', 'elo_win': '-14', 'elo_penalty': '', 'elo_after': '1783', 'arena_win': None, 'arena_after': '1.1500'} 

            i += 1

