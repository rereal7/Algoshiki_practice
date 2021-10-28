# 解説確認後
import math

n = int(input())
C = [list(map(int, input().split())) for i in range(n)]

# 二頂点間の距離を求める関数（三平方の定理を参照）
def distance(x, y):
	result = math.sqrt((C[y][0] - C[x][0])**2 + (C[y][1] - C[x][1])**2)
	return result


# すでに訪れた頂点を set 型で管理（重複しないため）
visited = set()
visited.add(0) # 原点を追加

# 前回の頂点
pre = 0

ans = 0
# 毎回貪欲に頂点を選んでいく
for i in range(n - 1): # 原点があるので、-1する必要がある
	# 残っている頂点で最も近いところを探す
	T = []
	for j, xy in enumerate(C):
		if j not in visited:
			T.append([distance(pre, j), j])
	min_dis, nex = min(T)
	# 以上のコードを短縮したもの
	# min_dis, nex = min([([distance(pre, j), j]) for j, xy in enumerate(C) if j not in visited])

	# 新たに頂点 nex を訪れる
	visited.add(nex)
	ans += min_dis

	# 前回頂点を更新
	pre = nex
# 最後に頂点 0 へ戻る
ans += distance(pre, 0)

print(ans)