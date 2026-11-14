<h1 align="center">Gilbert Cheruiyot Tangus</h1>

<p align="center">
  <b>AI systems engineer</b><br/>
  I build LLM systems that are measured, governed and affordable to run.
</p>

<p align="center">
  <a href="https://tangus.me">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/gilbert-cheruiyot-1a44781a0/">LinkedIn</a> ·
  <a href="https://hashnode.com/@gilbertofke">Hashnode</a> ·
  <a href="https://medium.com/@gilbertofke">Medium</a> ·
  <a href="mailto:gilbertofke@gmail.com">Email</a>
</p>

<p align="center">
  Open to LLM infrastructure, agentic AI and AI platform roles. Based in Kenya, working remote and in Nairobi.
</p>

---

## About

I build and operate AI systems from the data and the model to the infrastructure, the guardrails and the bill. I work with open models on my own hardware, with managed cloud services and with hosted APIs, because the right choice depends on the data, the rules and the cost per outcome. I publish code, benchmarks and failure drills as they exist, and I say plainly what was simulated.

## What I work on

| Focus | What it means in practice |
|---|---|
| **LLM serving and infrastructure** | Quantized open models behind a stable API, containers, Kubernetes, GPU scheduling, capacity planning |
| **Retrieval and agents** | RAG pipelines with hybrid search and reranking, tool-calling agents with narrow permissions |
| **Governance** | Audit logs with replay, human review, tenant isolation, prompt-injection tests |
| **AI unit economics** | Cost per request, per task and per outcome, spend caps, and the break-even point between self-hosting and hosted APIs |

## Currently building

| Project | What it is | Status |
|---|---|---|
| [PikiBytes](https://github.com/gilbertofke/pikibytes) | Open-source early warning for fleet battery telemetry. Explainable detectors decide, and a local open-weight model explains. Includes RAG, read-only tools, an audit log with replay, and a Helm chart rehearsed on a three-node KIND cluster. | 28-day public build from 16 November 2026, on simulated telemetry |

More projects will be added here once they ship with results.

## Open source

I am starting upstream contributions now, beginning with documentation fixes and small bug fixes in the tools I use for serving, gateways and evaluation. Merged pull requests will be listed here with a link and one line on what changed.

<!--
Enable this table once the first pull request is merged.

| Project | Contribution | Link |
|---|---|---|
| name | one line on what changed and why | pull request link |
-->

## How I build

- **Measure before claiming.** Every project ships an evaluation set and publishes the conditions behind each number.
- **Cost is a design input.** I track cost per outcome from version one, record which model served each request, and cap spend per tenant.
- **Deterministic code decides and the model explains** wherever a wrong answer could hurt someone, and I test that rule.
- **Every decision can be replayed** from an audit trail.
- **Failure is rehearsed.** I break the system on purpose, record what happened and fix it before anyone depends on it.
- **Decisions and limits are written down**, including what I would change and what was not tested.

## Tech stack

| Area | Tools |
|---|---|
| Languages and backend | <img src="https://skillicons.dev/icons?i=python,ts,bash,fastapi,django,nodejs,nextjs" alt="Python, TypeScript, Bash, FastAPI, Django, Node.js, Next.js" /> |
| Data | <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,kafka" alt="PostgreSQL, MongoDB, Redis, Kafka" /> |
| Models and gateway | ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white) ![llama.cpp](https://img.shields.io/badge/llama.cpp-5C5C5C?style=flat-square) ![LiteLLM](https://img.shields.io/badge/LiteLLM-2D6CDF?style=flat-square) |
| Retrieval and agents | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square) |
| Cloud and delivery | <img src="https://skillicons.dev/icons?i=aws,docker,kubernetes,githubactions,linux,git" alt="AWS, Docker, Kubernetes, GitHub Actions, Linux, Git" /> ![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white) |
| Observability and testing | <img src="https://skillicons.dev/icons?i=prometheus,grafana,pytest" alt="Prometheus, Grafana, Pytest" /> |
| Hosted models | ![Anthropic](https://img.shields.io/badge/Anthropic_API-D4A574?style=flat-square&logo=anthropic&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat-square&logo=openai&logoColor=white) |

**Learning next, and moved up once it ships in a repo.** vLLM, NVIDIA GPU Operator, Langfuse, promptfoo, OpenTelemetry, Terraform.

## Background

Three years of production engineering across site reliability, DevOps, full stack and applied AI agents, including building agents on business data and training other developers. AWS Certified Cloud Practitioner.

## Writing

Build notes and write-ups go on [Hashnode](https://hashnode.com/@gilbertofke) and [Medium](https://medium.com/@gilbertofke), with one article a week during the PikiBytes build.
