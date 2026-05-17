from graphviz import Digraph

dot = Digraph('Hill_Climbing_Workflow', format='pdf')

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

dot.node('B', 'Generate Random Board')

dot.node('C', 'Calculate Conflicts')

dot.node('D', 'Generate Neighbor States')

dot.node('E', 'Choose Best Neighbor')

dot.node('F', 'Conflict Reduced?')

dot.node('G', 'Move to Better State')

dot.node('H', 'Local Optimum Reached')

dot.node('I', 'Solution Found')

dot.node('J', 'End')

dot.edge('A', 'B')

dot.edge('B', 'C')

dot.edge('C', 'D')

dot.edge('D', 'E')

dot.edge('E', 'F')

dot.edge('F', 'G', xlabel=' Yes ')

dot.edge('G', 'C')

dot.edge('F', 'H', xlabel=' No ')

dot.edge('H', 'I')

dot.edge('I', 'J')

dot.render('hill_climbing_workflow', view=True)

print("Hill Climbing workflow generated successfully!")