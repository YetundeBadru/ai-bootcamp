# Day 4, Part 2: NumPy

# Step 1: Install it
# Already installed and stored in requirements.txt

# Step 2: Make an array
import numpy as np
scores = np.array([0.92, 0.85, 0.69, 0.78])

print(scores)
print(type(scores))

# Step 3: Math on the whole array at once (Vectorization)
print(scores * 100)
print(scores + 0.05)
print(scores > 0.8)

# Step 4: Built-in statistics
print(scores.mean())
print(scores.max())
print(scores.min())
print(scores.std())

# Step 5: Filtering with a condition
high = scores[scores > 0.8]
print(high)

# Step 6: 2D arrays (a table)
data = np.array([
    [0.92, 0.85, 0.69],
    [0.78, 0.88, 0.95]
])
print(data.shape)
print(data[0])
print(data[:, 1])
print(data.mean(axis=0))
print(data.mean(axis=1))

# My exercises
# Make an array of 6 accuracy scores. Print the mean, max, and min.
accuracy_scores = np.array([0.77, 0.92, 0.85, 0.80, 0.64, 0.43])
print(accuracy_scores.mean())
print(accuracy_scores.max())
print(accuracy_scores.min())

# Use a condition to print only the scores above the mean.
above_mean = accuracy_scores[accuracy_scores > accuracy_scores.mean()]
print(np.round(above_mean, 2))

# Multiply all scores by 100 to get percentages, and round them with np.round(percentages, 1).
print(np.round(accuracy_scores * 100, 1))

# Challenge: Make a 3x3 array (3 students, 3 scores each). Print each student’s average (hint: axis=1) and each subject’s average (hint: axis=0).
student_scores = np.array([
    [0.95, 0.78, 0.82],
    [0.95, 0.89, 0.93],
    [0.45, 0.68, 0.75]
])
print(np.round(student_scores.mean(axis=1), 2))
print(np.round(student_scores.mean(axis=0), 2))