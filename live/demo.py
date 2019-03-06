class RockPaperScissors:

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def moves(self):
        return ["ROCK", "PAPER", "SCISSORS"]

    def play(self):

        player_one_move = self.player_one.pick_action(self.moves())
        player_two_move = self.player_two.pick_action(self.moves())

        if player_one_move == player_two_move:
            print("It's a tie!")
        elif player_one_move == "ROCK" and player_two_move =="SCISSORS":
            print("Player One wins!")
        elif player_one_move == "PAPER" and player_two_move =="ROCK":
            print("Player One wins!")
        elif player_one_move == "SCISSORS" and player_two_move =="PAPER":
            print("Player One wins!")
        else:
            print("Player Two wins!")

class HumanPlayer:

    def __init__(self):
        pass

    def pick_action(self, moves, state=None):

        i = 1

        print("Please select your move:")

        for move in moves:
            print(i, ':', move)
            i += 1

        user_input = input()
        user_choice = int(user_input)

        return moves[user_choice - 1]

import random

class RandomPlayer:
    def __init__(self):
        pass

    def pick_action(self, moves, state=None):
        # Given a list of possible moves, pick a random one

        move = random.choice(moves)
        print("Random Player has picked", move)

        return move


class TicTacToe:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.reset_state()

    def moves(self):
        move_list = []

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == '_':
                    move_list.append((i, j))

        return move_list

    def reset_state(self):
        self.state = [['_' for _ in range(3)] for _ in range(3)]

    def play(self):

        game_over = False
        players = [self.player_one, self.player_two]
        player_index = 0
        turn = 0

        while not game_over and turn < 9:
            self.show_state()

            player = players[player_index]

            x, y = player.pick_action(self.moves(), state=self.state)
            self.state[x][y] = str(player_index)

            if self.state[0][y] == self.state[1][y] == self.state[2][y] or \
                self.state[x][0] == self.state[x][1] == self.state[x][2] or \
                ((self.state[0][0] == self.state[1][1] == self.state[2][2] or \
                self.state[0][2] == self.state[1][1] == self.state[2][0]) and \
                 self.state[1][1] != "_"):
                game_over = True
                self.win(player_index)

            player_index = 1 - player_index
            turn += 1

        if turn == 9:
            print("It's a tie!")

    def show_state(self):
        print()

        for row in self.state:
            print(row)
        print()

    def win(self, winner):

        if winner == 0:
            print("Player One Wins!")
        else:
            print("Player Two Wins!")

        self.show_state()


game = TicTacToe(HumanPlayer(), RandomPlayer())
game.play()
