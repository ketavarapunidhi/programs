def kelement(k,a):
          n=len(a)
          for i in range(n):
                    for j in range(i,n):
                              if(a[i]>a[j]):
                                 t=a[i]
                                 a[i]=a[j]
                                 a[j]=t
          return(a[k-1])

#drivercode
a=[7,10,4,3,20,15]
k=4
print(kelement(k,a))
