# Print the Fibonacci sequence up to n terms.

def generate_fibonacci(n):
    # Initialize the first two numbers
    a, b = 0, 1
    
    # Generate and print the sequence using a loop
    for i in range(n):
        print(a, end=" ")
        # Update 'a' to the current 'b', and 'b' to the sum of both
        a, b = b, a + b

# Example usage: Generate the first 10 Fibonacci numbers
generate_fibonacci(5)


