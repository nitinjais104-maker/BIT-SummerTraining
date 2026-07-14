Question 1: Traditional Machine Learning and Deep Learning

Traditional Machine Learning:
Traditional Machine Learning is a method where humans manually select useful features from data before training the model. The model learns patterns from these selected features and makes predictions.

Example:
In email spam detection, humans select features like number of links, email length, and keywords. The model uses these features to classify emails as spam or not spam.

Deep Learning:
Deep Learning is a type of machine learning where neural networks automatically learn useful features from raw data. Humans do not need to manually select most features.

Example:
In face recognition, a deep learning model learns features like eyes, face shape, and patterns directly from images.

Difference:
Traditional ML requires manual feature selection, while Deep Learning automatically learns features from raw data.


Question 2: LLMs, Tokens, and Context Windows

1. What is a Large Language Model (LLM)?
A Large Language Model is an AI model trained on a large amount of text data. It can understand and generate human-like text, answer questions, summarize information, and create content.

2. What is a Token?
A token is a small unit of text processed by an AI model. It can be a word, part of a word, or a character.

Sentence:
Artificial intelligence is changing the world.

Simple token approximation:

Artificial
intelligence
is
changing
the
world

A real tokenizer may split text differently because AI models use specific rules and vocabulary to divide words into smaller pieces.


Question 3: Compare Vague and Specific Prompts

Prompt 1:
Explain machine learning.

Response Summary:
The response explains the basic concept of machine learning, types, and examples.

Usefulness:
It provides general information but does not specify the audience or format.


Prompt 2:
Explain machine learning to a 10-year-old in two sentences using one cricket example.

Response Summary:
The response explains machine learning in simple words with a cricket example.

More Useful Response:
The second prompt is more useful because it clearly defines the audience, length, and example, making the answer more focused.


Question 4: Write Two Effective Prompts

Prompt 1:

Task:
Classify the following review as Positive, Negative, or Neutral and explain the answer in one sentence.

Review:
"Service bahut slow thi, dobara nahi aaunga."

Output Format:
Category:
Reason:

Tone:
Simple and clear.

Constraint:
The explanation must be only one sentence.


Prompt 2:

Task:
Create a short Hinglish Instagram caption for a home-cleaning service.

Output Format:
One catchy caption with emojis.

Tone:
Friendly, attractive, and promotional.

Constraint:
Keep the caption under 20 words and suitable for Instagram.


Question 5: Detect and Verify a Possible Hallucination

Prompt:
List three inventions by Gorakhpur scientist Dr. Rakesh Chaturvedi Meelan.

What should be verified:
- Whether the person actually exists.
- Whether the person is a scientist from Gorakhpur.
- Whether the inventions are real.
- Whether reliable sources mention these claims.

Reliable sources:
1. Official government science websites or research organization websites.
2. Academic papers, university websites, and trusted news sources.

If the claim cannot be verified:
"I could not verify reliable information about Dr. Rakesh Chaturvedi Meelan and these inventions, so I cannot confirm these claims."

Why confident AI wording is not proof:
AI can generate incorrect information that sounds believable. A confident response does not guarantee that the information is true.


Question 6: Embeddings, Vector Databases, and RAG

Connection:

Text
↓
Embeddings
↓
Vector Database
↓
Relevant Results
↓
LLM Answer


Embeddings:
Embeddings convert text into numerical vectors that represent the meaning of the text.

Vector Database:
A vector database stores these embeddings and helps find similar information quickly.

Relevant Results:
The system searches the database and retrieves information related to the user's question.

LLM Answer:
The LLM uses retrieved information to generate a better answer.

Example:
A training institute can store class notes, assignments, and study material in a vector database.

When a student asks a question:
1. The question is converted into an embedding.
2. Similar notes are searched.
3. Relevant information is retrieved.
4. The LLM generates an answer using those notes.

This process is called Retrieval-Augmented Generation (RAG).


Question 7: AI Agents and MCP

AI Agent vs Chatbot:
A chatbot only gives text responses based on the conversation.

An AI agent can understand goals, make decisions, use tools, and complete tasks automatically.

Tool in Agent System:
A tool is an external service or function that an AI agent can use, such as a database, calculator, search engine, or API.

MCP:
Model Context Protocol (MCP) helps AI systems connect with external tools and data sources in a standard way.

Example Agent Task:
Task:
Schedule a meeting.

Steps:
1. Understand the user's request.
2. Check calendar availability.
3. Find a suitable time.
4. Create the meeting event.
5. Send confirmation.


Question 8: Responsible AI Checklist

Responsible AI Checklist:

☐ Verify facts from reliable sources before using AI-generated information.

☐ Protect privacy and do not share personal or sensitive information.

☐ Check AI output for bias and unfair assumptions.

☐ Perform human review before final decisions or publishing.

☐ Acknowledge AI usage and sources properly.

☐ Check whether the output follows the requested format.

☐ Avoid depending completely on AI for high-risk decisions.

☐ Review and improve AI-generated content before use.


Reflection:

AI should not be used as the only source for important decisions. AI can make mistakes, provide incorrect information, or misunderstand situations. Human checking and critical thinking are required before trusting AI answers.