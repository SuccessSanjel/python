import Date
import LS
def Borrow():
    A=False
    Total = 0
    while(True):
        FN=input("Enter the first name : ")
        if FN.isalpha():
            break
        print("Enter Name in Alphabet Form")
    while(True):
        LN=input("Enter the last name : ")
        if LN.isalpha():
            break
        print("Enter Name in alphabet form")
            
    t="Borrow-"+FN+".txt"
    with open(t,"w+") as f:
        f.write("                 Royal Library  \n")
        f.write("    Borrowed By: "+ FN+" "+LN+"\n")
        f.write(" Date: " + Date.getDate()+"    Time:"+ Date.getTime()+"\n\n")
        f.write("S.N. \t\t    Bookname: \t\tAuthorname: \n" )
        
   
    while A == False:
        print("Select One option:")
        for i in range(len(LS.bookname)):
            print("Enter", i, "to borrow book", LS.bookname[i])
    
        try:   
            a=int(input())
           
            try:
                
                if(int(LS.quantity[a])>0):
                    print("\n The book is available")
                    Total += int(LS.cost[a])
                 
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ LS.bookname[a]+"\t\t  "+LS.authorname[a]+"\n")

                    LS.quantity[a]=int(LS.quantity[a])-1
                    with open("Books.txt","w+") as f:
                        for i in range(5):
                            f.write(LS.bookname[i]+","+LS.authorname[i]+","+str(LS.quantity[i])+","+"$"+LS.cost[i]+"\n")


                    L=True
                    count=1
                    
                    while L==True:
                        choice=str(input(" Do u want to borrow any other books. If yes press Y and if no press N."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(LS.bookname)):
                                print("Enter", i, "to borrow book", LS.bookname[i])
                            a=int(input())
                            if(int(LS.quantity[a])>0):
                                print("Book is available")
                                Total += int(LS.cost[a])
                                
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ LS.bookname[a]+"\t\t  "+LS.authorname[a]+"\n")

                                LS.quantity[a]=int(LS.quantity[a])-1
                                with open("Books.txt","w+") as f:
                                    for i in range(5):
                                        f.write(LS.bookname[i]+","+LS.authorname[i]+","+str(LS.quantity[i])+","+"$"+LS.cost[i]+"\n")
                                        A=False
                            else:
                                L=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you: ")
                            print("")
                            L=False
                            A=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("That book is not available")
                    Borrow()
                    A=False
            except IndexError:
                print("")
                print("Please choose book acording to their ID")
        except ValueError:
            print("")
            print("Please choose as instructed")
    with open(t,"a") as f:
        f.write("\n\t\t\t\tTotal Price: $"+str(Total))
    



