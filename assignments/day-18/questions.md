# Day 18 Assignment

## Topic: How Transformers Understand Text

Complete all questions in one Markdown file named `answers.md`.

Use your own explanations and examples. Simple diagrams may use arrows, lists, or fenced text blocks.

Use headings from `## Question 1` through `## Question 10` so every answer is easy to review.

## Questions

### Question 1: Pre-Trained Models

Compare training a language model from scratch with using a pre-trained model.

Include:

- data requirements;
- computing cost;
- training time;
- one reason to choose a pre-trained model.

### Question 2: Sequential Models and Transformers

Use this sequence:

```text
I -> love -> machine -> learning
```

Explain how an RNN or LSTM processes a sequence step by step. Then explain how transformer training can examine many token relationships in parallel.

### Question 3: From Text to Representations

Explain every stage in:

```text
Text -> Tokens -> Embeddings -> Transformer layers -> Output
```

For the sentence `I love AI`, show a simple example token list. Do not invent real embedding numbers; explain what the vectors represent.

### Question 4: Positional Encoding

Compare:

```text
Dog bites man.
Man bites dog.
```

The sentences contain the same words. Explain why their meanings differ and how positional information helps a transformer preserve word order.

### Question 5: Attention and Context

Study:

```text
The animal did not cross the road because it was tired.
```

What might `it` refer to? Explain how surrounding words help resolve the reference and why attention is useful for this task.

### Question 6: Query, Key, and Value

Use this sentence:

```text
The cat sat on the mat because it was tired.
```

Explain Query, Key, and Value using the classroom questions:

```text
Query: What am I looking for?
Key: What information is available?
Value: What information should be passed forward?
```

Describe why `cat` should receive more attention than `mat` when interpreting `it`.

### Question 7: Attention Scores

Write this simplified formula:

```text
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

Explain, without performing matrix calculations:

- what a high attention score means;
- what a low attention score means;
- why `softmax` is useful;
- why the scores are applied to the values.

### Question 8: Multi-Head Attention

Use:

```text
The student solved the problem because he understood the concept.
```

Describe four different relationships that separate attention heads could examine, such as grammar, subject-object relationships, meaning, and pronoun reference.

Explain why several heads can be more useful than one.

### Question 9: Draw a Transformer Block

Create a labelled text diagram containing:

```text
Embeddings + Positional Encoding
Multi-Head Self-Attention
Add & Norm
Feed-Forward Network
Add & Norm
Output to the next layer
```

Under the diagram, explain the purpose of the attention part and the feed-forward part in one or two sentences each.

### Question 10: Why Transformers Enabled Modern LLMs

Explain these four advantages:

1. considering many words together;
2. capturing long-range relationships;
3. parallel training;
4. scaling with more data, computing power, and model parameters.

Finish with one limitation or cost of large transformer models.

## Submission

Submit:

```text
assignments/day-18/submissions/batch-a/your-name/answers.md
```

or:

```text
assignments/day-18/submissions/batch-b/your-name/answers.md
```

Before submitting, preview the Markdown and check that the transformer block diagram is readable.
