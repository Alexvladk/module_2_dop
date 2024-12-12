num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number_1= int(input("Введите число: " ))
result = set()
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] == number_1:
            result.add((num[i], num[j]))
print(result)