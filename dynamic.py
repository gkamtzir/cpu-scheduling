#Initialize data
 
t = [1, 5, 7, 1]
p = [0, 2, 5, 6]
 
 
#Dynamic Programming
 
def CPU(t, p):
    c = []
    for i in range(0, len(t)):
        new = []
        for j in range(0, len(p)):
            new.append(0)
        c.append(new)
    for j in range(0, len(p)):
        c[len(t) - 1][j] = min(t[len(t) - 1], p[j])
    for i in range (len(p) - 2, -1, -1):
        for j in range(0, len(p) - 1):
            c[i][j] = max(min(t[i], p[j]) + c[i + 1][0], c[i + 1][j + 1])
    return c
 
print("Dynamic Programming")
c = CPU(t, p)
for i in range(0, len(t)):
    for j in range(0, len(p)):
        print(c[i][j], end=" ")
    print("")
print("Final answer: ", c[0][0])
