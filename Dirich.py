import sympy
import matplotlib.pyplot as plt
from collections import defaultdict

def generate_primes(limit):
    """Generate a list of prime numbers up to the given limit."""
    
    primes = []
    for p in sympy.primerange(2, limit):
        primes.append(p)
        
    return primes

def convert_to_base(number, base):
    """Convert a number to a specified base and return its last digit."""
    if base < 2:
        raise ValueError("Base must be at least 2.")
    
    return number % base

def count_last_digits_in_base(primes, base):
    """Count the occurrences of the last digits of primes in the specified base."""
    counts = defaultdict(int)
    for prime in primes:
        last_digit = convert_to_base(prime, base)
        counts[last_digit] += 1

    for digit in range(base):
        counts.setdefault(digit, 0)
    
    return dict(sorted(counts.items()))

def plot_histogram(counts, base, limit):
    """Plot a histogram of the counts of last digits."""
    digits = list(counts.keys())
    frequencies = list(counts.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(digits, frequencies, color='skyblue', edgecolor='black')
    

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{height}', ha='center', va='bottom')
    
    plt.xlabel('Last Digits in Base ' + str(base), fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Distribution of Last Digits of Primes (up to {limit}) in Base {base}', fontsize=14)
    plt.xticks(digits)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    try:
        base = int(input("Choose your desired base (greater than 1): "))
        if base < 2:
            print("Error: Base must be at least 2.")
            return
            
        limit_input = input(f"Enter the upper limit for primes (default=1000000, max recommended=10^7): ")
        limit = int(limit_input) if limit_input.strip() else 10**6
        
        print(f"Generating prime numbers up to {limit}...")
        primes = generate_primes(limit)
        print(f"Found {len(primes)} prime numbers.")
        
        print(f"Counting the last digits in base {base}...")
        counts = count_last_digits_in_base(primes, base)
        print("Last digit counts:", counts)
        
        print("Plotting the results...")
        plot_histogram(counts, base, limit)
        
    except ValueError as e:
        print(f"Input error: {e}. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()