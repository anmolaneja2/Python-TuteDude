list=[]

for i in range(1,11):
    list.append(i)

print(f"Orignal List: {list}")
first_five = list[:5]
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {first_five[::-1]}")