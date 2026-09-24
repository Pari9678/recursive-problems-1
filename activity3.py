def is_power4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return is_power4(n // 4)
    return False

input("is_power4 dividesby 4 - n==1 returns True, remainder returns false. press enter ")
print(" is_power4(16) =", is_power4(16))
print(" is_power4(12) =", is_power4(12))

n = int(input("Enter a number: "))
guess = input("What is is_power4(" + str(n) + ")? ")
input("is_power4 has 2 stops - n==1 is True, remainder or n<=0 is false. press enter ")
print(" is_power4(" + str(n) + ") =", is_power4(n), " your guess:", guess)