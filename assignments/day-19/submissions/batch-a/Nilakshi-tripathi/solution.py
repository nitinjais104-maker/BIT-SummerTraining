import random
from collections import Counter

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# -------------------------
# Question 1: Prepare words
# -------------------------

text = text.replace(".", "")
words = text.split()

print("Total words:", len(words))
print("First 10 words:", words[:10])
print("Unique words:", len(set(words)))

# -------------------------
# Question 2: Build chains
# -------------------------

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nTransition Chains:")
print(chains)

# A word can have multiple next words because it appears in different contexts
# in the training data, so different sentences may follow different paths.

# -------------------------
# Question 3: Inspect transitions
# -------------------------

print("\nNext words for 'artificial':", chains.get("artificial", []))
print("Next words for 'is':", chains.get("is", []))
print("Next words for 'machine':", chains.get("machine", []))

# -------------------------
# Question 4: Generator function
# -------------------------

def generate(start_word, max_new_words=15):
    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]
    current = start_word

    for _ in range(max_new_words):
        if current not in chains:
            break

        current = random.choice(chains[current])
        result.append(current)

    return " ".join(result)

print("\nGenerated (artificial):")
print(generate("artificial"))

# -------------------------
# Question 5: Seed reproducibility
# -------------------------

random.seed(42)
output1 = generate("artificial")

random.seed(42)
output2 = generate("artificial")

print("\nOutput 1:", output1)
print("Output 2:", output2)
print("Are both outputs equal?", output1 == output2)

# Seed ensures reproducibility of random choices, which helps in debugging
# and comparing results consistently.

# -------------------------
# Question 6: Different starts
# -------------------------

print("\n--- Starting word: machine ---")
print(generate("machine"))

print("\n--- Starting word: data ---")
print(generate("data"))

print("\n--- Starting word: world ---")
print(generate("world"))

# -------------------------
# Question 7: Most likely next word
# -------------------------

def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    counter = Counter(chains[word])
    return counter.most_common(1)[0]

print("\nMost likely next words:")
print("artificial:", most_likely_next("artificial"))
print("machine:", most_likely_next("machine"))
print("unknown:", most_likely_next("robot"))

# -------------------------
# Question 8: Unknown start word
# -------------------------

print("\nUnknown start test:")
print(generate("robot"))

# -------------------------
# Question 9: Limitations (comments + print)
# -------------------------

# 1. The generator only uses patterns present in training text,
#    so it cannot create new knowledge.
#
# 2. Output can become repetitive or incorrect because it only
#    follows local word transitions without understanding grammar.
#
# 3. Unlike transformers, this model only looks at one previous word,
#    while transformers consider full context using attention.

print("\nThis classroom generator is NOT a real GPT model.")