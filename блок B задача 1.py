import math
#комментарии к задаче смотрите в решении
a=float(input())
b=float(input())
l=float(input())
x=float(input())
y=float(input())
R=float(input())
alpha=float(input())/180*math.pi
const=R/abs(math.cos(alpha))-math.tan(alpha)*(l+x)-y
v=[]
for n in range(10**3):
    for m in range(10**3):
        if m<=(const+a*n*math.tan(alpha))/b:
            v.append((n,m))
min_summ=+math.inf
for summ in v:
    min_summ=min(summ[0]+summ[1],min_summ)
if not v:
    print("никогда не пересечет")
else:
    print("пересечет спустя", min_summ, "отражений")



