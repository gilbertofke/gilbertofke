<h1 align="center">Gilbert Cheruiyot Tangus</h1>

<p align="center">
  <b>AI systems engineer</b><br/>
  I build LLM systems that are measured, governed and affordable to run.
</p>

<p align="center">
  <a href="https://tangus.vercel.app">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/gilbert-cheruiyot-1a44781a0/">LinkedIn</a> ·
  <a href="https://medium.com/@gilbertofke">Medium</a> ·
  <a href="mailto:gilbertofke@gmail.com">Email</a>
</p>

<p align="center">
  Hiring for LLM infrastructure, agentic AI or AI platform work? I am open to roles, remote or in Nairobi. <a href="mailto:gilbertofke@gmail.com">Email me</a>.
</p>

---

## About

I build and operate AI systems from the data and the model to the infrastructure, the guardrails and the bill. I work with open models on my own hardware, with managed cloud services and with hosted APIs, because the right choice depends on the data, the rules and the cost per outcome. Everything here links to code you can run, with benchmarks and failure drills published as they exist, and I say plainly what was simulated.

## What I work on

| Focus | What I bring to a team |
|---|---|
| **LLM serving and infrastructure** | Quantized open models behind a stable API, containers, Kubernetes, GPU scheduling, capacity planning |
| **Retrieval and agents** | RAG pipelines with hybrid search and reranking, tool-calling agents with narrow permissions |
| **Governance** | Audit logs with replay, human review, tenant isolation, prompt-injection tests |
| **AI unit economics** | Cost per request, per task and per outcome, spend caps, and the break-even point between self-hosting and hosted APIs |

## Currently building

| Project | What it is | Status |
|---|---|---|
| [PikiBytes](https://github.com/gilbertofke/pikibytes) | Open-source early warning for fleet battery telemetry. Explainable detectors decide, and a local open-weight model explains. Includes RAG, read-only tools, an audit log with replay, and a Helm chart rehearsed on a three-node KIND cluster. | In progress |

Watch the repo to follow the build as it happens. New projects appear here once they ship with results.

## Open source

I am beginning upstream contributions to the tools I use for serving, gateways and evaluation, starting with documentation and small fixes. Merged pull requests appear here with a link and a one-line summary.

<!--
Enable this table once the first pull request is merged.

| Project | Contribution | Link |
|---|---|---|
| name | one line on what changed and why | pull request link |
-->

## What to expect from my work

- **Numbers with conditions.** Every project ships an evaluation set, and every figure comes with the hardware, data and settings behind it.
- **Cost you can see.** Cost per outcome is tracked from version one, with the serving model recorded on every request and spend capped per tenant.
- **Predictable behavior.** Deterministic code makes the decisions that could hurt someone, the model explains them, and a test enforces that rule.
- **Decisions you can trace.** Any output can be replayed from the audit trail.
- **Failures shown, not hidden.** I break the system on purpose, record what happened and fix it before anyone depends on it.
- **Honest limits.** Decisions are written down, including what I would change and what was not tested.

## Tech stack

| Area | Tools |
|---|---|
| Languages | <img src="https://skillicons.dev/icons?i=python,ts,js,bash" alt="Python, TypeScript, JavaScript, Bash" /> |
| Backend and web | <img src="https://skillicons.dev/icons?i=fastapi,django,nodejs,nextjs,react,tailwind" alt="FastAPI, Django, Node.js, Next.js, React, Tailwind" /> ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white) |
| Data and messaging | <img src="https://skillicons.dev/icons?i=postgres,mongodb,mysql,redis,kafka" alt="PostgreSQL, MongoDB, MySQL, Redis, Kafka" /> ![TimescaleDB](https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black) ![Mosquitto](https://img.shields.io/badge/Mosquitto_MQTT-3C5280?style=flat-square&logo=eclipsemosquitto&logoColor=white) |
| Open model serving | ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white) ![llama.cpp](https://img.shields.io/badge/llama.cpp-5C5C5C?style=flat-square) ![vLLM](https://img.shields.io/badge/vLLM-30A2FF?style=flat-square) ![LMDeploy](https://img.shields.io/badge/LMDeploy-6B7280?style=flat-square) ![TGI](https://img.shields.io/badge/TGI-FFD21E?style=flat-square&logo=huggingface&logoColor=black) |
| Gateway and hosted models | ![LiteLLM](https://img.shields.io/badge/LiteLLM-2D6CDF?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic_API-D4A574?style=flat-square&logo=anthropic&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat-square&logo=openai&logoColor=white) ![Amazon Bedrock](https://img.shields.io/badge/Amazon_Bedrock-232F3E?style=flat-square&logo=amazonaws&logoColor=white) ![Amazon SageMaker](https://img.shields.io/badge/Amazon_SageMaker-232F3E?style=flat-square&logo=amazonaws&logoColor=white) |
| Retrieval | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square) ![LlamaIndex](https://img.shields.io/badge/LlamaIndex-6B7280?style=flat-square) ![SearXNG](https://img.shields.io/badge/SearXNG-3050FF?style=flat-square) |
| Agents and front-ends | ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square) ![LibreChat](https://img.shields.io/badge/LibreChat-10A37F?style=flat-square) ![Hermes](https://img.shields.io/badge/Hermes_agent_models-6B7280?style=flat-square) ![OpenClaw](https://img.shields.io/badge/OpenClaw-6B7280?style=flat-square) |
| Classical ML | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![ONNX Runtime](https://img.shields.io/badge/ONNX_Runtime-005CED?style=flat-square&logo=onnx&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black) |
| Model adaptation | ![PEFT LoRA](https://img.shields.io/badge/PEFT_LoRA-FFD21E?style=flat-square) ![AWQ](https://img.shields.io/badge/AWQ_quantization-5C5C5C?style=flat-square) |
| Containers and Kubernetes | <img src="https://skillicons.dev/icons?i=docker,kubernetes" alt="Docker, Kubernetes" /> ![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white) ![KIND](https://img.shields.io/badge/KIND-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=flat-square&logo=traefikproxy&logoColor=white) ![MetalLB](https://img.shields.io/badge/MetalLB-326CE5?style=flat-square) ![Longhorn](https://img.shields.io/badge/Longhorn-5F224A?style=flat-square) ![NVIDIA GPU Operator](https://img.shields.io/badge/NVIDIA_GPU_Operator-76B900?style=flat-square&logo=nvidia&logoColor=white) |
| Cloud and delivery | <img src="https://skillicons.dev/icons?i=aws,githubactions,linux,git,vercel" alt="AWS, GitHub Actions, Linux, Git, Vercel" /> <img src="https://skillicons.dev/icons?i=terraform" alt="Terraform" /> |
| Observability and cost | <img src="https://skillicons.dev/icons?i=prometheus,grafana" alt="Prometheus, Grafana" /> ![DCGM](https://img.shields.io/badge/DCGM_exporter-76B900?style=flat-square&logo=nvidia&logoColor=white) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-425CC7?style=flat-square&logo=opentelemetry&logoColor=white) ![Langfuse](https://img.shields.io/badge/Langfuse-000000?style=flat-square) ![OpenCost](https://img.shields.io/badge/OpenCost-0F766E?style=flat-square) |
| Testing and evals | <img src="https://skillicons.dev/icons?i=pytest" alt="Pytest" /> ![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black) ![mypy](https://img.shields.io/badge/mypy-2A6DB2?style=flat-square) ![Promptfoo](https://img.shields.io/badge/Promptfoo-1F6FEB?style=flat-square) ![DeepEval](https://img.shields.io/badge/DeepEval-6B7280?style=flat-square) ![Locust](https://img.shields.io/badge/Locust-3AA655?style=flat-square) |
| Business systems and automation | ![Zoho](https://img.shields.io/badge/Zoho-C8202B?style=flat-square) ![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white) |

## Background

All-round full stack developer with 3+ years of production experience, from backend and frontend to DevOps and applied AI. I have built AI agents on real business data, connected them to the systems teams already rely on, and run them on cloud and container infrastructure with cost tracked from the first version.

## Writing

Read my build notes and write-ups on [Medium](https://medium.com/@gilbertofke).

## Get in touch

Hiring, collaborating or have a question about any project here? [Email me](mailto:gilbertofke@gmail.com) or message me on [LinkedIn](https://www.linkedin.com/in/gilbert-cheruiyot-1a44781a0/).
