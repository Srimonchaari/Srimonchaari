<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=24&duration=3500&pause=800&color=0078D4&center=true&vCenter=true&width=650&lines=Production+LLM+Systems+Engineer;Building+RAG+%26+Agentic+Pipelines+%40+Robert+Bosch;M.Sc.+Artificial+Intelligence+%C2%B7+BTU+Cottbus;Rapid+Prototyper+%C2%B7+Cursor+%C2%B7+Jules+%C2%B7+LangGraph)](https://git.io/typing-svg)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-srimon-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/srimon/)
[![Portfolio](https://img.shields.io/badge/Portfolio-srimonchaari.eu-0078D4?style=flat-square&logo=vercel&logoColor=white)](https://www.srimonchaari.eu)
[![Email](https://img.shields.io/badge/Email-srimonchaari%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:srimonchaari@gmail.com)
![Location](https://img.shields.io/badge/Cottbus%2C_Germany-🇩🇪-1F6FEB?style=flat-square)
![Profile Views](https://komarev.com/ghpvc/?username=Srimonchaari&color=0078D4&style=flat-square&label=Profile+Views)

</div>

---

## About

Production AI Engineer at **Robert Bosch GmbH** — shipping RAG systems and agentic pipelines for MEMS engineering workflows used by domain experts and lab engineers in manufacturing.

Pursuing **M.Sc. Artificial Intelligence** at Brandenburg University of Technology, Cottbus (2024–present). Completed a Bosch internship with a formal *Zeugnis* rated outstanding across all evaluation dimensions.

🔍 Open to AI Engineer / LLM Engineer roles in Germany or remote-EU.

---

## Tech Stack

**LLM & AI**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented_Generation-0078D4?style=flat-square)
![Prompt Engineering](https://img.shields.io/badge/Prompt_Engineering-Context_Design-6e40c9?style=flat-square)

**MLOps & Infrastructure**

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

**Backend & Cloud**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=flat-square)
![Chroma](https://img.shields.io/badge/Chroma-FF6F00?style=flat-square)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square)

---

## Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### 📡 SensorSpeak

Natural-language search over real-time manufacturing sensor data — fully offline, no external APIs.

`FastAPI` `LangGraph` `Ollama` `RAG` `React` `pytest`

- **100K readings/min** — ingested, vectorized, and queried in real time
- **85 pytest tests** — full coverage across ingestion, retrieval, and response
- Zero external API calls — runs on Qwen 2.5 + BAAI embeddings locally
- Keyword fallback prevents hallucinations when retrieval confidence is low

[→ View Repository](https://github.com/Srimonchaari/SensorSpeak)

</td>
<td width="50%" valign="top">

### 📊 LLM Observability Dashboard

Production monitoring for Generative AI APIs — latency, cost, and token usage in real time.

`FastAPI` `Prometheus` `Grafana` `Docker`

- **p50 / p95 / p99 latency** tracked per request
- **Per-call USD cost** estimated from token counts
- Single `docker compose up` — zero manual configuration
- Pre-wired Grafana dashboards out of the box

[→ View Repository](https://github.com/Srimonchaari/LLM-Observability)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⚡ Prompt Optimiser

Chrome extension — transforms rough prompts into production-quality instructions inline, inside ChatGPT, Gemini, and DeepSeek.

`JavaScript` `Chrome Manifest V3` `Client-side`

- **Reflect-then-Refine** two-call algorithm with local scoring
- Supports **GPT · Claude · Gemini · DeepSeek · Nvidia NIM**
- 100% client-side — no backend, no subscriptions, no data sent anywhere
- Framework selector: RISEN / RTF / TAG / COSTAR per use case

[→ View Repository](https://github.com/Srimonchaari/Prompt_Optimiser)

</td>
<td width="50%" valign="top">

### 🧠 Synapz — AI Learning Lab

Prerequisite-aware curriculum engine — delivers one structured AI engineering concept daily with RSS-fed context from live research feeds.

`Python` `YAML` `pytest` `feedparser`

- Deterministic prerequisite graph traversal — no ML recommendations needed
- Feeds from **arXiv · HuggingFace · AWS ML Blog · Google Cloud AI**
- Three-tier fallback: strict → broader → global topic selection
- Atomic JSON state — no database dependency

[→ View Repository](https://github.com/Srimonchaari/ai-learning-lab-v1)

</td>
</tr>
</table>

> **Published** — UAV Autonomous Cleaning System · *AIP Conference Proceedings 2024* · [DOI: 10.1063/5.0235050](https://doi.org/10.1063/5.0235050)

---

## GitHub Stats

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=Srimonchaari&show_icons=true&theme=default&hide_border=true&count_private=true&rank_icon=github" />
  <img height="165" src="https://streak-stats.demolab.com/?user=Srimonchaari&theme=default&hide_border=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Srimonchaari&layout=compact&theme=default&hide_border=true&langs_count=6" />
</div>

---

## Contribution Activity

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="dist/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="dist/github-snake.svg" />
    <img alt="Contribution Snake" src="dist/github-snake.svg" />
  </picture>
</div>

---

## Certifications

[![Databricks](https://img.shields.io/badge/Databricks-Generative%20AI%20Engineer%20Associate-FF3621?style=flat-square&logo=databricks&logoColor=white)](https://credentials.databricks.com/search#q=generative%20ai%20engineer&t=credentials)
[![Azure](https://img.shields.io/badge/Microsoft-Azure%20AI%20Engineer%20Associate-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/)
[![Salesforce](https://img.shields.io/badge/Salesforce-Agentforce%20Specialist-00A1E0?style=flat-square&logo=salesforce&logoColor=white)](https://www.salesforce.com/trailhead/en/credentials/specialist/agentforce-specialist/)

---

## Daily Engineering Log

> *"The bitter lesson: general methods that leverage computation are ultimately the most effective."* — Rich Sutton

Updated daily via GitHub Actions — [View Full Log →](AI_LEARNING_LOG.md)

---

## Connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/srimon/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-0078D4?style=for-the-badge&logo=vercel&logoColor=white)](https://www.srimonchaari.eu)
[![Email](https://img.shields.io/badge/Email-Reach%20Out-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:srimonchaari@gmail.com)

</div>
