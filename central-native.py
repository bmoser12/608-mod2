grades = [47, 95, 88, 73, 88, 84]
grades.sort()
total = sum(grades)
count = len(grades)
average = sum(grades)/len(grades)
print('The average of the grades is:', average)
print('The number of grades is:',count)
print('The total of the grades is:',total)
if count %2==0:
  median1 = grades[count//2]
  median2 = grades[count//2-1]
  median = (median1+median2)/2
else:
  median = grades[count//2]
print('The median is:'+str(median))
print(grades)
data = collections.counter(grades)
data_list=dict(data)
print(data_list)
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value)
if len(mod_val)==len(num_list):
   print('no mode in the list')
else:
   print('The mode of the list is:'+','.join(map(str,mode_val)))
