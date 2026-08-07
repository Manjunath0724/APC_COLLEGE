numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

left_rotated = numbers[1:] + [numbers[0]]
right_rotated = [numbers[-1]] + numbers[:-1]

print("Left rotated by one:", left_rotated)
print("Right rotated by one:", right_rotated)
