class Board():

    def __init__(self):
        self.Values = [[1 for x in range(9)] for y in range(9)]
        self.Boards = []
        self.main()

    def main(self):
        count = 0
        for x in range(9):
            for y in range(9):
                print(self.Values[x][y])
                count += 1
        print(count)

        for x in range(3):
            self.Boards.append("  X | X | X   ||   X | X | X   ||   X | X | X   \n"
                               "+---+---+---+ || +---+---+---+ || +---+---+---+ \n"
                               "  X | X | X   ||   X | X | X   ||   X | X | X   \n"
                               "+---+---+---+ || +---+---+---+ || +---+---+---+ \n"
                               "  X | X | X   ||   X | X | X   ||   X | X | X   ")
            if x <= 1:
                self.Boards.append("===============================================")

        for x in range(len(self.Boards)):
            print(self.Boards[x])


        #print("  X | X | X  \n+---+---+---+\n  X | X | X \n+---+---+---+\n  X | X | X \n")

Board()