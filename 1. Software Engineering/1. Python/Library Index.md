# 📚 Python Library Index

> Master reference for every Python library, organized by domain.

---

## Data Structures & Performance
| Library | Purpose |
|---------|--------|
| `numpy` | N-dimensional arrays, linear algebra, broadcasting |
| `polars` | Lightning-fast DataFrame (Rust-backed, zero-copy) |
| `pandas` | Data manipulation and analysis |
| `arrow` / `pyarrow` | Columnar in-memory format, zero-copy IPC |
| `vaex` | Out-of-core DataFrames for billion-row datasets |
| `numba` | JIT compilation, CUDA GPU kernels |
| `cython` | C-extension compiler for Python |
| `pybind11` | C++ ↔ Python bindings |

## Web Scraping & HTTP
| Library | Purpose |
|---------|--------|
| `requests` | HTTP client |
| `httpx` | Async-capable HTTP client |
| `aiohttp` | Async HTTP client/server |
| `beautifulsoup4` | HTML/XML parsing |
| `scrapy` | Full scraping framework with pipelines |
| `playwright` | Modern async browser automation |
| `selenium` | Browser automation |
| `pdfplumber` | PDF table/text extraction |
| `camelot` | PDF table extraction |
| `pytesseract` | OCR (Tesseract wrapper) |

## Data Cleaning & Validation
| Library | Purpose |
|---------|--------|
| `pandas` | Core cleaning operations |
| `ftfy` | Fix mojibake / broken unicode text |
| `unidecode` | Transliterate unicode to ASCII |
| `dateutil` | Flexible date parsing |
| `pandera` | DataFrame schema validation |
| `great_expectations` | Data quality testing at scale |
| `pydantic` | Data validation with type hints |
| `cerberus` | Lightweight schema validation |

## Machine Learning
| Library | Purpose |
|---------|--------|
| `scikit-learn` | Classical ML algorithms, pipelines, metrics |
| `xgboost` | Gradient boosting (competition winner) |
| `lightgbm` | Fast gradient boosting (Microsoft) |
| `catboost` | Gradient boosting with categorical support |
| `optuna` | Hyperparameter optimization (Bayesian) |
| `imbalanced-learn` | SMOTE and resampling techniques |
| `scipy` | Scientific computing, optimization, signal processing |
| `statsmodels` | Statistical modeling and tests |

## Deep Learning
| Library | Purpose |
|---------|--------|
| `torch` (PyTorch) | Neural networks, autograd, GPU training |
| `torchvision` | CV datasets, transforms, pretrained models |
| `torchaudio` | Audio processing and models |
| `transformers` | Hugging Face — pretrained NLP/CV/audio models |
| `datasets` | Hugging Face — dataset loading and processing |
| `accelerate` | Distributed training simplified |
| `peft` | Parameter-efficient fine-tuning (LoRA, QLoRA) |
| `bitsandbytes` | Quantization (4-bit, 8-bit) for LLMs |
| `safetensors` | Safe, fast model weight serialization |
| `onnx` / `onnxruntime` | Model export and cross-platform inference |

## Computer Vision
| Library | Purpose |
|---------|--------|
| `opencv-python` | Image processing, video, feature detection |
| `Pillow` | Image manipulation (open, resize, filter) |
| `albumentations` | Fast image augmentation for training |
| `torchvision` | PyTorch CV transforms and models |
| `ultralytics` | YOLOv8+ object detection |
| `mediapipe` | Face, hand, pose detection (Google) |
| `open3d` | 3D point cloud processing |

## NLP & LLMs
| Library | Purpose |
|---------|--------|
| `transformers` | Pretrained models (BERT, GPT, T5, etc.) |
| `tokenizers` | Fast tokenization (Rust-backed) |
| `spacy` | Industrial NLP (NER, POS, dependency parsing) |
| `nltk` | Classic NLP toolkit |
| `sentence-transformers` | Sentence/text embeddings |
| `langchain` | LLM application framework |
| `llamaindex` | Data-aware LLM applications, RAG |
| `openai` | OpenAI API client |
| `vllm` | High-throughput LLM serving |

## MLOps & Serving
| Library | Purpose |
|---------|--------|
| `mlflow` | Experiment tracking, model registry |
| `wandb` | Weights & Biases — experiment tracking |
| `dvc` | Data/model version control |
| `bentoml` | Model serving framework |
| `fastapi` | REST API for model serving |
| `streamlit` | Rapid ML demo UIs |
| `gradio` | Interactive ML demos |
| `ray` | Distributed computing, Ray Serve, Ray Tune |

## Visualization
| Library | Purpose |
|---------|--------|
| `matplotlib` | Foundational plotting |
| `seaborn` | Statistical visualization |
| `plotly` | Interactive plots and dashboards |
| `bokeh` | Interactive web visualization |
| `altair` | Declarative statistical visualization |

## Reinforcement Learning
| Library | Purpose |
|---------|--------|
| `gymnasium` (Gym) | RL environments and benchmarks |
| `stable-baselines3` | Reliable RL algorithm implementations |
| `cleanrl` | Single-file RL implementations |
| `tianshou` | Modular RL library (PyTorch) |

## Hardware, Robotics & Embedded
| Library | Purpose |
|---------|--------|
| `pyserial` | Serial port communication (UART) |
| `RPi.GPIO` / `gpiozero` | Raspberry Pi GPIO control |
| `micropython` | Python for microcontrollers (ESP32, Pico) |
| `circuitpython` | Adafruit microcontroller Python |
| `pyFirmata` | Arduino control from Python |
| `rclpy` | ROS2 Python client library |
| `dronekit` | Drone control via MAVLink |
| `pymavlink` | Low-level MAVLink protocol |
| `pybullet` | Physics simulation for robotics |
| `mujoco` | Advanced physics simulation (DeepMind) |
| `bleak` | Bluetooth Low Energy (BLE) |
| `paho-mqtt` | MQTT messaging for IoT |
| `pyzmq` | ZeroMQ messaging (low-latency IPC) |
| `python-can` | CAN bus communication |
| `spidev` | SPI device interface (Linux) |
| `smbus2` | I2C communication |
| `picamera2` | Raspberry Pi camera |
| `adafruit-circuitpython-*` | Sensor drivers (BMP280, MPU6050, etc.) |

## Low-Latency & Performance
| Library | Purpose |
|---------|--------|
| `cython` | Compile Python to C extensions |
| `numba` | JIT compile numeric Python + CUDA |
| `pybind11` | High-performance C++ bindings |
| `cupy` | NumPy on GPU (CUDA) |
| `pycuda` | Low-level CUDA from Python |
| `uvloop` | Ultra-fast asyncio event loop |
| `orjson` | Fastest JSON serialization |
| `msgpack` | Binary serialization (faster than JSON) |
| `polars` | Multi-threaded DataFrames (Rust engine) |
| `pyarrow` | Zero-copy columnar data |
| `mmap` (stdlib) | Memory-mapped file I/O |
| `multiprocessing.shared_memory` | Zero-copy shared memory between processes |
| `line_profiler` | Line-by-line profiling |
| `scalene` | CPU + GPU + memory profiler |
| `py-spy` | Sampling profiler (no code changes) |
