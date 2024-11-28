def sum_with_while(start, end):
    """
    Calculate the sum of all numbers between start and end (inclusive) using a while loop.
    """
    return sum(list(i for i in range(start, end + 1)))

def count_vowels_in_string(input_string):
    """
    Count the number of vowels in a given string using a for loop.
    """
    counter = 0
    for i in input_string:
        if i.lower() in "aeiou":
            counter += 1
    return counter

def filter_numbers(numbers):
    """
    Filter a list of numbers based on specific conditions using a for loop and conditionals.
    """
    positive = list()
    even = list()
    odd = list()
    negetive = list()
    dict_of_nums = {"positive":positive,
                    "negative":negetive,
                    "even" :even,
                    "odd":odd}
    
    for number in numbers: 
        if number % 2 == 0:
            even.append(number) 
        elif number % 2 != 0:
            odd.append(number)
    for number in numbers:
        if str(number) in "123456789":
            positive.append(number)
        elif str(number) in "-1-2-3-4-5-6-7-8-9":
            negetive.append(number)
           
    return dict_of_nums


def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms using a while loop.
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_nums = list()
        a, b = 0, 1
        while a < n:
            fib_nums.append(a)
            a ,b = b , a + b
        return fib_nums
   
def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    """
    pass

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.
    """
    pass

def find_dna_sequence(dna, sequence):
    """
    Find the first occurrence of a DNA subsequence within a larger DNA string.
    """
    pass

def is_palindrome(input_string):
    """
    Check if a given string is a palindrome (ignoring spaces, capitalization, and punctuation).
    """
    word = list(letter.lower() for letter in input_string if letter.lower() in "abcdefghijklmnopqrstuvwxyz")
    return word == word[::-1]


def generate_permutations(input_string):
    """
    Return all possible permutations of a given string.
    """
    pass

def is_valid_sudoku(board):
    """
    Validate a given 9x9 Sudoku board.
    """
    pass

def solve_n_queens(n):
    """
    Find all possible solutions to the N-Queens problem.
    """
    pass

def longest_common_subsequence(str1, str2):
    """
    Find the length of the longest subsequence common to both strings.
    """
    counter = 0
    for letter in str2:
        if letter in str1:
            counter += 1
    return counter

if __name__ == "__main__":
    pass
