from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
#import urllib.error as urlerr
#import time

houseURL = 'http://clerk.house.gov/evs/2017/roll699.xml'

def scrapeStore(congress,session,vote):
    voteNum = str(vote).zfill(5)
    url = 'https://www.senate.gov/legislative/LIS/roll_call_lists/roll_call_vote_cfm.cfm?congress=' + str(congress) + '&session=' + str(session) + '&vote=' + str(voteNum)    
    html = urlopen(url)
    
#    try:
#        html = urlopen(url)
#        voteError = False
#    except urlerr.HTTPError as err:
#        voteError = True
#    else:
#        print('error')
#        time.sleep(2)
#        html = urlopen(url)
#    
#    if voteError == True:
#        return voteError
        
    soup = bs(html, 'lxml')
    code = soup.prettify()

    fileName = 'tempStorage_' + str(congress) + '_' + str(session) + '_' + str(vote) + '.txt'
    
    file = open(fileName,'w+')
#    try:
#        file.write(code)    
#    except UnicodeEncodeError:
#        file = open(fileName,'w+',encoding="utf-8")
#        file.write(code)   
    file.write(code)    
    file.close()    

    file = open(fileName,'r')
    lines = file.readlines()
    file.close()
    
    return lines

def lineSearch(search,data,index):
    lineIndex = -1
    searchResult = False
    
    for line in data:
        lineIndex += 1
        if search in line:
            searchResult = True
            break            
    
    lineIndex += index
    
    if searchResult == False:
        lineIndex = 0
    
    return lineIndex