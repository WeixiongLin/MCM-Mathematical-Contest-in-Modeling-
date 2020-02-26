from buildgraph import *
import numpy as np
import networkx as nx
import csv


G = Graph('Huskies', [i + 1 for i in range(38)])
G.build()
re_G = nx.from_numpy_matrix(G.reverse_adjM())

# re_G的直径（最长最短路径的长度）
print(nx.diameter(re_G))


# print(nx.dijkstra_path(re_G, 29, 0))
# print(nx.dijkstra_path(re_G, 29, 18))
# print(nx.dijkstra_path(re_G, 18, 0))
# print(nx.dijkstra_path(re_G, 6, 10))



# 最短路矩阵
# floyd = nx.floyd_warshall_numpy(re_G)


"""
for i in range(31):
    for j in range(31):
        floyd[i, j] = round(floyd[i, j], 2)

floyd = floyd.tolist()


headers = ['_F1', '_F2', '_F3', '_F4', '_F5', '_F6', '_D1', '_D2', '_D3', '_D4', '_D5', '_D6', '_D7', '_D8', '_D9',
           '_D10','_M1', '_M2', '_M3', '_M4', '_M5', '_M6', '_M7', '_M8', '_M9', '_M10', '_M11', '_M12', '_M13','_G1', '_G2']
rows = []
for i in range(31):
    rows.append([headers[i]] + floyd[i])
with open('floyd.csv', 'w', newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
"""