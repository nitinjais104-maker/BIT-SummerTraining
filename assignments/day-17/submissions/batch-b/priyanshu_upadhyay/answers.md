# Day 17 Answers

## Question 1

Traditional machine learning relies on humans to manually select and engineer useful features from data before feeding it to a model. For example, to detect spam emails, a person might manually choose features like word frequency, sender address, and subject line keywords.

Deep learning, on the other hand, learns useful features automatically from raw data through multiple layers of a neural network. For example, in image recognition, the model learns to detect edges, shapes, and patterns on its own without any manual feature selection.

## Question 2

1. A large language model (LLM) is an AI system trained on massive amounts of text data that can understand and generate human-like text by predicting the most likely next word or token.

2. A token is a small unit of text that a model processes — it can be a word, part of a word, or a punctuation mark.

3. A context window limits how much text (in tokens) the model can consider at one time during a conversation or task.

Sentence split into tokens (classroom approximation):
["Artificial", "intelligence", "is", "changing", "the", "world", "."]

A real tokenizer may split text differently because it uses subword algorithms like Byte Pair Encoding (BPE), which can break uncommon words into smaller pieces to handle vocabulary more efficiently.

## Question 3

**Prompt 1:** "Explain machine learning."
**Response summary:** A general explanation covering supervised, unsupervised learning, algorithms, and applications — quite long and broad.
**Usefulness:** Less useful because it lacks focus and audience context.

**Prompt 2:** "Explain machine learning to a 10-year-old in two sentences using one cricket example."
**Response summary:** A simple, clear explanation comparing ML to how a cricket coach learns from match data to predict the best batting order.
**Usefulness:** Much more useful because it was specific, concise, and relatable for the intended audience.

The second prompt was more useful because adding constraints (age, length, example type) gave the AI clear direction and produced a focused, actionable response.

## Question 4

**Prompt 1:**
"Classify the following customer review as Positive, Negative, or Neutral. Provide your answer as a single word on the first line, followed by one sentence explaining your reasoning. Review: 'Service bahut slow thi, dobara nahi aaunga.'"

**Prompt 2:**
"Write a short Instagram caption (maximum 2 sentences) in Hinglish for a home-cleaning service. The tone should be friendly and energetic. Include one emoji and end with a call to action."

## Question 5

Before answering this prompt, the following should be verified:

1. Whether Dr. Rakesh Chaturvedi Meelan is a real, documented person.
2. Whether they are actually from Gorakhpur and work as a scientist.
3. Whether the claimed inventions are documented in credible sources.

**Two reliable source types to search:**
- Government research institution websites (like CSIR, ICAR, or university faculty pages)
- Peer-reviewed academic databases like Google Scholar or ResearchGate

**If the claim cannot be verified:**
"I was unable to find any verified information about Dr. Rakesh Chaturvedi Meelan or their inventions in reliable sources. I recommend checking official institutional records before accepting this claim."

**Why confident AI wording is not proof:**
AI models can generate text that sounds factual and authoritative even when the information is fabricated or hallucinated. Confident tone in an AI response reflects its training patterns, not verified truth. Always cross-check with primary or credible secondary sources.

## Question 6

**How these ideas connect:**

When text is converted into embeddings, it becomes a list of numbers (vectors) that represent the meaning of the text mathematically. These vectors are stored in a vector database, which can quickly find the most relevant pieces of text when given a query. The relevant results are then passed to an LLM, which uses them as context to generate an accurate, grounded answer — this is called Retrieval-Augmented Generation (RAG).

**Training institute example:**
A training institute could store all its class notes, PDFs, and assignments as embeddings in a vector database. When a student asks "What is gradient descent?", the system retrieves the most relevant notes and passes them to the LLM, which then answers using the institute's own content instead of general internet knowledge.

## Question 7

1. An AI agent differs from a simple chatbot because it can take actions — like searching the web, writing files, running code, or calling APIs — not just return text. A chatbot only responds; an agent plans and executes multi-step tasks.

2. A tool in an agent system is any external capability the agent can use, such as a web search engine, a calculator, a database query, or a code executor.

3. MCP (Model Context Protocol) provides a standardized way for AI systems to connect to external tools and data sources, making it easier to build agents that interact with real-world services without custom integrations for each tool.

**Example agent task:** "Book the cheapest flight from Lucknow to Delhi for next Monday."

**Steps the agent might take:**
1. Search for available flights using a travel API tool
2. Compare prices across results
3. Identify the cheapest option
4. Ask the user to confirm
5. Complete the booking using a payment/booking tool
6. Send a confirmation summary to the user

## Question 8

**Responsible AI Checklist:**

- [ ] **Fact verification:** Cross-check all factual claims with reliable, primary sources before using them.
- [ ] **Privacy:** Do not input personal, confidential, or sensitive information into AI tools.
- [ ] **Bias check:** Review AI output for stereotypes, unfair assumptions, or one-sided perspectives.
- [ ] **Human review:** Always have a human read and evaluate AI-generated content before publishing or submitting.
- [ ] **Source acknowledgement:** Clearly indicate when content was AI-assisted or AI-generated.
- [ ] **Format check:** Verify that the output follows the requested format, length, and style.
- [ ] **Hallucination check:** Be alert to confident-sounding but unverifiable claims in AI responses.
- [ ] **Context accuracy:** Ensure the AI understood your question correctly and answered what was actually asked.

**Reflection:**
You should not rely on an AI answer alone when the topic involves medical, legal, or financial decisions where errors can cause serious harm. AI should also not be the sole source when you need verified, up-to-date facts about real people, recent events, or scientific findings. In any high-stakes situation, human expertise and verified sources must always take priority over AI-generated content.