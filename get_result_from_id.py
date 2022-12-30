from datetime import *
from scrap_result import *
import psycopg2
from difflib import SequenceMatcher
import pdb


conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % ("138.195.138.37", "coteur-scraping", "postgres", "pclmdp99"))
cur = conn.cursor()


def find_matching_team(team_a, game_results):
    max_score = 0
    coord_max = [0, 0, 0, 0]
    constr_table_max = 0

    ## c'est un peu degeu mais on travail ici avec un tableau a 4 dim
    for indice_ligne in range(len(game_results)):
        for indice_colonne in range(len(game_results[indice_ligne])):
            constr_table =  game_results[indice_ligne][indice_colonne][1]
            for indice_mot in range(len(game_results[indice_ligne][indice_colonne][2])):
                for ind_mot in range(len(game_results[indice_ligne][indice_colonne][2][indice_mot])):
                    word = str(game_results[indice_ligne][indice_colonne][2][indice_mot][ind_mot]).upper()
                    team_a = team_a.upper()
                    score = SequenceMatcher(a=word,b=team_a).ratio()
                
                    if score > max_score:
                        max_score = score
                        coord_max = [indice_ligne, indice_colonne, indice_mot, ind_mot]
                        constr_table_max = constr_table

    a, b, c, d= coord_max
    return (constr_table_max, game_results[a][b][2][c])


## cette fct renvoi le nom du gagnant
def winner(constr_table, match):
    score_index = constr_table.index('Score')
    score = match[score_index]
    try :
        s_a = score[0]
        s_b = score[-1]

        if s_a == s_b :
            return 'Draw'

        if s_a > s_b:
            home_index = constr_table.index('Home')
            return match[home_index]

        else:
            away_index = constr_table.index('Away')
            return match[away_index]
    
    except:
        return 'match non joué'



def get_result(game_id):
    ## ici je cree le dictionnaire avec les resultats du jour
    day_of_year = datetime.now().timetuple().tm_yday 
    game_results = scrap(day_of_year-1, day_of_year, 2022)

    ## ici je selctionne la ligne qui corespond au game id et je place toute les infos dans des variables pour plus de clarté
    sql = "Select * From games where id = %d;" % game_id
    cur.execute(sql)
    info_match = cur.fetchall()
    team_a = info_match[0][1]

    ## je cherche pas par championnats finalement car la db est en francais et les infos sur les resultats en anglais
    constr_table, match = find_matching_team(team_a, game_results)
    winr = winner(constr_table, match)
    return winr
    
    





