from Class import *
node = Node()
agent1 = Agent(ab_search, 0, 0)
agent2 = Agent(ab_search, 0, 1)
while 1:
    check_win(node)
    node = ab_search(node, agent1)
    check_win(node)
    node = ab_search(node, agent2)



