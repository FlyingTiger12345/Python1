table = ["sixseven",6,7,["sixseven",6,7]]
print(table)

table1 = (67,6,7,677,667,67,67,67,67,67)
table12 = (76,76,7,677,667,76,76,76,76,76)
print(table1)
print(table12)

table1 = table1 + (10000,)
print(table1)
table12 = table12 + (10000,)
print(table12)

print("the count of sixseven",table1.count(67),table12.count(76))
print(table[2:4])
print(table[:-1])
print(table[1:-1])