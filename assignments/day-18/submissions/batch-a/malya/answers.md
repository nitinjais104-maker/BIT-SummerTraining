#day18
Question 1: Pre-Trained Models
Training a language model from scratch means creating a model with random parameters and teaching it using a very large amount of data.

Using a pre-trained model means using an already trained model and adapting it for a specific task.

Comparison:

1. Data Requirements:
- Training from scratch requires a huge amount of text data.
- Pre-trained models need less data because they already learned general language patterns.

2. Computing Cost:
- Training from scratch requires expensive hardware like many GPUs and large memory.
- Pre-trained models require less computing power for fine-tuning or usage.

3. Training Time:
- Training from scratch can take weeks or months.
- Using a pre-trained model takes much less time.

4. Reason to choose a pre-trained model:
A pre-trained model saves time, cost, and resources because it already understands language patterns.


--------------------------------------------------


Question 2: Sequential Models and Transformers

Sequence:

I -> love -> machine -> learning


RNN/LSTM Processing:

An RNN processes words one by one.

Step 1:
The model receives "I" and creates a hidden state containing information about this word.

Step 2:
It receives "love" and combines it with the previous hidden state to understand the relationship between "I" and "love".

Step 3:
It receives "machine" and updates its memory with information from previous words.

Step 4:
It receives "learning" and uses all previous information to understand the complete sentence.

LSTM improves RNN by using memory gates that help remember important information for longer sequences.

Transformer Processing:

A transformer can examine relationships between many tokens at the same time using self-attention.

It can understand how every word is related to other words in the sentence in parallel, making training faster and improving long-context understanding.


--------------------------------------------------


Question 3: From Text to Representations

Process:

Text -> Tokens -> Embeddings -> Transformer Layers -> Output


1. Text:
Original sentence:

"I love AI"


2. Tokens:
A simple token example:

["I", "love", "AI"]


3. Embeddings:
Tokens are converted into numerical vectors.

These vectors do not store exact meanings like dictionary definitions. They represent patterns, relationships, and meanings learned from large amounts of text data.


4. Transformer Layers:
Transformer layers process these vectors using attention mechanisms and learn relationships between words.


5. Output:
The model generates an output such as a prediction, answer, or next token.


--------------------------------------------------


Question 4: Positional Encoding

Sentences:

1. Dog bites man.
2. Man bites dog.


Both sentences contain the same words, but their meanings are different because the word order changes.

"Dog bites man" means the dog performs the action.

"Man bites dog" means the man performs the action.

Transformers process words in parallel, so they need positional information to understand the order of words.

Positional encoding gives each token information about its position in the sentence, helping the transformer understand word order and meaning.


--------------------------------------------------


Question 5: Attention and Context

Sentence:

"The animal did not cross the road because it was tired."


The word "it" could refer to the animal because an animal can become tired.

The surrounding words provide context:
- "animal"
- "was tired"

Attention helps the model focus on important words and relationships. It gives more importance to words that help determine the correct meaning of "it".


--------------------------------------------------


Question 6: Query, Key, and Value

Sentence:

"The cat sat on the mat because it was tired."


Query:
What am I looking for?

The model looks for the word that "it" refers to.

Key:
What information is available?

The available information includes words like cat, mat, sat, and tired.

Value:
What information should be passed forward?

The useful information about the possible reference is passed to understand the meaning.


Why cat receives more attention than mat:

A cat can be tired, but a mat cannot. Therefore, the relationship between "it" and "cat" is stronger, so attention gives more importance to "cat".


--------------------------------------------------


Question 7: Attention Scores

Formula:

Attention(Q, K, V) = softmax(QKᵀ / √d) V


Meaning:

High Attention Score:
A high score means two words are strongly related and the model should focus more on that information.

Low Attention Score:
A low score means the words have less relationship, so the model gives less importance.

Why Softmax is useful:
Softmax converts scores into probabilities that add up to 1, making it easier to decide how much attention each word receives.

Why scores are applied to values:
The scores decide which information from the values should be combined to create a better representation.


--------------------------------------------------


Question 8: Multi-Head Attention

Sentence:

"The student solved the problem because he understood the concept."


Different attention heads can examine:

1. Grammar Relationship:
Identify that "student" is the subject performing the action.

2. Subject-Object Relationship:
Understand that "student" solved the "problem".

3. Meaning Relationship:
Connect "understood the concept" with successful problem solving.

4. Pronoun Reference:
Understand that "he" refers to "student".

Several attention heads are useful because each head can learn different types of relationships at the same time, giving the model a deeper understanding of language.


--------------------------------------------------


Question 9: Transformer Block Diagram


                Input Text
                    |
                    ↓
     Embeddings + Positional Encoding
                    |
                    ↓
        Multi-Head Self-Attention
                    |
                    ↓
               Add & Norm
                    |
                    ↓
        Feed-Forward Network
                    |
                    ↓
               Add & Norm
                    |
                    ↓
          Output to Next Layer


Attention Part:
The attention part helps the model understand relationships between different words and identify which words are important for the current context.

Feed-Forward Part:
The feed-forward network processes the information further and learns complex patterns and representations.


--------------------------------------------------


Question 10: Why Transformers Enabled Modern LLMs

Advantages of Transformers:

1. Considering Many Words Together:
Transformers can analyze multiple words at the same time instead of processing only one word at a time.

2. Capturing Long-Range Relationships:
Transformers can connect words that are far apart in a sentence and understand long contexts.

3. Parallel Training:
Transformers allow many calculations to happen simultaneously, making training faster.

4. Scaling:
Transformers improve when provided with more data, more computing power, and more model parameters.

Limitation:
Large transformer models require huge amounts of computing power, energy, and expensive hardware for training and operation.