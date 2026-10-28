class Massiv:
    def __init__(self, a):
        self.a = a

n = int(input())
a = [list(map(int, input().split()))
for _ in range(n)]
m = Massiv(a)
print(sum(max(max(row[:k]) for row in m.a[:k]) for k in range(1, n+1)))
