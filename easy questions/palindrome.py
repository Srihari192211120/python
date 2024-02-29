from random import choice

def is_palindrome(s):
    return s == s[::-1]

def is_number_palindrome(n):
    return str(n) == str(n)[::-1]

def main():
    test_cases = [
        "MONEY",
        5678765,
        "MALAY12321ALAM",
        "MALAYALAM",
        1234.4321
    ]

    case = choice([1, 2])
    print("Case:", case)

    if case == 1:
        string = choice(test_cases)
        print("String:", string)
        if is_palindrome(string):
            print("Palindrome")
        else:
            print("Not a Palindrome")
    else:
        number = choice(test_cases)
        print("Number:", number)
        if is_number_palindrome(number):
            print("Palindrome")
        else:
            print("Not a Palindrome")

if __name__ == "__main__":
    main()
