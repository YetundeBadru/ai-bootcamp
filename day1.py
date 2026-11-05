print("Hello, AI Engineer")

# Concept 1 : Variables and types
name = "Ada"
age = 25
score = 0.92
is_learning = True
print(f"{name} is {age} and score {score}")

name = ("Tope")
age = ("20")
gender = ("Female")
score = 0.85
is_learning = True
print(f"{name} is {age} a {gender}{","} and scored {score}")

# Concept 2: lists and loops
scores = [0.98, 0.77, 0.82, 0.45, 0.68]
for s in scores:
    print (s)

total = 0
for s in scores:
    total += s
print(total / len(scores))

# Concept 3: if/else
accuracy = 0.87

if accuracy > 0.9:
    print ("Good model")
elif accuracy > 0.8:
    print ("Decent, keep tunning")
else:
    print ("Needs work")

# Concept 4: Functions
def average (numbers):
    return sum(numbers) / len(numbers)
print (average([1, 2, 3, 4]))

# My turn: Exercises
# Make a list of 6 numbers. Print the average, the smallest, and the largest. Use a function for the average.
def average(numbers):
    return sum (numbers) / len(numbers)
numbers = [41, 20, 13, 42, 35, 66]
print (round(average(numbers), 2), min(numbers), max(numbers))

# Write a function grade_model(accuracy) that returns "Great", "Decent", or "Needs work" using the thresholds above. Test it with three different values.
def grade_model(accuracy):
    if accuracy > 0.9:
        return "Great Model"
    elif accuracy > 0.8:
        return "Decent, keep tuning"
    else:
        return "Bad Model, needs work !"

print (grade_model(0.92))
print (grade_model(0.85))
print (grade_model(0.69))

# Write a function count_above(numbers, threshold) that returns how many numbers are above the threshold. Test it on [0.91, 0.85, 0.93, 0.78] with threshold 0.9. The answer should be 2.
def count_above(numbers, threshold):
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count

numbers = [0.91, 0.85, 0.93, 0.78]
threshold = 0.9
print(count_above(numbers, threshold))

# Challenge: Given [3, 8, 1, 9, 4], find the biggest number using a loop, without max().
def max_number(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest
    
print(max_number([3, 8, 1, 9, 4]))
print(max_number([-5, -2, -8]))

# THE ENDI LOPIN CINEMA !!!!!!!!!!!!!!!