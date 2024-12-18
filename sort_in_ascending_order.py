import numpy as np
data_type = [('name','S15'),('class',int),('height',float)]
student_details = [('Mack',8,68),('Aryan',6,63),('Yahya',7,65)]

students = np.array(student_details,dtype=data_type)
print("Original array")
print(students)
print("Sort by height")
print(np.sort(students,order='height'))