# Test/Train splitting.
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)
    
    dataset_1 = test_cache.head()
    dataset_2 = train_cache.head()

# Cross Validation.
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.classification import DecisionTreeClassificationTrainer
from ggml.model_selection import cross_val_score

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache", parts=1)
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    trainer = DecisionTreeClassificationTrainer()
    score = cross_val_score(trainer, cache)
score
