# Decision Tree classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.classification import DecisionTreeClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = DecisionTreeClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))

# Decision Tree classification with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_classification
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import accuracy_score
from ignite_ml.classification import DecisionTreeClassificationTrainer 

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = DecisionTreeClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))

# ANN classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.classification import ANNClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = ANNClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))

# ANN classification with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_classification
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import accuracy_score
from ignite_ml.classification import ANNClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = ANNClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))

# KNN classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.classification import KNNClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = KNNClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))

# KNN classification with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_classification
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import accuracy_score
from ignite_ml.classification import KNNClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = KNNClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))

# LogReg classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.classification import LogRegClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LogRegClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))

# LogReg classification with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_classification
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import accuracy_score
from ignite_ml.classification import LogRegClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = LogRegClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))

# SVM classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.classification import SVMClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = SVMClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))

# SVM classification with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_classification
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import accuracy_score
from ignite_ml.classification import SVMClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = SVMClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))

# Random Forest classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.classification import RandomForestClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = RandomForestClassificationTrainer(20)
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))

# Random Forest classification with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_classification
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import accuracy_score
from ignite_ml.classification import RandomForestClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = RandomForestClassificationTrainer(20)
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))

# MLP classification with Ignite ML (local).
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ignite_ml.regression import MLPArchitecture
from ignite_ml.regression import MLPRegressionTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

def encode_label(x):
    if x:
        return [0, 1]
    else:
        return [1, 0]

def decode_label(x):
    if x[0] > x[1]:
        return 0
    else:
        return 1

trainer = MLPRegressionTrainer(MLPArchitecture(20).with_layer(2, activator='sigmoid'))
model = trainer.fit(x_train, [encode_label(x) for x in y_train])

accuracy_score(y_test, [decode_label(x) for x in model.predict(x_test)])
