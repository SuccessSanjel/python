def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    bookname = []
    authorname = []
    quantity = []
    cost = []
    with open("Books.txt","r") as f:

        lines = f.readlines()
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ID = 0
            for a in lines[i].split(','):
                if(ID== 0):
                    bookname.append(a)
                elif(ID == 1):
                    authorname.append(a)
                elif(ID == 2):
                    quantity.append(a)
                elif(ID== 3):
                    cost.append(a.strip("$"))
                ID += 1
