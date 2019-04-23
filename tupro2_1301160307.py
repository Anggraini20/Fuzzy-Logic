import numpy as np

A = np.genfromtxt('DataTugas2.csv',skip_header=1, delimiter=',')



def naik(x, b, a):
    return ((x - a) / (b - a))


def turun(x, b, a):
    return (-1 * (x - b) / (b - a))


def pendapatan(p):
    p_low =0
    p_med =0
    p_high =0
    if p >= 0 and p <= 1:
        if p <= 0.7:
            p_low = 1
        else:
            p_low = turun(p, 1, 0.7)
            p_med = naik(p, 1,0.7 )
    elif p > 0.7 and p <= 1.7:
        if p >= 1 and p <= 1.4:
            p_med = 1
        elif p > 1.4 and p <= 1.7:
            p_med = turun(p, 1.8, 1.4)
            p_high = naik(p, 1.8, 1.4)
    else:
        p_high = 1


    return p_low, p_med, p_high

def hutang(h):
    h_low = 0
    h_med = 0
    h_high =0
    if h>=0 and h<=35.0 :
        if h<=30.0 :
            h_low =1
        else:
            h_low = turun(h,35.0,30.0)
            h_med = naik(h,35.0,30.0)
    elif h >30.0 and h<=65.0 :
        if h>=35.0 and h<=60.0 :
            h_med = 1
        elif h>60.0 and h<=65.0 :
            h_med = turun(h,65.0,60.0)
            h_high = naik(h,65.0,60.0)
    else:
        h_high = 1
    return h_low,h_med,h_high
inf=[]
no = 1
for item in A :
    plow,pmed,phigh = pendapatan(item[1])
    hlow, hmed, hhigh = hutang(item[2])
    inf.append([[plow,pmed,phigh],[hlow,hmed, hhigh]])

B=[]

for item in inf :
    rej = max((min(item[0][0],item[1][0])),(min(item[0][1],item[1][0])),(min(item[0][1],item[1][1])),(min(item[0][2],item[1][0])),(min(item[0][2],item[1][1])),(min(item[0][2],item[1][2])))
    con = min(item[0][1],item[1][2])
    acc = max((min(item[0][0],item[1][1])),(min(item[0][0],item[1][2])))
    B.append([rej,con,acc])
C=[]
D=[]
i=1
for item in B:
    C.append([((item[0]*50)+(item[1]*70)+(item[2]*100))/(item[0]+item[1]+item[2]),i])
    i=i+1

C.sort(key=lambda isi:isi[0], reverse=True)
for item in C:
    D.append(item[1])
    if len(D)>19 :
        break

for item in D :
    print(item)

np.savetxt('TebakanTugas2.csv',D,fmt='%i')

