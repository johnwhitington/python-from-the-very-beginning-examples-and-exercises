def found_values(l, d):
    output = []
    for k in l:
        v = d.get(k)
        if v != None:
            output.append(v)
    return output



>>> def f(x, y): return x + y + z
... 
>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
NameError: name 'z' is not defined
>>> z = 3
>>> f(1, 2)
6

