# Day 20 Assignment

## Topic: Using Pre-Trained Models With Hugging Face

Complete all questions in one file named `solution.py`.

This assignment downloads public pre-trained models. The first run requires an internet connection and may take several minutes.

Install the required libraries if needed:

```bash
python3 -m pip install torch transformers
```

Start your program with:

```python
import torch
from transformers import pipeline, set_seed
```

Use these exact model names:

```text
distilbert/distilbert-base-uncased-finetuned-sst-2-english
openai-community/gpt2
```

## Questions

### Question 1: Select CPU or GPU

Create:

```python
device = 0 if torch.cuda.is_available() else -1
```

Print:

1. whether CUDA is available;
2. `GPU` when `device == 0`, otherwise `CPU`.

Add a comment explaining why the same program should still work when a GPU is unavailable.

### Question 2: Create a Sentiment Pipeline

Create:

```python
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)
```

Analyze and print the complete result for:

```text
This course is absolutely amazing!
The service was terrible and slow.
```

### Question 3: Analyze a Batch of Reviews

Use:

```python
reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]
```

Pass the full list to the pipeline in one call.

For each review, print:

```text
<review> -> <label> | score <score rounded to 3 decimals>
```

### Question 4: Examine an Unclear Input

Analyze:

```text
Blah blah lorem ipsum.
```

Print its label and confidence score.

In comments, explain why a high confidence score does not prove that a meaningless or out-of-domain input was understood correctly.

### Question 5: Create a Text-Generation Pipeline

Create:

```python
generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)
```

Set the seed to `42` and generate from:

```text
Artificial Intelligence will
```

Use:

```python
max_new_tokens=25
do_sample=True
temperature=0.8
top_p=0.95
pad_token_id=generator.tokenizer.eos_token_id
```

Print the generated text.

### Question 6: Generate From Several Prompts

Generate text from:

```python
prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]
```

Reset the seed to `42` before the loop. Print every prompt and generated result with clear separators.

Generated text may contain inaccurate information. Do not present it as verified fact.

### Question 7: Compare Temperature Settings

Using the same prompt and resetting the seed before each call, generate once with:

```text
temperature = 0.3
```

and once with:

```text
temperature = 1.2
```

Keep `do_sample=True`, `top_p=0.95`, and `max_new_tokens=25`.

Print both results and add comments describing which output appears more predictable and which appears more varied. Exact wording is not graded.

### Question 8: Compare Sampling With Greedy Generation

Generate from the same prompt using:

```text
do_sample = False
```

Do not pass `temperature` or `top_p` in this call.

Print the result and explain in comments why greedy generation is usually more repeatable than sampled generation.

### Question 9: Write a Limitations Reflection

Add comments answering:

1. Why should generated facts be verified?
2. How could training-data bias affect an output?
3. Why can model downloads be difficult on a slow connection?
4. Why might CPU generation be slower than GPU generation?
5. Why should private information not be placed into an unapproved AI system?

Print one final sentence explaining that pre-trained model output still requires human review.

## Submission

Submit:

```text
assignments/day-20/submissions/batch-a/your-name/solution.py
```

or:

```text
assignments/day-20/submissions/batch-b/your-name/solution.py
```

Run it before submitting:

```bash
python3 assignments/day-20/submissions/batch-a/your-name/solution.py
```

The generated sentences do not need to match a fixed expected output. Evaluation is based on correct pipeline use, parameter comparison, labelled output, and reflection comments.
