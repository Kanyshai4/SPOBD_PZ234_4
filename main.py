
#n=int(input())
#F = [0] * (n + 1)
#F[1] = 1
#for i in range(2, n + 1):
   # F[i] = (i%2==0) + F[i-1]
#print(F[i])

#def f(x):
  #  if (x==0):
        #return 0
    #if (x==1):
        #return 0
    #if (x==2):
        #return 2

import matplotlib.pyplot as plt

n = 100
Price=[]
for ii in range(0,101):
    Price.append(ii)
F = [0] * (n + 1)
F[1] = 1
itogst=0
for i in range(2, n+1):
    if(i%2==0):
        if Price[i-1] < Price[i//2]:
            itogst+=Price[i-1]
        if Price[i-1] >= Price[i//2]:
            itogst+=Price[i//2]
    else:
        itogst+=Price[i]
print(itogst)


for i in range(2, n+1):
    if i -1 >= 1:
        F[i] += F[i - 1]
    if i % 2 == 0 and i // 2 >= 1:
        F[i] += F[i // 2]

print("Количество способов достичь точки n из точки 1:", F[n])

# Визуализация на координатной прямой
x = list(range(1, n+1))
y = F[1:]

plt.plot(x, y)
plt.xlabel('Координата')
plt.ylabel('Количество способов')
plt.title('Оптимальное решение задачи о количестве способов достичь точки n из точки 1')
plt.show()