# Concept 1: Lists
scores = [0.98, 0.84, 0.93]

scores.append(0.78)    # adding to the list
scores[0]              # calling the first item
scores[-1]             # calling the last item
print(len(scores))     # no of items
print(scores[1:3])     # 2nd to third item

high = [s for s in scores if s > 0.9]
low = [s for s in scores if s < 0.9]
print(high)
print(low)

# Concept 2: Dictionaries
model = {"name" : "Random forest", 
          "accuracy" : 0.93,
          "features" : 12
}
print(model["name"])
model["accuracy"] = 0.95
model["trained"] = True

for key, value in model.items():
    print(key, value)

model = {"name" : "Linear regression",
         "accuracy" : 0.68,
         "Features" : 8
}

print(model["name"])
model["accuracy"] = 0.78
model["Trained"] = True

for key, value in model.items():
    print(key, value)

# Concept 3: Reading and writing files
# write
with open("notes.txt", "w") as f:
    f.write("Day 2 notes\n")
# read
with open("notes.txt", "r") as f:
    text = f.read()
print(text)

# Concept 4: JSON
import json
data = {"name": "Ada", "scores": [0.9, 0.8]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["scores"])

import json
model = {"name": "Decision tree",
         "accuracy": 0.68,
         "Features": 8,
         "Trees": 10
}
with open("model.json", "w") as f:
    json.dump(model, f, indent=2)
with open("model.json", "r") as f:
    loaded = json.load(f)
print(loaded["Trees"])

# My exercises
#Make a list of 6 accuracy scores. Use a list comprehension to build a new list of only the scores above 0.8, and print it.
scores = [0.93, 0.80, 0.47, 0.71, 0.90, 0.68]
threshold = [s for s in scores if s >0.8]
print(threshold)

# Make a dictionary for a student with name, age, and scores (a list of 3 numbers). Print the student’s name and the average of their scores, using your average function idea.
def average(numbers):
    return sum (numbers) / len(numbers)
student = {"name": "Bimpe",
           "age": 23,
           "scores": [0.65, 0.83, 0.49]
}
print(student["name"])
avg = average(student["scores"])
print(f"{student['name']} averaged {round(avg, 2)}")

# Write a function save_scores(scores, filename) that writes each score on its own line in a text file. Then run it and open the file in VS Code to check it.
def save_scores(scores, filename):
    with open(filename, "w") as f:
        for score in scores:
            f.write(str(score) + "\n")

scores = [0.58, 0.82, 0.63, 0.90]
save_scores(scores, "scores.txt")

with open("scores.txt", "r") as f:
    text = f.read()
print(text)

# Challenge: Save your student dictionary to a JSON file, then read it back and print the name and scores to prove it worked.
import json
student = {"name": "Bimpe",
           "age": 23,
           "scores": [0.65, 0.83, 0.49]
}
with open("student.json", "w") as f:
    json.dump(student, f, indent=2)
with open("student.json", "r") as f:
    loaded = json.load(f)
print(loaded)
print(loaded["name"])

# THE ENDI LOPIN CINEMA !!!!!!!!!!!!!!!