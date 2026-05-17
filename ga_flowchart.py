from graphviz import Digraph

# Create directed graph
dot = Digraph('Genetic_Algorithm_Workflow', format='pdf')

# Graph styling
dot.attr(rankdir='TB')
dot.attr(splines='ortho')
dot.attr(nodesep='0.6')
dot.attr(ranksep='0.8')
dot.attr(size='8,10')

# Node styling
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

# Nodes
dot.node('A', 'Start')

dot.node('B', 'Generate Initial Population')

dot.node('C', 'Evaluate Fitness')

dot.node('D', 'Selection')

dot.node('E', 'Crossover')

dot.node('F', 'Mutation')

dot.node('G', 'Create New Population')

dot.node('H', 'Termination Condition Met?')

dot.node('I', 'Best Solution Found')

dot.node('J', 'End')

# Main workflow
dot.edge('A', 'B')

dot.edge('B', 'C')

dot.edge('C', 'D')

dot.edge('D', 'E')

dot.edge('E', 'F')

dot.edge('F', 'G')

dot.edge('G', 'H')

# Yes path
dot.edge(
    'H',
    'I',
    xlabel='  Yes  '
)

dot.edge(
    'I',
    'J'
)

# Improved No loop with spacing
dot.edge(
    'H',
    'C',
    xlabel='   No   ',
    minlen='3',
    constraint='false'
)

# Generate PDF
dot.render(
    'genetic_algorithm_workflow',
    view=True
)

print("Flowchart generated successfully!")