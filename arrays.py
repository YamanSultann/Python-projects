import array as arr
array_num = arr.array("i",[1,3,5,6,3,7,9,3])
print("The original array"+ str(array_num))
print("The occurence of 3 =",array_num.count(3))

array_num.reverse()
print("Reversed array"+ str(array_num))