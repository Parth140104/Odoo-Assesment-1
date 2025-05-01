import sys
sys.setrecursionlimit(1200)  # Allows slightly deeper recursion

def print_down(n):
    if n < 1:
        return
    print(n)
    print_down(n - 1)

# Start the countdown from 1000
print_down(1000)

