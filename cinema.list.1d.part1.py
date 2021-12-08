from os import system
# LEGEND:
# 0 - free
# 1 - reserved
# 2 - bought
seats = [ 0, 0, 1, 2, 0, 0, 0, 0 ]
# index   0, 1, 2, 3, 4, 5, 6, 7
       
option = -1
while option != 0:
    # iterative count algorith ###########
    #free_seats = 0
    #for pi in range(len(seats)):
    #    if seats[pi] == 0:
    #        free_seats += 1
    free_seats = len(seats)
    for pi in range(len(seats)):
        if seats[pi] != 0:
            free_seats = free_seats - 1

    # ####################################        

    # ############### PLOT ###############
    system("cls")
    print()
    for pi in range(len(seats)):
        print("", pi+1, "", end = "  ")
    print()

    for pi in range(len(seats)):
        if seats[pi] == 1:
            print("|-|", end = "  ")
        elif seats[pi] == 2:
            print("|+|", end = "  ")
        else:
            print("| |", end = "  ")
    print("\nFree seats: ", free_seats)
    print("\n")
    # ############### PLOT ###############

    # ### Show MENU ######################
    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("---------------------------")
    # #################################### 


    option = int(input(">>>"))
    if option == 1:
        place = int(input("Which place? "))
        if place-1 in range(0,len(seats)):
            if seats[place-1] == 0:
                seats[place - 1] = 1
                print("You're booking was succesful")
            else:
                print("This seat is ocupied! PLease choose another one!")
        else:
            print("Please choose a existing seat")


    if option == 2:
        place = int(input("Which place? "))
        if place-1 in range(0,len(seats)):
            if seats[place-1] == 0:
                seats[place - 1] = 2
                print("You bought succesfully")
            else:
                print("This seat is ocupied! PLease choose another one!")
        else:
            print("Please choose a existing seat")


    if option == 3:
        place = int(input("Which place? "))
        if place-1 in range(0,len(seats)):
            if seats[place-1] == 1:
                seats[place - 1] = 0
                print("You canceled succesfully")
            else:
                print("You can't cancel!")
        else:
            print("Please choose a existing seat")             
            