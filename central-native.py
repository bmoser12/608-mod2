grades = [47, 95, 88, 73, 88, 84]
total = sum(grades)
count = len(grades)
average = sum(grades)/len(grades)
print('The average of the grades is:', average)
print('The number of grades is:',count)
print('The total of the grades is:',total)
sorted(grades):
  if count %2==0:
    median1 = grades[count//2]
    median2 = grades[count//2-1]
    median = (median1+median2)/2
  else:
    median = grades[count//2]
  print('The median is:'+str(median))
