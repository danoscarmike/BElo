import json
import os
import datetime as dt

data = []
with open(os.path.expanduser('~/Documents/dataViz/dataBlogs/BElo/data/nfl.json')) as f:
    for line in f:
        data.append(json.loads(line))

nflTeams = {}

for row in data:
    row['Date'] = dt.datetime.strptime(row['Date'], '%m/%d/%Y').date()

year = 2013
for year in xrange(2013,1977,-1):
    for row in data:
        if row["Date"].year == year:
            if row["Home Team"] in nflTeams:
                pass
            else:
                nflTeams[row['Home Team']] = {}
                nflTeams[row['Home Team']]["last_season"] = row["Date"].year
        if row["Home Team"] in nflTeams and nflTeams[row["Home Team"]]['last_season'] == 2013:
            nflTeams[row['Home Team']]["current"] = "TRUE"
    year -= 1

# for key,value in nflTeams.iteritems:
#     if value['current']:
#         pass
#     else:
#         value['current'] = 'FALSE'

def dicterate(d):
  for k, v in d.iteritems():
    if isinstance(v, dict):
        print k
        print v
        dicterate(v)
    else:
        print "{0} : {1}".format(k, v)

dicterate(nflTeams)

# for pair in nflTeams:
#     print pair, nflTeams[pair]
