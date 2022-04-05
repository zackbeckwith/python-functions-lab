#Challenge 1

def sum_to(n):
  return(n*(n+1) // 2)

print(sum_to(10))

#Challenge 2

def largest(list):
  return max(list)

print(largest([1, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

#Challenge 3

def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'e')) 
print(occurrences('fleep floop', 'p')) 
print(occurrences('fleep floop', 'ee')) 
print(occurrences('fleep floop', 'fe'))

#Challenge 4