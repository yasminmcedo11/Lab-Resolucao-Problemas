n = int(input())
copos_quebrados = 0
for i in range(n):
    latas, copos = map(int, input().split())
    if latas > copos:
        copos_quebrados += copos
print(copos_quebrados)
