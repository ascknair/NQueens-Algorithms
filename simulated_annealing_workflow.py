from graphviz import Digraph

dot = Digraph('Simulated_Annealing_Workflow', format='pdf')

dot.attr(rankdir='TB')
dot.attr(splines='ortho')
dot.attr(nodesep='0.6')
dot.attr(ranksep='0.8')
dot.attr(size='8,10')

dot.attr(
    'node',
    shape='rectangle',
    style='rounded,filled',
    fillcolor='lightblue',
    color='black',
    fontsize='12',
    fontname='Helvetica',
    margin='0.2,0.1'
)

dot.node('A', 'Start')

dot.node('B', 'Generate Initial State')

dot.node('C', 'Set Initial Temperature')

dot.node('D', 'Generate Random Neighbor')

dot.node('E', 'Calculate Energy Difference')

dot.node('F', 'Better Solution?')

dot.node('G', 'Accept Move')

dot.node('H', 'Accept Probabilistically?')

dot.node('I', 'Reject Move')

dot.node('J', 'Reduce Temperature')

dot.node('K', 'Stopping Condition Met?')

dot.node('L', 'End')

dot.edge('A', 'B')

dot.edge('B', 'C')

dot.edge('C', 'D')

dot.edge('D', 'E')

dot.edge('E', 'F')

dot.edge('F', 'G', xlabel=' Yes ')

dot.edge('F', 'H', xlabel=' No ')

dot.edge('H', 'G', xlabel=' Yes ')

dot.edge('H', 'I', xlabel=' No ')

dot.edge('G', 'J')

dot.edge('I', 'J')

dot.edge('J', 'K')

dot.edge('K', 'L', xlabel=' Yes ')

dot.edge(
    'K',
    'D',
    xlabel='   No   ',
    minlen='3',
    constraint='false'
)

dot.render('simulated_annealing_workflow', view=True)

print("Simulated Annealing workflow generated successfully!")