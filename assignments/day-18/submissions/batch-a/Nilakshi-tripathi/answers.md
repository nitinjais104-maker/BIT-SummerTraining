# Day 18 Answers

## Question 1: Pre-Trained Models

Training a language model from scratch means starting with random weights and training on a very large dataset. Using a pre-trained model means starting with an already trained model and fine-tuning it for a specific task.

- **Data requirements:**
  - From scratch: requires massive datasets (internet-scale text).
  - Pre-trained: needs smaller, task-specific dataset for fine-tuning.

- **Computing cost:**
  - From scratch: extremely high GPU/TPU cost.
  - Pre-trained: much lower cost.

- **Training time:**
  - From scratch: weeks or months.
  - Pre-trained: hours or days.

- **Reason to choose pre-trained model:**
  It saves time and resources while still giving strong performance.

---

## Question 2: Sequential Models and Transformers

### RNN/LSTM processing:
For the sequence:
```
I -> love -> machine -> learning
```

An RNN/LSTM processes one token at a time in order. It reads "I", then passes hidden state to "love", then "machine", then "learning". Each step depends on previous context, so it is sequential and slower.

### Transformer processing:
Transformers process all tokens at once. They use self-attention to look at relationships between all words in parallel, so "love" can directly relate to "learning" without waiting for sequential steps.

---

## Question 3: From Text to Representations

Pipeline:
```
Text -> Tokens -> Embeddings -> Transformer layers -> Output
```

### Example: "I love AI"

- Tokens: ["I", "love", "AI"]

- Embeddings:
Each token is converted into a vector that represents its meaning in high-dimensional space.

- Transformer layers:
These layers learn relationships between tokens like how "love" relates to "AI" and "I".

- Output:
Final result depends on the task (classification, prediction, generation, etc.).

---

## Question 4: Positional Encoding

Sentences:
```
Dog bites man.
Man bites dog.
```

Both sentences use the same words, but meaning changes because word order changes.

- In the first sentence, dog is the subject.
- In the second sentence, man is the subject.

Transformers use positional encoding to add information about word order, so the model knows which word comes first and how meaning changes with position.

---

## Question 5: Attention and Context

Sentence:
```
The animal did not cross the road because it was tired.
```

The word "it" likely refers to "the animal".

Attention helps by looking at surrounding words like "animal", "cross", and "tired" to determine which word "it" is most related to. This helps resolve ambiguity in language.

---

## Question 6: Query, Key, and Value

Sentence:
```
The cat sat on the mat because it was tired.
```

- **Query:** What is "it" looking for?
- **Key:** Information from all words (cat, mat, etc.).
- **Value:** The actual meaning/content passed forward.

In this sentence, "it" (Query) matches more strongly with "cat" (Key) than "mat", so attention focuses more on "cat" because it makes more sense semantically.

---

## Question 7: Attention Scores

```
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

- **High attention score:**
  Means two tokens are highly related and influence each other strongly.

- **Low attention score:**
  Means weak or no relationship between tokens.

- **Why softmax is useful:**
  It converts scores into probabilities so that attention weights sum to 1.

- **Why apply scores to values:**
  Because values contain the actual information that should be passed forward, weighted by importance.

---

## Question 8: Multi-Head Attention

Sentence:
```
The student solved the problem because he understood the concept.
```

Different attention heads can focus on:

1. Grammar structure (subject-verb-object)
2. Pronoun reference ("he" → "student")
3. Cause-effect relationship ("because")
4. Semantic meaning (understanding concept → solving problem)

Multiple heads are useful because each head learns different relationships simultaneously, improving understanding.

---

## Question 9: Transformer Block Diagram

```
Input Tokens
      ↓
Embeddings + Positional Encoding
      ↓
Multi-Head Self-Attention
      ↓
Add & Norm
      ↓
Feed-Forward Network
      ↓
Add & Norm
      ↓
Output to next layer
```

### Explanation:
- **Attention part:** helps the model understand relationships between all words in the sentence.
- **Feed-forward part:** processes each token individually to refine learned features and improve representation.

---

## Question 10: Why Transformers Enabled Modern LLMs

1. **Considering many words together:**
   Transformers process all tokens at once, capturing full context.

2. **Long-range relationships:**
   They can connect words that are far apart in a sentence.

3. **Parallel training:**
   Unlike RNNs, transformers can be trained in parallel, making training faster.

4. **Scalability:**
   They improve effectively when more data, compute, and parameters are added.

### Limitation:
Large transformer models require very high computation, memory, and energy, making them expensive to train and run.