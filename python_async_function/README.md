# Python Async Function

## 📌 Description

This project introduces asynchronous programming in Python using:

- `async` and `await`
- `asyncio`
- Concurrent coroutines
- Tasks
- Measuring execution time
- The `random` module

The goal is to understand how Python handles concurrency using a single-threaded event loop.

---

## 🧠 Concepts Covered

- Writing asynchronous coroutines
- Running coroutines concurrently
- Creating and managing `asyncio.Task`
- Using `asyncio.gather()` and `asyncio.as_completed()`
- Measuring runtime performance
- Understanding concurrency vs sequential execution

---

## 📂 Files

| File | Description |
|------|------------|
| `0-basic_async_syntax.py` | Async coroutine `wait_random` |
| `1-concurrent_coroutines.py` | Runs multiple coroutines concurrently |
| `2-measure_runtime.py` | Measures average execution time |
| `3-tasks.py` | Creates and returns `asyncio.Task` |
| `4-tasks.py` | Concurrent tasks execution |

---

## 🚀 Example Usage

### wait_random

```python
import asyncio
from 0-basic_async_syntax import wait_random

print(asyncio.run(wait_random(5)))

---
## 👨‍💻 Author

Rateel Bahathek
