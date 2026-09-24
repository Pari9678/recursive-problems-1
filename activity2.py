def flip_name(s):
    if len(s) == 1:
        return s
    return flip_name(s[1:]) + s[0]

input("flip_name recurse on (s[1:]) and then attaches s[0] at the end. press enter ")
print(" flip_name('Maya') =", flip_name('Maya'))
print(" flip_name('Code') =", flip_name('Code'))

n = input("Enter a name: ")
guess = input("What is flip_name(" + str(n) + ")? ")
input("flip_name(s) = (s[1:]) + s[0], first charcter continues lands last. press enter ")
print(" flip_name(" + str(n) + ") =", flip_name(n), " your guess:", guess)