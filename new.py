#for i in [1, 2, 3]: j = 1 while j<=i: print (i) j = j+1 print ('Blastoff!')
#i = 1
#height = 4
#while i <= height:
 #   j = 1
 #   line =""
 #   while j <= i:
#        line += str(i*(j*1)) + "\t"
#        j = j+1
#    print (line)
#    i = i+1
    
#x = range(3,6)
#sum = 0.0
#i = 0
#while i < len(x):
 #   sum += x[i]
  #  i += 1
#avg = sum/len(x)

#print("average is: ", avg)
  
  
#counts = dict()
#names = ['csev','cwen','csev','zqian','cwen']
#for name in names:
 #   counts[name] = counts.get(   name,0) + 1
#print(counts)


#L=["cccc","b","dd","aaa"]
#print("Normal sort: ",sorted(L))
#print("Sort with len: ", sorted(L,key=len))

#x = {1:2, 3:4, 4:3, 2:1, 0:0}
#sorted_by_value = sorted(x.items(), key = lambda kv : kv[-1])
 
import pandas as pd
s = pd.series(["a","b","c","d"])
print (s)

largest_so_far = -1
for current in [3, 41, 12, 9, 74, 15]:
    if current > largest_so_far:
        largest_so_far = current
print largest_so_far