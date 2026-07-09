# Day 18 Answers

## Question 1

| Training from Scratch | Pre-trained Model |
|------------------------|------------------|
| Requires a huge amount of data | Uses knowledge already learned |
| Very expensive to train | Much cheaper |
| Takes weeks or months | Ready to use immediately |
| Needs powerful GPUs | Can run with fine-tuning |

A pre-trained model is a better choice because it saves time, reduces cost, and already understands language patterns.

---

## Question 2

Sequence:

I → love → machine → learning

### RNN/LSTM

RNN reads one word at a time.

Step 1: Read **I**

Step 2: Read **love** and remember **I**

Step 3: Read **machine** while keeping previous information

Step 4: Read **learning** using information from all previous words.

The information moves sequentially from one word to another.

### Transformer

A transformer can look at all words together instead of reading one after another.

It learns relationships between every word in parallel, making training much faster and better for long sentences.

---

## Question 3

Flow:

```
Text
   ↓
Tokens
   ↓
Embeddings
   ↓
Transformer Layers
   ↓
Output
```

Example:

Sentence:

```
I love AI
```

Tokens:

```
["I", "love", "AI"]
```

Embeddings convert every token into a vector containing its meaning.

Transformer layers learn relationships between these vectors.

Finally, the model predicts the next word or generates a response.

---

## Question 4

Sentence 1:

```
Dog bites man.
```

Sentence 2:

```
Man bites dog.
```

Both sentences contain the same words, but their meanings are completely different because the order of the words changes.

Transformers use positional encoding to understand where each word appears in the sentence.

Without positional encoding, both sentences would look identical to the model.

---

## Question 5

Sentence:

```
The animal did not cross the road because it was tired.
```

Here, **it** most likely refers to **the animal**.

The surrounding words help the model understand that being tired is more likely for an animal than for a road.

Attention allows the transformer to focus on important words even if they are far apart.

---

## Question 6

Sentence:

```
The cat sat on the mat because it was tired.
```

**Query**

What am I looking for?

The model wants to know what **it** refers to.

**Key**

What information is available?

Possible words are **cat** and **mat**.

**Value**

What information should be passed forward?

The information related to **cat** is more useful.

The model gives more attention to **cat** because living things become tired, while a mat cannot.

---

## Question 7

Formula:

```
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

High attention score means two words are strongly related.

Low attention score means the words have little relationship.

Softmax converts scores into probabilities whose total equals 1.

The scores are multiplied with the values so the model focuses more on important information and less on irrelevant information.

---

## Question 8

Sentence:

```
The student solved the problem because he understood the concept.
```

Different attention heads can learn different relationships.

**Head 1**

Grammar

Student is the subject.

**Head 2**

Meaning

Understanding the concept helped solve the problem.

**Head 3**

Pronoun reference

"He" refers to the student.

**Head 4**

Context

Concept and problem are connected.

Using multiple attention heads helps the model understand many different relationships at the same time instead of focusing on only one.

---

## Question 9

```
                INPUT
                  │
                  ▼
   Embeddings + Positional Encoding
                  │
                  ▼
      Multi-Head Self-Attention
                  │
                  ▼
             Add & Norm
                  │
                  ▼
       Feed-Forward Network
                  │
                  ▼
             Add & Norm
                  │
                  ▼
        Output to Next Layer
```

### Attention

Attention finds the most important words related to each token and builds context.

### Feed Forward Network

The feed-forward network processes the learned information further and improves the representation before passing it to the next layer.

---

## Question 10

Transformers made modern LLMs successful because they can:

1. Look at many words together instead of one by one.

2. Capture long-distance relationships between words.

3. Train in parallel, making learning much faster.

4. Scale easily with more data, larger models, and better hardware.

### Limitation

Large transformer models require a lot of memory, computing power, and electricity, making them expensive to train and run.