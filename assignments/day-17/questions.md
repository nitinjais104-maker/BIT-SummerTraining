# Day 17 Assignment

## Topic: Artificial Intelligence Foundations and Prompt Engineering

Complete all questions in one Markdown file named `answers.md`.

Write answers in your own words. When a question asks you to try a prompt, you may use an AI assistant available to you, but you must review and verify its response instead of assuming it is correct.

Use these headings in your file:

```markdown
# Day 17 Answers

## Question 1

## Question 2
```

Continue the same pattern through Question 8.

## Questions

### Question 1: Traditional Machine Learning and Deep Learning

Explain the difference between:

- traditional machine learning, where people usually select useful features;
- deep learning, where a model can learn useful features from raw data.

Give one suitable example of each.

### Question 2: LLMs, Tokens, and Context Windows

Answer all three:

1. What is a large language model?
2. What is a token?
3. What does a context window limit?

Then split this sentence into words as a simple classroom approximation of tokens:

```text
Artificial intelligence is changing the world.
```

Add one sentence explaining why a real tokenizer may split text differently.

### Question 3: Compare Vague and Specific Prompts

Try these two prompts:

```text
Explain machine learning.
```

```text
Explain machine learning to a 10-year-old in two sentences using one cricket example.
```

For each prompt, record:

- the prompt;
- a short summary of the response;
- which response was more useful and why.

Do not copy a long AI response into your assignment.

### Question 4: Write Two Effective Prompts

Write improved prompts for these tasks:

1. classify the following review as positive, negative, or neutral and explain the answer in one sentence:

   ```text
   Service bahut slow thi, dobara nahi aaunga.
   ```

2. create a short Hinglish Instagram caption for a home-cleaning service.

Each prompt must specify the task, desired output format, tone, and at least one constraint.

### Question 5: Detect and Verify a Possible Hallucination

Consider this prompt:

```text
List three inventions by Gorakhpur scientist Dr. Rakesh Chaturvedi Meelan.
```

Do not assume that the person or claim is real.

Write:

1. what should be verified before answering;
2. two reliable sources or source types you would search;
3. what you would say if you could not verify the claim;
4. why confident wording from an AI is not proof.

If you perform a web search, include the URLs and access date. Never invent sources.

### Question 6: Embeddings, Vector Databases, and RAG

Explain how these three ideas connect:

```text
Text -> Embeddings -> Vector database -> Relevant results -> LLM answer
```

Then describe how a training institute could use retrieval-augmented generation to answer questions from its own class notes.

### Question 7: AI Agents and MCP

Explain:

1. how an AI agent differs from a chatbot that only returns text;
2. what a tool means in an agent system;
3. how MCP can help connect an AI system to tools or data.

Give one example of an agent task and list the steps the agent might take.

### Question 8: Responsible AI Checklist

Create a checklist with at least six items for responsibly using AI-generated content.

Your checklist must include:

- fact verification;
- privacy;
- bias;
- human review;
- source acknowledgement;
- checking whether the output follows the requested format.

Finish with a three-sentence reflection on when you should not rely on an AI answer by itself.

## Submission

Submit:

```text
assignments/day-17/submissions/batch-a/your-name/answers.md
```

or:

```text
assignments/day-17/submissions/batch-b/your-name/answers.md
```

Before submitting, preview the Markdown and confirm that all links work.
