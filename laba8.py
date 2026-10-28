class Massiv:
    def __init__(self, a):
        self.a = a

    def summa(self):
        i, j = self.a.index(min(self.a)), self.a.index(max(self.a))
        if i > j:
            i, j = j, i
        return sum(self.a[i+1:j])

a = list(map(float, input().split()))
print(Massiv(a).summa())
