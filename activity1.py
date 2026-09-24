def flip_number(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flip_number(num // 10)
    return last * pow(10, len(str(rest))) + rest

print("flipnumber peels last digit with % 10 then recurses on // 10. Press enter ")
print(" flip_number(123) =", flip_number(123))
print(" flip_number(456) =", flip_number(456))

n = int(input("Enter a number: "))
guess = input("What is flip_number(" + str(n) + ")? ")
input("flip_number peels last digit then places it at the front of each step ")
print(" flip_number(" + str(n) + ") =", flip_number(n), " your guess:", guess)