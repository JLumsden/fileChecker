first = open(input("Let's check if your files are the same!\nEnter the first file name: "), 'r')
second = open(input("Enter the second file name: "), 'r')
while True:
    firstCont = ""
    secondCont = ""
    for line in first:
        firstCont = line
        break
    for line in second:
        secondCont = line
        break
    if firstCont != secondCont:
        print("They are not identical, here is the difference:\n" + firstCont + "\n" + secondCont)
        break
    elif firstCont == secondCont and firstCont == "":
        print("They are identical.")
        break
first.close()
second.close()
