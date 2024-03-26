
def hcf(number1, number2):
    prime_factors_number1 = prime_factorisation(number1)
    prime_factors_number2 = prime_factorisation(number2)
    multiplicands = cmnlst(prime_factors_number1, prime_factors_number2)
    highest_common_factor = 1
    for i in multiplicands:
        highest_common_factor = highest_common_factor * i
    return highest_common_factor


def lcm(number1, number2):
    if iscoprime(number1, number2):
        return number1 * number2
    else:
        smaller_number = number2
        larger_number = number1
        if number1 < number2:
            larger_number = number2
            smaller_number = number1
        if larger_number % smaller_number == 0:
            return larger_number
        multiples = []
        for numbers in range(smaller_number, ((number1 * number2) + 1)):
            if numbers % number1 == 0 and numbers % number2 == 0:
                multiples.append(numbers)
        return multiples[-1]


def isprime(number):
    is_prime = True
    if number == 0 or number == 1:
        is_prime = False
    if number == 2 or number % 2 != 0:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
    else:
        is_prime = False
    return is_prime


def iscoprime(number1, number2):
    prime_fact1 = prime_factorisation(number1)
    prime_fact2 = prime_factorisation(number2)
    common_prime_factors = cmnlst(prime_fact1, prime_fact2)
    if len(common_prime_factors) > 0:
        return False
    else:
        return True


def primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(2 * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    final_list = []
    for i in range(n+1):
        if prime[i]:
            final_list.append(i)
    return final_list


def prime_factorisation(number):
    prime_factors = []
    divisors = 2
    while number != 1 and divisors <= number:
        if number % divisors == 0 and isprime(divisors):
            number = number / divisors
            prime_factors.append(divisors)
        else:
            divisors += 1
    return prime_factors


def factors(number):
    prime_factors1 = prime_factorisation(number)
    prime_factors2 = prime_factors1[:]  # To be printed at last with non-prime factors.
    factors_of_number = [1, number]
    for j in range(len(prime_factors1)-1):
        i = 0
        while i < (len(prime_factors1)-1):
            factors_of_number.append(prime_factors1[0] * prime_factors1[i + 1])
            i += 1
        else:
            del prime_factors1[0]
    return sorted(remdup(prime_factors2 + factors_of_number))     # Return Sorted List of uniques.


def cmnlst(list1, list2):
    common_list = []
    for i in list1:
        if i in list2:
            common_list.append(i)
            list2.remove(i)

    return common_list


def float_to_fraction(number):
    str_number = str(number)
    str_number_split = str_number.split('.', 1)     # Get the decimal part
    power_of_10 = len(str_number_split[-1])         # Get Number of decimal places
    numerator = round(number * 10 ** power_of_10)
    denominator = round(10 ** power_of_10)
    # Simplify the fraction:
    highest_common_factor = hcf(numerator, denominator)
    numerator, denominator = int(numerator / highest_common_factor), int(denominator / highest_common_factor)
    # For Mixed Fraction:
    quotient = numerator // denominator
    remainder = numerator % denominator
    return numerator, denominator, quotient, remainder


def remdup(list1):      # Removes duplicates from a list
    uniques = []
    for i in list1:
        if i not in uniques:
            uniques.append(i)
    return uniques


def factorsum(number):
    return sum(remdup(factors(number) + prime_factorisation(number)))


def pfactorsum(number):     # Proper Factor Sum
    return factorsum(number) - number


def isabundant(number):
    is_abundant = False
    list_divisors = []
    for numbers in range(1, number):
        if number % numbers == 0:
            list_divisors.append(numbers)
    if sum(list_divisors) > number:
        is_abundant = True
    return is_abundant


def isamicable(a, b):
    sum_factors_a = pfactorsum(a)
    sum_factors_b = pfactorsum(b)
    return True if sum_factors_a == b and sum_factors_b == a and a != b else False


def reverse(number):
    string = str(number)
    revnum = 0
    place_value = 1
    for i in string:
        revnum += int(i) * place_value
        place_value *= 10
    return revnum

