# Brainf**k++ Interpreter

## Description

This is a simple interpreter for the esoteric programming language [Brainf**k](https://en.wikipedia.org/wiki/Brainfuck) written in Python 3.

This implementation adds a few extra commands to the language, hence the name Brainf**k++.

This interpreter has been written based on the language specifications provided in [this](https://www.codeabbey.com/index/wiki/brainfuck) CodeAbbey wiki page.

## Usage

### From command line:

```bash
$ python3 bfpp.py filepath
```

### In a Python program:

```python
from bfpp import bf

program = "+++++:"
bf.run(program)  # 5
```