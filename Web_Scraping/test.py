def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

user_input = input("Enter a number: ")
user_number = int(user_input)
result = find_factors(user_number)
print(result)