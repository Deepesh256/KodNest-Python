word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

# Slice the string, list and tuple
middle = word[1:-1]
first_two = numbers[:2]
reverse_tuple = record[::-1]

print("Middle:",middle)
print("First Two:",first_two)
print("Reversed Tuple:",reverse_tuple)