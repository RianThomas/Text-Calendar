import time
import os

#Colors that are important for color coding in the calender
RESET = "\u001b[0m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = '\u001b[34m'
RED = "\u001b[31m"
MANGENTA = "\u001b[35m"

#The number of days in each month
month = {
    "1":31,
    "2":28,
    "3":31,
    "4":30,
    "5":31,
    "6":30,
    "7":31,
    "8":31,
    "9":30,
    "10":31,
    "11":30,
    "12":31
}
#Important Lists
days = [] 
befdays = [] #Days before the starting day
taskn = [] #These lists are here for the tasks
taskd = []
taski = []
taskde = []

beforedays = False

#Important functions
def settings():
    global beforedays
    clear()
    print("1 - First Numbers")
    option2 = input()
    if option2 == "1":
        clear() #Just check if it is true or false and based on that change it
        if beforedays:
            print("Before days are turned on. Do you want to keep that? Y/N")
        else:
            print("Before days are turned off. Do you want to keep that? Y/N")
        choice = input()
        if (choice == "Y") and beforedays:
            print("Ok!")
        elif choice == "N" and beforedays:
            print("The before days are removed!")
            beforedays = False
        elif choice == "Y" and not beforedays:
            print("Ok!")
        elif choice == "N" and not beforedays:
            print("The before days are added!")
            beforedays = True
        time.sleep(2)
def tasks():
    clear()
    print("1 - Add a Task       2 - Delete a task")
    option1 = input()
    clear()
    if option1 == "1":
        print("Name: ")
        name = input()
        taskn.append(name)
        x = True
        while x:
            print("Date: (Format: year month day hourmil NO SPACES)") #Like 241128 for 2024 November 28th
            date = input()
            try: 
                trier = int(date)
                x = False
                taskd.append(int(date + str(len(taskn)))) #Add a check thing to see if it is an integer
            except:
                print("This needs to be an integer!")
                x = True
            
        print("Importance (N/A exactly): ")
        importa = input()
        if importa != "N/A":
            taski.append(importa) #Find a way to make the importance optional and colorful
        print("Description: ")
        descr = input()
        taskde.append(descr)
        # Tasks
        # ------------------
        # (1)  task         Date            Importance (in color?)
        # ... <-- All the tasks go under here
    if option1 == "2": #This part of the tasks allows you to delete a task
        y = True
        while y:
            if len(taskn) > 0:
                print("Which task would you like to delete? (number)")
                changer = input()
                try:
                    b = int(changer)
                    taskn.pop(int(str(taskd[int(changer)-1])[8:len(str(taskd[int(changer)-1]))])-1)
                    taskde.pop(int(str(taskd[int(changer)-1])[8:len(str(taskd[int(changer)-1]))])-1)
                    try:
                        taski.pop(int(str(taskd[int(changer)-1])[8:len(str(taskd[int(changer)-1]))])-1)
                    except:
                        pass
                    taskd.pop(int(changer)-1)
                except:
                    print("It needs to be an integer!")
                
            
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

current_time = time.localtime()
startday = (time.ctime(time.time() - (int(time.ctime(time.time())[8:10])-1) * 86400)[0:3]) #Finds the first day of the month
current_timeID = (str(current_time.tm_year)[2:4] + str(current_time.tm_mon) + str(current_time.tm_mday)) #Creates a time ID for task ordering

#This gets all the days before the month
if startday == "Mon":
    for i in range(0,1):
        befdays.append(i - month[str(time.gmtime()[1]-1)] + 59)
        days.append(" ")
if startday == "Tue":
    for i in range(0,2):
        befdays.append(i - month[str(time.gmtime()[1]-1)] + 59)
        days.append(" ")
if startday == "Wed":
    for i in range(0,3):
        befdays.append(i - month[str(time.gmtime()[1]-1)] + 59)
        days.append(" ")
if startday == "Thu":
    for i in range(0,4):
        befdays.append(i - month[str(time.gmtime()[1]-1)] + 59)
        days.append(" ")
if startday == "Fri":
    for i in range(0,5):
        befdays.append(i - month[str(time.gmtime()[1]-1)] + 58)
        days.append(" ")
if startday == "Sat":
    for i in range(0,6):
        befdays.append(i - month[str(time.gmtime()[1]-1)] + 59)
        days.append(" ")

for i in range(0, month[str(time.gmtime()[1])]): #This gets all the rest of the days of the month
    days.append(str(i - (int(time.ctime(time.time())[8:10])) + (int(time.ctime(time.time())[8:10])) + 1))

#This color codes the current day so the user is able to identify the current day
if str(time.asctime()[8:10]) in days:
    if len(str(days[days.index(str(time.asctime()[8:10]))])) == 2:
        days[days.index(str(time.asctime()[8:10]))] = f'{BLUE} ' + days[days.index(str(time.asctime()[8:10]))] + f'{RESET}'
else:
    days[days.index(str(time.asctime()[9:10]))] = f'{BLUE}  ' + days[days.index(str(time.asctime()[9:10]))] + f'{RESET}' #This may not work depending on the amount of numbers in the day

while True:
    if beforedays:
        for j in range(0, len(befdays)):
            days[j] = f'{RED}' + str(befdays[j]) + f'{RESET}' #Have no idea if this works

    print("       " + time.asctime()[4:8] + str(current_time.tm_year)[0:4]) #Prints the month
    print("")
    print("  S  M  T  W  T  F  S")
    for i in range(0, len(days)): #Determines the number of spaces needed based on the size of the number
        if len(str(days[i])) == 2:
            days[i] = " " + str(days[i])
        if len(str(days[i])) == 1:
            days[i] = "  " + str(days[i])

    #Prints out the days
    print(str(days[0]) + str(days[1]) + str(days[2]) + str(days[3]) + str(days[4]) + str(days[5]) + str(days[6]))
    print(str(days[7]) + str(days[8]) + str(days[9]) + str(days[10]) + str(days[11]) + str(days[12]) + str(days[13]))
    print(str(days[14]) + str(days[15]) + str(days[16]) + str(days[17]) + str(days[18]) + str(days[19]) + str(days[20]))
    print(str(days[21]) + str(days[22]) + str(days[23]) + str(days[24]) + str(days[25]) + str(days[26]) + str(days[27]))
    laststr = ""
    for j in range(28, month[str(time.gmtime()[1])]):
        laststr += (str(days[j]))
    print(laststr)
    #The stuff under the calender used for the other functions
    print("")
    if len(taskn) > 0:
        print("          Tasks")
        print("-------------------------")
        taskd.sort()
        for i in range(0, len(taskn)):
            if len(taski) > int(str(taskd[i])[8:len(str(taskd[i]))])-1:
                print("(" + str(i + 1) + ")" + "    " + taskn[int(str(taskd[i])[8:len(str(taskd[i]))])-1] + "    Due: " + str(taskd[i])[2:4] + "/" + str(taskd[i])[4:6] + "/" + str(taskd[i])[0:2] + "      Importance: " + taski[int(str(taskd[i])[8:len(str(taskd[i]))])-1] + "       Description: " + taskde[int(str(taskd[i])[8:len(str(taskd[i]))])-1]) #How to check for the first one
            else:
                print("(" + str(i + 1) + ")" + "    " + taskn[int(str(taskd[i])[8:len(str(taskd[i]))])-1] + "    Due: " + str(taskd[i])[2:4] + "/" + str(taskd[i])[4:6] + "/" + str(taskd[i])[0:2] + "       Description: " + taskde[int(str(taskd[i])[8:len(str(taskd[i]))])-1])
    print("")
    print("Functions: ")
    print("s - Settings \nt - Tasks")
    option = input()
    if option == "s":
        settings()
    if option == "t":
        tasks()
    clear()
