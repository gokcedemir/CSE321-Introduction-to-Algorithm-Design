import collections

# Returns the breadth-first search tree of the graph.
#Given a graph and a starting vertex, this method returns the breadth-first 
#search tree of graph, rooted at the vertex start.
def bfs_iterative(graph, start, path=[]):
    queue=[start]
    while queue:
        vertex = queue.pop(0)
        if not vertex in path:
            path+=[vertex]
            queue += graph[vertex]
    return path

#Traverse with DFS
def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path
  
  
#Driver code 
#Give the location of the file 
#loc = ("Graph_data.XLS") 

# default dictionary to store graph 
#g = Graph()

# Dosyadan okuma kısmını devre dışı bırakıp, direkt olarak matrisi doldurdum.
#Gerekli işlemler adjaceny_matris üzerinden yapılmaktadır. 

"""
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
sheet.cell_value(0, 0) 
print(sheet.nrows)
print(sheet.ncols)

for i in range(3,sheet.nrows):
    g.addEdge(int(sheet.cell_value(i, 0)),int(sheet.cell_value(i, 1)))
    
"""

#Excel dosyasındaki örnek neticesinde adjaceny matris oluşturuldu. # 
adjacency_matrix = {1: [2, 3,4,5,8], 2: [4],
                    3: [5,6,9], 4: [5], 5: [6],
                    6: [7], 7: [8,10], 8:[9,10], 9:[10],10:[]}

print("DFS traversal from a given graph: "+ str(dfs_recursive(adjacency_matrix, 1)))
print("BFS traversal from a given graph: " + str(bfs_iterative(adjacency_matrix, 1)))
