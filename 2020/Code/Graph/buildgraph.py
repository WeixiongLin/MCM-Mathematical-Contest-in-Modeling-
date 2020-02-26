"""建立网络，返回邻接矩阵"""


import xlrd
import numpy as np

# 对球员进行编号
pos = {'_F1': 0, '_F2': 1, '_F3': 2, '_F4': 3, '_F5': 4, '_F6': 5,
       '_D1': 6, '_D2': 7, '_D3': 8, '_D4': 9, '_D5': 10, '_D6': 11, '_D7': 12, '_D8': 13, '_D9': 14, '_D10': 15,
       '_M1': 16, '_M2': 17, '_M3': 18, '_M4': 19, '_M5': 20, '_M6': 21, '_M7': 22, '_M8': 23, '_M9': 24, '_M10': 25, '_M11': 26, '_M12': 27, '_M13': 28,
       '_G1': 29, '_G2': 30,
       0: '_F1', 1: '_F2', 2: '_F3', 3: '_F4', 4: '_F5', 5: '_F6',
       6: '_D1', 7: '_D2', 8: '_D3', 9: '_D4', 10: '_D5', 11: '_D6', 12: '_D7', 13: '_D8', 14: '_D9', 15: '_D10',
       16: '_M1', 17: '_M2', 18: '_M3', 19: '_M4', 20: '_M5', 21: '_M6', 22: '_M7', 23: '_M8', 24: '_M9', 25: '_M10', 26: '_M11', 27: '_M2', 28: '_M13',
       29: '_G1', 30: '_G2'}


def formal_pos(platerid):
    if platerid[-3]=='_':
        return platerid[-3:]
    else:
        return platerid[-4:]


class Graph:
    # 点的集合，共有31个位置
    V = ['_F1', '_F2', '_F3', '_F4', '_F5', '_F6', '_D1', '_D2', '_D3', '_D4', '_D5', '_D6', '_D7', '_D8', '_D9',
         '_D10', '_M1', '_M2', '_M3', '_M4', '_M5', '_M6', '_M7', '_M8', '_M9', '_M10', '_M11', '_M12', '_M13', '_G1',
         '_G2']
    # 未上场球员在pos中的数字位置
    subV = np.zeros(31)
    # 邻接矩阵
    E = np.zeros((31, 31))
    TeamID = ''
    # 参与建图的比赛
    MatchID = []

    def __init__(self, TeamID, MatchID):
        self.TeamID = TeamID
        for i in range(len(self.V)):
            self.V[i] += TeamID
        self.MatchID = MatchID

    def build(self):
        data = xlrd.open_workbook(r"data\passingevents.xlsx")
        table = data.sheets()[0]  # 通过索引顺序获取
        rows = table.nrows-1  # 获取行数，第一行不算
        col_MatchID = [int(i) for i in table.col_values(0)[1:]]
        col_TeamID = table.col_values(1)[1:]
        col_OriginPlayerID = table.col_values(2)[1:]
        col_DestinationPlayerID = table.col_values(3)[1:]

        temp = np.zeros(31)
        for player in col_OriginPlayerID[:565]:
            if player[0]!='H':
                continue
            temp[pos[formal_pos(player)]] = 1
            # print(pos[formal_pos(player)])
        for player in col_DestinationPlayerID[:565]:
            if player[0]!='H':
                continue
            temp[pos[formal_pos(player)]] = 1
            # print(pos[formal_pos(player)])

        self.subV = np.argwhere(temp==0)

        for id in self.MatchID:
            for i in range(rows):
                if id == col_MatchID[i] and self.TeamID == col_TeamID[i]:
                    # 找到PlayerID在矩阵中的位置
                    x = pos[formal_pos(col_OriginPlayerID[i])]
                    y = pos[formal_pos(col_DestinationPlayerID[i])]
                    self.E[x, y] += 1
        # print(self.E)

    def adjMatrix(self):
        return self.E

    def substi(self):
        return self.subV

    def reverse_adjM(self):
        E = self.E.copy()
        for i in range(31):
            for j in range(31):
                E[i, j] = 1 / E[i, j]
        return E


def build_graph(TeamID, MatchID):
    G = Graph(TeamID, MatchID)
    G.build()
    np.save('G.npy', G.adjMatrix())
    return G.adjMatrix()
