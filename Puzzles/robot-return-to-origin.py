class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dictionary = {
            'U': 0,
            'D': 0,
            'L': 0,
            'R': 0
        }
        for move in moves:
            dictionary[move] += 1
        
        if dictionary['U'] - dictionary['D'] != 0 or dictionary['L'] - dictionary['R'] != 0:
            return False
        else:
            return True