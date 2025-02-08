x0, y0, x1, y1 = map(int, input().split())
x0_2, y0_2, x1_2, y1_2 = map(int, input().split())
if x0_2 > x1 or y0_2 > y1:
    print("0")
elif (x0_2 < x0 and x1_2 < x0) or (y0_2 < y0 and y1_2 < y0):
    print("0")
else:
    print("1")