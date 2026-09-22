# Day 1 – Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## Overview

This project demonstrates three different approaches to solving the same private-data problem:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The selected scenario is a Course Information Assistant that answers questions using course information stored in a local JSON file.

The same question is tested with all three approaches:

> What is the fee for AI202?

## Project Structure

```text
day1 asses/
│
├── chatbot/
│   └── chatbot.py
│
├── rule_based/
│   └── workflow.py
│
├── agent/
│   └── agent.py
│
├── data/
│   └── courses.json
│
├── Output/
│   ├── chatbot_output.png
│   ├── rule_based_output.png
│   └── agent_output.png
│
├── analysis.md
├── README.md
├── requirements.txt
└── .gitignore