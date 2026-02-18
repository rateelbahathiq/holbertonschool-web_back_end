Python Variable Annotations
📌 Project Overview

This project introduces Python type annotations and progressively explores advanced typing concepts such as:

Variable annotations

Function annotations

List and Union types

Tuple typing

Callable typing

Higher-order functions

Abstract container types (Iterable, Sequence)

The goal is to understand how to:

Clearly define function contracts

Improve code readability

Enable static type checking

Design flexible and precise interfaces

All tasks follow:

PEP 8 style guidelines

Proper documentation standards

Type annotation best practices

🧠 Concepts Covered
1️⃣ Basic Variable Annotations

Using PEP 526 syntax:

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"


Purpose:

Make variable types explicit

Improve readability

Support static analysis tools

2️⃣ Function Type Annotations

Annotating parameters and return types:

def add(a: float, b: float) -> float:
    return a + b


Syntax:

(parameter: Type) -> ReturnType

3️⃣ Collection Typing

Using the typing module:

from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)


Describes:

A list containing floats

Return type guarantee

4️⃣ Union Types

Allowing multiple possible types:

from typing import Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)


Meaning:

Each element can be int OR float

5️⃣ Tuple Typing

Describing fixed-length structured returns:

from typing import Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))


Tuple typing ensures:

Position matters

Type order matters

6️⃣ Callable Typing (Higher-Order Functions)

Typing functions that return functions:

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply


Callable[[float], float] means:

Takes a float

Returns a float

This introduces:

Closures

Function factories

Higher-order design

7️⃣ Abstract Container Types

Using abstract interfaces instead of concrete types:

from typing import Iterable, Sequence, List, Tuple

def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]


Why abstract types?

Instead of:

List[str]


We use:

Iterable[Sequence]


This makes the function:

More flexible

More generic

Interface-based
