<h1 align="center">Gilbert Cheruiyot Tangus</h1>

<p align="center">
  <b>AI systems engineer</b><br/>
  Measurable, governable and affordable AI, whether it runs on my hardware, in the cloud or both.
</p>

<p align="center">
  <a href="https://tangus.vercel.app">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/gilbert-cheruiyot-1a44781a0/">LinkedIn</a> ·
  <a href="https://hashnode.com/@gilbertofke">Hashnode</a> ·
  <a href="https://medium.com/@gilbertofke">Medium</a> ·
  <a href="mailto:gilbertofke@gmail.com">Email</a>
</p>

<p align="center">
  Open to roles in LLM infrastructure, agentic AI and AI governance. Nairobi, and remote.
</p>

---

## About

This is where the work happens. I build and operate AI systems end to end, from the data and the model to the infrastructure, the guardrails and the bill. I work across open models on my own hardware, managed cloud services and hosted APIs, and the hybrids in between, because the right answer depends on the data, the regulator and the unit economics. I publish code, benchmarks, failure drills and design decisions as they exist, and I say plainly what was simulated and what was not.

## Kipimo, how I measure AI systems

*Kipimo* is Swahili for a measurement. Every system I ship reports the same five meters, with the conditions behind each number, so any two designs can be compared fairly.

| Meter | The question | Reported as |
|---|---|---|
| **Cost** | What does one unit of useful work cost, all in? | Cost per request, per task and per outcome, with hardware or API price included, plus the break-even volume between self-hosted and hosted |
| **Speed** | Does it answer in time and stay up? | p95 latency, queue lag, availability, and how often the fallback path ran |
| **Quality** | Is the answer right and grounded? | Pass rate on a fixed evaluation set, groundedness, schema validity |
| **Control** | Can I prove who did what, and stop it? | Audit replay, tenant isolation tests, injection cases passed, human review path |
| **Portability** | Can I move it? | What it takes to switch between self-hosted, managed and hybrid, and which providers swap without code changes |

The cost meter follows a ladder, because a token price alone hides most of the bill.

```
token     what the provider bills, or what the GPU burns
request   one model call
task      every call an agent makes to finish one job
outcome   one resolved ticket, one reconciled payment, one useful alert
```

I record the model that served every request, so computed cost reconciles with the invoice. For self-hosted models I price the hardware and the idle time, so the comparison with a hosted API is honest.

### Scorecard

| System | Cost | Speed | Quality | Control | Portability | Status |
|---|---|---|---|---|---|---|
| [PikiBytes](https://github.com/gilbertofke/pikibytes) | Share of packets that never touch a model, tokens per alert, notional cost per 1,000 packets | p95 latency, queue lag, fallback rate | Retrieval hit rate on 30 questions, schema validity | Audit replay, ten failure drills including budget cap and prompt injection | CPU on KIND, GPU profile, one optional GPU session | In build, 28 days from 16 November 2026, simulated telemetry |

New rows are added only when a system has numbers to put in them.

## The work this profile is built for

A reference role in LLM infrastructure and agentic AI asks for the same things most teams ask for. This is how I map to it, and how honest the evidence is today.

| Capability | What I build | Evidence |
|---|---|---|
| Model serving | Quantized open models behind a stable API, GGUF on CPU, AWQ on GPU | PikiBytes, in build |
| Gateway and routing | One endpoint in front of every model, with budgets, timeouts and routing rules | PikiBytes, in build |
| Retrieval | Hybrid dense and keyword search with reranking, scored on a fixed question set | Professional work, public write-up planned. PikiBytes, in build |
| Agents and tools | Tool-calling agents with read-only, tenant-scoped tools and cited answers | Professional work on business data. PikiBytes, in build |
| Kubernetes and GPU operations | Helm charts, scheduling, resource limits, rehearsed failure drills | PikiBytes, in build |
| Observability and evals | Metrics, traces and a fixed evaluation set that runs in CI | PikiBytes, in build |
| Governance and cost control | Audit logs, human review, budgets, injection tests | PikiBytes, in build |
| Integration into existing systems | Connecting AI to CRMs, ERPs, payment and messaging systems | Professional work |

## Self-hosted, managed or hybrid

I do not start from a tool. I start from the data, the regulator and the volume, and the deployment model follows.

| Mode | Choose it when | What I design | Tools |
|---|---|---|---|
| Self-hosted | Data cannot leave the building, volume is steady, or the rules demand control | Serving, quantization, GPU scheduling, capacity and cost per outcome | Ollama, llama.cpp, vLLM, Kubernetes, Helm |
| Managed cloud | Speed to market, spiky demand or small teams matter most | Provider abstraction, spend limits, evaluation and logging around a hosted model | AWS, hosted APIs, a gateway in front |
| Hybrid | Sensitive requests stay local and the rest use the cheapest model that passes the evals | Routing by sensitivity, cost and quality, with a fallback path that still works | LiteLLM, rule-based routing, shared audit log |

The number I want on every comparison is the break-even volume, the point where renting stops being cheaper than owning.

## Where it applies

The patterns repeat across sectors and regions. The rules and the unit that matters change.

| Sector | Typical system | Governance pressure | The unit that matters |
|---|---|---|---|
| Payments and financial services | Reconciliation agents, support copilots, fraud triage | Auditability, personal data, human sign-off | Cost per reconciled transaction |
| Business operations (CRM, ERP) | Agents acting on business data inside existing tools | Access control, change history | Cost per automated workflow |
| Customer support and BPO | Answer drafting, ticket triage, quality review | Disclosure, escalation to a person | Cost per resolved ticket |
| Health | Note summarization, triage support, record search | Sensitive data, residency, clinical oversight | Cost per note or case handled |
| Education | Tutoring support, curriculum tools, learner analytics | Minors, fairness, transparency | Cost per learner per month |
| Mobility and energy | Telemetry early warning with an explaining copilot | Safety claims stated plainly | Cost per 1,000 packets, per useful alert |
| Agriculture and public services | Advice in local languages over SMS or voice, case processing | Data residency, accessibility, accountability | Cost per advisory or case delivered |

## Governance as running code

Most governance material is paperwork. I want mine to be something a reviewer can run, so each control ships with the evidence that it works.

| Control | Evidence | Control family |
|---|---|---|
| Decision audit log with replay | Any alert or answer rebuilt end to end from stored rows | Traceability |
| Human review of high-severity output | Alert lifecycle with acknowledgement and reviewer record | Human oversight |
| Fallback when the model fails | Failure drill with the fallback rate published | Robustness |
| Per-tenant budgets and rate limits | Budget-cap drill result | Cost and abuse control |
| Tenant-scoped, read-only tools | Test that a tool call cannot cross tenants | Access control |
| Prompt-injection test set | Pass count on a fixed set of cases | Security |
| Data minimization in schema and prompts | Schema docs and a stated retention rule | Data protection |
| Model card and stated limits | Published with every release, including what was simulated | Transparency |

Each repository maps its controls to the EU AI Act, NIST AI RMF and ISO/IEC 42001, and to Kenya's Data Protection Act 2019. Kenya's National AI Strategy 2025 to 2030 is published, and an AI Bill (2026) has been proposed but is not law. These mappings describe engineering evidence. They are not legal advice or certification.

## Pinned projects

| Project | What it is |
|---|---|
| [PikiBytes](https://github.com/gilbertofke/pikibytes) | Open-source early warning for fleet battery telemetry. MQTT ingest, explainable detectors, a local open-weight LLM copilot with RAG and read-only tools, an audit log with replay, and a Helm chart rehearsed on a three-node KIND cluster. A 28-day public build starting 16 November 2026, running on simulated telemetry. |

<!--
Upstream contributions, enable once merged
| Project | Contribution | Link |
|---|---|---|
| name | one line on what changed and why | pull request link |
-->

## The standard for every project I ship

Experiments are exempt until they graduate. Everything else gets the following.

- **A README that states the problem**, the architecture, and how to run it in three commands.
- **A Kipimo table** with the five meters and the conditions behind each number.
- **A verify command** that reproduces the headline result on your machine.
- **Benchmarks with their conditions**, meaning hardware, dataset, seed and what failed.
- **Architecture decision records** in `docs/adr`, so every trade-off can be challenged.
- **An evaluation set in CI**, so quality is checked on every push.
- **Limits stated plainly**, including what is simulated and what was not tested.
- **Small, signed commits** with clear messages and pull requests that explain why.

## Tech stack

### Building with now

| Area | Tools |
|---|---|
| Languages | <img src="https://skillicons.dev/icons?i=python,ts,js,bash" alt="Python, TypeScript, JavaScript, Bash" /> |
| Backend and web | <img src="https://skillicons.dev/icons?i=fastapi,django,nodejs,nextjs,react,tailwind" alt="FastAPI, Django, Node.js, Next.js, React, Tailwind" /> |
| Data and messaging | <img src="https://skillicons.dev/icons?i=postgres,mongodb,mysql,redis,kafka" alt="PostgreSQL, MongoDB, MySQL, Redis, Kafka" /> ![TimescaleDB](https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black) ![Mosquitto](https://img.shields.io/badge/Mosquitto_MQTT-3C5280?style=flat-square&logo=eclipsemosquitto&logoColor=white) |
| Open model serving and gateway | ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white) ![llama.cpp](https://img.shields.io/badge/llama.cpp-5C5C5C?style=flat-square) ![LiteLLM](https://img.shields.io/badge/LiteLLM-2D6CDF?style=flat-square) |
| Hosted models | ![Anthropic](https://img.shields.io/badge/Anthropic_API-D4A574?style=flat-square&logo=anthropic&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat-square&logo=openai&logoColor=white) |
| Retrieval and agents | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square) ![LibreChat](https://img.shields.io/badge/LibreChat-10A37F?style=flat-square) |
| Classical ML | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) ![ONNX Runtime](https://img.shields.io/badge/ONNX_Runtime-005CED?style=flat-square&logo=onnx&logoColor=white) ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white) |
| Cloud and delivery | <img src="https://skillicons.dev/icons?i=aws,docker,kubernetes,githubactions,linux,git,vercel" alt="AWS, Docker, Kubernetes, GitHub Actions, Linux, Git, Vercel" /> ![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white) ![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=flat-square&logo=traefikproxy&logoColor=white) ![KIND](https://img.shields.io/badge/KIND-326CE5?style=flat-square&logo=kubernetes&logoColor=white) |
| Observability and testing | <img src="https://skillicons.dev/icons?i=prometheus,grafana,pytest" alt="Prometheus, Grafana, Pytest" /> ![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black) ![mypy](https://img.shields.io/badge/mypy-2A6DB2?style=flat-square) |
| Business systems and automation | ![Zoho](https://img.shields.io/badge/Zoho-C8202B?style=flat-square) ![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white) |

<details>
<summary><b>Growing into</b>, the next tools on my list. They move up once they ship in a repo.</summary>

<br/>

| Area | Tools |
|---|---|
| Inference at scale | ![vLLM](https://img.shields.io/badge/vLLM-30A2FF?style=flat-square) ![LMDeploy](https://img.shields.io/badge/LMDeploy-6B7280?style=flat-square) ![TGI](https://img.shields.io/badge/TGI-FFD21E?style=flat-square&logo=huggingface&logoColor=black) ![NVIDIA GPU Operator](https://img.shields.io/badge/NVIDIA_GPU_Operator-76B900?style=flat-square&logo=nvidia&logoColor=white) ![DCGM](https://img.shields.io/badge/DCGM_exporter-76B900?style=flat-square&logo=nvidia&logoColor=white) |
| Managed AI on AWS | ![Amazon Bedrock](https://img.shields.io/badge/Amazon_Bedrock-232F3E?style=flat-square&logo=amazonaws&logoColor=white) ![Amazon SageMaker](https://img.shields.io/badge/Amazon_SageMaker-232F3E?style=flat-square&logo=amazonaws&logoColor=white) |
| Model adaptation | ![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![PEFT LoRA](https://img.shields.io/badge/PEFT_LoRA-FFD21E?style=flat-square) ![AWQ](https://img.shields.io/badge/AWQ_quantization-5C5C5C?style=flat-square) |
| Evals and LLM observability | ![Promptfoo](https://img.shields.io/badge/Promptfoo-1F6FEB?style=flat-square) ![DeepEval](https://img.shields.io/badge/DeepEval-6B7280?style=flat-square) ![Langfuse](https://img.shields.io/badge/Langfuse-000000?style=flat-square) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-425CC7?style=flat-square&logo=opentelemetry&logoColor=white) ![Locust](https://img.shields.io/badge/Locust-3AA655?style=flat-square) |
| Cost visibility | ![OpenCost](https://img.shields.io/badge/OpenCost-0F766E?style=flat-square) |
| Agents | ![Hermes](https://img.shields.io/badge/Hermes_agent_models-6B7280?style=flat-square) ![OpenClaw](https://img.shields.io/badge/OpenClaw-6B7280?style=flat-square) ![SearXNG](https://img.shields.io/badge/SearXNG-3050FF?style=flat-square) |
| Infrastructure as code | <img src="https://skillicons.dev/icons?i=terraform" alt="Terraform" /> ![Longhorn](https://img.shields.io/badge/Longhorn-5F224A?style=flat-square) |

</details>

## How I work

- **Measure before you claim.** I build the evaluation set and the cost meter before launch, and I publish the conditions with every number.
- **Cost is a design input.** I track cost per outcome from the first version, and I cap spend per tenant.
- **The model explains and deterministic code decides**, wherever a wrong answer could hurt someone. I test that rule.
- **Access is part of the design.** Each agent acts only within the tenant and permissions of the person it serves, and its tools are read-only unless there is a written reason.
- **Every decision can be replayed.** I keep an audit trail so any output can be reconstructed end to end.
- **Failure is rehearsed.** I break the system on purpose, record what happened and fix it before anyone depends on it.
- **Decisions are written down**, including what I would change, so the next person can challenge them.
- **Test the certain, evaluate the uncertain.** Deterministic code gets tests and model behaviour gets evals.

<details>
<summary><b>How I learn</b></summary>

<br/>

- I build the smallest working version, then measure it.
- I stay on one topic until it ships in a repo.
- I write up what I measured, including what failed.
- I read primary documentation before tutorials.
- I rent hardware in short, scripted sessions and publish what the run showed.

</details>

## Background

Three years of production engineering across site reliability, DevOps, full stack and applied AI agents, including building agents on business data and training developers. Holder of the AWS Certified Cloud Practitioner certification. Based in Nairobi.

## Writing and docs

Write-ups go on [Hashnode](https://hashnode.com/@gilbertofke) and [Medium](https://medium.com/@gilbertofke), with one article a week during the PikiBytes build. Project documentation lives beside the code, with design decisions recorded in each repository.
