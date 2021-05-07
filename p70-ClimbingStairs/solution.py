''' You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 '''
def GenerateGraph(n: int) -> "return a dictionary of vertices and its adjacent vertices":
    result = {}
    for i in range(1, n + 1):
        if (i < 2):
            result[i] = [i - 1]
        else:
            result[i] = [i-1, i-2]
    return result

def FindAllPaths(graph: {}, start: int, dest: int, path = []) -> "return a list of possible paths  leading to dest":

    print(f'Current start: {start}')
    print(f'Current path: {path}')

    # create new list containing start and add it to path
    path = path + [start]
    
    # check if current vertex (start) is the destination
    # return the current [path] if yes
    if start == dest: 
        print("Found")
        return [path]
    # return empty array if the current vertex leads to nowhere (dead end)
    if start not in graph.keys(): 
        return []
    
    paths = []

    # loop through all possible vertices that the current (start) leads to
    for node in graph[start]:
        # if the node is not visited in the current path
        print(graph[start])
        if node not in path:
            # find all possible new_paths leading to the originally specified destination
            # starting from the current node
            # with path is the path leading to the current node
            new_paths = FindAllPaths(graph, node, dest, path)
            for new_path in new_paths:
                # add all new paths found in paths
                paths.append(new_path)
            
            print(f"New paths: {new_paths}")
            print(f'Current paths: {paths}')
    
    print(f"Complete looping through node from start: {start}")
    return paths


# def find_all_paths(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return [path]
#     if not start in graph.keys():
#         return []
#     paths = []
#     for node in graph[start]:
#         if node not in path:
#             newpaths = find_all_paths(graph, node, end, path)
#             for newpath in newpaths:
#                 paths.append(newpath)
#     return paths

if __name__ == "__main__":
    n = int(input("Please enter a number: ")) 
    dict = GenerateGraph(n)

    possiblePaths = FindAllPaths(dict, n, 0)
    print(len(possiblePaths))
    
    

   
