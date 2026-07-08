# Day 18 Answers

## Question 1

| Factor | Training from Scratch | Using a Pre-Trained Model |
|---|---|---|
| Data requirements | Billions of text samples needed | Little or no additional data needed |
| Computing cost | Extremely high (thousands of GPUs) | Low (fine-tuning only) |
| Training time | Weeks to months | Hours to days |

One reason to choose a pre-trained model: A pre-trained model already understands language structure, grammar, and general knowledge, so it can be fine-tuned for a specific task with much less data and cost.

## Question 2

RNN/LSTM (sequential processing):

Step 1: reads "I"        -> produces hidden state h1
Step 2: reads "love"     -> uses h1, produces h2
Step 3: reads "machine"  -> uses h2, produces h3
Step 4: reads "learning" -> uses h3, produces h4

Each step depends on the previous one, so early words can be forgotten by the time the model reaches later words.

Transformer (parallel processing): The transformer looks at all four tokens at the same time and calculates relationships between every pair simultaneously. This is faster and captures long-range relationships more effectively.

## Question 3

- Text: Raw input sentence — I love AI
- Tokens: Text is split into units — ["I", "love", "AI"]
- Embeddings: Each token is converted into a vector that represents its meaning. Similar words have similar vectors.
- Transformer layers: Multiple layers refine each token's representation by considering context from all other tokens using attention.
- Output: The final representations are used for the task — next word prediction, classification, translation, etc.

The embedding vectors do not have fixed real values — they are learned during training and represent meaning, not arbitrary numbers.

## Question 4

"Dog bites man" — the dog is performing the action on the man.
"Man bites dog" — the man is performing the action on the dog.

The words are identical but their positions change who is doing what. A transformer uses positional encoding — a numerical signal added to each token's embedding — to record the position of each word in the sequence. This allows the model to know that position 1 is the subject and position 3 is the object, preserving meaning even when words are the same.

## Question 5

"it" most likely refers to the animal, not the road, because the reason given is tiredness — which applies to a living being, not a road.

Attention helps here by letting the model look at all surrounding words simultaneously and calculate which word "it" is most related to. Words like "animal", "tired", and "did not cross" together guide the model to resolve "it" correctly. Without attention, a model might incorrectly link "it" to the nearest noun ("road").

## Question 6

Using "The cat sat on the mat because it was tired":

- Query (What am I looking for?): When processing "it", the model asks — which earlier word does "it" refer to?
- Key (What information is available?): Every other word offers itself as a possible match — cat, mat, sat, road.
- Value (What information should be passed forward?): The actual meaning of the matched word is passed forward.

"cat" should receive more attention than "mat" because "cat" is a living subject capable of being tired, while "mat" is an inanimate object.

## Question 7

Attention(Q, K, V) = softmax(QKt / sqrt(d)) V

- High attention score: The query and key are very similar — this token is highly relevant to the current word being processed.
- Low attention score: The query and key are dissimilar — this token is less relevant and contributes little.
- Why softmax: Softmax converts raw scores into probabilities that add up to 1, making it easier to compare and weight tokens fairly.
- Why scores are applied to values: The scores decide how much of each value to include in the final output. High-scoring tokens contribute more meaning; low-scoring tokens contribute less.

## Question 8

Using "The student solved the problem because he understood the concept":

- Head 1 (Grammar): Examines subject-verb agreement — "student" and "solved" are connected.
- Head 2 (Subject-Object): Identifies that "student" performed the action on "problem".
- Head 3 (Meaning): Links "solved" and "understood" as related concepts — understanding leads to solving.
- Head 4 (Pronoun reference): Resolves that "he" refers to "student", not any other noun.

Using multiple heads is more useful than one because each head can specialise in a different type of relationship simultaneously.

## Question 9

Input Sentence
     |
     v
Embeddings + Positional Encoding
     |
     v
Multi-Head Self-Attention
     |
     v
Add and Norm
     |
     v
Feed-Forward Network
     |
     v
Add and Norm
     |
     v
Output to the next layer

Attention part: The multi-head self-attention layer allows each token to look at all other tokens and gather relevant context, helping the model understand relationships and resolve ambiguity.

Feed-forward part: The feed-forward network processes each token independently after attention, applying learned transformations to refine its representation for the next layer.

## Question 10

1. Considering many words together: Transformers process the entire input at once, so every word can directly influence every other word in a single step.

2. Capturing long-range relationships: Attention connects any two tokens regardless of distance, solving the problem RNNs had with forgetting early words in long sequences.

3. Parallel training: Since transformers do not process tokens one by one, training can be distributed across many GPUs simultaneously, making it much faster.

4. Scaling: Transformers improve consistently as more data, computing power, and parameters are added — this scaling property enabled models like GPT and BERT to achieve state-of-the-art results.

One limitation: Large transformer models require enormous computing resources and energy to train, making them expensive and inaccessible for most individuals or small organisations.