# imports
import random


# classes block
class TicTacToe:
    """Class for implementation of the classic game: tic-tac-toe"""

    def __init__(self):
        self.grid = [["---", "---", "---"],
                     ["---", "---", "---"],
                     ["---", "---", "---"]]

    @staticmethod
    def choose_first_player():
        return random.randint(0, 1)

    @staticmethod
    def swap_player_turn(player):
        """This function swaps the player turns"""
        return "X" if player == "O" else "O"

    def update_the_spot(self, row: int, column: int, player: str):
        """
        Updates the spot on the grid, when players make the move
        :param player: sign for the player
        :param row: index for the row
        :param column: index for the column
        :return:
        """
        self.grid[row][column] = player

    def print_grid(self):
        """
        This function prints grid for the user
        :return: nothing
        """
        print(f"{self.grid[0][0]} {self.grid[0][1]} {self.grid[0][2]}\n"
              f"{self.grid[1][0]} {self.grid[1][1]} {self.grid[1][2]}\n"
              f"{self.grid[2][0]} {self.grid[2][1]} {self.grid[2][2]}")

    def is_filled(self):
        """
        This function checks if the board is filled
        :return: returns True if filled, False if not
        """
        for row in self.grid:
            for space in row:
                if space == "---":
                    return False

        return True

    def is_won(self, player):
        """
        This function checks if one of the players have won
        :return: return True if won, return False if not
        """
        # helping variable
        is_win = None

        # check rows
        for row in self.grid:
            if row.count(player) == len(row) and row:
                return True

        # check columns
        for i in range(len(self.grid)):
            is_win = True
            for j in range(len(self.grid)):
                if self.grid[j][i] != player:
                    is_win = False
                    break

            if is_win:
                return is_win

        # check diagonals
        is_win = True
        for i in range(len(self.grid)):
            if self.grid[i][i] != player:
                is_win = False
                break

        if is_win:
            return is_win

        is_win = True
        for i in range(len(self.grid)):
            if self.grid[i][len(self.grid) - 1 - i] != player:
                is_win = False
                break

        if is_win:
            return is_win

        # if all of this if passed, then the player have definitely win
        return False

    def main(self):
        """
        Main function for the game. Infinite loop
        :return:
        """
        # helping variables
        player = "X" if self.choose_first_player() == 1 else "O"

        print("Welcome to the Tic Tac Toe Game")
        while True:
            print(f"Player's {player} turn.")

            # print grid
            self.print_grid()

            # update the spot
            players_move = input(
                "Please write where you can place you mark. Type indexes from 0-2 for row and column, use space. ").split(
                " ")
            self.update_the_spot(int(players_move[0]), int(players_move[1]), player)

            # check if the user won
            if self.is_won(player):
                print(f"Congratulations! Player {player} won the game!")
                break

            # check if the bord is filled
            if self.is_filled():
                print("We have a draw!")
                break

            # show the final board
            self.print_grid()

            # swap the player
            player = self.swap_player_turn(player)


# run config
if __name__ == "__main__":
    game = TicTacToe()
    game.main()
