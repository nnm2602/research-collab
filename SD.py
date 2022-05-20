import networkx as nx 

def main():
    test() 

def find_dominated_vertices(graph): 
    dominated = set()
    for k in graph: 
        vec_1_neighbors = set(graph.neighbors(k))
        vec_1_neighbors.add(k)
        len1 = len(vec_1_neighbors)
        for j in graph.neighbors(k):
            vec_2_neighbors = set(graph.neighbors(j))
            vec_2_neighbors.add(j)
            len2 = len(vec_2_neighbors)
            intersection = vec_1_neighbors.intersection(vec_2_neighbors)
            len3 = len(intersection)
            if len3 == len1 and len3 == len2:
                if k not in dominated:
                    print("{} = {}".format(j,k))
                    dominated.add(j)
            else:
                set_diff1 = vec_1_neighbors.difference(vec_2_neighbors)
                len4 = len(set_diff1)
                if len4 == 0:
                    print("{} > {}".format(j, k))
                    dominated.add(k)
                else:
                    set_diff2 = vec_2_neighbors.difference(vec_1_neighbors)
                    len5 = len(set_diff2)
                    if len5 == 0:
                        dominated.add(j)
                        print("{} < {}".format(j, k))
    return dominated

def test(): 
    graph = nx.Graph()
    edge_list = [(1,2), (1,3), (1,4), (2,3), (2,5), (3,4), (3,5), (4,6), (5,6)]
    graph.add_edges_from(edge_list) 
    dominated_vertices = find_dominated_vertices(graph)


if __name__ == '__main__':
    main() 
