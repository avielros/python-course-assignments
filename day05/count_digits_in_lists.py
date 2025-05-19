numbers = [1203, 1256, 312456, 98, 555]

count = [0] * 10

for num in numbers:
    for char in str(num):      
        count[int(char)] += 1


for digit in range(10):
    print(f"{digit}  {count[digit]}")
