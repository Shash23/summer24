import sys

def sum_of_squares_of_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

def is_happy_number(n):
    
    visited = set()
    
    while n != 1 and n not in visited:
        
        visited.add(n)
        n = sum_of_squares_of_digits(n)
        
    return n == 1

def main():
    
    input = sys.stdin.read
    numbers = input().split()
    for number in numbers:
        n = int(number)
        if is_happy_number(n):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()
