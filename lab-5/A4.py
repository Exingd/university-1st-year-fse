def command_find(n):
    a = open(r"D:/python/lab-5/commands.0.txt", "r")
    comm = a.read()
    comm = comm.split("\n")
    commsplit = comm[n].split()
    command = commsplit[0]
    return command
def search(x, n, o):
    a = open(r"D:/python/lab-5/sequences.0.txt", "r")
    seq = a.read()
    seq = seq.split("\n")
    c = 0
    flag = 0
    for i in range(5):
        seqtable = seq[c].split("	")
        if x in seqtable[2]:
            print(f"Operation {o}: search   {x} \nOrganism: {seqtable[1]} \nProtein: {seqtable[0]}\n")
            flag = flag + 1
        c = c + 1
    if flag == 0:
        print(f"Operation {o}: search   {x} \nOrganism: NOT FOUND \nProtein: NOT FOUND\n")
    else:
        flag = 0
    return " "
def search_seq(n):
    a = open(r"D:/python/lab-5/commands.0.txt", "r")
    seq = a.read()
    seq = seq.split("\n")
    seqtable = seq[n].split()
    return seqtable[1]
def diff(b1, b2, n):
    a = open(r"D:/python/lab-5/commands.0.txt", "r")
    comm = a.read()
    comm = comm.split("\n")
    commtable = comm[n].split("	")
    name1 = commtable[1]
    name2 = commtable[2]
    if b1[0] == " " or b2[0] == " ":
        if b1[0] == " " and b2[0] == " ":
            name1 == "MISSING: " + name1
            name2 == "MISSING: " + name2
            print(f"Operation {o}: diff    {name1}     {name2}\namino-acids difference: {name1}, {name2}")
        if b1[0] == " ":
            name1 == "MISSING: " + name1
            print(f"Operation {o}: diff    {name1}     {name2}\namino-acids difference: {name1}")
        if b2[0] == " ":
            name2 == "MISSING: " + name2
            print(f"Operation {o}: diff    {name1}     {name2}\namino-acids difference: {name2}")
    c = 0
    counter = 0
    minlen = min(len(b1), len(b2))
    for symbol in range(minlen):
        if not b1[symbol] == b2[symbol]:
            counter = counter + 1
        c = c + 1
    counter = counter + abs(len(b1) - len(b2))
    print(f"Operation {o}: diff    {name1}     {name2}\namino-acids difference: {counter}")
    return " "
def diff_seq(n):
    c = 0
    c2 = 0
    a = open(r"D:/python/lab-5/sequences.0.txt", "r")
    b = open(r"D:/python/lab-5/commands.0.txt", "r")
    seq = a.read()
    seq = seq.split("\n")
    comm = b.read()
    comm = comm.split("\n")
    commtable = comm[n].split("	")
    for i in range(5):
        seqtable = seq[c].split("	")
        if commtable[1] in seqtable[0]:
            b1 = seqtable[2]
        c = c + 1
        seqtable = seq[c2].split("	")
        if commtable[2] in seqtable[0]:
            b2 = seqtable[2]
        c2 = c2 + 1
    return b1, b2
n = 0
o = 1
for i in range(8):
    command = command_find(n)
    if command == "search":
        x = search_seq(n)
        search(x, n, o)
    if command == "diff":
        b1 = diff_seq(n)[0]
        b2 = diff_seq(n)[1]
        print(diff(b1, b2, n))
    if command == "mode":

    n = n + 1
    o = o + 1