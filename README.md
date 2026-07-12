# ML Engineer Roadmap (Degree-Independent, Proof-of-Work First)

> **Mission**
>
> Become a production-ready Machine Learning Engineer and secure a full-time ML Engineering role before **31 December 2026**.
>
> This roadmap is intentionally **engineering-focused**, **portfolio-first**, and **startup-oriented**. It avoids unnecessary academic depth and instead focuses on building skills that companies can immediately use.

---

# Guiding Principles

## 1. Build More Than You Study

For every concept you learn:

- Read
- Implement
- Benchmark
- Deploy
- Document
- Publish

Never let knowledge remain inside notebooks.

---

## 2. Think Like an Engineer

Don't ask

> "Can I train a model?"

Ask

> "Can another engineer deploy, monitor, reproduce and scale this model?"

---

## 3. Every Repository Must Feel Like Open Source

Every serious project should contain

```
README.md
LICENSE
requirements.txt / pyproject.toml
Dockerfile
Makefile
tests/
docs/
examples/
benchmarks/
images/
```

A recruiter should understand your project within 5 minutes.

---

## 4. Everything Must Be Reproducible

Someone should be able to run

```bash
git clone ...
uv sync
docker compose up
```

and reproduce your results.

---

# Phase 0 — Engineering Mindset

Before ML, become comfortable with software engineering.

## Linux

Must know

- filesystem
- permissions
- ssh
- tmux
- cron
- grep
- sed
- awk
- curl
- wget
- systemctl
- journalctl
- networking basics

---

## Git

Master

- branching
- rebasing
- cherry-pick
- stash
- tags
- release workflow
- resolving merge conflicts

Every project should use Git properly.

---

## Github

Know

- Issues
- Pull Requests
- Discussions
- Releases
- Github Actions
- Security
- Dependabot

---

## Documentation

Write documentation as if another engineer depends on it.

Use

- Markdown
- MyST
- MkDocs or Sphinx

---

# Phase 1 — Python Mastery

Python is your primary engineering language.

Become fluent.

---

## Core Python

- data structures
- functions
- OOP
- decorators
- context managers
- generators
- iterators
- comprehensions
- lambda
- closures
- exceptions
- logging

---

## Advanced Python

- asyncio
- multiprocessing
- multithreading
- queues
- memory management
- profiling
- type hinting
- dataclasses
- pathlib
- descriptors
- metaclasses (basic understanding)

---

## Performance

Know how to optimize code.

Use

- cProfile
- line_profiler
- memory_profiler
- NumPy vectorization

Understand

- CPU bottlenecks
- memory bottlenecks
- I/O bottlenecks

---

# Phase 2 — Mathematical Foundation

Only learn what is useful.

## Linear Algebra

- vectors
- matrices
- matrix multiplication
- transpose
- inverse
- eigenvalues
- eigenvectors
- SVD

---

## Probability

- distributions
- conditional probability
- Bayes theorem
- expectation
- variance

---

## Statistics

- hypothesis testing
- confidence intervals
- correlation
- covariance
- sampling
- A/B testing

---

## Calculus

Only enough for deep learning.

- derivatives
- gradients
- chain rule
- partial derivatives

---

# Phase 3 — Data Engineering Basics

Real companies spend more time cleaning data than training models.

Know

- Pandas
- NumPy
- Polars (recommended)
- SQL
- Parquet
- Feather

Learn

- missing values
- feature engineering
- joins
- aggregations
- pipelines

---

# Phase 4 — Machine Learning

## Scikit-Learn

Master

- Pipeline
- ColumnTransformer
- GridSearchCV
- RandomizedSearchCV
- Cross Validation

Models

- Linear Regression
- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

Understand

- bias-variance
- overfitting
- regularization
- metrics
- feature importance

---

# Phase 5 — Deep Learning

## PyTorch

Master

- tensors
- autograd
- Dataset
- DataLoader
- custom Dataset
- transforms
- custom training loops
- schedulers
- mixed precision
- checkpointing

Learn

- CNN
- RNN
- LSTM
- GRU
- Transformer
- Attention

---

## Model Training

Know

- early stopping
- gradient clipping
- accumulation
- distributed training (basic)
- DDP basics

---

# Phase 6 — Modern AI

## Hugging Face

Learn

- datasets
- tokenizers
- transformers
- accelerate
- peft

---

## LLM

Understand

- tokenizer
- embeddings
- attention
- KV cache
- context window
- LoRA
- QLoRA
- RAG
- Fine tuning

---

## Vision

Learn

- ViT
- CLIP
- SAM

---

## Multimodal

Understand

- VLM
- OCR
- image captioning

---

# Phase 7 — Model Optimization

Companies pay for lower inference cost.

Master

- ONNX
- TensorRT
- OpenVINO (optional)
- ONNX Runtime

Understand

- FP32
- FP16
- BF16
- INT8
- quantization
- pruning
- batching
- caching

Benchmark everything.

---

# Phase 8 — Model Serving

## FastAPI

Must know

- REST APIs
- async endpoints
- WebSocket
- background tasks
- dependency injection

---

## Serving

Master

- vLLM
- Triton Inference Server

Know

- batching
- streaming
- concurrency
- GPU utilization

---

# Phase 9 — MLOps

## Docker

Know

- multi-stage builds
- GPU Docker
- Docker Compose
- image optimization

---

## CI/CD

Github Actions

Automate

- tests
- linting
- formatting
- deployment

---

## Experiment Tracking

Choose one

- MLflow
- Weights & Biases

---

## Monitoring

Know

- Prometheus
- Grafana

Understand

- latency
- throughput
- GPU utilization
- failures

---

# Phase 10 — Software Engineering

Companies hire engineers.

Not notebook users.

Learn

- SOLID principles
- Clean Architecture
- Design Patterns
- Dependency Injection
- Unit Testing
- Integration Testing

Testing

- pytest
- mocking
- coverage

Code Quality

- Ruff
- Black
- mypy
- pre-commit

---

# Phase 11 — Cloud Fundamentals

Understand

- AWS basics
- EC2
- S3
- IAM
- Docker deployment

Optional

- Azure
- GCP

---

# Phase 12 — Portfolio

Every project must include

- architecture diagram
- benchmarks
- Docker
- CI/CD
- tests
- API
- documentation
- screenshots
- demo video

Never upload notebooks alone.

---

# Signature Projects

## Project 1

High Throughput LLM Inference System

Stack

- PyTorch
- vLLM
- FastAPI
- Docker

Include

- benchmarking
- concurrency testing
- caching
- streaming
- latency comparison

---

## Project 2

Real-Time Streaming Inference Pipeline

Stack

- PyTorch
- ONNX Runtime
- asyncio
- FastAPI

Include

- fault tolerance
- memory optimization
- latency profiling
- monitoring dashboard

---

## Project 3

Production Recommendation System

Include

- training pipeline
- feature engineering
- API
- retraining
- monitoring

---

## Project 4

End-to-End MLOps Pipeline

Includes

- training
- tracking
- deployment
- Docker
- CI/CD

---

## Project 5

RAG System

Include

- vector database
- embeddings
- reranking
- evaluation

---

# Benchmark Everything

Every repository should answer

- How fast?
- How much RAM?
- GPU utilization?
- Throughput?
- Latency?
- Model size?
- Cost per million requests?

---

# Resume Strategy

Your resume should be one page.

Focus on

- production systems
- measurable impact
- engineering
- GitHub
- deployed demos

Avoid

- coursework
- irrelevant certificates
- generic objectives

---

# Github Strategy

Every week

- improve one repository
- improve one README
- fix one issue
- add one benchmark
- add one test

Your GitHub should look alive.

---

# Networking Strategy

Don't mass apply.

Instead

- build
- publish
- explain
- connect

Reach out with proof.

Example

> I built an optimized vLLM inference server reducing latency by 35%. Here is the architecture and benchmark.

---

# Daily Routine

Every day

- 2 hours learning
- 4 hours building
- 1 hour reading code
- 30 minutes documentation
- 30 minutes improving GitHub

Always prioritize building.

---

# Things I Must Know

## Programming

- Python

---

## Machine Learning

- NumPy
- Pandas
- Polars
- Matplotlib
- Seaborn
- Scikit-Learn
- PyTorch

---

## Mathematics

- Linear Algebra
- Probability
- Statistics
- Calculus

---

## Backend

- FastAPI
- asyncio

---

## Deployment

- Docker
- Docker Compose
- ONNX Runtime
- TensorRT
- Triton
- vLLM

---

## MLOps

- MLflow
- Weights & Biases
- Github Actions

---

## Version Control

- Git
- Github

---

## Documentation

- Markdown
- MyST
- MkDocs

---

## Testing

- pytest
- Ruff
- Black
- mypy
- pre-commit

---

## Linux

- Shell
- SSH
- tmux
- systemd
- networking basics

---

## Databases

- SQLite
- PostgreSQL
- Redis

---

## Cloud

- AWS fundamentals

---

# Success Criteria

By **31 December 2026**, I should be able to:

- Build ML systems from scratch.
- Train and optimize deep learning models.
- Export models to ONNX and TensorRT.
- Serve models using FastAPI, vLLM, and Triton.
- Containerize applications with Docker.
- Implement CI/CD pipelines.
- Track experiments professionally.
- Write production-quality Python.
- Build complete end-to-end ML systems.
- Maintain open-source-quality GitHub repositories.
- Explain every engineering decision during interviews.
- Pass coding interviews for ML Engineer roles.
- Demonstrate enough publicly visible work that my portfolio outweighs the lack of a formal degree.

---

> **Core Philosophy**
>
> **Companies do not hire degrees; they hire engineers who consistently solve real problems, communicate clearly, and ship reliable software. Every project you build should be undeniable proof that you can contribute from day one.**
