# HACKER RANK PYTHON #
# Q1
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
  # Q2
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)

# Q3
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)

# Q4
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))

# Q5
n = int(input())

for i in range(1, n + 1):
    print(i, end="")
  
