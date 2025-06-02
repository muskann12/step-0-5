# Step 00: Understanding the Foundation - Swarm, Agents SDK, and Anthropic Patterns

##  What is Swarm?

Swarm is an experimental framework by OpenAI designed to coordinate multiple AI agents in a simple and scalable way.  
It introduces two main ideas:

- **Agents** – Individual units designed to perform specific tasks (e.g., answering billing questions or providing support).
- **Handoffs** – The process of transferring a task or control from one agent to another based on context.

This makes Swarm flexible and efficient when building systems where different agents collaborate on complex workflows.

---

## 🚀 What is the OpenAI Agents SDK?

The **Agents SDK** is a production-ready version that builds on the ideas from Swarm.

✅ It allows developers to:
- Define agents with specific tools or logic.
- Use **handoffs** to switch between agents dynamically.
- Orchestrate complex tasks using multiple specialized agents.

Basically, it's Swarm, but much more polished and powerful — ready for real-world apps.

---

## 📐 Anthropic Design Patterns

The SDK also follows design patterns outlined by Anthropic for creating powerful AI agents:

1. **Prompt Chaining**  
   → Break down complex tasks into smaller steps that run in sequence.

2. **Routing**  
   → Choose the best agent for each task and hand off the job dynamically.

3. **Parallelization**  
   → Run multiple agents in parallel to speed up execution.

4. **Orchestrator-Worker**  
   → One agent acts as a manager (orchestrator) and delegates subtasks to others (workers).

5. **Evaluator-Optimizer**  
   → One agent evaluates and improves the performance of others in a feedback loop.

---

## ✍️ Summary (In My Words)

This step was all about understanding **how modern multi-agent systems are designed**.

The **Agents SDK** gives us the tools to:
- Break down problems
- Assign agents specific responsibilities
- Connect them in a smart, coordinated way

It’s like building a team of AI workers, each with their own job — and giving them the ability to talk, switch tasks, and improve together.
