# Day 20 Assignment - Using Pre-Trained Models With Hugging Face

import torch
from transformers import pipeline, set_seed

# Question 1: Select CPU or GPU
# The same program works without a GPU because the device is set to -1 (CPU)
# when CUDA is unavailable, so all operations run on CPU instead.
print("=== Question 1 ===")
device = 0 if torch.cuda.is_available() else -1
print("CUDA available:", torch.cuda.is_available())
print("Using:", "GPU" if device == 0 else "CPU")

# Question 2: Create a Sentiment Pipeline
print("\n=== Question 2 ===")
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)
result1 = sentiment("This course is absolutely amazing!")
result2 = sentiment("The service was terrible and slow.")
print("This course is absolutely amazing! ->", result1)
print("The service was terrible and slow. ->", result2)

# Question 3: Analyze a Batch of Reviews
print("\n=== Question 3 ===")
reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]
results = sentiment(reviews)
for review, result in zip(reviews, results):
    print(f"{review} -> {result['label']} | score {round(result['score'], 3)}")

# Question 4: Examine an Unclear Input
# A high confidence score does not prove the model understood the input correctly.
# The model always outputs a label and score — it cannot say "I don't know".
# For meaningless or out-of-domain text, the model still picks the most likely
# label based on surface patterns, not actual understanding.
print("\n=== Question 4 ===")
unclear = sentiment("Blah blah lorem ipsum.")
print("Label:", unclear[0]["label"])
print("Confidence score:", round(unclear[0]["score"], 3))

# Question 5: Create a Text-Generation Pipeline
print("\n=== Question 5 ===")
generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)
set_seed(42)
output = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)
print("Generated:", output[0]["generated_text"])

# Question 6: Generate From Several Prompts
print("\n=== Question 6 ===")
prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]
set_seed(42)
for prompt in prompts:
    result = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )
    print("-" * 50)
    print("Prompt:", prompt)
    print("Generated:", result[0]["generated_text"])

# Question 7: Compare Temperature Settings
print("\n=== Question 7 ===")
prompt = "Artificial Intelligence will"

set_seed(42)
low_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)
# temperature=0.3 produces more predictable, focused output
# because low temperature sharpens the probability distribution
print("Temperature 0.3 (more predictable):")
print(low_temp[0]["generated_text"])

set_seed(42)
high_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)
# temperature=1.2 produces more varied, creative but sometimes incoherent output
# because high temperature flattens the probability distribution
print("Temperature 1.2 (more varied):")
print(high_temp[0]["generated_text"])

# Question 8: Compare Sampling With Greedy Generation
# Greedy generation is more repeatable because it always picks the single
# highest-probability next token, with no randomness involved.
# Sampled generation picks from a distribution, so results vary each run.
print("\n=== Question 8 ===")
greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)
print("Greedy generation:")
print(greedy[0]["generated_text"])

# Question 9: Limitations Reflection
# 1. Generated facts should be verified because the model predicts likely text
#    based on training data patterns, not verified knowledge. It can confidently
#    state incorrect information (hallucination).
#
# 2. Training-data bias can affect output because if the training data contains
#    biased language about gender, race, or culture, the model may reproduce
#    and amplify those biases in its output.
#
# 3. Model downloads can be difficult on slow connections because pre-trained
#    models like GPT-2 are hundreds of megabytes in size and require stable
#    internet to download completely.
#
# 4. CPU generation is slower than GPU because GPUs have thousands of cores
#    designed for parallel matrix operations, which is exactly what transformer
#    models require. CPUs have far fewer cores optimised for sequential tasks.
#
# 5. Private information should not be placed into an unapproved AI system
#    because the data may be stored, logged, or used for further training,
#    risking privacy violations and data leaks.

print("\nPre-trained model output still requires human review before use.")