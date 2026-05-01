# List Stats using Functions

def list_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg, max(numbers), min(numbers)

nums = [10, 20, 30, 40, 50]

total, avg, maximum, minimum = list_stats(nums)

print("Sum:", total)
print("Average:", avg)
print("Max:", maximum)
print("Min:", minimum)

