# Distributed inference using Ignite ML.
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from ignite_ml.core import Ignite
from ignite_ml.inference import IgniteDistributedModel
from ignite_ml.classification import DecisionTreeClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = DecisionTreeClassificationTrainer()
model = trainer.fit(x_train, y_train)

with Ignite("example-ignite.xml") as ignite:
    with IgniteDistributedModel(ignite, model) as ignite_distr_mdl:
        print(accuracy_score(
            y_test, 
            ignite_distr_mdl.predict(x_test)
        ))

# Model storage using Ignite ML (local).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.core import Ignite
from ignite_ml.regression import LinearRegressionTrainer
from ignite_ml.storage import save_model
from ignite_ml.storage import read_model

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LinearRegressionTrainer()
model = trainer.fit(x_train, y_train)

with Ignite("example-ignite.xml") as ignite:
    save_model(model, 'test.mdl', ignite)
    model = read_model('test.mdl', ignite)

r2_score(y_test, model.predict(x_test))

# Model storage using Ignite ML (cache).
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ignite_ml.core import Ignite
from ignite_ml.regression import LinearRegressionTrainer
from ignite_ml.storage import save_model
from ignite_ml.storage import read_model

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LinearRegressionTrainer()
model = trainer.fit(x_train, y_train)

with Ignite("example-ignite-ml.xml") as ignite:
    save_model(model, 'igfs:///test.mdl', ignite)
    model = read_model('igfs:///test.mdl', ignite)

r2_score(y_test, model.predict(x_test))
