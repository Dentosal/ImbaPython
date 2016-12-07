# ImbaPython <sub>v0.1.0</sub><sup><sup>A bit unstable</sup></sup>

ImbaPython is a Python extender, using the [forbiddenfruit](https://github.com/clarete/forbiddenfruit) library. The maing goal of this project is to show how good Python could be if it had functional lists and consistent method/function separation. Less legacy, more methods.

This project is heavily influenced by Haskell and Scala, and it is trying to provide similar toolset. While this is only demonstration, I hope that some day we will have programming language like this.

## Installation

First install the [forbiddenfruit](https://github.com/clarete/forbiddenfruit) library:
`pip3 install forbiddenfruit`
Then just copy the [`imba.py`](imba.py) file to your project directory.

## Usage

```python
# Import it
import imba

# Install addtional features
imba.install(["requests", "json"])

# Do whatever you want

# times table
print(
    range(1,11)
        .map(lambda row: range(1,11)
        .map(lambda col: row*col))
        .map(lambda row: row.fmt("{:4}")).join("\n")
)

# fetch ip
print("http://httpbin.org/ip".fetch().json["origin"])

# quick and efficient factorial
def factorial(n):
    assert n > 0
    return range(1, n+1).product()
```
