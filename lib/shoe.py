#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will call the setter for size
        self.condition = "New"  # Set the initial condition to "New"

    @property
    def size(self):    
        return self._size

    @size.setter
    def size(self, size):
        # Corrected isinstance to check if size is an integer
        if not isinstance(size, int):
            print("size must be an integer")
            self._size = None  # Optionally set to None for invalid size
        else:
            self._size = size  # Set the size if valid

    def cobble(self):
        # Update the condition when the shoe is repaired
        self.condition = "New"
        print("Your shoe is as good as new!")

# Example Usage

# Creating a valid shoe instance
shoe1 = Shoe("Nike", 42)
print(shoe1.condition)  # Output: New (initial condition)

# Repairing the shoe (changes condition)
shoe1.cobble()  # Output: The Nike shoe has been repaired. Condition is now Repaired.
print(shoe1.condition)  # Output: Repaired

# Creating an invalid shoe instance (size is not an integer)
shoe2 = Shoe("Adidas", "large")  # Output: size must be an integer
print(shoe2.condition)  # Output: New (default condition, repair hasn't been called)
