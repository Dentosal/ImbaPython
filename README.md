# ImbaPython <sub>v0.1.0</sub><sup><sup>A bit unstable</sup></sup>

ImbaPython is a Python extender, using the [forbiddenfruit](https://github.com/clarete/forbiddenfruit) library. The maing goal of this project is to show how good python could be it designed with functional list and consistent method/function separation, for example how `len` works.

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
my_ip = "http://httpbin.org/ip".fetch().json["origin"]
print(my_ip)

print(
    range(1,11)
        .map(lambda row: range(1,11)
        .map(lambda col: row*col))
        .map(lambda row: row.fmt("{:4}")).join("\n")
)
```
