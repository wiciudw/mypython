# -*- coding: utf-8 -*-
import sys

tickets = []    #A list which will represent a file (a pile) of tickets
                #I assume that one person cannot have more traveles during life which could take whole memory in a computer
                #TODO:Another way, we need to work directly with file or database.

#First step: rewrite whole file to the list
# #with open(sys.argv[1], encoding="ansi") as f:
with open('FileDRandom.txt', encoding="ansi") as f: #I realise that I need ansi coding of file.
                                      #TODO: In the case of utf-8 encoding I found some strange sign at the beginning of file
     for line in f:                   #For every line in the file
         line = line.replace('\n','') #Remove sign end of the line
         ticket = line.split(",")     #Split elements of ticket's description
         tickets.append(ticket)       #Append every ticket to the list
f.close()                             #Closes the file

#Second step: finding first station
index = 0                       #I initiate variable with the number of the index of the first station
for i in range(len(tickets)):   #For every beginning station...
    flag = True
    for j in range(len(tickets)):
        if i != j and tickets[i][0] == tickets[j][1]:   #...check end station If some of end stations
                                                        #(from different ticket than beginning) is equal to the beginning station
                                                        #it means that
            flag = False                                #this beginning station is not the first station of the trip.
            break                                       #Take next a beginning station trom next ticket
    if flag == True:                                    #If during j-loops we didn't find equal stations we found the first station
        index = i
        break

tickets.append(tickets[index])              #Append found ticket to the end of list
tickets.remove(tickets[index])              #Remove found ticket from the previous position in the list

#Third step: sorting other elements
n = 1                                       #We found the first station. Now we need to sort other tickets.

while n < len(tickets):
    for i in range(len(tickets)-n):         #Every circle of loops makes our base list of tickets shorter
        if tickets[i][0] == tickets[len(tickets)-1][1]: #Check all left tickets for the next station
            tickets.append(tickets[i])     #Move found the next station to the end of list
            tickets.remove(tickets[i])
            n = n + 1
            break

#Fourth step: formating of output
count = 1
for ticket in tickets:
    if count == 1:
        if len(ticket) == 3:
            print('{}.Rusz za pomocą {} z {} do {}'.format(count, ticket[2], ticket[0], ticket[1]))
        if len(ticket) == 4:
            print('{}.Rusz za pomocą {} z {} do {} (miejsce {})'.format(count, ticket[3], ticket[0], ticket[1], ticket[2]))
    if count > 1:
        if len(ticket) == 3:
            print('{}.Przesiądź się do {} z {} do {}'.format(count, ticket[2], ticket[0], ticket[1]))
        if len(ticket) == 4:
            print('{}.Przesiądź się do {} z {} do {} (miejsce {})'.format(count, ticket[3], ticket[0], ticket[1], ticket[2]))
    count = count + 1
print('{}.Jesteś na miejscu'.format(count))