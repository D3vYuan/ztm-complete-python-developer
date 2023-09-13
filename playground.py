def question_1():
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
    between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
    """
    combined_string=""
    for i in range(2000, 3200 + 1):
        if (i % 7 == 0 and i % 5 != 0):
            if combined_string:
                combined_string += "," + str(i)
            else:
                combined_string = str(i)
    print(combined_string)

def question_2(num):
    """
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output should be:40320
    """
    factorial_sum=1
    for i in range(num + 1):
        if i == 0 or i == 1:
            continue
        factorial_sum *= i
    print(factorial_sum)

def question_3(num):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
    such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
    Suppose the following input is supplied to the program: 8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    """
    integral_dict = {}
    for item in range(num):
        integral_dict[item + 1] = (item + 1) ** 2
    print(integral_dict)

def question_4(num):
    """
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program: 34,67,55,33,12,98
    Then, the output should be: ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
    """
    num_list = list(num.split(","))
    num_tuple = tuple(num_list)
    print(num_list)
    print(num_tuple)

def question_5():
    """
    Define a class which has at least two methods:

    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    """
    class IOString():
        def __init__(self):
            pass

        def getString(self):
            self.input = input("Please enter a number")

        def printString(self):
            print(self.input.upper())

def question_6():
    """
    Write a program that calculates and prints the value according to the given formula:
        Q = Square root of [(2 _ C _ D)/H]
    Following are the fixed values of C and H:
        C is 50. H is 30.
        D is the variable whose values should be input to your program in a comma-separated sequence.
    For example Let us assume the following comma separated input sequence is given to the program:
        100,150,180
    The output of the program should be:
        18,22,24
    """

def question_7(X, Y):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
    Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
    Then, the output of the program should be:
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    array2d = []
    for i in range(X):
        arrayRow = []
        for j in range(Y):
            arrayRow.append(i * j)
        array2d.append(arrayRow)
    print(array2d)            

def question_8(items):
    """
    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
        without,hello,bag,world
    Then, the output should be:
        bag,hello,without,world
    """
    item_list = list(items.split(","))
    sorted_list = sorted(item_list)
    print(sorted_list)

def question_9():
    """
    Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
        Hello world
        Practice makes perfect
    Then, the output should be:
        HELLO WORLD
        PRACTICE MAKES PERFECT
    """
    input_string=""
    while input_string != "Q":
        input_string = input()
        print(input_string.upper())

def question_10(input_string):
    """
    Write a program that accepts a sequence of whitespace separated words as input 
    and prints the words after removing all duplicate words and sorting them alphanumerically.
    """
    item_set = set(input_string.split(" "))
    sorted_set = sorted(item_set)
    for item in sorted_set:
        print(item, end=" ")
    print()

def question_11(input_string):
    """
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

    Example:
        0100,0011,1010,1001
    Then the output should be:
        1010
    """
    item_list = input_string.split(",")
    for item in item_list:
        # print(f"{item} - decimal {int(item, 2)}")
        item_decimal = int(item, 2)
        if (item_decimal % 5 == 0):
            print(item)

def question_12():
    """
    Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
    """
    even_list = [str(i) for i in range(1000, 3001) if i % 2 == 0]
    # print(even_list)
    print(",".join(even_list))

    # for i in range(1000, 3001):
    #     if (i % 2 == 0):
    #         print(i, end=",")

def question_13(input_string):
    """
    Write a program that accepts a sentence and calculate the number of letters and digits.

    Suppose the following input is supplied to the program:
        hello world! 123
    Then, the output should be:
        LETTERS 10
        DIGITS 3
    """
    letter_count = 0
    digit_count = 0
    for current_character in input_string:
        print(current_character)
        if current_character:
            if current_character.isalpha():
                letter_count += 1
            elif current_character.isdigit():
                digit_count += 1
    print(f"LETTERS {letter_count}")
    print(f"DIGITS {digit_count}")

def question_14(input_string):
    """
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:
        Hello world!
    Then, the output should be:
        UPPER CASE 1
        LOWER CASE 9
    """
    upper_count = 0
    lower_count = 0
    for current_character in input_string:
        if current_character:
            if current_character.isupper():
                upper_count += 1
            elif current_character.islower():
                lower_count += 1
    print(f"UPPER CASE {upper_count}")
    print(f"LOWER CASE {lower_count}")

def question_15(input_num):
    """
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:
        9
    Then, the output should be:
        11106
    """
    total_sum = 0
    input_string = str(input_num)
    for i in range(4):
        current_input = input_string * (i + 1)
        total_sum += int(current_input)
    print(total_sum)

def question_16(input_num):
    """
    Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
        1,2,3,4,5,6,7,8,9
    Then, the output should be:
        1,9,25,49,81
    """
    square_list = [ i ** 2 for i in input_num if i % 2 == 1 ]
    print(square_list)

def question_17(transaction_list):
    """
    Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
        D 100
        W 200
    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:
        D 300
        D 300
        W 200
        D 100
    Then, the output should be:
        500
    """
    balance = 0
    for transaction in transaction_list:
        transaction_split = transaction.split(" ")
        transaction_type = transaction_split[0]
        transaction_amount = transaction_split[1]
        if transaction_type == "D":
            balance += int(transaction_amount)
        elif transaction_type == "W":
            balance -= int(transaction_amount)
    print(balance)

def question_18():
    """
    A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

    Following are the criteria for checking the password:
        At least 1 letter between [a-z]
        At least 1 number between [0-9]
        At least 1 letter between [A-Z]
        At least 1 character from [$#@]
        Minimum length of transaction password: 6
        Maximum length of transaction password: 12

    Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

    Example

    If the following passwords are given as input to the program:
        ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
        ABd1234@1
    """

def question_19(input_list):
    """
    You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
        1: Sort based on name
        2: Then sort based on age
        3: Then sort by score
    The priority is that name > age > score.

    If the following tuples are given as input to the program:
        Tom,19,80
        John,20,90
        Jony,17,91
        Jony,17,93
        Json,21,85
    Then, the output of the program should be:
        [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    """
    # print(sorted(input_list, key=lambda tup: (tup[0],tup[1],tup[2])))

if __name__ == "__main__":
    # question_1()
    # question_2(8)
    # question_3(8)
    # question_4("34,67,55,33,12,98")
    # question_7(3, 5)
    # question_8("without,hello,bag,world")
    # question_9()
    # question_10("hello world and practice makes perfect and hello world again")
    # question_11("0100,0011,1010,1001")
    # question_12()
    # question_13("hello world! 123")
    # question_14("Hello world!")
    # question_15(9)
    # question_16([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # question_17(["D 300", "D 300", "W 200", "D100"])
    # question_19([("Tom", 19, 80), ("John", 20, 90), ("Jony", 17, 91), ("Jony", 17, 93), ("Json", 21, 85)])
     