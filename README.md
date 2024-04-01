# rapid-web
Provides tools for generating web front ends for API's written in python. 
The web front-ends generated are for testing only and are not recommended for production environment

## How to use:
Download rapid-web by executing:
```
git clone https://github.com/Austin-rgb/rapid-web
cd webapp
```
## Example code:

```python
from api_server import api2flask_app
class Demo:
  def __init__(self):
    pass

# We recommend providing type annotations to help in data conversion
# process for your methods
  def add(number1:int, number2:int):
    return number1 + number2

demo = Demo()
app = api2flask_app(demo)
```
