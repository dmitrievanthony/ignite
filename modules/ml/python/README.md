# Apache Ignite ML Python API

Apache Ignite ML Python API that allows to use Ignite ML from Python.

## Prerequisites

- Python 3.4 or above (3.6 is tested),
- Access to loca Apache Ignite node with started Py4J server. The server starts automatically if you specify `MLPlugin`
with enabled `withPython` property:

```xml
<property name="pluginConfigurations">
    <bean class="org.apache.ignite.ml.util.plugin.MLPluginConfiguration">
        <property name="withPython" value="#{true}" />
    </bean>
</property>
```

## Installation

#### *For end user*
If you only want to use the `ignite_ml` module in your project, do:
```
$ pip install ignite_ml
```

#### *For developer*
If you want to run tests, examples or build documentation, clone
the whole repository:
```
$ git clone git@github.com:apache/ignite.git
$ cd ignite/modules/ml/python
$ pip install -e .
```

This will install the repository version of `ignite_ml` into your environment
in so-called “develop” or “editable” mode. You may read more about
[editable installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)
in the `pip` manual.

Then run through the contents of `requirements` folder to install
the additional requirements into your working Python environment using
```
$ pip install -r requirements/<your task>.txt
```

You may also want to consult the `setuptools` manual about using `setup.py`.

## Documentation
[The package documentation](https://apache-ignite-binary-protocol-client.readthedocs.io)
is available at *RTD* for your convenience.

If you want to build the documentation from source, do the developer
installation as described above, then run the following commands:
```
$ cd ignite/modules/ml/python
$ pip install -r requirements/docs.txt
$ cd docs
$ make html
```

Then open `ignite/modules/ml/python/docs/generated/html/index.html`
in your browser.

## Examples
Some examples of using `ignite_ml` are provided in
`ignite/modules/ml/python/examples` folder.

This code implies that it is run in the environment with `ignite_ml` package
installed, and Apache Ignite node is running locally with `MLPlugin` and enabled `withPython` option.

## Testing
Run
```
$ cd ignite/modules/ml/python
$ python setup.py pytest
```

*NB!* All tests require Apache Ignite node running locally with `MLPlugin` and enabled `withPython` option.
