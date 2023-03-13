def minisumofproduct(a,b):
          n=len(a)
          s=0
          for i in range(n):
                    s+=(min(a)*min(b))
                    a.remove(min(a))
                    b.remove(min(b))
          print(s)
#drivercode
a=[3,1,1]
b=[6,5,4]
minisumofproduct(a,b)
