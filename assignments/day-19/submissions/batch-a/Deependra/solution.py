
import random
from collections import Counter

# Training text
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

# Remove full stops and split into words
words = text.replace(".", "").split()

print("Question 1")
print("Number of words:", len(words))
print("First ten words:", words[:10])
print("Number of unique words:", len(set(words)))

# ==========================================================
# Question 2: Build the Transition Chain
# ==========================================================

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nQuestion 2")
print("Transition Dictionary:")
print(chains)

# A word can have several possible next words because it may
# appear multiple times in the training text with different words after it.

# ==========================================================
# Question 3: Inspect Learned Transitions
# ==========================================================

print("\nQuestion 3")
print("Next words after 'artificial':", chains.get("artificial", []))
print("Next words after 'is':", chains.get("is", []))
print("Next words after 'machine':", chains.get("machine", []))

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

print("\nQuestion 4")
print(generate("artificial"))

# ==========================================================
# Question 5: Make Random Output Reproducible
# ==========================================================

print("\nQuestion 5")

random.seed(42)
result1 = generate("artificial")

random.seed(42)
result2 = generate("artificial")

print("First Result:")
print(result1)

print("\nSecond Result:")
print(result2)

print("\nAre both results equal?", result1 == result2)

# Setting the same random seed makes random choices repeat,
# which helps debugging and comparing program outputs.

# ==========================================================
# Question 6: Compare Starting Words
# ==========================================================

print("\nQuestion 6")

print("Starting with 'machine':")
print(generate("machine"))

print("\nStarting with 'data':")
print(generate("data"))

print("\nStarting with 'world':")
print(generate("world"))

# ==========================================================
# Question 7: Find the Most Likely Next Word
# ==========================================================

def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    counts = Counter(chains[word])
    return counts.most_common(1)[0]

print("\nQuestion 7")
print("artificial ->", most_likely_next("artificial"))
print("machine ->", most_likely_next("machine"))
print("unknown ->", most_likely_next("unknown"))

# ==========================================================
# Question 8: Handle an Unknown Start Word
# ==========================================================

print("\nQuestion 8")

message = generate("robot")
print(message)
print("Program completed successfully without raising an exception.")

# ==========================================================
# Question 9: Explain the Limitations
# ==========================================================

print("\nQuestion 9")
print("This classroom generator is not a real GPT model.")

# Why can the generator only use patterns found in its training text?
# It only learns which word follows another word from the given text.
# It cannot create knowledge or patterns that were never seen.

# Why can the output become repetitive or grammatically incorrect?
# It only considers one previous word when choosing the next word,
# so it ignores sentence structure and long-range context.

# How is this one-word transition model different from a transformer?
# A one-word transition model only looks at the current word to predict
# the next one. A transformer uses the entire context of the sentence,
# attention mechanisms, and millions or billions of learned parameters
# to generate more accurate and meaningful text.