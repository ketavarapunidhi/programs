def countofarray(a,b):
          c=0
          for i in range(len(a)):
                    for j in range(len(b)):
                              if(a[i]==b[j]):
                                 c=c+1
          return c

#drivercode
a=[3,9,4]
b=[3,2,1]
print(countofarray(a,b))
