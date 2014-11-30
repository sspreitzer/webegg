webegg
======

Python webegg, run code from URL

Usage
-----

Loading and later reloading a webegg
```python
import webegg

w = webegg.load('https://example.com/py/helloworld.py', globals())

w.reload()
```

Loading via xload
```python
import webegg

webegg.load('https://example.com/py/helloworld.py', globals())
webegg.load('https://example.com/py/test.py', globals())

webegg.xload('https://example.com/py', ['helloworld', 'test'], globals())
```
