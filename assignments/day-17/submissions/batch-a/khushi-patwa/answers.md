## Topic: Artificial Intelligence Foundations and Prompt Engineering

# Day 17 Answers

# Day 17 Answers

## Question 1

### Traditional Machine Learning vs Deep Learning

>Traditional machine learning and deep learning are both used to solve problems using data, but they work differently.

>In traditional machine learning, we usually select the important features before training the model. The quality of   these features has a big impact on the model's performance.
 
 **Example of Traditional Machine Learning:**
Predicting house prices using Linear Regression based on features like area, location, and number of bedrooms.

>In deep learning, the model automatically learns useful features from raw data without much manual feature selection. It is mainly used for complex tasks like image recognition and language processing.

 **Example of Deep Learning:**
Recognizing handwritten digits or identifying cats and dogs from images using a Convolutional Neural Network (CNN) or pixel values.

---

## Question 2

### 1. What is a Large Language Model?

A Large Language Model (LLM) is an AI model that is trained on a huge amount of text data. It can understand and generate human-like text and can perform tasks like answering questions, summarizing, translating, and writing code.

### 2. What is a Token?

A token is the basic unit of text that an AI model processes. A token can be a **word, part of a word, punctuation mark, or symbol.**

### 3. What does a Context Window limit?

A context window limits how much text or tokens the model can remember while generating a response.

### Classroom Approximation of Tokens

**Sentence:**

Artificial intelligence is changing the world.

**Words:**

1. Artificial
2. intelligence
3. is
4. changing
5. the
6. world

A real tokenizer may split words differently because it works with subwords and punctuation instead of only complete words.

---

## Question 3

### Prompt 1

**Prompt:**

```
Explain machine learning.
```

**Summary of Response:**

The response explained what machine learning is, how it learns from data, and mentioned a few common applications.

---

### Prompt 2

**Prompt:**

```
Explain machine learning to a 10-year-old in two sentences using one cricket example.
```

**Summary of Response:**

The response explained machine learning in very simple language and used a cricket example to make the concept easy to understand.

---

### Which response was more useful?

The second response was more useful because it clearly mentioned the audience, response length, and the example to use. The answer became easier to understand and more focused.

---

## Question 4

### Prompt 1

```
Task:
Classify the following review as Positive, Negative, or Neutral.

Review:
"Service bahut slow thi, dobara nahi aaunga."

Output Format:
Sentiment:
Reason:

Tone:
Professional

Constraint:
Explain the reason in exactly one sentence.
```

---

### Prompt 2

```
Task:
Create a short Hinglish Instagram caption for a home-cleaning service.

Output Format:
Caption:
Hashtags:

Tone:
Friendly and promotional

Constraints:
Maximum 20 words and include exactly three hashtags.
```

---

## Question 5

Before answering this question, I would first verify whether Dr. Rakesh Chaturvedi Meelan is a real scientist and whether the inventions mentioned are supported by reliable sources.

### Reliable sources I would check:

- Official government or university websites
- Research papers or trusted news websites

### If I could not verify the claim:

I could not find reliable information to confirm this claim, so I cannot confidently provide an answer.

### Why confident AI responses are not always correct

AI can sometimes generate information that sounds correct even when it is wrong. That is why important information should always be verified using trusted sources.

---

## Question 6

The connection between these concepts is shown below:

```
Text
   ↓
Embeddings
   ↓
Vector Database
   ↓
Relevant Results
   ↓
LLM Answer
```

**Explanation:**

The text is first converted into embeddings, which are numerical representations of its meaning. These embeddings are stored in a vector database. When a user asks a question, the system searches for similar embeddings and retrieves the most relevant information. The LLM then uses that information to generate a better and more accurate answer.

### Example of RAG in a Training Institute

A training institute can store class notes, assignments, and lecture materials in a vector database. When students ask questions, the system first retrieves the relevant notes and then the LLM generates answers using those notes. This helps provide more accurate and course-specific answers.

---

## Question 7

### 1. Difference between an AI Agent and a Chatbot

A chatbot mainly answers questions by generating text.

An AI agent can perform tasks, use different tools, make decisions, and complete multiple steps to achieve a goal.

### 2. What is a Tool?

A tool is something an AI agent can use to complete a task, such as a calculator, database, Python, search engine, or API.

### 3. What is MCP?

MCP (Model Context Protocol) is a standard that helps AI models connect safely with external tools, applications, and data sources.

### Example of an AI Agent Task

**Task:** Book a meeting.

Steps:

1. Read the user's request.
2. Check the calendar.
3. Find a free time slot.
4. Create the meeting.
5. Send invitations.
6. Confirm that the meeting has been scheduled.

---

## Question 8

### Responsible AI Checklist

- Verify important facts before trusting AI-generated information.
- Do not share personal or sensitive information with AI tools.
- Check whether the response contains any bias.
- Review the output before using or submitting it.
- Mention reliable sources whenever required.
- Make sure the output follows the requested format.
- Check grammar and spelling.
- Use AI as a helper, not as the only source of information.

### Reflection

AI is a powerful tool, but it can sometimes give incorrect or outdated information. For important decisions, facts should always be verified using reliable sources and human judgment. I should use AI to support my learning, but I should not depend on it completely.