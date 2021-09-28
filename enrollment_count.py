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

thisdict = {
    "firstYears": Constituency(), 
    "actSci": Constituency(),
    "business": Constituency(),
    "cfm": Constituency(),
    "cs": Constituency(),
    "other": Constituency(),
    "pmamco": Constituency(),
    "se": Constituency(),
    "teaching": Constituency()
}

with open("pub_enrolment_heads_csv_fall2020_1.csv") as f:
    data = csv.reader(f, delimiter='^')

    for row in data:
        if (row[5] == "2020/21") and (row[9] == "Fall term") and (row[7] == "Bachelors"):
            if (row[8] == "1" and (row[4] == "MATH" or row[4] == "CFM")):
                thisdict["firstYears"].students += int(row[13])
            elif (row[6] == "Actuarial Science"):
                thisdict["actSci"].students += int(row[13])
            elif (row[6] == "Applied Mathematics"):
                thisdict["pmamco"].students += int(row[13])
            elif (row[6] == "Business Administration and Computer Science"):
                thisdict["business"].students += int(row[13])
                thisdict["cs"].students += int(row[13])
            elif(row[6] == "Business Administration and Mathematics"):
                thisdict["business"].students += int(row[13])
            elif(row[6] == "Chartered Professional Accountancy"):
                thisdict["business"].students += int(row[13])
            elif (row[6] == "Combinatorics and Optimization"):
                thisdict["pmamco"].students += int(row[13])
            elif (row[6] == "Computational Mathematics"):
                thisdict["cs"].students += int(row[13])
                thisdict["pmamco"].students += int(row[13])
            elif (row[6] == "Computer Science"):
                thisdict["cs"].students += int(row[13])
            elif (row[6] =="Financial Analysis and Risk Management"):
                thisdict["business"].students += int(row[13])
            elif (row[6] == "Information Technology Management"):
                thisdict["business"].students += int(row[13])
            elif (row[6] == "Mathematical Finance"):
                thisdict["actSci"].students+= int(row[13])
                thisdict["pmamco"].students += int(row[13])
            elif (row[6] == "Mathematical Studies"):
               thisdict["other"].students += int(row[13])
            elif (row[6] == "Mathematics"):
                thisdict["other"].students += int(row[13])
            elif (row[6] == "Mathematics/Business Administration"):
                thisdict["business"].students += int(row[13])
            elif (row[6] == "Mathematics/Teaching"):
                thisdict["teaching"].students += int(row[13])
            elif(row[6] == "Pure Mathematics"):
                thisdict["pmamco"].students += int(row[13])
            elif(row[6] == "Statistics"):
                thisdict["actSci"].students += int(row[13])
            elif (row[4] == "MATH"):
                thisdict["other"].students += int(row[13])
            elif (row[4] == "CFM"):
                thisdict["cfm"].students += int(row[13])
            elif (row[4] == "SE"):
                thisdict["se"].students += int(row[13])
            else:
                continue

print("Students per Constituency:")
for key in thisdict.keys():
    print(key + ":" + str(thisdict[key].students))


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
    print(highest_key + ":" + str(thisdict[highest_key].priority))
    thisdict[highest_key].seats += 1
    calculate_priority(thisdict[highest_key])

    seats_avaialble-=1

print("\n\nSeat Allocations:")
for key in thisdict.keys():
    print(key + ":" + str(thisdict[key].seats))


