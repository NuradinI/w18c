for number in [1,2,3,25,234,151,423,453,5,45,4,12]:
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print('oops none are divisible!')