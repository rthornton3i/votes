import scrape_functions as sf
from math import ceil
from time import sleep

#number of votes per session
yearStart = 2013
yearEnd = 2018

congressStart = ceil((yearStart-1788)/2)
congressEnd = ceil((yearEnd-1788)/2) + 1

for n in range(congressStart,congressEnd):
    for m in range(1,3):
        numVotes = sf.voteCheck(n,m)
        numVotes = str(numVotes[:numVotes.find("(")-1])

congress = 115
session = 2
voteNum = 223

dataLines = sf.voteScrape(congress,session,voteNum)

#vote results
searchTerm = 'Alphabetical by Senator Name'
dataIndex = sf.lineSearch(searchTerm,dataLines,6)

senator = []
party = []
state = []
vote = []
for n in range(100):
    senatorData = dataLines[dataIndex].strip().replace(',','')
    senatorName = senatorData[0:senatorData.find("(")-1]
    senatorParty = senatorData[senatorData.find("(")+1]
    senatorState = senatorData[senatorData.find("-")+1:][:2]
    
    senator.append(senatorName)
    party.append(senatorParty)
    state.append(senatorState)
    
    dataIndex += 2
    
    vote.append(dataLines[dataIndex].strip())

    dataIndex += 3

votes = list(zip(senator,party,state,vote))

for line in votes:
    if line[0] == 'Murkowski':
        print(line)
        break

'agreed to'
'rejected'
'confirmed'
'passed'