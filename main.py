#Importing neccessary libraries
import pandas as pd

#Header colors
class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#Header
print(bcolors.FAIL + bcolors.BOLD + "GRADER" + bcolors.ENDC)

#Creating empty lists
Name = []
Reg_no = []
FDA = []
CHEM = []
MAT = []
BIO = []
POE = []
LAN = []
GA = []
MECH = []
Total = []
Percent = []
Grade = []
Rank = []

#Condition for running the loop
running = True

#Starting the loop
while running:
    print("===================")
    actions = ["Marks Entry", "Results", "Exit"]
    i = 0
    for action in actions:
        print(str(i + 1) + ".", actions[i])
        i += 1
    #Input action from user
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        #Input no of students
        n = int(input("Enter no of students: "))

        #Loop for getting data from user
        for i in range(0, n):
            name = input("Enter name: ")
            reg = input("Enter Reg. NO: ")
            fda = int(input("Enter marks in FDA: "))
            chem = int(input("Enter marks in CHEMISTRY: "))
            mat = int(input("Enter marks in MATHS: "))
            bio = int(input("Enter marks in BIOLOGY: "))
            poe = int(input("Enter marks in POE: "))
            lan = int(input("Enter marks in LANGUAGE: "))
            ga = int(input("Enter marks in GENERAL APTITUDE: "))
            mech = int(input("Enter marks in MECHANICAL: "))
            Name.append(name)
            Reg_no.append(reg)
            FDA.append(fda)
            CHEM.append(chem)
            MAT.append(mat)
            BIO.append(bio)
            POE.append(poe)
            LAN.append(lan)
            GA.append(ga)
            MECH.append(mech)
            Total.append(fda + chem + mat + bio + poe + lan + ga + mech)
            Percent.append(Total[i] / 800 * 100)
            if Percent[i] >= 90 and Percent[i] <= 100:
                Grade.append('O')
            elif Percent[i] >= 80 and Percent[i] < 90:
                Grade.append('A+')
            elif Percent[i] >= 70 and Percent[i] < 80:
                Grade.append('B+')
            elif Percent[i] >= 60 and Percent[i] < 70:
                Grade.append('B')
            elif Percent[i] >= 50 and Percent[i] < 60:
                Grade.append('C')
            elif Percent[i] < 50:
                Grade.append('F')
            Rank.append(i + 1)

        #Dictionary with subject wise marks
        students = {'Name': Name, 'Reg_no': Reg_no, 'FDA': FDA, 'CHEM': CHEM, 'MATHS': MAT, 'BIO': BIO, 'POE': POE, 'LAN': LAN,
                    'GA': GA, 'MECH': MECH}

        #Dictionary with overall performance of each student
        student = {'Name': Name, 'Reg_no': Reg_no, 'Total': Total, 'Percentage': Percent, 'Grade': Grade}

        label = []
        for i in range(1, n + 1):
            label.append(i)

        #DataFrame with subject wise marks
        data1 = pd.DataFrame(students, index=label)
        print("Marks entered: \n")
        print(data1)

        #DataFrame with overall performance of each student
        data2 = pd.DataFrame(student, index=Reg_no)

        #DataFrame with Ranks
        data3 = data2.sort_values(by="Total", ascending=False)
        data3['Rank'] = Rank
        data3.set_index('Reg_no')

        actions_ask1 = ["Go Back to main menu", "Exit"]
        i = 0
        for action in actions_ask1:
            print(str(i + 1) + ".", actions_ask1[i])
            i += 1
        #Input further action from user
        choice2 =int(input("Choose action: "))
        if choice2 == 1:
            continue
        elif choice2 == 2:
            running = False

    elif index == 1:
        if len(Name) == 0:
            print("No records!")
        else:
            print(data1)
            actions_ask2 = ["Individual result", "Rank sheet", "Go to main menu", "Exit"]
            i = 0
            for action in actions_ask2:
                print(str(i + 1) + ".", actions_ask2[i])
                i += 1
            #Input further action from user
            choice2 = int(input("Choose action: "))
            if choice2 == 1:
                choice3 = input("Enter Reg. No of the student: ")
                check = 0
                for reg in Reg_no:
                    if choice3 == data3['Reg_no'][reg]:
                        print(data3.loc[reg])
                    else:
                        check += 1
                if check == n:
                    print("No record found!")

            elif choice2 == 2:
                print(data3)
            elif choice2 == 3:
                continue
            elif choice == 4:
                running = False

    #Ending the loop
    elif index == 2:
        running = False
