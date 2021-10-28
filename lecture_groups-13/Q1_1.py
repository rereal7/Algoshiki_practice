n = int(input())
ans = 0

# ５円玉の枚数と、残りの１円玉の枚数を求める
ans += n//5
ans += n%5

print(ans)