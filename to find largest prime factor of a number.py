
# Program to check if a number is prime or not

def is_prime(num):

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
    flag = False

# prime numbers are greater than 1
    if num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break

# check if flag is True
    return not flag


def largest_prime_factor(num):

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
    factor = 1

# prime numbers are greater than 1
    if num > 1:
    # check for factors
        for i in range(2, int(num/2) +1):
            if (num % i) != 0 or not is_prime(i):
             # continue execution of loop
                continue
            # if factor is found, set flag to True
            factor = i

# check if flag is True
    return factor

print(largest_prime_factor(101))

