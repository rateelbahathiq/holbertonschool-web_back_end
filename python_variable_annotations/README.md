# Python Variable Annotations

## 📌 Description

This project introduces **type annotations in Python** and explores progressively advanced typing concepts including:

- Variable annotations  
- Function annotations  
- List and Union types  
- Tuple typing  
- Callable typing  
- Higher-order functions  
- Abstract container types (`Iterable`, `Sequence`)  

The goal is to understand how Python’s typing system improves code clarity, readability, and maintainability while keeping Python dynamically typed.

---

## 🧠 Concepts Covered

- Using PEP 526 variable annotations  
- Annotating function parameters and return types  
- Typing collections with `List`, `Tuple`, and `Union`  
- Writing higher-order functions with `Callable`  
- Understanding abstract types like `Iterable` and `Sequence`  
- Designing flexible and precise type contracts  
- Writing clean, PEP 8–compliant code  

---

## 📂 Files

| File | Description |
|------|------------|
| `0-add.py` | Function that adds two floats |
| `1-concat.py` | Concatenates two strings |
| `2-floor.py` | Returns the floor of a float |
| `3-to_str.py` | Converts a float to string |
| `4-define_variables.py` | Defines annotated variables |
| `5-sum_list.py` | Sums a list of floats |
| `6-sum_mixed_list.py` | Sums a list of ints and floats |
| `7-to_kv.py` | Returns a tuple with squared value |
| `8-make_multiplier.py` | Returns a multiplier function |
| `9-element_length.py` | Returns elements and their lengths |

---

## 🚀 Example Usage

### add

```python
from 0-add import add

print(add(1.11, 2.22))
```

### sum_mixed_list

```python
from 6-sum_mixed_list import sum_mixed_list

print(sum_mixed_list([5, 4, 3.14, 666, 0.99]))
```

### make_multiplier

```python
from 8-make_multiplier import make_multiplier

times_two = make_multiplier(2.0)
print(times_two(3.0))
```

---


## 👨‍💻 Author

Rateel Bahathek

