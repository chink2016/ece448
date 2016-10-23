from Class import *

node = Node()
agent1 = Agent(0, 0)  # 0,0 represents offensive strategy and move from bottom to top
agent2 = Agent(0, 1)  # 0,1 represents offensive strategy and move from top to bottom
while 1:
    check_win(node)
    for y in range(8):
        print('\n')
        for x in range(8):
            print(node.board[y][x])
    node = ab_search(node, agent1)
    for y in range(8):
        print('\n')
        for x in range(8):
            print(node.board[y][x])
    check_win(node)
    node = ab_search(node, agent2)

