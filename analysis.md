# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The scenario selected for this task is a **Course Information Assistant**.

The system contains private course information stored in a local JSON file named `courses.json`. The file contains course IDs, course names, fees, and durations.

For example:

- AI202 – Artificial Intelligence – ₹5000 – 6 months
- CS101 – Programming Fundamentals – ₹4000 – 4 months
- DB201 – Database Systems – ₹4500 – 5 months

The same user request is tested with all three approaches:

> **What is the fee for AI202?**

The purpose is to demonstrate how a plain chatbot, a rule-based workflow, and an AI agent handle the same problem differently.

---

## 2. Plain Chatbot

The plain chatbot uses a Large Language Model (LLM) to generate responses to the user's questions. In this implementation, Gemini is used as the LLM.

The chatbot receives the user's question and sends it directly to the LLM. The LLM then generates a response based on the information available to it. The chatbot does not directly access the private `courses.json` file and does not use a separate tool to search the course database.

The flow is:

```text
User Question
     ↓
LLM
     ↓
Generated Response