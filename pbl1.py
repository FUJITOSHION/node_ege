import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# dataを読み込み
kt = pd.read_csv('edges.csv', header=None)

# カラム名を追加
kt.columns = ['startID', 'endID','cost', 'y','x','yend','xend']

# ノードデータの作成
kt_nodes = kt[['endID','xend', 'yend']]

# 重複したノードデータの削除
kt_nodes = kt_nodes.drop_duplicates()

# node_dataの格納
nodes = kt_nodes['endID'].values.tolist()

# エッジデータの格納
edges = kt[['startID','endID']].values.tolist()

# ノードデータの格納
pos = kt_nodes.set_index('endID').T.to_dict('list')

# print(pos)
# グラフを

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
ax = plt.subplot()
nx.draw_networkx(G,pos, with_labels=False, node_size=3, node_color='green', node_shape ='o', ax = ax)

ax.tick_params(left = True, bottom = True, labelleft = True, labelbottom = True)
ax.set_title('Figure1')

plt.show()
