# Day 17 Answers

## Question 1

**Traditional Machine Learning**

Traditional machine learning usually requires people to choose the most useful features before training the model. The quality of these manually selected features has a strong effect on the model's performance.

**Example:** Predicting house prices using features such as house size, number of bedrooms, and location.

**Deep Learning**

Deep learning uses neural networks that can automatically learn useful features directly from raw data, such as images, text, or audio. This reduces the need for manual feature engineering.

**Example:** An image recognition system that learns to identify cats and dogs directly from pixel values.

---

## Question 2

**1. What is a Large Language Model (LLM)?**

A Large Language Model (LLM) is an AI model trained on large amounts of text to understand and generate human-like language. It can answer questions, summarize information, translate languages, and assist with many writing tasks.

**2. What is a token?**

A token is a small unit of text that an AI model processes. A token may be a whole word, part of a word, punctuation, or a symbol.

**3. What does a context window limit?**

A context window limits the amount of text the model can consider at one time while generating a response.

**Sentence split into words (simple classroom approximation):**

- Artificial
- intelligence
- is
- changing
- the
- world

**Why a real tokenizer may split text differently**

A real tokenizer may split long words, punctuation, or special characters into multiple tokens instead of treating each word as one token.

---

## Question 3

### Prompt 1

**Prompt:**

Explain machine learning.

**Response Summary:**

The response gave a general explanation of machine learning, describing how computers learn patterns from data to make predictions or decisions.

---

### Prompt 2

**Prompt:**

Explain machine learning to a 10-year-old in two sentences using one cricket example.

**Response Summary:**

The response used simple language and explained machine learning with a cricket example, making the idea easier for a child to understand.

---

**Which response was more useful and why?**

The second response was more useful because it clearly defined the audience, limited the length, and requested a cricket example, making the explanation easier to understand.

---

## Question 4

### Prompt 1

**Task:** Classify a review.

**Improved Prompt:**

Classify the following review as **Positive**, **Negative**, or **Neutral**. Return the answer in the format:

- Sentiment:
- Reason:

Use a professional tone and explain the reason in exactly one sentence.

Review:
*Service bahut slow thi, dobara nahi aaunga.*

---

### Prompt 2

**Task:** Create an Instagram caption.

**Improved Prompt:**

Write a short Hinglish Instagram caption for a home-cleaning service. Return only one caption with one relevant emoji and exactly three hashtags. Keep the tone friendly and promotional, and limit the caption to 20 words.

---

## Question 5

Before answering the prompt, I would verify whether **Dr. Rakesh Chaturvedi Meelan** is a real scientist and whether the claimed inventions actually exist.

**Reliable sources to check:**

1. Google Scholar (https://scholar.google.com/)
2. Indian Patent Advanced Search System (https://iprsearch.ipindia.gov.in/)

**If I could not verify the claim:**

I would say that I could not find reliable evidence confirming the person's identity or the claimed inventions, so I cannot present them as facts.

**Why confident AI wording is not proof**

AI systems can sometimes generate incorrect or unsupported information confidently. Claims should always be verified using reliable and trustworthy sources.

**Access Date:** 8 July 2026

---

## Question 6

The connection between these concepts is:

**Text → Embeddings → Vector Database → Relevant Results → LLM Answer**

First, the text is converted into numerical embeddings that represent its meaning. These embeddings are stored in a vector database. When a user asks a question, the database searches for the most relevant information using similarity matching. The retrieved information is then provided to the LLM, which generates an answer based on both the retrieved data and its language understanding.

A training institute could use Retrieval-Augmented Generation (RAG) by storing class notes, study materials, and course documents in a vector database. When students ask questions, the system retrieves the most relevant notes and uses them to generate accurate answers based on the institute's own learning material.

---

## Question 7

An AI agent differs from a chatbot because an AI agent can perform actions in addition to generating text. A chatbot mainly provides text responses, while an agent can use external tools, access data, and complete tasks.

A **tool** is a resource that an AI agent can use, such as a calculator, database, email service, or web search.

**MCP (Model Context Protocol)** helps connect AI systems to external tools and data sources using a standardized interface, making it easier for the AI to access information and perform actions.

**Example Agent Task:** Book a meeting.

**Steps the agent might take:**

1. Read the user's request.
2. Check the calendar for available time slots.
3. Suggest suitable meeting times.
4. Create the calendar event.
5. Send meeting invitations to participants.
6. Confirm the booking with the user.

---

## Question 8

### Responsible AI Checklist

- Verify important facts using reliable sources.
- Protect personal and sensitive information before sharing it with AI.
- Check the output for possible bias or unfair statements.
- Review AI-generated content before using or submitting it.
- Acknowledge sources whenever information comes from external references.
- Confirm that the output follows the requested format and instructions.

### Reflection

AI-generated answers should not be trusted without verification when they involve important facts, medical advice, legal matters, or financial decisions. AI can produce confident but incorrect information, so reliable sources should always be checked. Human judgment remains important for ensuring accuracy, fairness, and responsible use of AI.