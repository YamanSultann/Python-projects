class pair_elements:
    def twoSum(self,num,target):
        lookup = {}

        for i, num in enumerate(num):
            if target - num in lookup:
                return (lookup[target - num],i)
            lookup[num] = i

value = int(input("Enter the sum for which you want to make this search: "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70,80,90),value))