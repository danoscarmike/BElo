import csv
import json
import os

fieldsREG = ("Date","Visitor","Visitor Score","Home Team","Home Score","Line","Total Line")
fieldsPOST = ("Date","Round","Visitor","Visitor Score","Home Team","Home Score","Line","Total Line")
jsonfile = open('nfl.json', 'w')

for year_counter in range (1978,2014):
    for filename in os.listdir(os.getcwd()):
        if str(year_counter) in filename:
            print(str(year_counter) + " " + filename)
            csvfile = open(filename, 'r')
            if "nfl" in filename:
                reader = csv.DictReader(csvfile, fieldsREG)
                next(reader)
                for row in reader:
                    json.dump(row, jsonfile)
                    jsonfile.write('\n')
            if "post" in filename:
                reader = csv.DictReader(csvfile, fieldsPOST)
                next(reader)
                for row in reader:
                    json.dump(row, jsonfile)
                    jsonfile.write('\n')
    year_counter += 1
