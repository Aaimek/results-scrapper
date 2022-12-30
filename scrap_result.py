import requests as rq
from bs4 import BeautifulSoup 
from datetime import datetime 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

import time
import random as rd
import copy

all_championas = [ 'fr Division 1 Féminine', 'eng National League', 'jp WE League', 'it Coppa Italia',  'cn Chinese Super League', 'Copa Libertadores', 'cl Primera División', 'se Allsvenskan', 'nl Eredivisie', 'za Premier Division', 'br Série A', 'br Série B', 'eng EFL Cup', 'ch Swiss Super League', 'pt Primeira Liga', 'fr Coupe de France', 'eng Championship', 'es Copa del Rey', 'bo Bolivian Primera División', 'pe Liga 1', 'WCQ — OFC (M)', 'in I-League', 'de DFB-Pokal', 'uy Primera División', 'de 3. Liga', 'ec Serie A', 'de Bundesliga', 'ro Liga I', 'nl Eerste Divisie', 'ua Ukrainian Premier League', 'Algarve Cup', "AFC Women's Asian Cup", 'eng FA Cup', 'jp J2 League', 'hu NB I', 'py Primera División', 'de U17 Bundesliga', 'bg Bulgarian First League', 'de DFB-Pokal Frauen', 'us NWSL', 'ar Primera División', 'be Belgian First Division B', 'sa Saudi Professional League', 'eng League One', 'be Belgian First Division A', 'WCQ — UEFA (W)', 'mx Liga MX', 'ru Russian Premier League', 'fr Ligue 2', 'jp J1 League', 'CONCACAF W Championship', 'es La Liga', 'fi Veikkausliiga', 'ca Canadian Premier League', "be Women's Super League", 'UEFA Super Cup', "eng Women's Super League", 'Europa Conference League', 'eng Premier League 2 — Division 1', 'Europa League', 'br Série A1', 'co Categoría Primera A', 'gr Super League Greece', 'in Indian Super League', 'rs Serbian SuperLiga', 'fr Ligue 1', 'no Eliteserien', 'sct Scottish Championship', 'ir Persian Gulf Pro League', 'hr 1. HNL', 'no Toppserien', 'es Segunda División', 'se Damallsvenskan', 'kr K League 1', 'Copa Sudamericana', "UEFA Women's Euro", 'tr Süper Lig', 'au A-League Women', 'ch Swiss 1/2 Relegation/Promotion Play-offs (W)', 'it Serie A', 'se Superettan', 'us NWSL Challenge Cup', 'SheBelieves Cup', 'nl Eredivisie Vrouwen', 'eng Premier League 2 — Division 2', 'de 2. Bundesliga', 'dk Danish 1/2 Relegation/Promotion Play-offs (W)', 'UEFA Nations League', 'eng Premier League', 'au A-League Men', 'de U19 Bundesliga', 'Champions League', 'Friendlies (W)', 'de Frauen-Bundesliga', 'us USL Championship', 'Africa Cup of Nations', 'be Belgian 1/2 Relegation/Promotion Play-off', 'Africa Women Cup of Nations', 'dk Kvindeligaen', "ch Women's Super League", 'cn Chinese 1/2 Relegation/Promotion Play-off', 'Africa Cup of Nations qualification', 'eng League Two', 'pl Ekstraklasa', 'it Supercoppa Italiana', 'sct Scottish Premiership', 'es Supercopa de España', 'it Serie B', 'at Frauenliga', 'sct Scottish 2/3 Relegation/Promotion Play-off', 'dk Superliga', 'us Major League Soccer', 'cz Czech First League', 'at Austrian Bundesliga', 'Friendlies (M)']
championas = [ 'fr Division 1 Féminine', 'eng National League', 'jp WE League', 'it Coppa Italia',  'cn Chinese Super League', 'Copa Libertadores', 'cl Primera División', 'se Allsvenskan', 'nl Eredivisie', 'br Série A', 'eng EFL Cup', 'ch Swiss Super League', 'pt Primeira Liga', 'fr Coupe de France', 'eng Championship', 'es Copa del Rey', 'in I-League', 'de DFB-Pokal', 'uy Primera División', 'ec Serie A', 'de Bundesliga', 'ro Liga I', 'nl Eerste Divisie', 'ua Ukrainian Premier League', 'Algarve Cup', "AFC Women's Asian Cup", 'eng FA Cup', 'hu NB I', 'py Primera División', 'bg Bulgarian First League', 'de DFB-Pokal Frauen', 'us NWSL', 'ar Primera División', 'be Belgian First Division B', 'sa Saudi Professional League', 'eng League One', 'be Belgian First Division A', 'WCQ — UEFA (W)', 'mx Liga MX', 'ru Russian Premier League', 'fr Ligue 2', 'jp J1 League', 'CONCACAF W Championship', 'es La Liga', 'fi Veikkausliiga', 'ca Canadian Premier League', "be Women's Super League", 'UEFA Super Cup', "eng Women's Super League", 'Europa Conference League', 'eng Premier League 2 — Division 1', 'Europa League', 'br Série A1', 'co Categoría Primera A', 'gr Super League Greece', 'rs Serbian SuperLiga', 'fr Ligue 1', 'no Eliteserien', 'sct Scottish Championship', 'hr 1. HNL', 'no Toppserien', 'es Segunda División', 'se Damallsvenskan', 'kr K League 1', 'Copa Sudamericana', "UEFA Women's Euro", 'tr Süper Lig', 'au A-League Women', 'ch Swiss 1/2 Relegation/Promotion Play-offs (W)', 'it Serie A', 'us NWSL Challenge Cup', 'SheBelieves Cup', 'nl Eredivisie Vrouwen', 'eng Premier League 2 — Division 2', 'de 2. Bundesliga', 'dk Danish 1/2 Relegation/Promotion Play-offs (W)', 'UEFA Nations League', 'eng Premier League', 'au A-League Men', 'Champions League', 'de Frauen-Bundesliga', 'us USL Championship', 'Africa Cup of Nations', 'be Belgian 1/2 Relegation/Promotion Play-off', 'Africa Women Cup of Nations', 'dk Kvindeligaen', "ch Women's Super League", 'cn Chinese 1/2 Relegation/Promotion Play-off', 'Africa Cup of Nations qualification', 'eng League Two', 'pl Ekstraklasa', 'it Supercoppa Italiana', 'sct Scottish Premiership', 'es Supercopa de España', 'it Serie B', 'at Frauenliga', 'sct Scottish 2/3 Relegation/Promotion Play-off', 'dk Superliga', 'us Major League Soccer', 'cz Czech First League', 'at Austrian Bundesliga']
table = [ [k, []] for k in championas]



#############
def verif_list(championas):
  for champ in championas:
    if len(champ)>25:
      print(' len pb ' + champ)
    if champ[1] == ' ':
      print(champ)


def jour(day_num, year):
  day_num = str(day_num) 
  day_num.rjust(3 + len(day_num), '0')  
  year = str(year)   
  res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%m-%d-%Y") 
  res = str(res)
  return res[6: 13] + '-' + res[:3] + res[3: 5] 

def winner(score):
    if isinstance(score, float):
      return 'not played'
    elif len(score) == 3:
      home = int(score[0])
      away = int(score[2])
      if away < home:
        return "team_home"
      elif away == home:
        return "draw"
      return "team_away"
    
    elif len(score) == 10:
      home = int(score[1])
      away = int(score[9])
      if away < home:
        return 'team_home'
      elif away == home:
        return "draw"
      return 'team_away'

def correct_team_name(name):
  name = str(name)
  if len(name)> 4:
    if name[-3] == ' ':
      if name[-2].islower() and name[-1].islower():
        name = name[:-3]
    
    elif name[-4] == ' ':
      if name[-2].islower() and name[-1].islower() and name[-3].islower():
        name = name[:-4]
    
    elif name[2] == ' ':
      if name[0].islower() and name[1].islower():
        name = name[3:]

    elif name[3] == ' ':
      if name[0].islower() and name[1].islower() and name[2].islower() :
        name = name[4:]
    
  return name


def scrap(debut, fin, annee = 2022):
  data = []
  for k in range(debut, fin):
    date = jour(k, annee)
    table = pd.read_html('https://fbref.com/en/matches/' + date)
    sleepy_time = 3.1
    time.sleep(sleepy_time)
    url = 'https://fbref.com/fr/matchs/' + date
    res = rq.get(url)
    soup = BeautifulSoup(res.text, features="lxml")
    time.sleep(sleepy_time)
    rows = soup.findAll('div', class_ = "table_wrapper tabbed")
    nrows = len(rows)
    L = []
    for i in range(nrows):
      champ = rows[i].find('h2').text
      if champ in championas:
        L.append([champ, list(table[i]) ,table[i].values.tolist()])
    data.append(L)
  return data

def tri_ekip(data):
  teams = {}
  data_copie = copy.deepcopy(data)
  for journe in data_copie:
    for champ in journe:

      indice_home = champ[1].index("Home")
      indice_away = champ[1].index("Away")
      indice_score = champ[1].index("Score")

      
      for match in champ[2]:

        team_home = correct_team_name(match[indice_home]) 
        team_away = correct_team_name(match[indice_away])
        score = match[indice_score]

        if winner(score) == 'not played':
          winner_name = "not played"
        else:
          winner_name = "draw"


          
        if winner(score) == "team_away": winner_name = team_away
        elif winner(score) == "team_home":  winner_name = team_home
        match.append(champ[0])
        match.append(len(match)+1)
        match.append(winner_name)

        if team_home in teams.keys():
          teams[team_home].append(match)
        else:
          teams[team_home] = [match]

        if team_away in teams.keys():
          teams[team_away].append(match)
        else:
          teams[team_away] = [match]

  return teams


def dict_to_list(L):
  tuple_list = L.items()
  lst = []
  for elt in tuple_list:
    a = [elt[0], list(elt[1])]
    lst.append(a)
  return lst

  
def scrap_results(date_debut, date_fin, annee):
    dic = {}
    print('Resultats du ' + str(jour(date_debut, annee)) + ' au ' +str(jour(date_fin, annee)) )
    res = scrap(date_debut, date_fin, annee)[0]
    for elt in res:
        dic[elt[0]] = elt[1:]
    
    return dic



