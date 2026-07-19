import array as arr

array1 = arr.array('i', [1,2,3,4,5,3,7,8,3])
print("the original",array1)

array2 = array1.count(3)
print("the count of threes",array2)

array1.reverse()
print("the reverse of this is",array1)