def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
try:
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

my_numbers = []
try:
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

my_numbers = [10, 20, 'a']
try:
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")
