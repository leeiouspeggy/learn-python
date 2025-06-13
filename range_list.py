numbers = list(range(1,6))
print(numbers)
#this prints numbers as a list

odd_numbers = list(range(1,11,2))
print(odd_numbers)
#allows you to generate numbers in a range in a specific pattern

squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)
