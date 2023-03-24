###########################################
# Name:Amirhossein Mansouri
# Email:amir01mn@my.yorku.ca
###########################################


import random
import time
import utilites

def task1():
    def printOutcome(user , computer):
        if user == computer:
            print("A tie!")
        elif user == 1 and computer == 2:
            print("HAL wins!")
        elif user == 1 and computer == 3:
            print("You win!")
        elif user == 2 and computer == 1:
            print("You win!")
        elif user == 2 and computer == 3:
            print("HAL wins!")
        elif user == 3 and computer == 1:
            print("HAL wins!")
        elif user == 3 and computer == 2:
            print("You win!")




    print("Rock, Paper, Scissors!")
    answer = "Y"
    while(answer == "Y"):
        print("Make your selection. . .")
        user = int(input("(1) rock, (2) paper, (3) scissors? "))
        while user != 1 and user != 2 and user != 3:
            print("Invalid selection. Try again.")
            print("Make your selection. . .")
            user = int(input("(1) rock, (2) paper, (3) scissors? "))
        if user == 1:
            print("You: rock")

        elif user == 2:
            print("You: paper")
        elif user == 3:
            print("You: scissors")
        computer = random.randint(1, 3)
        if computer == 1:
            print("HAL: rock")
        elif computer == 2:
            print("HAL: paper")
        elif computer == 3:
            print("HAL: scissors")
        printOutcome(user, computer)
        answer = input("Play again (Y/N)")
        answer = answer.upper()


def task2():
    def swapAdjacentElements(alist):

        assert len(alist) >= 2, "Must enter two or more characters!"

        for i in range(0,len(alist)-1,2):
            cpy = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = cpy

    Str = input("Input two or more chars separated by spaces: ")
    Str = Str.replace(" ","")
    alist = []
    for i in range(len(Str)):
        alist.append(Str[i])
    print("Initial list")
    print(alist)
    print("String version: '{}'".format(Str))

    swapAdjacentElements(alist)
    Str2 =""

    print("Modified list")
    print(alist)
    for i in range(len(alist)):
        Str2 = Str2 + alist[i]
    print("String version: '{}'".format(Str2))

def task3():

    from utilites import students
    from utilites import studentsInfo
    finaldict = {}
    for index in range(len(students)):
        year = ""
        for i in range(1, 5):

            for value in studentsInfo["Year {}".format(i)]:
                if value == index:
                    year = "Year {}".format(i)

        program = ""
        for value in studentsInfo["CS"]:
            if value == index:
                program = "CS"
        for value in studentsInfo["DM"]:
            if value == index:
                program = "DM"
        for value in studentsInfo["BZ"]:
            if value == index:
                program = "BZ"
        for value in studentsInfo["SE"]:
            if value == index:
                program = "SE"

        campus = ""
        for value in studentsInfo["On Campus"]:
            if value == index:
                campus = "On Campus"
        for value in studentsInfo["Off Campus"]:
            if value == index:
                campus = "Off Campus"

        finaldict[students[index]] = "{0:>10} ({1}) Program: {2} Housing: {3}".format(students[index], year, program,
                                                                                      campus)

    for key in sorted(finaldict):
        print(finaldict[key])

def task4():
    input("Press enter to start aquarium...")

    creature1 = utilites.SeaLife(random.randint(0, 1), random.randint(5, 30))
    creature2 = utilites.SeaLife(random.randint(0, 1), random.randint(5, 30))
    creature3 = utilites.SeaLife(random.randint(0, 1), random.randint(5, 30))
    creature4 = utilites.SeaLife(random.randint(0, 1), random.randint(5, 30))
    creature5 = utilites.SeaLife(random.randint(0, 1), random.randint(5, 30))

    seaLifeList = [creature1, creature2, creature3, creature4, creature5]

    timeStep = 1

    while (timeStep <= 50):
        print(40 * "-" + f"Time: {timeStep}")
        for objects in seaLifeList:
            print(objects.getStr())
            objects.move()

        timeStep += 1
        time.sleep(0.3)


def main():

    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()

