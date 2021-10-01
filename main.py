one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"
avaliable_choises = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
usercurrentchoice = ""


def tictactoe():
    print("\n")
    print("\t     |     |")
    print(f"\t {one}   |  {two}  |  {three} ")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t {four}   |  {five}  |  {six} ")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print(f"\t {seven}   |  {eight}  |  {nine} ")
    print("\t     |     |")
    print("\n")


current_player = 0
current_symbol = ""
player1name = ""
player2name = ""
current_name = ""
iswin = False


def turns():
    if current_player == 1:
        print(f"{player1name} Turns '{current_symbol}'")
    else:
        print(f"{player2name} Turns '{current_symbol}'")


def changeturn():
    global current_player, current_symbol, current_name
    if current_player == 0:
        current_player = 1
        current_symbol = "X"
        current_name = player1name
    elif current_player == 1:
        current_player = 2
        current_symbol = "O"
        current_name = player2name
    else:
        current_player = 1
        current_symbol = "X"
        current_name = player1name


def placeuserchoice(inn):
    global one, two, three, four, five, six, seven, eight, nine
    if inn == "1":
        one = current_symbol
    elif inn == "2":
        two = current_symbol
    elif inn == "3":
        three = current_symbol
    elif inn == "4":
        four = current_symbol
    elif inn == "5":
        five = current_symbol
    elif inn == "6":
        six = current_symbol
    elif inn == "7":
        seven = current_symbol
    elif inn == "8":
        eight = current_symbol
    elif inn == "9":
        nine = current_symbol
    else:
        print("some thing is wrong")


def checkwin():
    global avaliable_choises, one, two, three, four, five, six, seven, eight, nine, iswin
    if (one == two and two == three) \
            or (one == four and four == seven) \
            or (two == five and five == eight) \
            or (three == six and six == nine) \
            or (four == five and five == six) \
            or (seven == eight and eight == nine) \
            or (one == five and five == nine) \
            or (three == five and five == seven):
        iswin = True
        print("\n----------------------------------")
        print(f"{current_name} Wins")
        print("----------------------------------\n")
    else:
        if (not avaliable_choises) and (not iswin):
            print("\n----------------------------------")
            print("Game Draw")
            print("----------------------------------\n")
        else:
            changeturn()
            turns()
            return getchoiceinput()


def getchoiceinput():
    global usercurrentchoice, avaliable_choises
    usercurrentchoice = input('Enter Your Choice: ')
    if avaliable_choises.__contains__(usercurrentchoice):
        placeuserchoice(usercurrentchoice)
        avaliable_choises.remove(usercurrentchoice)
        tictactoe()
        return checkwin()
    else:
        print(f"Not Avaliable Chose From {avaliable_choises}")
        return getchoiceinput()


print("Welcome To Tic Tac Toe")
print("======================\n")


def start():
    global player1name, player2name
    player1name = input('Enter Player One Name ')
    player2name = input('Enter Player Two Name ')
    if player1name == "" or player2name == "":
        print("\nPlease Enter Players Name ITs Required")
        print("**************************************\n")
        return start()

    print("\n----------------------------------")
    print(f"player 1 {player1name} Symbol 'X' ")
    print(f"player 2 {player2name} Symbol 'O' ")
    print("----------------------------------\n")
    changeturn()
    turns()
    tictactoe()
    getchoiceinput()


start()
