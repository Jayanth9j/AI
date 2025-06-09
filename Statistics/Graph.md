Network & Graph Theory

Entity is nothing but a persona i.e for each usecase the entity changes in some cases it will be user sometimes it will be another type of object.

Social Network - It is nothing but a structure made up of entities(nodes) and the relationship(edges) between them. Mainly Persons most of the time.

Graph - It is made up of vertices(nodes) and connection(edges) between them.

Graph Database - It is a type of database where data is stored as nodes and edges i.e we can use unstructred structured and semi structured data.

Example - Neo4j Database

Why Graph database perform better than traditional databases like Sql,Oracle?
It is because when performing complex queries the sql database need to retrieve data from multiple tables by joining then giving the final result but in case of graph database we can just interact with that particular nodes which corresponds to our query and gives the result very quickly.

Centrality - We can know which of the nodes are most prominent or influential in that particular network.

Betweeness - how many times a particular node is in between the shortest path of another 2 nodes

Closeness - it just measures a node distance from all the other nodes in the network.

Degree of a node - It is the count of number of edges that particular node has. The node with highest degree can be said to be Centrality of network most of the times.

Shortest Path Between Nodes - It is nothing but the path with least number of edges. can be used to calculate shortest path between nodes.

Eigen Vector Centrality - It measures the nodes it connected to and their importance(quality of connections) 
Example - if two nodes have same degree and among them one is connected to a node with higher degree than both of them then the this node can be higher than the another node.
