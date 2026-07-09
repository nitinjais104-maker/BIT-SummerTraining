import random
from collections import Counter

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# ==========================================================
# Question 1: Prepare the Words
# ==========================================================

text = text.replace(".", "")

words = text.split()
print("Total Words :", len(words))
print("First 10 Words :", words[:10])
print("Unique Words :", len(set(words)))

print("=" * 50)
# ==========================================================
# Question 2: Build the Transition Chain
# ==========================================================

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])
print("Transition Chain Dictionary:\n")
print(chains)

# One word can have multiple next words because it may appear
# in different places in the training text.

print("=" * 50)
# ==========================================================
# Question 3: Inspect Learned Transitions
# ==========================================================

for word in ["artificial", "is", "machine"]:
    print(f"{word} -> {chains.get(word, [])}")

print("=" * 50)
# ==========================================================
# Question 4: Create a Safe Generator
# ==========================================================

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

print("=" * 50)
# ==========================================================
# Question 5: Make Random Output Reproducible
# ==========================================================

random.seed(42)

sentence1 = generate("artificial")

random.seed(42)

sentence2 = generate("artificial")

print(sentence1)
print(sentence2)

print("Equal :", sentence1 == sentence2)

# Random seed makes random output repeatable.
# It helps while debugging and comparing results.

print("=" * 50)
# ==========================================================
# Question 6: Compare Starting Words
# ==========================================================

for word in ["machine", "data", "world"]:
    print(f"\nStarting Word : {word}")
    print(generate(word))

print("=" * 50)
# ==========================================================
# Question 7: Find the Most Likely Next Word
# ==========================================================

def most_likely_next(word):

    word = word.lower()

    if word not in chains:
        return None

    count = Counter(chains[word])

    return count.most_common(1)[0]

print("artificial :", most_likely_next("artificial"))
print("machine :", most_likely_next("machine"))
print("robot :", most_likely_next("robot"))

print("=" * 50)
# ==========================================================
# Question 8: Handle an Unknown Start Word
# ==========================================================

print(generate("robot"))

print("Program executed successfully without any exception.")

print("=" * 50)
# ==========================================================
# Question 9: Explain the Limitations
# ==========================================================

print("This classroom generator is not a real GPT model.")
# Why can the generator only use patterns found in its training text?
# It can only generate patterns that already exist
# in the training text.

# Why can the output become repetitive or grammatically incorrect?
# The output can become repetitive or grammatically incorrect
# because it only predicts one next word at a time.

# How is this one-word transition model different from a transformer?
# A transformer understands context using attention,
# while this model simply stores word-to-word transitions.

print("=" * 50)