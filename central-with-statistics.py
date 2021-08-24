import statistics
grades = [47, 95, 88, 73, 88, 84]
total = sum(grades)
count = len(grades)
mean = statistics.mean(grades)
mode = statistics.mode(grades)
median = statistics.median(grades)
print('The mean is:', mean)
print('The mode is:', mode)
print('The median is:', median)
print('The sum of the grades is:',total)
print('The count of the grades is:',count)
