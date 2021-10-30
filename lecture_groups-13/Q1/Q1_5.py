n = int(input())
ans = 0

# 後ろから見て貪欲法
while n > 0:
	if n%3 == 0:
		n //= 3
	else:
		n -= 1
	ans += 1
print(ans)