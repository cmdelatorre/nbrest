# nbrest

```
pip install -e ./
jupyter notebook --NotebookApp.nbserver_extensions="{'nbrest.ext':True}"
```

# Usage

To automatically expose a function in an HTTP endpoint, decorate it with `nbrest.resources.expose`:

```python
from nbrest.resources import expose

# Expose the `foo`function in the URL http://localhost:5000/hello/
@expose("/hello/")
def foo():
    return "hello world!"


# Expose the `foo`function in the URL http://localhost:5000/add/?x=8&y=9
@expose("/add/")
def add(x, y):
    return x + y

```
