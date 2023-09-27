def freqDist(f):
    d={}
    for i in range(len(f)):
     if(f[i] in d):
        d[f[i]]+=1
     else:
        d[f[i]]=1
    print(d)
f=list(map(int,input().split()))
freqDist(f)
