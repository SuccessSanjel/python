import BorrowBook
import Date
import LS
import ReturnBook
import DisplayBook



while(True):
    print("                     Welcome to Royal Library Management System ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Enter 1 To Display")
    print("Enter 2: To Borrow a Book")
    print("Enter 3: To Return a Book")
    print("Enter 4: To Exit")
    try:
        IN = int(input("Select from 1 to 4 "))
        print()
        if (IN == 1):
            DisplayBook.Display()
        elif(IN == 2):
             
            LS.listSplit()
            BorrowBook.Borrow()
        elif(IN == 3):
            LS.listSplit()
            ReturnBook.Return()
        elif(IN == 4):
            print("Thank you for using  ")
            break
        else:
            print("Please enter a valid number")
    except ValueError:
        print("Please input as suggested.")
