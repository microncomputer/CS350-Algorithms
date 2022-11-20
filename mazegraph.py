def main():
    adjacency_list_testGraph = {1: {6}, 2: {3}, 3: {2, 4}, 4: {3, 5}, 5: {4, 10}, 6: {1, 7}, 7: {6, 8}, 8: {7, 9, 13},
                                9: {8, 10}, 10: {5, 9}, 11: {12}, 12: {11, 17}, 13: {8, 14, 18}, 14: {13, 15},
                                15: {14, 20},
                                16: {21}, 17: {12, 22}, 18: {13, 23}, 19: {20, 24}, 20: {15, 19}, 21: {16, 22},
                                22: {17, 21, 23}, 23: {18, 22}, 24: {19, 25}, 25: {24}}
    '''
    rules of a graph of a maze:

    elements 1-5, 1+5*a for a in range(1, 4), 5+5*a for a in range(1,4), 21-25 all on outer edge of maze 
    which means something different for each of them so that maybe needs to be specified

    all elements i can have at most 4 connections and only with i-1, i+1, i+5, i-5 and not all of those for 
    the special outer elements listed above
    '''

    def DFSinit(G: dict):
        """
        :param G: a dictionary implementation of a graph
        :return: depth first search data structure of the graph
        """
        visited = set()
        return visited


    # color is not needed, if node is not in visited, add it
    def maze_traversal_solve(maze: dict):
        '''
        depth first search with a stack
        for an nxn maze, the top right corner is key 1 and the bottom left is key n^2
        we start at 1 and find out if there is a path from 1 to n^2
        :return: array of the path that solves the maze, consisting of consecutive vertices to traverse
                or 0 if no solution
        '''
        visited = DFSinit(maze)
        print(visited)
        solvable = DFSRec(maze, visited, 1, 25)
        return solvable

    def DFSRec(maze: dict, visited: set, key: int, end: int):
        if maze[key] == 0 or key in visited:
            print(key, "in visited, returning")
            return
        elif key == end:
            return True
        else:
            visited.add(key)
            print("visited so far", visited)
            '''
            try:
                print(maze[key])
                DFSRec(maze, visited, maze[key], end)
            except:
            '''
            for value in maze[key]:
                DFSRec(maze, visited, value, end)

    print(maze_traversal_solve(adjacency_list_testGraph))



if __name__ == "__main__":
    main()



