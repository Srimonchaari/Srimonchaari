#!/usr/bin/env python3
"""Prepends today's AI/ML engineering note to AI_LEARNING_LOG.md, rotating by day-of-year."""

from datetime import date

NOTES = [
    "The bitter lesson: general methods that leverage computation are ultimately the most effective. — Rich Sutton",
    "Attention is all you need. — Vaswani et al., 2017",
    "RAG is not a feature — it's an architecture decision that determines what your model can know at inference time.",
    "Hallucination is a retrieval failure, not a model failure. Fix the retrieval. — LLM engineering principle",
    "The best model is the one you can actually deploy and monitor. — MLOps axiom",
    "Language models are few-shot learners. — Brown et al., GPT-3, 2020",
    "Scaling laws suggest that larger models trained on more data are predictably better. — Kaplan et al., 2020",
    "Evaluation is the hardest part of building LLM systems. Without it, you're flying blind.",
    "Prompt engineering is context engineering — every token in the context window is a decision.",
    "Chain-of-thought prompting elicits reasoning in large language models. — Wei et al., 2022",
    "Tool use transforms LLMs from readers into actors. — Agentic AI principle",
    "An agent without memory is a stateless function. Memory is what makes it an agent.",
    "The embedding space is a compressed representation of meaning — not of tokens.",
    "Vector similarity is approximate; always validate retrieved context before grounding a response.",
    "Chunking strategy is the most underrated decision in a RAG pipeline.",
    "Latency is a feature. Users leave if your AI takes more than 3 seconds to respond.",
    "Observability in ML is harder than in software — outputs are probabilistic, not deterministic.",
    "Fine-tuning without evaluation is wishful thinking.",
    "A model that cannot explain its uncertainty should not be trusted in production.",
    "Context length is not free — longer contexts increase latency and cost nonlinearly.",
    "The transformer architecture is a general-purpose differentiable computer. — Andrej Karpathy",
    "Reinforcement learning from human feedback (RLHF) aligns model outputs with human preferences. — Christiano et al., 2017",
    "Grounding prevents hallucination. Every factual claim in a response should trace to a retrieved source.",
    "LLM output quality degrades at the edges of the context window — place critical information at the start or end.",
    "Streaming responses reduce perceived latency even when total latency stays the same.",
    "Infrastructure is not separate from AI engineering — the model is only as good as its deployment.",
    "Docker is the unit of reproducibility in modern MLOps.",
    "Prometheus metrics answer what is happening. Logs answer why it happened.",
    "A Grafana dashboard nobody monitors is just decoration.",
    "CI/CD for ML means testing data, model behavior, and deployment — not just code.",
    "MLflow tracks experiments so you can reproduce the result that accidentally worked.",
    "Kubernetes autoscaling for inference workloads requires GPU-aware scheduling.",
    "Cold start latency in serverless inference can be worse than keeping a warm instance running.",
    "FastAPI is the right choice for ML inference APIs — async-first, type-safe, and auto-documented.",
    "Token cost is a first-class metric, not an afterthought.",
    "The p99 latency is the experience of your worst 1% of users — and often your loudest complainers.",
    "Semantic caching reduces LLM API costs by serving cached responses to near-duplicate queries.",
    "A retrieval system with no reranker is leaving precision on the table.",
    "FAISS is fast but HNSW indexes scale better for approximate nearest neighbor at production volume.",
    "Hybrid search — dense vectors + BM25 — outperforms either alone for most retrieval tasks.",
    "The embedding model matters as much as the generation model in a RAG system.",
    "Chunking with overlap prevents context fragmentation at chunk boundaries.",
    "Metadata filtering cuts retrieval search space before vector similarity — always add it.",
    "LangGraph makes agent state explicit — that explicitness is what allows you to debug it.",
    "Multi-agent systems fail at the handoff. Define the interface before the agents.",
    "Tool call validation should happen on the schema, not on the model's output text.",
    "An agentic loop without a termination condition is a production incident waiting to happen.",
    "Structured output (JSON mode) is more reliable than parsing free-text from an LLM.",
    "System prompts are not immutable — version-control them like code.",
    "The model is not the product. The product is everything the model does inside your system.",
    "Few-shot examples in a prompt are the fastest form of fine-tuning with no training cost.",
    "Instruction tuning is supervised fine-tuning on (instruction, response) pairs — not magic.",
    "LoRA fine-tuning reduces trainable parameters by injecting low-rank matrices — same quality, less compute.",
    "RLHF without a good reward model is worse than supervised fine-tuning alone.",
    "Constitutional AI replaces human labelers with a set of principles the model uses to self-critique.",
    "Quantization trades precision for speed — 4-bit inference is often indistinguishable from 16-bit.",
    "Flash Attention rewrites the attention kernel to reduce memory usage by processing in blocks.",
    "Speculative decoding uses a smaller draft model to generate candidate tokens, then verifies in parallel.",
    "Model distillation compresses a large model's knowledge into a smaller one via soft labels.",
    "Mixture of experts routes each token to a subset of parameters — more capacity, same inference cost.",
    "Benchmarks measure models in controlled conditions. Production measures them in real ones.",
    "MMLU covers 57 academic subjects — high scores do not guarantee useful real-world performance.",
    "HumanEval tests code generation on 164 hand-crafted programming problems.",
    "TruthfulQA measures whether a model generates truthful answers to questions humans often get wrong.",
    "HELM (Holistic Evaluation of Language Models) evaluates across accuracy, calibration, fairness, and efficiency.",
    "Evaluation datasets leak into training data — always maintain a held-out test set you never publish.",
    "A/B testing LLM outputs requires human preference labels, not just automated metrics.",
    "LLM-as-a-judge can evaluate model outputs at scale — but the judge model has its own biases.",
    "Exact match is the weakest evaluation metric for generative systems. Use semantic similarity.",
    "ROUGE measures recall of n-gram overlap — useful for summarization, misleading for reasoning tasks.",
    "BERTScore uses contextual embeddings to measure semantic similarity between generated and reference text.",
    "The hallucination rate of a RAG system is the retrieval failure rate, not a model property.",
    "Calibration means a model that says 70% confident should be right 70% of the time.",
    "Safety is not a post-deployment concern — it is an architectural constraint from day one.",
    "Prompt injection is the SQL injection of LLM systems — never trust unsanitized user input in a prompt.",
    "Output filtering is a last line of defense, not a primary safety mechanism.",
    "Jailbreaks exploit the tension between instruction following and safety alignment.",
    "Adversarial prompting tests model robustness the same way penetration testing tests software.",
    "Data privacy in LLM systems requires knowing exactly what goes into the context window.",
    "PII in training data surfaces in model outputs — scrub before training, not after.",
    "Industrie 4.0 shifts manufacturing from reactive to predictive — LLMs are the interface layer.",
    "Digital twins in manufacturing create a live model of physical systems — LLMs make them queryable.",
    "Predictive maintenance with sensor data + LLM summarization reduces unplanned downtime.",
    "MEMS sensors generate high-frequency signals — anomaly detection requires signal processing before LLM input.",
    "Edge inference brings the model to the sensor — critical when network latency is unacceptable.",
    "Sensor fusion combines IMU, camera, and optical flow — EKF is the standard filter for localization.",
    "ROS (Robot Operating System) is the messaging backbone of autonomous systems research.",
    "SLAM (Simultaneous Localization and Mapping) solves navigation without GPS — ORB-SLAM3 is state of the art.",
    "MAVLink is the lightweight protocol connecting flight controllers to companion computers.",
    "PX4 is the open-source autopilot stack powering most research-grade autonomous drones.",
    "Autonomous mission execution requires deterministic waypoint logic — not probabilistic generation.",
    "The gap between simulation (Gazebo) and real deployment is where most robotics projects fail.",
    "ROS bags record all topic messages — the equivalent of a flight data recorder for robots.",
    "Chrome Manifest V3 moves to service workers instead of background pages — offline-first design matters.",
    "A two-call LLM pattern (draft + critique) produces higher-quality output than a single generation.",
    "Client-side AI keeps user data local — a privacy architecture decision, not just a convenience.",
    "RSS parsing gives you a live feed of the research ecosystem at zero API cost.",
    "YAML-defined curriculum graphs are human-readable, version-controllable, and debuggable.",
    "Deterministic traversal over prerequisite graphs produces reproducible learning sequences.",
    "GitHub Actions runs on Ubuntu, macOS, and Windows — test your workflows on the target OS.",
    "Cron schedules in GitHub Actions use UTC — always convert to your local timezone when debugging.",
    "Contribution graphs are not vanity metrics — they are evidence of consistent engineering practice.",
    "Open source contributions are the best portfolio — every PR is a peer-reviewed artifact.",
    "The best documentation explains why, not what. Code already shows what.",
    "Write tests before you refactor — tests are the specification, not the implementation.",
    "Code review is the highest-leverage activity on an engineering team. Do it slowly.",
    "Technical debt is a loan with compounding interest. Pay it down before it compounds.",
    "The simplest system that solves the problem is the right system. Complexity is a liability.",
]

LOG_FILE = "AI_LEARNING_LOG.md"
HEADER = "# AI Engineering Log\n\nOne note per day — updated automatically via GitHub Actions.\n\n---\n\n"


def main() -> None:
    today = date.today()
    note = NOTES[today.timetuple().tm_yday % len(NOTES)]
    entry = f"## {today.isoformat()}\n\n> *{note}*\n\n---\n\n"

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            existing = f.read()
        if existing.startswith("# AI Engineering Log"):
            body = existing[existing.index("\n---\n\n") + 6:]
        else:
            body = existing
    except FileNotFoundError:
        body = ""

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER + entry + body)


if __name__ == "__main__":
    main()
