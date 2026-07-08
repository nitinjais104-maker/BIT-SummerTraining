# Day 17 Answers

## Question 1

### Traditional Machine Learning
Traditional machine learning usually requires humans to manually select the important features from the data before training the model. The quality of these features greatly affects the model's performance.

**Example:** Email spam detection using features like the number of links, sender information, and specific keywords.

### Deep Learning
Deep learning can automatically learn useful features directly from raw data using neural networks. It reduces the need for manual feature engineering.

**Example:** Image recognition where a deep learning model learns shapes, edges, and objects directly from images.

---

## Question 2

### 1. What is a Large Language Model (LLM)?
A Large Language Model is an AI model trained on a huge amount of text to understand and generate human-like language.

### 2. What is a token?
A token is a small unit of text processed by an AI model. A token may be a whole word, part of a word, or even punctuation.

### 3. What does a context window limit?
The context window limits how many tokens the model can read and remember in one conversation or request.

### Sentence split into words (classroom approximation of tokens)

Artificial | intelligence | is | changing | the | world.

### Why can a real tokenizer split differently?
A real tokenizer may split words into smaller pieces or combine punctuation separately, so actual tokens may not exactly match individual words.

---

## Question 3

### Prompt 1
**Prompt:**
```
Explain machine learning.
```

**Summary of the response:**
The response gives a general explanation of machine learning, how it works, and where it is used.

### Prompt 2
**Prompt:**
```
Explain machine learning to a 10-year-old in two sentences using one cricket example.
```

**Summary of the response:**
The response explains machine learning in simple language using a cricket example and keeps the answer short.

### Which response was more useful and why?
The second response was more useful because it matched the audience, included a real-life example, and followed the requested length.

---

## Question 4

### Prompt 1

```
Task: Classify the following review as Positive, Negative, or Neutral.

Review:
"Service bahut slow thi, dobara nahi aaunga."

Output Format:
- Sentiment:
- Explanation:

Tone: Professional

Constraint: Use only one sentence for the explanation.
```

### Prompt 2

```
Task: Create a short Hinglish Instagram caption for a home-cleaning service.

Output Format:
Caption only

Tone: Friendly and attractive

Constraints:
- Maximum 20 words.
- Include one relevant emoji.
- Add one hashtag.
```

---

## Question 5

### 1. What should be verified before answering?
I should first verify whether Dr. Rakesh Chaturvedi Meelan is a real scientist and whether the claimed inventions actually exist.

### 2. Two reliable sources
- Google Scholar (https://scholar.google.com/)
- Government or official institution websites such as CSIR or IIT websites.

### 3. What would you say if you could not verify the claim?
I could not find reliable evidence that confirms this person or the claimed inventions. Therefore, I cannot confidently provide an answer.

### 4. Why is confident wording from an AI not proof?
AI can sometimes generate incorrect information that sounds convincing, so every factual claim should be verified using reliable sources.

---

## Question 6

The connection works like this:

**Text → Embeddings → Vector Database → Relevant Results → LLM Answer**

First, the text is converted into embeddings, which are numerical representations of its meaning. These embeddings are stored in a vector database. When a user asks a question, the database finds the most relevant information using similarity search. The retrieved information is then provided to the LLM, which generates an accurate answer based on that information.

A training institute can use Retrieval-Augmented Generation (RAG) by storing its class notes in a vector database. When students ask questions, the system retrieves the most relevant notes and the LLM answers using those notes instead of relying only on its general knowledge.

---

## Question 7

### 1. Difference between an AI agent and a chatbot
A chatbot mainly generates text responses, while an AI agent can plan tasks, use tools, make decisions, and perform actions to achieve a goal.

### 2. What is a tool in an agent system?
A tool is an external resource, such as a calculator, database, API, or search engine, that an AI agent uses to complete tasks.

### 3. How does MCP help?
MCP (Model Context Protocol) provides a standard way for AI systems to connect with external tools, databases, and applications, making integrations simpler and more reliable.

### Example of an agent task

**Task:** Book a meeting.

**Steps:**
1. Read the user's request.
2. Check the calendar for available time.
3. Find a suitable time slot.
4. Create the meeting.
5. Send invitations.
6. Confirm the booking to the user.

---

## Question 8

### Responsible AI Checklist

- ✔ Verify important facts before trusting the answer.
- ✔ Protect personal and private information.
- ✔ Check for bias or unfair statements.
- ✔ Review the output manually before using it.
- ✔ Acknowledge or cite reliable sources when needed.
- ✔ Make sure the output follows the requested format.
- ✔ Correct any factual or grammatical mistakes.
- ✔ Avoid using AI-generated content without understanding it.

### Reflection

AI can make mistakes or generate false information that sounds correct. I should not rely on AI alone for important decisions, research, or medical, legal, and financial advice. I should always verify important information using reliable sources and apply human judgment before using it.