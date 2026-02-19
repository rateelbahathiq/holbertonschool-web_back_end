# Python Async Comprehension

## 📌 Description

This project explores advanced asynchronous programming concepts in Python using:

- Async generators
- Async comprehensions
- Parallel execution with `asyncio.gather`
- Measuring runtime performance

The goal is to understand how asynchronous execution improves performance for I/O-bound operations.

---

## 🧠 Concepts Covered

- Creating async generators
- Using `async for`
- Writing async list comprehensions
- Running coroutines in parallel
- Measuring execution time
- Understanding concurrency with the event loop

---

## 📂 Files

| File | Description |
|------|------------|
| `0-async_generator.py` | Async generator yielding random numbers |
| `1-async_comprehension.py` | Collect values using async comprehension |
| `2-measure_runtime.py` | Run multiple comprehensions in parallel and measure runtime |

---

## 🚀 Example Usage

### Async Generator

```python
async for value in async_generator():
    print(value)
```
---
## 👨‍💻 Author

Rateel Bahathek
