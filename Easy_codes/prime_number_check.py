# Write your code below this line 👇
def prime_checker(number):
    flag = True
    n = int(number / 2);
    while n >= 2:

        if number % n == 0:
            flag = False
            print(f"{number} is divisible by {n}")
        n -= 1

    if not flag:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



