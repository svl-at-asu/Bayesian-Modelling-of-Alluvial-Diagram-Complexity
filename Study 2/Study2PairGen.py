
import csv

d = {}

totalSet = set()

with open("Diagrams_Complexity - Sheet1.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    rowCount = 0
    for row in csvReader:
        if(rowCount != 0):
            if(row[1] not in d.keys()):
                d[row[1]] = []
            d[row[1]].append(row[0])

        rowCount += 1

print(d)


# MAXDISTANCEAWAY = 30

# for i in d:

#     searchList = []
#     MINDIST = int(i) - MAXDISTANCEAWAY
#     MAXDIST = int(i) + MAXDISTANCEAWAY

#     r = list(range(MINDIST, MAXDIST))
#     # print(r)

#     for j in r:
#         if(i == str(j)):
#             continue
#         try:
#             searchList.extend(d[str(j)])
#         except KeyError:
#             continue

#     # print(d[i])
#     # print(searchList)

#     for elem1 in d[i]:
#         for elem2 in searchList:

#             if(tuple(sorted((elem1, elem2))) in totalSet):
#                 continue
#             else:
#                 totalSet.add((elem1, elem2))



r = list(range(1,46))
for i in range(len(r)):
    for j in range(len(r)):
        if(i == j):
            continue
        if(tuple(sorted((r[i], r[j]))) in totalSet):
            continue
        else:
            totalSet.add((r[i],r[j]))

print("\n\n\n\n\n\n\n\n")
print(sorted(totalSet, key=lambda x: x[0]))
# print(totalSet)
print(len(totalSet))

with open("Study2Pairs.csv", "w") as csvFile:
    csvWriter = csv.writer(csvFile)
    for i in sorted(totalSet):
        csvWriter.writerow(i)
    

