# DateTime Parser

This repo contains a Python implementation of a relative time string parser like `now()+1d+3h`.

## Example

```python
from parser import parse

print(parse("now()+2d+4h"))
