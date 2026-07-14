import torch
from transformers import pipeline, set_seed

# ==========================================================
# Question 1: Select CPU or GPU
# ==========================================================

device = 0 if torch.cuda.is_available() else -1

print("CUDA Available:", torch.cuda.is_available())
print("Using:", "GPU" if device == 0 else "CPU")

# The same program still works without a GPU because
# Hugging Face pipelines automatically run on the CPU
# when CUDA is unavailable. GPU only makes execution faster.


# ==========================================================
# Question 2: Create a Sentiment Pipeline
# ==========================================================

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

print("\n========== Question 2 ==========")

result1 = sentiment("This course is absolutely amazing!")
result2 = sentiment("The service was terrible and slow.")

print(result1)
print(result2)


# ==========================================================
# Question 3: Analyze a Batch of Reviews
# ==========================================================

print("\n========== Question 3 ==========")

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

results = sentiment(reviews)

for review, result in zip(reviews, results):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")


# ==========================================================
# Question 4: Examine an Unclear Input
# ==========================================================

print("\n========== Question 4 ==========")

unclear = "Blah blah lorem ipsum."

result = sentiment(unclear)[0]

print("Input:", unclear)
print("Label:", result["label"])
print("Confidence:", round(result["score"], 3))

# A high confidence score does NOT prove that the model
# correctly understood meaningless or out-of-domain text.
# The model is forced to choose one of its known labels,
# even if the input has little or no real meaning.


# ==========================================================
# Question 5: Create a Text-Generation Pipeline
# ==========================================================

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

print("\n========== Question 5 ==========")

set_seed(42)

generated = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(generated[0]["generated_text"])


# ==========================================================
# Question 6: Generate From Several Prompts
# ==========================================================

print("\n========== Question 6 ==========")

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("-" * 60)
    print("Prompt:")
    print(prompt)
    print("\nGenerated Text:")
    print(output[0]["generated_text"])

# Generated text may contain inaccurate information.
# Do not treat generated text as verified fact.


# ==========================================================
# Question 7: Compare Temperature Settings
# ==========================================================

print("\n========== Question 7 ==========")

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

set_seed(42)

high_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("\nTemperature = 0.3")
print(low_temp[0]["generated_text"])

print("\nTemperature = 1.2")
print(high_temp[0]["generated_text"])

# Lower temperature usually produces more predictable,
# focused, and conservative text.
#
# Higher temperature usually produces more diverse,
# creative, and sometimes less consistent text.


# ==========================================================
# Question 8: Compare Sampling With Greedy Generation
# ==========================================================

print("\n========== Question 8 ==========")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always chooses the most probable
# next token, making the output much more repeatable.
# Sampling introduces randomness, so outputs may differ
# between runs.


# ==========================================================
# Question 9: Reflection
# ==========================================================

# Generated facts should always be verified because
# language models can produce incorrect or outdated information.

# Training data bias can influence the model's responses,
# causing unfair or unbalanced outputs.

# Model downloads can be slow because pre-trained models
# are often hundreds of megabytes in size.

# CPU generation is slower because CPUs have fewer
# parallel processing cores than GPUs.

# Private or confidential information should never be
# entered into an unapproved AI system because it may
# create privacy or security risks.

print("\nPre-trained model output should always be reviewed and verified by a human before being trusted.")
