l1 = [1,2,3]
l2 = [4,5,6]
l3 = list(zip(l1,l2))
print(l3)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = list(zip(l1,l2[::-1]))

print(l3)

stocks = ['PLDT','Meralco','San Miguel Corporation']
prices = [1295,603,71.50]

new_dict = {s:p for s,p in zip(stocks,prices)}

print(new_dict)