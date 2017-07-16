#Initialize data

t = [1, 5, 7, 1]
p = [0, 2, 5, 6]

#Recursive function
 
def CPU_REC(time, Dt, t, p):
    if time + 1 > len(t):
        return 0
    elif min(t[time], p[Dt]) == 0:
        if Dt == len(p):
            return CPU_REC(time + 1, Dt, t, p)
        else:
            return CPU_REC(time + 1, Dt + 1, t, p)
       
    else:
        if Dt == len(p):
            return max(min(t[time], p[Dt]) + CPU_REC(time + 1, 0, t, p), CPU_REC(time + 1, Dt, t, p))
        else:
            return max(min(t[time], p[Dt]) + CPU_REC(time + 1, 0, t, p), CPU_REC(time + 1, Dt + 1, t, p))
print("Recursive: ", CPU_REC(0, 0, t, p))
