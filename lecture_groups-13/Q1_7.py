# 解説確認後
n = int(input())
S = [list(map(int, input().split())) for i in range(n)]

# 終了時刻でソート
S.sort(key = lambda x: x[1])

pre = 0
ans = 0
for s, t in S:
	# 前の予定の終了時刻に間に合わない場合、スキップ
	if pre > s:
		continue
	pre = s
	ans += 1

print(ans)


# 別解（なぜ、WAになるのかわからない）
# 方針：スタート時間でソート

# 入力
n = int(input())
S = sorted([list(map(int, input().split())) for i in range(n)])

# 予定数を格納する配列
ans = [1]

for i in range(n):
	pre = i
	count = 1
	for j in range(i, n):
		if S[pre][1] > S[j][0]:
			continue
		pre = j
		count += 1
	ans.append(count)

print(max(ans))