class Board:
    def __init__(self):
        self.board = self.create_board()

    @staticmethod
    def create_board():
        board = []
        for y in range(8):
            board_y = []
            for x in range(8):
                board_y.append('.')
            board.append(board_y)
        for x in range(8):
            board[0][x] = 'a'
            board[1][x] = 'a'
            board[6][x] = 'b'
            board[7][x] = 'b'
        return board


class Node:
    def __init__(self):
        self.board = Board()
        self.heuristic = 0


class Agent:
    def __init__(self, strategy, direction):
        self.strategy = strategy
        self.direction = direction


class Move:
    def __init__(self, posx, posy, upleft, up, upright, downleft, down, downright):
        self.posx = posx
        self.posy = posy
        self.upleft = upleft
        self.up = up
        self.upright = upright
        self.downleft = downleft
        self.down = down
        self.downright = downright


def ab_search(node, agent):
    node = max_value(node, agent, -9999, 9999, 0)
    return node


def max_value(node, agent, a, b, depth):
    depth += 1
    if depth == 5:
        return utility(node, agent)
    node.heuristic = -9999
    moves = get_possible_moves(node, agent)
    all_possible_nodes = update_node(node, moves)
    for one_node in all_possible_nodes:
        node.heuristic = max(node.heuristic, min_value(one_node, agent, a, b, depth).heuristic)
        if node.heuristic >= b:
            return node
        a = max(a, node.heuristic)
    return node


def min_value(node, agent, a, b, depth):
    depth += 1
    if depth == 5:
        return utility(node, agent)
    node.heuristic = 9999
    moves = get_possible_moves(node, agent)
    all_possible_nodes = update_node(node, moves)
    for one_node in all_possible_nodes:
        node.heuristic = min(node.heuristic, max_value(one_node, agent, a, b, depth).heuristic)
        if node.heuristic <= a:
            return node
        b = min(b, node.heuristic)
    return node


def get_possible_moves(node, agent):
    board = node.board
    moves = []
    move = Move(0, 0, 0, 0, 0, 0, 0, 0)
    if agent.direction == 0:
        for y in range(8):
            for x in range(8):
                if board[y][x] == 'b':
                    move = Move(x, y, 0, 0, 0, 0, 0, 0)
                    if y-1 >= 0 and board[y-1][x] != 'a' and board[y-1][x] != 'b':
                        move.up = 1
                    if y-1 >= 0 and x-1 >= 0 and board[y-1][x-1] != 'b':
                        move.upleft = 1
                    if y-1 >= 0 and x+1 <= 7 and board[y-1][x+1] != 'b':
                        move.upright = 1
                moves.append(move)
    else:
        for y in range(8):
            for x in range(8):
                if board[y][x] == 'a':
                    move = Move(x, y, 0, 0, 0, 0, 0, 0)
                    if y+1 <= 7 and board[y+1][x] != 'a' and board[y+1][x] != 'b':
                        move.down = 1
                    if y+1 <= 7 and x-1 >= 0 and board[y+1][x-1] != 'b':
                        move.downleft = 1
                    if y+1 <= 7 and x+1 <= 7 and board[y+1][x+1] != 'b':
                        move.downright = 1
                moves.append(move)
    return moves


def update_node(node, moves):
    all_possible_nodes = []
    for action in moves:
        x = action.posx
        y = action.posy
        if action.up:
            temp = node
            temp.board[y-1][x] = 'b'
            temp.board[y][x] = '.'
            all_possible_nodes.append(temp)
        if action.upleft:
            temp = node
            temp.board[y-1][x-1] = 'b'
            temp.board[y][x] = '.'
            all_possible_nodes.append(temp)
        if action.upright:
            temp = node
            temp.board[y-1][x+1] = 'b'
            temp.board[y][x] = '.'
            all_possible_nodes.append(temp)
        if action.down:
            temp = node
            temp.board[y+1][x] = 'a'
            temp.board[y][x] = '.'
            all_possible_nodes.append(temp)
        if action.downleft:
            temp = node
            temp.board[y+1][x-1] = 'a'
            temp.board[y][x] = '.'
            all_possible_nodes.append(temp)
        if action.downright:
            temp = node
            temp.board[y+1][x+1] = 'a'
            temp.board[y][x] = '.'
            all_possible_nodes.append(temp)
    return all_possible_nodes


def check_win(node):
    board = node.board
    count1 = 0  # number left for agent1
    count2 = 0  # number left for agent2
    for y in range(8):
        for x in range(8):
            if board[y][x] == 'b':
                count1 += 1
            if board[y][x] == 'a':
                count2 += 1
            if board[7][x] == 'a':
                print("agent2 wins")
                return
            if board[0][x] == 'b':
                print("agent1 wins")
                return
    if count1 == 0:
        print("agent2 wins")
    if count2 == 0:
        print("agent1 wins")
