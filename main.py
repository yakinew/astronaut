"""
  +---+---+---+---+---+
5 | @ |   | @ |   | @ |
  +---+---+---+---+---+
4 |   |   |   |   |   |
  +---+---+---+---+---+
3 |   |   | X |   |   |
  +---+---+---+---+---+
2 |   |   |   |   | @ |
  +---+---+---+---+---+
1 |   | A |   |   |   |
  +---+---+---+---+---+
   1   2   3   4   5

An astronaut needs to go to the middle of the square (mark with X).

"""
ASTRONAUT = 'A'
ROBOT = '@'
EMPTY = ' '


class AstronautRun:
   win_x = 3
   win_y = 3

   def __init__(self, width: int = 5, height: int = 5):
       self.width, self.height = width, height
       self.board = EMPTY * self.width * self.height

       self.board = self.set_element(self.board, 'A', 2, 1)
       self.board = self.set_element(self.board, '1', 1, 5)
       self.board = self.set_element(self.board, '2', 3, 5)
       self.board = self.set_element(self.board, '3', 5, 5)
       self.board = self.set_element(self.board, '4', 5, 2)

   def get_index(self, x, y):
       i = (x - 1) + self.width * (y - 1)
       if len(self.board) <= i:
           raise ValueError(f'Invalid point ({x}, {y})')
       return i

   def get_element(self, board, x, y):
       i = self.get_index(x, y)
       return board[i]

   def set_element(self, board, name, x, y):
       i = self.get_index(x, y)
       board = board[:i] + name + board[i + 1:]
       return board

   def get_next_moves(self, board: str):
       """
       This function returns all the possible moves of first move of the given board
       :param board:
       :return:
       """
       moves = []
       for y in range(1, self.height + 1):
           for x in range(1, self.width + 1):
               name = self.get_element(board, x, y)
               if name != EMPTY:
                   # Check if element can move up:
                   for i in range(y + 1, self.height + 1):
                       other = self.get_element(board, x, i)
                       if other != EMPTY:
                           if 1 < i - y:
                               # print(f'{name} can move UP to {other}!!')
                               new_board = self.set_element(board, EMPTY, x, y)
                               new_board = self.set_element(new_board, name, x, i - 1)
                               moves.append(new_board)
                           break

                   # Check if element can move down:
                   for i in range(y - 1, 0, -1):
                       other = self.get_element(board, x, i)
                       if other != EMPTY:
                           if 1 < y - i:
                               # print(f'{name} can move DOWN to {other}!!')
                               new_board = self.set_element(board, EMPTY, x, y)
                               new_board = self.set_element(new_board, name, x, i + 1)
                               moves.append(new_board)
                           break

                   # Check if element can move right:
                   for i in range(x + 1, self.width + 1):
                       other = self.get_element(board, i, y)
                       if other != EMPTY:
                           if 1 < i - x:
                               # print(f'{name} can move RIGHT to {other}!!')
                               new_board = self.set_element(board, EMPTY, x, y)
                               new_board = self.set_element(new_board, name, i - 1, y)
                               moves.append(new_board)
                           break

                   # Check if element can move right:
                   for i in range(x - 1, 0, -1):
                       other = self.get_element(board, i, y)
                       if other != EMPTY:
                           if 1 < x - i:
                               # print(f'{name} can move LEFT to {other}!!')
                               new_board = self.set_element(board, EMPTY, x, y)
                               new_board = self.set_element(new_board, name, i + 1, y)
                               moves.append(new_board)
                           break

       return moves

   def print(self):
       self.print_board(self.board)

   def print_board(self, board):
       txt = ''
       lines = [board[index: index + self.width] for index in range(0, len(board), self.width)]
       for i in range(self.height - 1, -1, -1):
           line = [char for char in lines[i]]
           txt += '   +' + '---+' * self.width + '\n'
           txt += f' {i + 1} | ' + ' | '.join(line) + ' |' + '\n'
       txt += '   +' + '---+' * self.width + '\n'
       txt += '     ' + '   '.join([str(i) for i in range(1, self.width + 1)]) + '\n'
       print(txt)

   def win_board(self, board):
       name = self.get_element(board, self.win_x, self.win_y)
       return name == ASTRONAUT

   def build_tree(self):
       queue = []
       visited = {}

       queue.append(('', self.board))
       visited[self.board] = ''

       while queue:
           parent, s = queue.pop(0)
           # self.print_board(s)

           if not self.win_board(s):
               moves = self.get_next_moves(s)

               for move in moves:
                   if move not in visited:
                       visited[move] = s
                       queue.append((s, move))
           else:
               print('WIN!!')

               p = s
               q = []
               while p:
                   q.append(p)
                   p = visited[p]

               q.reverse()
               for i, line in enumerate(q):
                   if i:
                       print(f'Step {i}:')
                   else:
                       print(f'Start:')
                   self.print_board(line)

               break


if __name__ == '__main__':
   ar = AstronautRun()
   ar.build_tree()
