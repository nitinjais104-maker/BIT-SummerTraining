
# Day 18 Answers

## Question 1: Pre-Trained Models

**Training from scratch:**
- Data requirements: Very large datasets (often billions of tokens)
- Computing cost: Extremely high (requires GPUs/TPUs for weeks or months)
- Training time: Very long (days to months)
- Use case: When building a completely new model for a specific domain or research

**Using a pre-trained model:**
- Data requirements: Much smaller dataset for fine-tuning
- Computing cost: Much lower
- Training time: Much faster (minutes to hours or days)

**Why choose a pre-trained model:**
It saves time and resources because the model already understands general language patterns and only needs small adjustments for a specific task.

---

## Question 2: Sequential Models and Transformers

Sequence:
I -> love -> machine -> learning

**RNN/LSTM processing:**
An RNN processes tokens one by one in order:
- Reads "I"
- Passes memory to next step
- Reads "love"
- Updates memory
- Reads "machine"
- Reads "learning"

Each step depends on the previous one, so processing is sequential.

**Transformer processing:**
A transformer processes all tokens at the same time.
It looks at relationships between all words in parallel:
- "I" can attend to "love", "machine", "learning"
- "machine" can attend to "learning", etc.

This parallel processing makes transformers much faster and better at capturing relationships.

---

## Question 3: From Text to Representations

Pipeline:

Text -> Tokens -> Embeddings -> Transformer layers -> Output

**Explanation:**
- Text: Raw sentence input
- Tokens: Split into small units (words or subwords)
- Embeddings: Convert tokens into numeric vectors
- Transformer layers: Learn relationships between tokens using attention
- Output: Final prediction (text, class, or next token)

**Example: "I love AI"**

Tokens:
- I
- love
- AI

**Embeddings:**
Each token becomes a vector that represents meaning, context, and relationships (not real words, just numbers).

---

## Question 4: Positional Encoding

Sentence 1: Dog bites man.  
Sentence 2: Man bites dog.

Both sentences use the same words but have different meanings because word order changes the meaning.

**Why positional encoding matters:**
Transformers need positional encoding because they process all words together. Without position information, the model would not know the order of words.

Positional encoding adds information like:
- Word position 1
- Word position 2
- Word position 3

This helps the model understand that "dog bites man" is different from "man bites dog".

---

## Question 5: Attention and Context

Sentence:
The animal did not cross the road because it was tired.

The word **"it"** refers to "the animal".

**How attention helps:**
Attention allows the model to look at surrounding words like "animal" and "tired" to understand what "it" refers to.

- "animal" is a strong candidate for "it"
- "road" is less relevant
- "tired" describes the animal

So attention connects "it" back to the correct word based on context.

---

## Question 6: Query, Key, and Value

Sentence:
The cat sat on the mat because it was tired.

- **Query:** What am I trying to understand? (the word "it")
- **Key:** What information is available? (cat, mat, sat, etc.)
- **Value:** The actual meaning information passed forward

**Why "cat" gets more attention:**
The word "it" is more strongly related to "cat" because cats are living beings that can be tired, while "mat" is not.

So:
- Query ("it") matches better with Key ("cat")
- Less relevance to "mat"

---

## Question 7: Attention Scores

Formula:
Attention(Q, K, V) = softmax(QKᵀ / √d) V

**High attention score:**
Means two words are strongly related and the model should focus more on that connection.

**Low attention score:**
Means weak or no relationship between words.

**Why softmax is useful:**
Softmax converts scores into probabilities so that important relationships get higher weights and all scores sum to 1.

**Why apply scores to values:**
Because values contain the actual information, and attention decides how much of each value should be used in the final output.

---

## Question 8: Multi-Head Attention

Sentence:
The student solved the problem because he understood the concept.

Different attention heads may focus on:

1. Grammar structure (subject-verb-object relationships)
2. Pronoun reference ("he" refers to "student")
3. Semantic meaning (understanding problem-solving)
4. Cause-effect relationship (understood → solved problem)

**Why multiple heads are useful:**
Different heads learn different patterns at the same time, giving the model a richer understanding of language compared to a single attention mechanism.

---

## Question 9: Transformer Block Diagram
            
            Input Text
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
         Output to Next Layer


**Attention part:**
It helps the model understand relationships between different words in a sentence, even if they are far apart.

**Feed-forward part:**
It processes each token individually and helps refine the learned features after attention.

---

## Question 10: Why Transformers Enabled Modern LLMs

**1. Considering many words together:**
Transformers can look at all words in a sentence at the same time.

**2. Capturing long-range relationships:**
They can connect words that are far apart in a sentence.

**3. Parallel training:**
Unlike RNNs, transformers process data in parallel, making training faster.

**4. Scaling ability:**
They improve significantly when given more data, compute power, and parameters.

**Limitation:**
Transformers require a lot of memory and computing power, making them expensive to train and run.