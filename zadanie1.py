import sys
count = 1
with open(sys.argv[1]) as f:
    for line in f:
        line = line.replace('\n','')
        ticket = line.split(",")
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
f.close()
