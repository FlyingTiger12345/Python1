class names:

    def twosum(self,tuple1,target):
        lookup = {}
        sum = 0
        for i,value in enumerate(tuple1,start=1):
            sum = sum + value
            lookup[i-1] = sum
            if sum >= target:
                print(lookup)
                return i

tuple1 = (10,20,30,40,50,60,70)
target = 100
objs = names()
print("the iteration no. where it reaches the target is",objs.twosum(tuple1,target))