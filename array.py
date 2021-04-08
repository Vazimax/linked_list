array = [x for x in range(0,10)]
target = 4

for i in array:
    if i == target :
        print("Gotcha")
        break

array.insert(0,2)
print(array)
numbers = []
numbers.extend([4,5,6])
print(numbers)