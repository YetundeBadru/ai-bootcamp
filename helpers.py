def average(numbers):
    return sum(numbers) / len(numbers)

def grade_model(accuracy):
    if accuracy > 0.9:
        return "Great"
    elif accuracy > 0.8:
        return "Decent, needs tuning"
    else:
        return "needs work"

def count_above(numbers, threshold):
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count

def read_scores(filename):
    scores = []
    try:
        with open(filename, "r") as f:
            for line in f:
                scores.append(float(line))
    except FileNotFoundError:
        print("That file does not exist")
    return scores