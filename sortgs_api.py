#sortgs_api

import serpapi
import sys
import pandas as pd


def get_title(data):
    try : title = data['title']
    except : title = pd.NA
    return title

def get_links(data):
    try : links = data['link']
    except : links = pd.NA
    return links

def get_citiations(data):
    try : 
        inline_links = data['inline_links']
        cited_by = inline_links['cited_by']
        citation = cited_by['total']
    except : 
        citation = pd.NA
    return citation

def get_author_year_journal(data):

    try:
        publication_info = data['publication_info']
        summary = publication_info['summary']
        author, year_journal, journal_link = summary.split(sep = " - ")

        print(author, year_journal, journal_link)

        try:
            if len(year_journal) > 4:
                year = year_journal[-4:]
                journal = year_journal[0:-4]
            else:
                year = year_journal
                journal = pd.NA
        
        except:
            year = year_journal
            journal = pd.NA

    except:
        author = pd.NA
        year = pd.NA
        journal = pd.NA
    
    return [author, year, journal]


keyword = sys.argv[1]
num = int(sys.argv[2])

path = "./" + keyword + ".csv"

links = list() #
title = list() #
year = list() #
rank = list() # 
citations = list() # 
author = list() # 
journal = list() # 

rank.append(0)
rank_n = 0

for n in range(0,num*10,10):

    params = {
        "engine" : "google_scholar",
        "q" : keyword,
        "api_key" : "Your Private Key",
        "start" : n
    }

    search = serpapi.search(params)
    orgres = search["organic_results"]

    for pos in orgres : #iteration : num of orgres

        links.append(get_links(pos))
        title.append(get_title(pos))
        citations.append(get_citiations(pos))

        author_year_journal = get_author_year_journal(pos)

        author.append(author_year_journal[0])
        year.append(author_year_journal[1])
        journal.append(author_year_journal[2])

        rank_n+=1
        rank.append(rank_n)

data = pd.DataFrame(zip(author, title, citations, year, journal, links), index = rank[1:], 
                    columns=['Author', 'Title', 'Citations', 'Year', 'Journal' ,'Source'])
data.index.name = 'Rank'

data_ranked = data.sort_values('Citations', ascending=False)

# Save results
data_ranked.to_csv(path, encoding='utf-8') # Change the path