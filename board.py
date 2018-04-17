"""

Written by: Michael Matthews
Updated: 4-2-18
Written for: Artifical Intelligence

This program is a game called Tic-Tac-Ception which the oppenent is an AI that uses minimax with alpha-beta triming


possible features:
    - have it play itself against a dummy that goes in random places and see how times it wins
    - Perform screen clear after each turn

"""

import random

class Board():

    #Constructor initlizes the board to an empty state and then proceeds to call the main function
    def __init__(self):
        self.Values = []
        for index in range(0,81):
            self.Values.append(" ")
        self.Boards = []
        self.main()

    def main(self):
        player = "" #the players symbol
        oppenent = "" #the AIs symbol
        occupied = set() #parts of the board that contain either an 'X' or 'O'
        #occupied = occupied.append(-1)
        boardIndexs = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],
                       [27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],
                       [54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]] #the indexs of each small board in order top left to bottom right
        #boardNumber = 4
        winningRows = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #these are all the possible ways to win a tic-tac-toe board
        wonBoards = []    #this list will contain the index of all small boards that have been won
        playerWins = []   #ths list will contain the index of boards that the player has won
        oppenentWins = [] #this list will contain the index of boards that the oppenent has won

        #This function returns the game board represented as an string
        def updateBoard():
            return "\n  " + self.Values[0] + " | " + self.Values[1] + " | " + self.Values[2] + "   ||   " + self.Values[3] + " | " + self.Values[4] + " | " + self.Values[5] + "   ||   " + self.Values[6] + " | " + self.Values[7] + " | " + self.Values[8] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + self.Values[9] + " | " + self.Values[10] + " | " + self.Values[11] + "   ||   " + self.Values[12] + " | " + self.Values[13] + " | " + self.Values[14] + "   ||   " + self.Values[15] + " | " + self.Values[16] + " | " + self.Values[17] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + self.Values[18] + " | " + self.Values[19] + " | " + self.Values[20] + "   ||   " + self.Values[21] + " | " + self.Values[22] + " | " + self.Values[23] + "   ||   " + self.Values[24] + " | " + self.Values[25] + " | " + self.Values[26] + "   \n" \
                     "===============================================\n" \
                     "  " + self.Values[27] + " | " + self.Values[28] + " | " + self.Values[29] + "   ||   " + self.Values[30] + " | " + self.Values[31] + " | " + self.Values[32] + "   ||   " + self.Values[33] + " | " + self.Values[34] + " | " + self.Values[35] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + self.Values[36] + " | " + self.Values[37] + " | " + self.Values[38] + "   ||   " + self.Values[39] + " | " + self.Values[40] + " | " + self.Values[41] + "   ||   " + self.Values[42] + " | " + self.Values[43] + " | " + self.Values[44] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + self.Values[45] + " | " + self.Values[46] + " | " + self.Values[47] + "   ||   " + self.Values[48] + " | " + self.Values[49] + " | " + self.Values[50] + "   ||   " + self.Values[51] + " | " + self.Values[52] + " | " + self.Values[53] + "   \n" \
                     "===============================================\n" \
                     "  " + self.Values[54] + " | " + self.Values[55] + " | " + self.Values[56] + "   ||   " + self.Values[57] + " | " + self.Values[58] + " | " + self.Values[59] + "   ||   " + self.Values[60] + " | " + self.Values[61] + " | " + self.Values[62] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + self.Values[63] + " | " + self.Values[64] + " | " + self.Values[65] + "   ||   " + self.Values[66] + " | " + self.Values[67] + " | " + self.Values[68] + "   ||   " + self.Values[69] + " | " + self.Values[70] + " | " + self.Values[71] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + self.Values[72] + " | " + self.Values[73] + " | " + self.Values[74] + "   ||   " + self.Values[75] + " | " + self.Values[76] + " | " + self.Values[77] + "   ||   " + self.Values[78] + " | " + self.Values[79] + " | " + self.Values[80] + "   \n"

        #Game loop starts
        while(player == ''):
            print("\nWelcome to M&M's Tic-Tac-Ception!\n\nWill you be playing as 'X' or 'O'?")
            user = input()

            if user == 'x' or user == 'X':
                player = 'X'
                oppenent = 'O'
            elif user == 'o' or user == 'O':
                player = 'O'
                oppenent = 'X'
            else:
                print("Please enter a valid symbol!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print(updateBoard())

        print("\nWhere would you like to go? \nEnter in the form of a coordinate")

        #This functiono calculates the h-value for a particular board
        def hValue(boardNumber):
            playerPieces = []
            oppenentPieces = []
            playersHValue = 0

            empty = True
            for number in boardIndexs[boardNumber]:
                if number in occupied:
                    empty = False

            if empty:
                return 0

            for number in range(0,9):
                if self.Values[boardIndexs[boardNumber][number]] == player:
                    playerPieces.append(number)
                elif self.Values[boardIndexs[boardNumber][number]] == oppenent:
                    oppenentPieces.append(number)

            if len(playerPieces) == 0:
                return 0

            for list in winningRows:
                for playerSymbol in playerPieces:
                    if playerSymbol in list:
                        for oppenentSymbol in oppenentPieces:
                            if not oppenentSymbol in list:
                                playersHValue += 1

            print(playersHValue)

            print(playerPieces)
            print(oppenentPieces)

        #This function checks the specified board to see if either the player or oppenet has 3 in a row there by winning that specified board
        #It returns
        #   0 if the player has won
        #   1 if the oppenent has won
        #   -1 if nobody has won the board
        def checkBoard(boardNumber):
            playerPieces = []
            oppenentPieces = []

            for number in range(0, 9):
                if self.Values[boardIndexs[boardNumber][number]] == player:
                    playerPieces.append(number)
                elif self.Values[boardIndexs[boardNumber][number]] == oppenent:
                    oppenentPieces.append(number)

            #playerPieces = set(playerPieces)
            #oppenentPieces = set(oppenentPieces)

            for list in winningRows:
                if list[0] in playerPieces and list[1] in playerPieces and list[2] in playerPieces:
                    return 0
                elif list[0] in oppenentPieces and list[1] in oppenentPieces and list[2] in oppenentPieces:
                    return 1

            return -1

        #This funcition checks to see if anybody has won the entire game, or if there was a tie
        #If somebody has won it clean exits
        def gameOver():
            if len(wonBoards) < 3:
                return

            for list in winningRows:
                if list[0] in playerWins and list[1] in playerWins and list[2] in playerWins:
                    print("Congratulations You've won!!!!!!!!")
                    exit(0)
                elif list[0] in oppenentWins and list[1] in oppenentWins and list[2] in oppenentWins:
                    print("You've lost...")
                    exit(0)

            return

        #This function updates the board to show that either the player or oppenent has won
        #If 'X' won then it updates that particular board, filling it up with X's in the shape of an X
        #If 'O' won then it updates that particular board, filling it up with O's in the shape of an O
        def wonRow(boardNumber, whoWon):
            list = boardIndexs[boardNumber]

            if whoWon == 'X':
                self.Values[list[0]] = 'X'
                self.Values[list[2]] = 'X'
                self.Values[list[4]] = 'X'
                self.Values[list[6]] = 'X'
                self.Values[list[8]] = 'X'
                self.Values[list[1]] = ' '
                self.Values[list[3]] = ' '
                self.Values[list[5]] = ' '
                self.Values[list[7]] = ' '
            else:
                self.Values[list[0]] = 'O'
                self.Values[list[1]] = 'O'
                self.Values[list[2]] = 'O'
                self.Values[list[3]] = 'O'
                self.Values[list[5]] = 'O'
                self.Values[list[6]] = 'O'
                self.Values[list[7]] = 'O'
                self.Values[list[8]] = 'O'
                self.Values[list[4]] = ' '

            updateBoard()

            wonBoards.append(boardNumber)
            for index in range(0,9):
                occupied.add(list[index])

        #Given an speicifed position return which position its in a smaller tic-tac-toe board
        def whichBoard(number):
            for board in range (0,9):
                for position in range(0,9):
                    if number == boardIndexs[board][position]:
                        return position
            return -1

        #Given an specified position return which board it's in
        def whereAmI(number):
            for board in range(0,9):
                for position in range(0,9):
                    if number == boardIndexs[board][position]:
                        return board

        #This function represents the AI taking a turn
        def oppenentTurn(boardNumber):
            if len(occupied) >= 81:
                print("What a draw!")
                exit(0)

            position = -1
            got_a_number = False
            first_corner_play = True

            for number in boardIndexs[boardNumber]:
                if number in occupied:
                    first_corner_play = False

            if(first_corner_play):
                position = boardIndexs[boardNumber][0]
                got_a_number = True

            while not got_a_number:
                position = random.randint(0,80)
                if not position in occupied and boardNumber in wonBoards:
                    got_a_number = True
                if (not position in occupied) and (position in boardIndexs[boardNumber]): #check for board
                    got_a_number = True

            self.Values[position] = oppenent
            occupied.add(position)
            if checkBoard(whereAmI(position))== 1:
                wonRow(whereAmI(position), oppenent)
                oppenentWins.append(whereAmI(position))
            else:
                checkIfFull(whereAmI(position))
            print(updateBoard())
            print(hValue(boardNumber))
            gameOver()
            return whichBoard(position)

        def checkIfInWonBoard(position):
            if(len(wonBoards)==0):
                return False
            for board in range(0, len(wonBoards)):
                if position in boardIndexs[wonBoards[board]]:
                    return True
            return False

        #Checks if a given board is full
        def checkIfFull(boardNumber):
            for index in range(0,9):
                if not (boardIndexs[boardNumber][index] in occupied):
                    return
            wonBoards.append(boardNumber)
            return

        #This function represents the player taking a turn
        def yourTurn(boardNumber):
            user = ""
            # while(user == '' ):
            #     user = input()

            parsed = False
            while not parsed:
                try:
                    user = int(input('Input: '))
                    parsed = True
                except ValueError:
                    print('Invalid value!')

            while(user != -1):
                if int(user) in occupied:
                    print("SPOT ALREADY TAKEN TRY AGAIN!")
                    try:
                        user = int(input('Input: '))
                        parsed = True
                    except ValueError:
                        print('Invalid value!1')
                if not int(user) in boardIndexs[boardNumber] and not boardNumber in wonBoards:
                    print("You must got in board ", boardNumber)
                    try:
                        user = int(input('Input: '))
                        parsed = True
                    except ValueError:
                        print('Invalid value!2')
                else:
                    self.Values[int(user)] = player
                    occupied.add(int(user))
                    print(updateBoard())
                    print("checking board")
                    print(whereAmI(int(user)))
                    print(checkBoard(whereAmI(int(user))))
                    if checkBoard(whereAmI(int(user))) == 0:
                        wonRow(whereAmI(int(user)), player)
                        playerWins.append(whereAmI(int(user)))
                    else:
                        checkIfFull(whereAmI(int(user)))
                    #print("board number: ", whichBoard(int(user)))
                    gameOver()
                    boardNumber = oppenentTurn(whichBoard(int(user)))
                    if len(occupied) >= 81:
                        print("What a draw!")
                        exit(0)
                    print("\nWhere would you like to go? \nEnter in the form of a coordinate")
                    try:
                        user = int(input('Input: '))
                        parsed = True
                    except ValueError:
                        print('Invalid value!')

        def genTree(boardNumber):
            tempOccupied = occupied.copy()
            possibleMoves = []
            for index in range(0,9):
                if not boardIndexs[boardNumber][index] in occupied:
                    possibleMoves.append(boardIndexs[boardNumber][index])
            if len(possibleMoves) == 0:
                return

        print("Okay you'll be playing as " + player + '.')
        yourTurn(4)
Board()