# AI Agent with Langgraph Framework Capabilities

## These are the phases

- Simple AI Agent
- Working With Chain
- Routing
- Agent with Memory
- States
- Filters and Reducers
- State Management
- Breakpoints
- Human in the loop
- Long term memory management

## Steps:

- Components of Graph.
- Langgraph is a framework wrapper on langchain.
- Langgraph has three main components: nodes, edges, state.
- Node is just a vertex representing python function or module to be executed.
- Here edge is a directional path between two nodes.
- We have normal edge and conditional edge.
- Normal edge means, the edge that needs to be traversed each time we run it.
- The conditional edge will be traversed when the condition is satisfied.
- An orphan node (sometimes called an isolated node) in graph theory is a node/vertex that has no edges connecting it to any other nodes in the graph.
- In other words, it's a completely disconnected vertex with 0 degree of Origin.
- State is a building block of graph.
- Graphs also have the ability to keep track of what is going on in the graph generally.
- This is where state comes in the picture.
- State is basically the object that we pass between different nodes and edges of our graph.
- This object holds information that is used to communicate between the different nodes and edges.
- It serves as the input/output schema for all nodes and edges.
- Building A Simple AI Agent
  - Building Graph State
  - Building Nodes Functions
  - Building Graph Nodes
  - Building Edges
