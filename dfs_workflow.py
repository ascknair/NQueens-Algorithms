from graphviz import Digraph

dot = Digraph('DFS_Workflow', format='pdf')

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

dot.node('B', 'Initialize Empty Board')

dot.node('C', 'Place Queen in Current Row')

dot.node('D', 'Is Position Safe?')

dot.node('E', 'Move to Next Row')

dot.node('F', 'All Queens Placed?')

dot.node('G', 'Solution Found')

dot.node('H', 'Backtrack')

dot.node('I', 'End')

dot.edge('A', 'B')

dot.edge('B', 'C')

dot.edge('C', 'D')

dot.edge('D', 'E', xlabel=' Yes ')

dot.edge('E', 'F')

dot.edge('F', 'G', xlabel=' Yes ')

dot.edge('G', 'I')

dot.edge('D', 'H', xlabel=' No ')

dot.edge('H', 'C')

dot.edge('F', 'H', xlabel=' No ')

dot.render('dfs_workflow', view=True)

print("DFS workflow generated successfully!")