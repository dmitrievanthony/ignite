import numpy as np
from sklearn.datasets import make_regression

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache", parts=10)
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache", parts=10)
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)
