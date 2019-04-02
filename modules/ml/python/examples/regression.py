# Linear regression with Ignite ML (local).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.regression import LinearRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LinearRegressionTrainer()
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))

# Linear regression with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_regression
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import rmse_score
from ignite_ml.regression import LinearRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)
    
    trainer = LinearRegressionTrainer()
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))

# Decision Tree regression with Ignite ML (local).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.regression import DecisionTreeRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = DecisionTreeRegressionTrainer()
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))

# Decision Tree regression with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_regression
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import rmse_score
from ignite_ml.regression import DecisionTreeRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = DecisionTreeRegressionTrainer()
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))

# KNN regression with Ignite ML (local).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.regression import KNNRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = KNNRegressionTrainer()
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))

# KNN regression with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_regression
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import rmse_score
from ignite_ml.regression import KNNRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = KNNRegressionTrainer()
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))

# Random Forest regression with Ignite ML (local).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.regression import RandomForestRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = RandomForestRegressionTrainer(100)
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))

# Random Forest regression with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_regression
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import rmse_score
from ignite_ml.regression import RandomForestRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = RandomForestRegressionTrainer(100)
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))

# MLP regression with Ignite ML (local).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.regression import MLPArchitecture
from ignite_ml.regression import MLPRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = MLPRegressionTrainer(MLPArchitecture(100).with_layer(1, activator='linear'))
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))

# MLP regression with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_regression
from ignite_ml.core import Ignite
from ignite_ml.model_selection import train_test_split
from ignite_ml.metrics import rmse_score
from ignite_ml.regression import MLPArchitecture
from ignite_ml.regression import MLPRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = MLPRegressionTrainer(MLPArchitecture(100).with_layer(1, activator='linear'))
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))
