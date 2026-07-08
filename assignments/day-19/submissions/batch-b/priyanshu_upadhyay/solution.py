# Day 19 Assignment - Build a Baby GPT With Word Transitions

import random
from collections import Counter

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# Question 1: Prepare the Words
words = text.replace(".", "").split()
print("=== Question 1 ===")
print("Number of words:", len(words))
print("First ten words:", words[:10])
print("Number of unique words:", len(set(words)))

# Question 2: Build the Transition Chain
# One word can have several possible next words because the same word
# may appear in different positions in the text, each followed by a different word.
print("\n=== Question 2 ===")
chains = {}
for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])
print(chains)

# Question 3: Inspect Learned Transitions
print("\n=== Question 3 ===")
for word in ["artificial", "is", "machine"]:
    print(f"{word} -> {chains.get(word, [])}")

# Question 4: Create a Safe Generator
print("\n=== Question 4 ===")

def generate(start_word, max_new_words=15):
    start_word = start_word.lower()
    if start_word not in chains:
        return f"No continuation found for '{start_word}'"
    result = [start_word]
    current = start_word
    for _ in range(max_new_words):
        next_words = chains.get(current, [])
        if not next_words:
            break
        current = random.choice(next_words)
        result.append(current)
    return " ".join(result)

print(generate("artificial"))

# Question 5: Make Random Output Reproducible
# A seed makes random choices predictable and repeatable.
# This helps with debugging because you get the same output every run,
# making it easier to compare results and find bugs.
print("\n=== Question 5 ===")
random.seed(42)
result1 = generate("artificial")
random.seed(42)
result2 = generate("artificial")
print("Result 1:", result1)
print("Result 2:", result2)
print("Both results are equal:", result1 == result2)

# Question 6: Compare Starting Words
print("\n=== Question 6 ===")
for word in ["machine", "data", "world"]:
    print(f"Starting with '{word}':", generate(word))

# Question 7: Find the Most Likely Next Word
print("\n=== Question 7 ===")

def most_likely_next(word):
    word = word.lower()
    next_words = chains.get(word, None)
    if not next_words:
        return None
    counter = Counter(next_words)
    most_common_word, count = counter.most_common(1)[0]
    return most_common_word, count

for word in ["artificial", "machine", "robot"]:
    result = most_likely_next(word)
    if result:
        print(f"Most likely next word after '{word}': '{result[0]}' (count: {result[1]})")
    else:
        print(f"'{word}' not found in chains")

# Question 8: Handle an Unknown Start Word
print("\n=== Question 8 ===")
message = generate("robot")
print(message)
print("Program did not raise an exception.")

# Question 9: Explain the Limitations
# 1. The generator can only use patterns from training text because it builds
#    its chain only from words it has seen. It has no knowledge of language rules
#    or words outside the training text.
#
# 2. Output can become repetitive or grammatically incorrect because the model
#    only looks at one previous word to predict the next. It has no understanding
#    of grammar, sentence structure, or long-range context.
#
# 3. This one-word transition model is different from a transformer because a
#    transformer uses attention to consider all words in context simultaneously,
#    learns deep semantic relationships, and is trained on massive data with
#    billions of parameters. This model simply counts word pairs.

print("\nThis classroom generator is not a real GPT model.")