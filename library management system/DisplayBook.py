def Display():
    with open("Books.txt", "r") as f:
              lines = f.read()
              print(" We have Following Books available")
              print("__________________________________")
              
              print(lines)
              print()

Display()
