# Day 19 Assignment
#================================================================>>>>>
import random
from collections import Counter
# Use this training text:
text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

#===============================================================>>>>>>>>>>
## Question 1: Prepare the Words

    # Remove full stops from `text`, split it into a list named `words`, and print:

    # 1. the number of words;
    # 2. the first ten words;
    # 3. the number of unique words.
text = text.replace(".", "")
words = text.split()

print("Total words:", len(words))
print("First 10 words:", words[:10])
print("Unique words:", len(set(words)))
print("="*50)
##===============================================================>>>>>>>>>>
## Question 2: Build the Transition Chain

    # Create an empty dictionary named `chains`.

    # For every word except the last word, store the following word in a list:

    # ```python
    # chains.setdefault(words[i], []).append(words[i + 1])
    # ```

    # Print the complete dictionary.

    # In a comment, explain why one word can have several possible next words.
chains = {}

for i in range(len(words)-1):
    chains.setdefault(words[i], []).append(words[i+1])

print(chains)                                           # One word can have many possible next words.
print("="*50)
###===============================================================>>>>>>>>>>
## Question 3: Inspect Learned Transitions

    # Print the possible next words for:

    # ```text
    # artificial
    # is
    # machine
    # ```

    # Use `.get(word, [])` so the program remains safe if a word is missing.
print("artificial:", chains.get("artificial", []))
print("is:", chains.get("is", []))
print("machine:", chains.get("machine", []))
print("="*50)
####===============================================================>>>>>>>>>>
# Question 4: Create a Safe Generator

    # Write:

    # ```python
    # def generate(start_word, max_new_words=15):
    # ```

    # The function must:

    # 1. convert `start_word` to lowercase;
    # 2. return `No continuation found for '<word>'` if it is not in `chains`;
    # 3. begin the result with the start word;
    # 4. repeatedly choose a next word using `random.choice`;
    # 5. stop after at most `max_new_words` new words;
    # 6. stop early if the current word has no continuation;
    # 7. return one joined string.

    # Generate and print text starting with `artificial`.
def generate(start_word, max_new_words=15):
    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]
    current = start_word

    for i in range(max_new_words):
        if current not in chains:
            break
        current = random.choice(chains[current])
        result.append(current)

    return " ".join(result)

print(generate("artificial"))
print("="*50)
#####===============================================================>>>>>>>>>>
# Question 5: Make Random Output Reproducible

    # Set:

    # ```python
    # random.seed(42)
    # ```

    # Generate one result. Reset the same seed to `42`, generate again, and print whether the two results are equal.

    # In a comment, explain how a seed helps debugging and comparison.
random.seed(42)
a = generate("artificial")

random.seed(42)
b = generate("artificial")

print(a)
print(b)
print(a == b)                                   # Seed gives the same random output every time.
print("="*50)
#####===============================================================>>>>>>>>>>
# Question 6: Compare Starting Words

    # Generate text from:

    # ```text
    # machine
    # data
    # world
    # ```

    # Print a clear label before every result. The generated wording does not need to match another student's wording.
print("Machine:", generate("machine"))
print("Data:", generate("data"))
print("World:", generate("world"))
print("="*50)
#####===============================================================>>>>>>>>>>
# Question 7: Find the Most Likely Next Word

    # Write:

    # ```python
    # def most_likely_next(word):
    # ```

    # Use `Counter` to return the most common next word and its count. If the word is unknown, return `None`.

    # Test it with `artificial`, `machine`, and an unknown word.
def most_likely_next(word):
    if word not in chains:
        return None
    return Counter(chains[word]).most_common(1)[0]

print(most_likely_next("artificial"))
print(most_likely_next("machine"))
print(most_likely_next("robot"))
print("="*50)
#####===============================================================>>>>>>>>>>
## Question 8: Handle an Unknown Start Word

    # Call `generate("robot")`.

    # Print the returned message and confirm that the program does not raise an exception.

print(generate("robot"))
print("Program runs without error.")
print("="*50)
#####===============================================================>>>>>>>>>>
### Question 9: Explain the Limitations

    # At the bottom of `solution.py`, add comments answering:

    # 1. Why can the generator only use patterns found in its training text?
    # 2. Why can the output become repetitive or grammatically incorrect?
    # 3. How is this one-word transition model different from a transformer?

    # Also print one sentence stating that this classroom generator is not a real GPT model.

"""Comment"""
# It only learns patterns from the given text.
# Output may repeat or be grammatically incorrect.
# A transformer understands context, this model only uses one-word transitions.

print("This classroom generator is not a real GPT model.")
print("="*50)
#####===============================================================>>>>>>>>>>