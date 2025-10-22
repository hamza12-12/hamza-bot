import random

class RunnerGame:
    def __init__(self):
        self.player_pos = 5
        self.score = 0
        self.speed = 1
    
    def reset_game(self):
        self.player_pos = 5
        self.score = 0
        self.speed = 1
    
    def move_player(self, direction):
        if direction == "UP":
            if self.player_pos > 0:
                self.player_pos -= 1
        elif direction == "DOWN":
            if self.player_pos < 9:
                self.player_pos += 1
    
    def update_game(self):
        self.score += 1
        if self.score > 10:
            self.speed = 2
    
    def get_game_board(self):
        board = "لعبة الجري\n\n"
        for i in range(10):
            if i == self.player_pos:
                board += "🏃‍♂️\n"
            else:
                board += "⬜\n"
        board += f"\nالنقاط: {self.score}\nالسرعة: {self.speed}"
        return board