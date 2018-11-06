from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
#import urllib.error as urlerr
#import time

houseURL = 'http://clerk.house.gov/evs/2017/roll699.xml'

def voteCheck(congress,session):
    url = 'https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_' + str(congress) + '_' + str(session) + '.htm'
    html = urlopen(url)
        
    soup = bs(html, 'lxml')
    code = soup.prettify()

    fileName = 'tempStorage_' + str(congress) + '_' + str(session) + '.txt'
    
    file = open(fileName,'w+')
    file.write(code)    
    file.close()
    
    file = open(fileName,'r')
    lines = file.readlines()
    file.close()    
    
    numVotes = lines[lineSearch('Vote (Tally)',lines,19,'exact')].strip()
    
    return numVotes
    
def voteScrape(congress,session,vote):
    voteNum = str(vote).zfill(5)
    url = 'https://www.senate.gov/legislative/LIS/roll_call_lists/roll_call_vote_cfm.cfm?congress=' + str(congress) + '&session=' + str(session) + '&vote=' + str(voteNum)    
    html = urlopen(url)
        
    soup = bs(html, 'lxml')
    code = soup.prettify()

    fileName = 'tempStorage_' + str(congress) + '_' + str(session) + '_' + str(vote) + '.txt'
    
    file = open(fileName,'w+')
    file.write(code)    
    file.close()    

    file = open(fileName,'r')
    lines = file.readlines()
    file.close()
    
    return lines

def lineSearch(search,data,index,precision='approx'):
    lineIndex = -1
    searchResult = False
    
    for line in data:
        lineIndex += 1
        if precision == 'approx':
            if search in line:
                searchResult = True
                break     
        if precision == 'exact':
            if search == line.strip():
                searchResult = True
                break 
    
    lineIndex += index
    
    if searchResult == False:
        lineIndex = 0
    
    return lineIndex