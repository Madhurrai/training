def histo(a):
    for i in a:
        print(i,end="")
        print("| "+a[i]*"===",a[i])
a = {2:6,1:3, 9:2,4:3,3:1}
histo(a)