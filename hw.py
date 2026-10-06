print("FLIP IT WITH RECURSION")

num = 4827
temp = num
while temp > 0:
    digit = temp % 10
    print("Digit:", digit)
    temp = temp // 10
def count_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num // 10)

print("Number of digits:", count_digits(num))
def reverse_number(num):
    if num < 10:
        return num
    digits = count_digits(num)
    last_digit = num % 10
    remaining = num // 10
    return last_digit * (10 ** (digits - 1)) + reverse_number(remaining)

print("Original:", num)
print("Reversed:", reverse_number(num))
def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]
text = "recursion"

print("Original:", text)
print("Reversed:", reverse_string(text))
def is_power_of_4(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    if num % 4 != 0:
        return False
    return is_power_of_4(num // 4)

numbers = [1, 4, 16, 64, 20]
for number in numbers:
    print(number, "is a power of 4:", is_power_of_4(number))


print("num <= 0 stops invalid checks.")
print("num == 1 confirms that the number is a power of 4.")
print("len(text) <= 1 stops the string recursion.")