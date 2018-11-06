import scrape_functions as sf
#import sys

congress = 115
session = 2
voteNum = 189

dataLines = sf.scrapeStore(congress,session,voteNum)

#if isinstance(dataLines, (bool)):
#    print('Congress, session, or vote does not exist.\n')
#    sys.exit()

#vote counts
searchTerm = 'Vote Counts'
dataIndex = sf.lineSearch(searchTerm,dataLines,6)

yeas = int(dataLines[dataIndex].strip())
nays = int(dataLines[dataIndex + 9].strip())
if 'Not Voting' in dataLines[dataIndex + 14]:
    noVote = int(dataLines[dataIndex + 17].strip())
else:
    noVote = 0

numVotes = sum((yeas,nays,noVote))
print([yeas,nays,noVote])

#vote results
searchTerm = 'Alphabetical by Senator Name'
dataIndex = sf.lineSearch(searchTerm,dataLines,6)

senator = []
party = []
state = []
vote = []
for n in range(numVotes):
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
    if line[0] == 'Booker':
        print(line)
        break

'agreed to'
'rejected'
'confirmed'
'passed'