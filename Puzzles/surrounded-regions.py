"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

    X X X X
    X O O X
    X X O X
    X O X X

After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        list of lists with connected O's at the end remove
        if a group of O's are connected to an edge remove the list from the list of lists
        """
        visited = set()
        islands = []
        
        def findNeihbors(coord1, coord2):
            output = {'region': [[coord1,coord2]], 'surrounded': True}
            visited.add(f"{coord1},{coord2}")
            for point in output['region']:

                if point[0] - 1 < 0:
                    output['surrounded'] = False
                elif board[point[0] - 1][point[1]] == 'O' and f"{point[0] - 1},{point[1]}" not in visited:
                    output["region"].append([point[0] - 1,point[1]])
                    visited.add(f"{point[0] - 1},{point[1]}")

                if not point[0] + 1 < len(board):
                    output["surrounded"] = False
                elif board[point[0] + 1][point[1]] == 'O' and f"{point[0] + 1},{point[1]}" not in visited:
                    output["region"].append([point[0] + 1,point[1]])
                    visited.add(f"{point[0] + 1},{point[1]}")

                if point[1] - 1 < 0:
                    output["surrounded"] = False
                elif board[point[0]][point[1] - 1] == 'O' and f"{point[0]},{point[1] - 1}" not in visited:
                    output["region"].append([point[0],point[1] - 1])
                    visited.add(f"{point[0]},{point[1] - 1}")

                if not point[1] + 1 < len(board[0]):
                    output["surrounded"] = False
                elif board[point[0]][point[1] + 1] == 'O' and f"{point[0]},{point[1] + 1}" not in visited:
                    output["region"].append([point[0],point[1] + 1])
                    visited.add(f"{point[0]},{point[1] + 1}")
                        
            return output
        
        for i, row in enumerate(board):
            
            for j, item in enumerate(row):
                if item == 'O' and f"{i},{j}" not in visited:
                    result = findNeihbors(i, j)
                    if result['surrounded']:
                        islands.append(result['region'])
                else:
                    visited.add(f"{i},{j}")
                    
        for region in islands:
            for coord in region:
                board[coord[0]][coord[1]] = 'X'
                        
        # print("board test", board[0][0])
        # print("visited", visited)
        # print("islands", islands)
        