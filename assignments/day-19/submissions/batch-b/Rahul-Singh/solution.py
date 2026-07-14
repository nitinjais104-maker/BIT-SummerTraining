import random
from collections import Counter

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# Question 1

text = text.replace(".", "")
words = text.split()

print("Number of words:", len(words))
print("First 10 words:", words[:10])
print("Unique words:", len(set(words)))

# Question 2

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nTransition Dictionary:")
print(chains)

# One word can have several possible next words because
# it may appear in different sentences or contexts.

# Question 3

print("\nNext words for 'artificial':", chains.get("artificial", []))
print("Next words for 'is':", chains.get("is", []))
print("Next words for 'machine':", chains.get("machine", []))

# Question 4

def generate(start_word, max_new_words=15):
    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]
    current = start_word

    for _ in range(max_new_words):
        next_words = chains.get(current)

        if not next_words:
            break

        current = random.choice(next_words)
        result.append(current)

    return " ".join(result)

print("\nGenerated from 'artificial':")
print(generate("artificial"))

# Question 5

random.seed(42)
text1 = generate("artificial")

random.seed(42)
text2 = generate("artificial")

print("\nResult 1:")
print(text1)

print("\nResult 2:")
print(text2)

print("\nAre both outputs equal?", text1 == text2)

# A random seed makes random results repeatable,
# which helps debugging and comparing outputs.

# Question 6

print("\nStarting with 'machine':")
print(generate("machine"))

print("\nStarting with 'data':")
print(generate("data"))

print("\nStarting with 'world':")
print(generate("world"))

# Question 7

def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    counter = Counter(chains[word])
    return counter.most_common(1)[0]

print("\nMost likely after 'artificial':", most_likely_next("artificial"))
print("Most likely after 'machine':", most_likely_next("machine"))
print("Most likely after 'robot':", most_likely_next("robot"))

# Question 8

print("\nUnknown word:")
print(generate("robot"))

print("Program handled the unknown word without any error.")

# Question 9

print("\nThis classroom generator is not a real GPT model.")

# The generator only learns patterns that exist in the training text.
# It cannot create knowledge beyond those learned transitions.
# The output may repeat words or become grammatically incorrect
# because it only looks at one previous word.
# A transformer understands long-range relationships and context,
# while this model only predicts using one-word transitions.