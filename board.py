class Board():

    def __init__(self):
        self.Values = []
        for index in range(0,81):
            self.Values.append(" ")
        self.Boards = []
        self.main()

    def main(self):
        player = "" #the players symbol

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
            elif user == 'o' or user == 'O':
                player = "O"
            else:
                print("Please enter a valid symbol!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print(updateBoard())

        print("\nWhere would you like to go? \nEnter in the form of a coorindat")
        user = raw_input()

        while(user != 'x'):
            self.Values[int(user)] = player
            print(self.Values[int(user)])
            print(updateBoard())
            print("\nWhere would you like to go? \nEnter in the form of a coorindat")
            user = raw_input()

        print("Okay you'll be playing as " + player + '.')
Board()