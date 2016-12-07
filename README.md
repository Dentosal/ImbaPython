# <a class="spin">Imba</a>Python <sub class="blink">v0.1.0</sub><sup class="slide-left" style="color: red !important;">A bit unstable</sup>

<!--- Testing css in GitHub readme limits --->

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


<!--- Styles
<style>
    h1 {
        transform: rotate(2deg);
        -moz-osx-font-smoothing: grayscale;
        -webkit-font-smoothing: antialiased;
        animation: slide 120s linear infinite, blinkx 2s linear infinite;
    }
    h2:nth-child(5n) {
        animation: blink 10s infinite;
    }
    h2:nth-child(3n) {
        animation: blink 0.5s linear infinite alternate, swing 1s infinite;
    }
    h2:nth-child(3n) + p {
        transform: rotate(-2deg);
        -moz-osx-font-smoothing: grayscale;
        -webkit-font-smoothing: antialiased;
        animation: swing 20s infinite;
    }
    p {
        transform: rotate(2deg);
        -moz-osx-font-smoothing: grayscale;
        -webkit-font-smoothing: antialiased;
        animation: swing 10s infinite;
    }
    div.line {
        background: red !important;
    }

    .blink {
        animation: blink 0.7s linear infinite alternate;
    }
    .spin {
        color: black;
        display: inline-block;
        transform: rotate(-2deg);
        animation: spin 3s linear infinite;
    }
    .slide-left {
        display: inline-block;
        transform: translate(-20px);
        animation: sliderev 3s linear infinite;
    }

    @keyframes swing {
        0%   {transform: rotate(2deg);}
        50%  {transform: rotate(-2deg);}
        100% {transform: rotate(2deg);}
    }
    @keyframes spin {
        0%   {transform: rotate(0deg);}
        50%  {transform: rotate(160deg);}
        100% {transform: rotate(359deg);}
    }
    @keyframes slide {
        0%   {transform: translate(0px);}
        50%  {transform: translate(50%);}
        100% {transform: translate(0px);}
    }
    @keyframes sliderev {
        0%   {transform: translate(-20px);}
        50%  {transform: translate(-40%);}
        100% {transform: translate(-20px);}
    }
    @keyframes blink {
        10%  {opacity: 1;}
        11%  {opacity: 0;}
        12%  {opacity: 1;}
        50%  {opacity: 1;}
        51%  {opacity: 0;}
        52%  {opacity: 1;}
        54%  {opacity: 0;}
        55%  {opacity: 1;}
        56%  {opacity: 0;}
        57%  {opacity: 1;}
        58%  {opacity: 0;}
        59%  {opacity: 1;}
        60%  {opacity: 0;}
        61%  {opacity: 1;}
        62%  {opacity: 0;}
        63%  {opacity: 1;}
        65%  {opacity: 0;}
    }
    @keyframes blinkx {
        49%  {opacity: 1;}
        50%  {opacity: 0;}
        51%  {opacity: 1;}
    }
</style>
--->
