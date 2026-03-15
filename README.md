## Performance Benchmark

![alt text](image.png)

Benchmark tool: wrk  
Machine: Debian Linux  
Duration: 10 seconds  
Connections: 60  


MachPoint achieves significantly higher throughput by delegating HTTP networking to Go's fasthttp while exposing a Python developer interface.

# MachPoint ⚡

> **High-performance API framework — Python ergonomics, Go networking.**

**MachPoint** combines the **developer experience of Python** with the **networking performance of Go**. Instead of handling HTTP traffic inside the Python runtime like traditional frameworks, MachPoint offloads the networking layer to a Go server built with [`fasthttp`](https://github.com/valyala/fasthttp), while exposing a clean Python interface for defining APIs.

> **Author:** Elias Joby &nbsp;|&nbsp; **License:** MIT

---

## ✨ Features

-  **High-performance HTTP server** powered by Go's `fasthttp`
-  **Python developer interface** for defining routes and handlers
-  **ctypes bridge** connecting Python and Go runtimes seamlessly
-  **Automatic OpenAPI generation** from your route definitions
-  **Built-in Swagger UI** documentation at `/swagger/`
-  **Middleware support** for request/response pipelines
-  **Configurable server parameters**
-  **Benchmarking suite** for comparing against popular frameworks

---

## 🧠 Core Idea

Traditional Python frameworks process every HTTP request inside the Python interpreter — which becomes the bottleneck at high concurrency:

```
HTTP Request → Python Runtime → Framework Router → Application Handler
```

MachPoint changes this by moving the networking layer to Go:

```
HTTP Request → Go fasthttp Server → MachPoint Routing Layer → Python Developer API
```

The result: **faster request processing**, **reduced interpreter overhead**, and **higher concurrency** — all while writing your API in Python.

---

## 🏗 Architecture

MachPoint uses a hybrid runtime architecture with three distinct layers:

```
Python Application
        │
        ▼
MachPoint Python API        ← You write code here
        │
        ▼
ctypes bridge               ← Connects Python ↔ Go
        │
        ▼
Go HTTP Server (fasthttp)   ← Handles all networking
        │
        ▼
HTTP Requests
```

### Key Components

**Python Layer**
- Developer-facing API for defining routes and handlers
- Route registration and middleware configuration
- Dependency injection support

**ctypes Bridge**
- Connects Python code to the compiled Go shared library
- Passes request/response data across runtimes with minimal overhead

**Go Layer**
- High-performance HTTP handling via `fasthttp`
- Request routing and middleware execution
- Native Go concurrency with goroutines

---

## 📊 Performance Benchmark

> *Can we keep Python's developer ergonomics while using a faster runtime for networking?*
> Benchmark results show the answer is **yes**.

**Tool:** `wrk` &nbsp;|&nbsp; **Machine:** Debian Linux &nbsp;|&nbsp; **Duration:** 10s &nbsp;|&nbsp; **Connections:** 60

```bash
wrk -t4 -c60 -d10s http://localhost:8080/hello
```

**Example output:**
```
Requests/sec: ~42,000
Average latency: ~2.2 ms
```

### Results

| Framework     | Requests / sec | vs MachPoint |
| ------------- | -------------- | ------------ |
| FastAPI       | ~4,000         | 10x slower   |
| Tornado       | ~5,000         | 8x slower    |
| Flask         | ~6,000         | 6.7x slower  |
| Starlette     | ~8,000         | 5x slower    |
| Sanic         | ~28,000        | 1.4x slower  |
| **MachPoint** | **~40,000** ✅  | —            |

> Results may vary depending on hardware and system configuration.

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Go 1.18+
- Git

### Steps

**1. Clone the repository:**
```bash
git clone https://github.com/<your-username>/MachPoint.git
cd MachPoint
```

**2. Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r req.txt
```

---

## 🚀 Quick Start

```python
from machpoint import MachPoint

app = MachPoint()

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    app.start()
```

**Run the application:**
```bash
python -m examples.basic_app
```

**Test the endpoint:**
```bash
curl http://localhost:8080/hello
```

**Expected response:**
```json
{
  "message": "Hello, World!"
}
```

---

## 📚 API Documentation

MachPoint automatically generates OpenAPI documentation for all registered routes at startup. Once the server is running, open:

```
http://localhost:8080/swagger/
```

---

## 🧪 Running Benchmarks

The repository includes a full benchmark suite comparing MachPoint against popular Python frameworks.

```bash
cd benchmarks
./benchmark.sh
```

**Frameworks tested:** FastAPI, Starlette, Sanic, Tornado, Flask, MachPoint

---

## 📂 Project Structure

```
MachPoint/
│
├── machpoint/        # Python API layer
├── benchmarks/       # Benchmark scripts and suite
├── examples/         # Example applications
├── swagger-ui/       # Swagger UI assets
├── req.txt           # Python dependencies
├── setup.py          # Python package setup
└── pyproject.toml    # Build configuration
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository and create a feature branch
2. Make your changes with clear, descriptive commit messages
3. Add or update tests as appropriate
4. Ensure benchmarks still pass
5. Open a pull request with a description of your changes

---

## 🗺 Roadmap

- [ ] WebSocket support
- [ ] Request validation with Pydantic-style schemas
- [ ] Background task queue integration
- [ ] gRPC transport layer support
- [ ] Docker-ready deployment templates
- [ ] Async/await handler support
- [ ] Plugin/extension system for custom middleware

---

## ❓ FAQ

**Do I need to know Go to use MachPoint?**  
No. MachPoint's Python API is the only interface you need. The Go layer is pre-compiled and abstracted away through the ctypes bridge.

**How does MachPoint compare to ASGI frameworks?**  
ASGI frameworks like FastAPI and Starlette still process HTTP requests within the Python runtime. MachPoint moves the networking layer entirely to Go — that's the core reason for the performance difference.

**Is MachPoint production-ready?**  
MachPoint is currently an experimental framework exploring the Python + Go hybrid architecture. It demonstrates significant performance gains but is best suited for research, benchmarking, and hobby projects at this stage.

**Can I use async/await in handlers?**  
Async handler support is on the roadmap. Currently, MachPoint handlers are synchronous Python functions.

---

## ⚡ Why MachPoint?

Many modern high-performance systems combine multiple languages — offloading compute-heavy or I/O-heavy work to faster runtimes while keeping developer-friendly interfaces in higher-level languages.

MachPoint applies this idea to web APIs: keep Python for the developer experience, use Go for the networking layer.

**Ideal for:**
- High-performance REST APIs requiring low latency
- Microservices with high request volumes
- Backend services where throughput is critical
- Exploring polyglot runtime architectures

---

##  License

MIT License

---

##  Author

**Elias Joby**