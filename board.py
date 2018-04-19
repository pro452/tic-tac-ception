"""
Written by: Michael Matthews
Updated: 4-2-18
Written for: Artificial Intelligence

This program is a game called Tic-Tac-Ception which the opponent is an AI that uses min-max with alpha-beta trimming
"""
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
        boardIndexs = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],
                       [27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],
                       [54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]] #the indexs of each small board in order top left to bottom right
        winningRows = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]                        #these are all the possible ways to win a tic-tac-toe board
        wonBoards = []    #this list will contain the index of all small boards that have been won
        playerWins = []   #ths list will contain the index of boards that the player has won
        oppenentWins = [] #this list will contain the index of boards that the oppenent has won

        #This function returns the game board represented as an string
        def updateBoard(values):
            return "\n  " + values[0] + " | " + values[1] + " | " + values[2] + "   ||   " + values[3] + " | " + values[4] + " | " + values[5] + "   ||   " + values[6] + " | " + values[7] + " | " + values[8] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + values[9] + " | " + values[10] + " | " + values[11] + "   ||   " + values[12] + " | " + values[13] + " | " + values[14] + "   ||   " + values[15] + " | " + values[16] + " | " + values[17] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + values[18] + " | " + values[19] + " | " + values[20] + "   ||   " + values[21] + " | " + values[22] + " | " + values[23] + "   ||   " + values[24] + " | " + values[25] + " | " + values[26] + "   \n" \
                     "===============================================\n" \
                     "  " + values[27] + " | " + values[28] + " | " + values[29] + "   ||   " + values[30] + " | " + values[31] + " | " + values[32] + "   ||   " + values[33] + " | " + values[34] + " | " + values[35] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + values[36] + " | " + values[37] + " | " + values[38] + "   ||   " + values[39] + " | " + values[40] + " | " + values[41] + "   ||   " + values[42] + " | " + values[43] + " | " + values[44] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + values[45] + " | " + values[46] + " | " + values[47] + "   ||   " + values[48] + " | " + values[49] + " | " + values[50] + "   ||   " + values[51] + " | " + values[52] + " | " + values[53] + "   \n" \
                     "===============================================\n" \
                     "  " + values[54] + " | " + values[55] + " | " + values[56] + "   ||   " + values[57] + " | " + values[58] + " | " + values[59] + "   ||   " + values[60] + " | " + values[61] + " | " + values[62] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + values[63] + " | " + values[64] + " | " + values[65] + "   ||   " + values[66] + " | " + values[67] + " | " + values[68] + "   ||   " + values[69] + " | " + values[70] + " | " + values[71] + "   \n" \
                     "+---+---+---+ || +---+---+---+ || +---+---+---+ \n" \
                     "  " + values[72] + " | " + values[73] + " | " + values[74] + "   ||   " + values[75] + " | " + values[76] + " | " + values[77] + "   ||   " + values[78] + " | " + values[79] + " | " + values[80] + "   \n"

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

        print(updateBoard(self.Values))

        print("\nWhere would you like to go? \nEnter in the form of a coordinate")

        #This functiono calculates the h-value for a particular board
        def hValue(boardNumber, position, player):
            if player == oppenent:
                if whichBoard(position) in wonBoards:
                    return 1
                if checkBoard(boardNumber, self.Values) == 1 and whichBoard(position) in wonBoards:
                    return 5
                if whichBoard(position) == 0 or whichBoard(position) == 2 or whichBoard(position) == 6 or whichBoard(position) == 8:
                    return 6
                if checkBoard(boardNumber, self.Values) == 1:
                    return 10
                return 0
            else:
                print('Checking for board')
                print(boardNumber)
                if checkBoard(boardNumber, self.Values) == 0:
                    return -10
                if whichBoard(position) == 0 or whichBoard(position) == 2 or whichBoard(position) == 6 or whichBoard(position) == 8:
                    return -6
                if checkBoard(boardNumber, self.Values) == 0 and whichBoard(position) in wonBoards:
                    return -5
                if whichBoard(position) in wonBoards:
                    return -1
                return 0

        #This function checks the specified board to see if either the player or oppenet has 3 in a row there by winning that specified board
        #It returns
        #   0 if the player has won
        #   1 if the oppenent has won
        #   -1 if nobody has won the board
        def checkBoard(boardNumber, values):
            playerPieces = []
            oppenentPieces = []

            for number in range(0, 9):
                if values[boardIndexs[boardNumber][number]] == player:
                    playerPieces.append(number)
                elif values[boardIndexs[boardNumber][number]] == oppenent:
                    oppenentPieces.append(number)

            for list in winningRows:
                if list[0] in playerPieces and list[1] in playerPieces and list[2] in playerPieces:
                    return 0
                elif list[0] in oppenentPieces and list[1] in oppenentPieces and list[2] in oppenentPieces:
                    return 1
            return -1

        #This funcition checks to see if anybody has won the entire game, or if there was a tie
        #If somebody has won it clean exits
        def gameOver(wonBoards, playerWins,oppenentWins):
            if len(wonBoards) < 3:
                return 0

            for list in winningRows:
                if list[0] in playerWins and list[1] in playerWins and list[2] in playerWins:
                    print("Congratulations You've won!!!!!!!!")
                    exit(0)
                    return -1
                elif list[0] in oppenentWins and list[1] in oppenentWins and list[2] in oppenentWins:
                    print("You've lost...")
                    exit(0)
                    return 1

            return 0

        #This function updates the board to show that either the player or oppenent has won
        #If 'X' won then it updates that particular board, filling it up with X's in the shape of an X
        #If 'O' won then it updates that particular board, filling it up with O's in the shape of an O
        def wonRow(boardNumber, whoWon, values, wonBoards):
            list = boardIndexs[boardNumber]

            if whoWon == 'X':
                values[list[0]] = 'X'
                values[list[2]] = 'X'
                values[list[4]] = 'X'
                values[list[6]] = 'X'
                values[list[8]] = 'X'
                values[list[1]] = ' '
                values[list[3]] = ' '
                values[list[5]] = ' '
                values[list[7]] = ' '
            else:
                values[list[0]] = 'O'
                values[list[1]] = 'O'
                values[list[2]] = 'O'
                values[list[3]] = 'O'
                values[list[5]] = 'O'
                values[list[6]] = 'O'
                values[list[7]] = 'O'
                values[list[8]] = 'O'
                values[list[4]] = ' '

            updateBoard(values)

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
            possibleMoves = []
            badpossibleMoves = []
            goodpossibleMoves = []

            if not boardNumber in wonBoards:
                for index in range(0,9):
                    if not boardIndexs[boardNumber][index] in occupied:
                        possibleMoves.append(boardIndexs[boardNumber][index])

                max = -1000

                for index in range(0,len(possibleMoves)):
                    whatTempValues = self.Values.copy()
                    #tempValues = self.Values.copy()
                    tempWonBoards = wonBoards.copy()
                    tempOccupied = occupied.copy()

                    #print(type(tempValues[boardNumber][whichBoard(possibleMoves[index])]))
                    self.Values[whichBoard(possibleMoves[index])] = oppenent
                    temp = hValue(boardNumber,possibleMoves[index],oppenent)
                    if(checkBoard(boardNumber,self.Values))==1:
                        tempWonBoards.append(whereAmI(possibleMoves[index]))

                    playerPossibleMoves = []
                    tempBoardNumber = whichBoard(possibleMoves[index])

                    for playerIndex in range(0,9):
                        if not boardIndexs[tempBoardNumber][playerIndex] in tempOccupied:
                            playerPossibleMoves.append(boardIndexs[boardNumber][playerIndex])

                    min = 1000

                    for playerIndex in range(0,len(playerPossibleMoves)):
                        playerTempValues = self.Values.copy()
                        #playerTempWonBoards = tempWonBoards.copy()
                        #playerTempOccupied = tempOccupied.copy()
                        #playerTempValues[whichBoard(possibleMoves[playerIndex])] = player
                        self.Values[playerPossibleMoves[playerIndex]] = player
                        playerTemp = hValue(tempBoardNumber,playerPossibleMoves[playerIndex],player)
                        print(updateBoard(self.Values))
                        #if(checkBoard(tempBoardNumber,playerTempValues)==0):

                        if playerTemp < min:
                            min = playerTemp
                            if not possibleMoves[index] in badpossibleMoves:
                                badpossibleMoves.append([possibleMoves[index], playerTemp])
                        self.Values = playerTempValues
                    # if temp > max:
                    max = temp
                    #tempPos = possibleMoves[index]
                    goodpossibleMoves.append([possibleMoves[index], temp])
                    self.Values = whatTempValues

                    #tempPoss.append(temp)
                def bubble(list):
                    for index in range(0,len(list)-1):
                        flag = False
                        for otherIndex in range(0,len(list)-index-1):
                            if list[otherIndex][1] > list[otherIndex+1][1]:
                                temp = list[otherIndex]
                                list[otherIndex] = list[otherIndex+1]
                                list[otherIndex+1] = temp
                                flag = True
                        if not flag:
                            return

                bubble(goodpossibleMoves)
                # print(goodpossibleMoves)

                goodMax = len(goodpossibleMoves) - 1
                badMax = len(badpossibleMoves) - 1
                print("good")
                print(goodpossibleMoves)
                print("Bad")
                print(badpossibleMoves)

                found = False

                while not found and goodMax != 0:
                    if goodpossibleMoves[goodMax][0] == badpossibleMoves[badMax][0]:
                        if goodMax > 0:
                            goodMax -= 1
                        if badMax > 0:
                            badMax -= 1
                    else:
                        found = True

                diff = 1000
                index

                for goodList in goodpossibleMoves:
                    for badList in badpossibleMoves:
                        if goodList[1] - badList[1] < diff:
                            diff = goodList[1] - badList[1]
                            index = goodList[0]

                #position = index
                position = goodpossibleMoves[goodMax][0]
                #position = tempPos
            else: #Fix this part so it selects an opperite value
                number = 0
                found = False
                while not found:
                    if not number in occupied:
                        found = True
                    else:
                        number += 1
                position = number

            self.Values[position] = oppenent
            occupied.add(position)
            if checkBoard(whereAmI(position),self.Values)== 1:
                wonRow(whereAmI(position), oppenent, self.Values, wonBoards)
                oppenentWins.append(whereAmI(position))
            else:
                checkIfFull(whereAmI(position))
            print(updateBoard(self.Values))
            gameOver(wonBoards, playerWins,oppenentWins)
            return whichBoard(position)

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
                    except ValueError:
                        print('Invalid value!')
                if not int(user) in boardIndexs[boardNumber] and not boardNumber in wonBoards:
                    print("You must got in board ", boardNumber)
                    try:
                        user = int(input('Input: '))
                    except ValueError:
                        print('Invalid value!')
                else:
                    self.Values[int(user)] = player
                    occupied.add(int(user))
                    print(updateBoard(self.Values))
                    print("checking board")
                    print(whereAmI(int(user)))
                    if checkBoard(whereAmI(int(user)),self.Values) == 0:
                        wonRow(whereAmI(int(user)), player, self.Values, wonBoards)
                        playerWins.append(whereAmI(int(user)))
                    else:
                        checkIfFull(whereAmI(int(user)))
                    print("board number: ", whichBoard(int(user)))
                    gameOver(wonBoards, playerWins,oppenentWins)
                    boardNumber = oppenentTurn(whichBoard(int(user)))

                    if len(occupied) >= 81:
                        print("What a draw!")
                        exit(0)
                    print("\nWhere would you like to go? \nEnter in the form of a coordinate")
                    try:
                        user = int(input('Input: '))
                    except ValueError:
                        print('Invalid value!')

        print("Okay you'll be playing as " + player + '.')
        yourTurn(4)
Board()