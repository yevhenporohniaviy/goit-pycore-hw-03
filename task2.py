import random

def get_numbers_ticket(min, max, quantity):
    # Validate input parameters
    if not (1 <= min <= max <= 1000):
        return []
    
    # Check if quantity is valid
    available_numbers = max - min + 1
    if quantity > available_numbers or quantity < min:
        print(f"Error: Cannot generate {quantity} unique numbers in range {min} to {max}")
        return []
    
    # Generate unique random numbers
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Sort the numbers before returning
    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))