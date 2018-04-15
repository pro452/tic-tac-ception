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
        winningRows = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,5]]
        wonBoards = []

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

        while(player == ''):
            print("\nWelcome to M&M's Tic-Tac-Ception!\n\nWill you be playing as 'X' or 'O'?")
            user = raw_input()

            if user == 'x' or user == 'X':
                player = 'X'
                oppenent = 'O'
            elif user == 'o' or user == 'O':
                player = 'O'
                oppenent = 'X'
            else:
                print("Please enter a valid symbol!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print(updateBoard())

        print("\nWhere would you like to go? \nEnter in the form of a coorindat")

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

        def whichBoard(number):
            for board in range (0,9):
                for position in range(0,9):
                    if number == boardIndexs[board][position]:
                        return position
            return -1

        def oppenentTurn(boardNumber):
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
                if (not position in occupied) and (position in boardIndexs[boardNumber]): #check for board
                    got_a_number = True

            self.Values[position] = oppenent
            occupied.add(position)
            if checkBoard(boardNumber)== 1:
                wonRow(boardNumber, oppenent)
            print(updateBoard())
            print(hValue(boardNumber))
            return whichBoard(position)

        def checkIfInWonBoard(position):
            if(len(wonBoards)==0):
                return False
            for board in range(0, len(wonBoards)):
                if position in boardIndexs[wonBoards[board]]:
                    return True
            return False

        def yourTurn(boardNumber):
            user = ""
            # while(user == '' ):
            #     user = raw_input()

            parsed = False
            while not parsed:
                try:
                    user = int(raw_input('Only Numbers! Try agin: '))
                    parsed = True
                except ValueError:
                    print('Invalid value!')

            while(user != -1):
                if int(user) in occupied:
                    print("SPOT ALREADY TAKEN TRY AGAIN!")
                    try:
                        user = int(raw_input('Input: '))
                        parsed = True
                    except ValueError:
                        print('Invalid value!1')
                elif not int(user) in boardIndexs[boardNumber] and not boardNumber in wonBoards:
                    print("You must got in board ", boardNumber)
                    try:
                        user = int(raw_input('Input: '))
                        parsed = True
                    except ValueError:
                        print('Invalid value!2')
                else:
                    self.Values[int(user)] = player
                    occupied.add(int(user))
                    print(updateBoard())
                    if checkBoard(boardNumber) == 0:
                        wonRow(boardNumber, player)
                    #print("board number: ", whichBoard(int(user)))

                    boardNumber = oppenentTurn(whichBoard(int(user)))
                    print("\nWhere would you like to go? \nEnter in the form of a coorindate")
                    try:
                        user = int(raw_input('Input: '))
                        parsed = True
                    except ValueError:
                        print('Invalid value!')

        yourTurn(4)

        print("Okay you'll be playing as " + player + '.')
Board()