import Date
import LS

def Return():
    name = input("Enter name:")
    a = "Borrow-" + name + ".txt"
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]

        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        print("The name was invalid")
        Return()

    b = "return-" + name + ".txt"
    with open(b, "w+")as f:
        f.write(" Royal library \n")
        f.write(" Returned By: " + name + "\n")
        f.write(" Date: " + Date.getDate() + "    Time:" + Date.getTime() + "\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")

    total = 0.0
    for i in range(3):
        if LS.bookname[i] in data:
            with open(b, "a") as f:
                f.write(str(i + 1) + "\t\t" + LS.bookname[i] + "\t\t$" + LS.cost[i] + "\n")
                LS.quantity[i] = int(LS.quantity[i]) + 1
            total += float(LS.cost[i])

   
    print("Is returned time expired")
    print("Press Y for Yes and N for No")
    stat = input()
    if (stat.upper() == "Y"):
        print("How many days was it returned late")
        D= int(input())
        fine= 3 * D
        with open(b, "a")as f:
            f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
        total = total + fine

    print("Final Total: " + "$" + str(total))
    with open(b, "a")as f:
        f.write("\t\t\t\t\tTotal: $" + str(total))

    with open("Books.txt", "w+") as f:
        for i in range(3):
            f.write(
                LS.bookname[i] + "," + LS.authorname[i] + "," + str(LS.quantity[i]) + "," + "$" +
                LS.cost[i] + "\n")




