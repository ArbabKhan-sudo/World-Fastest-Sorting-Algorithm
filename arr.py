import  time
from matplotlib import pyplot as plt

start=time.time()
########################################
##########################################
def sort(unsorted):
   result = [0] * len(unsorted)
   neg = min(unsorted)
   pos = max(unsorted)
   count_array = [0 for i in range(neg, pos+1)]

################################################
##part 2
##Output: sortedarray (input)
   for i in unsorted:
      count_array[i-neg] += 1

   for j in range(1, len(count_array)):
       count_array[j] += count_array[j - 1]

   for k in reversed(unsorted):
      result[count_array[k-neg] - 1] = k
      count_array[k-neg] -= 1
   return result

arr=[]
for i in range(1):
   arr.insert(i,i%2)
sort(arr)
best=time.time()
arr1=[]

for i in range(1000000):
   arr1.insert(i,i%2)
sort(arr1)
worst=time.time()

print(best,worst)

plt.plot(best)
plt.plot(worst)
plt.legend(['TIME TAKEN TO SORT (best & Worst)'],loc='upper right')
plt.show()
