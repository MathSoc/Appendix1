import csv 
import math

class Constituency:
    def __init__(self):
        self.seats = 1
        self.priority = 0
        self.students = 0

def calculate_priority(cons: Constituency):
    cons.priority = math.sqrt(cons.students/(cons.seats * (cons.seats + 1)))

seats_avaialble = 21

##########################################
#       REPLACE THESE VARIABLES
##########################################
fileName = "pub_enrolment_heads_csv_spring2021.csv"
year = "2020/21"
term = "Winter term"
##########################################


##########################################
#       CHECK THAT THESE LINE UP IN THE SPREADSHEET
##########################################
year_column = 5
term_column = 9
level_column = 7
study_year_column = 8
faculty_column = 4
program_column = 6
headcount_column = 12
##########################################


thisdict = {
    "firstYears": Constituency(), 
    "actSci": Constituency(),
    "business": Constituency(),
    "cfm": Constituency(),
    "cs": Constituency(),
    "other": Constituency(),
    "pmamco": Constituency(),
    "se": Constituency(),
    "stats": Constituency(),
    "teaching": Constituency()
}

with open(fileName) as f:
    data = csv.reader(f, delimiter=',')

    for row in data:
        if (row[year_column] == year) and (row[term_column] == term) and (row[level_column] == "Bachelors"):
            if (row[study_year_column] == "1" and (row[faculty_column] == "MATH" or row[faculty_column] == "CFM")):
                thisdict["firstYears"].students += int(row[headcount_column])
            elif (row[program_column] == "Actuarial Science"):
                thisdict["actSci"].students += int(row[headcount_column])
            elif (row[program_column] == "Applied Mathematics"):
                thisdict["pmamco"].students += int(row[headcount_column])
            elif(row[program_column] == "Bioinformatics"):
                thisdict["stats"].students += int(row[headcount_column])
            elif (row[program_column] == "Business Administration and Computer Science"):
                thisdict["business"].students += int(row[headcount_column])
                thisdict["cs"].students += int(row[headcount_column])
            elif(row[program_column] == "Business Administration and Mathematics"):
                thisdict["business"].students += int(row[headcount_column])
            elif(row[program_column] == "Chartered Professional Accountancy"):
                thisdict["business"].students += int(row[headcount_column])
            elif (row[program_column] == "Combinatorics and Optimization"):
                thisdict["pmamco"].students += int(row[headcount_column])
            elif (row[program_column] == "Computational Mathematics"):
                thisdict["cs"].students += int(row[headcount_column])
                thisdict["pmamco"].students += int(row[headcount_column])
            elif (row[program_column] == "Computer Science"):
                thisdict["cs"].students += int(row[headcount_column])
            elif(row[program_column] == "Data Science"):
                thisdict["stats"].students += int(row[headcount_column])
                thisdict["cs"].students += int(row[headcount_column])
            elif (row[program_column] =="Financial Analysis and Risk Management"):
                thisdict["business"].students += int(row[headcount_column])
            elif (row[program_column] == "Information Technology Management"):
                thisdict["business"].students += int(row[headcount_column])
            elif (row[program_column] == "Mathematical Finance"):
                thisdict["actSci"].students+= int(row[headcount_column])
                thisdict["pmamco"].students += int(row[headcount_column])
            elif (row[program_column] == "Mathematical Studies"):
               thisdict["other"].students += int(row[headcount_column])
            elif (row[program_column] == "Mathematics"):
                thisdict["other"].students += int(row[headcount_column])
            elif (row[program_column] == "Mathematics/Business Administration"):
                thisdict["business"].students += int(row[headcount_column])
            elif (row[program_column] == "Mathematics/Teaching"):
                thisdict["teaching"].students += int(row[headcount_column])
            elif(row[program_column] == "Pure Mathematics"):
                thisdict["pmamco"].students += int(row[headcount_column])
            elif(row[program_column] == "Statistics"):
                thisdict["stats"].students += int(row[headcount_column])
            elif (row[faculty_column] == "MATH"):
                thisdict["other"].students += int(row[headcount_column])
            elif (row[faculty_column] == "CFM"):
                thisdict["cfm"].students += int(row[headcount_column])
            elif (row[faculty_column] == "SE"):
                thisdict["se"].students += int(row[headcount_column])
            else:
                continue

print("Students per Constituency:")
for key in thisdict.keys():
    print(key + ": " + str(thisdict[key].students))


for cons in thisdict.values():
    calculate_priority(cons)

print("\n\nCalculations:")
while (seats_avaialble > 0):
    # find cons with highest priority + recaculate it
    highest = 0
    highest_key = ""
    for key in thisdict.keys():
        if (thisdict[key].priority > highest):
            highest = thisdict[key].priority
            highest_key = key
        elif (thisdict[key].priority == highest):
            print("This part has not been implemented yet. Add implementation when required")
            exit
    print(highest_key + ": " + str(thisdict[highest_key].priority))
    thisdict[highest_key].seats += 1
    calculate_priority(thisdict[highest_key])

    seats_avaialble-=1

print("\n\nSeat Allocations:")
for key in thisdict.keys():
    print(key + ": " + str(thisdict[key].seats))


