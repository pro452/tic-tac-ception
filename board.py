"""

Written by: Michael Matthews
Updated: 4-2-18
Written for: Artifical Intelligence

This program is a game called Tic-Tac-Ception which the oppenent is an AI that uses minimax with alpha-beta triming




possible features:
    - have it play itself against a dummy that goes in random places and see how times it wins

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
                       [54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,69,75,76,77],[60,61,62,70,71,72,78,79,80]] #the indexs of each small board in order top left to bottom right
        #boardNumber = 4

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
            print(updateBoard())
            return whichBoard(position)

        def yourTurn(boardNumber):
            user = raw_input()
            while(user != 'x'):
                if int(user) in occupied:
                    print("SPOT ALREADY TAKEN TRY AGAIN!")
                    user = raw_input()
                elif not int(user) in boardIndexs[boardNumber]:
                    print("You must got in board ", boardNumber)
                    user = raw_input()
                else:
                    self.Values[int(user)] = player
                    occupied.add(int(user))
                    print(updateBoard())
                    boardNumber = oppenentTurn(whichBoard(int(user)))
                    print("\nWhere would you like to go? \nEnter in the form of a coorindat")
                    user = raw_input()

        yourTurn(4)

        print("Okay you'll be playing as " + player + '.')
Board()