# KMeans clustering with Ignite ML (local).
from sklearn.datasets import make_blobs
from ggml.clustering import KMeansClusteringTrainer

x, y = make_blobs(
    n_samples=2000, 
    n_features=2, 
    cluster_std=1.0, 
    centers=[(-3, -3), (0, 0), (3, 3)]
)

trainer = KMeansClusteringTrainer(amount_of_clusters=3)
model = trainer.fit(x)

# KMeans clustering with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_blobs
from ggml.core import Ignite
from ggml.clustering import KMeansClusteringTrainer

with Ignite("example-ignite.xml") as ignite:
    x, y = make_blobs(
        n_samples=2000, 
        n_features=2, 
        cluster_std=1.0, 
        centers=[(-3, -3), (0, 0), (3, 3)]
    )
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack((x, y))):
        cache.put(i, row)

    trainer = KMeansClusteringTrainer(amount_of_clusters=3)
    model = trainer.fit(x)

# GMM clustering with Ignite ML (local).
from sklearn.datasets import make_blobs
from ggml.clustering import GMMClusteringTrainer

x, y = make_blobs(
    n_samples=2000,
    n_features=2, 
    cluster_std=1.0, 
    centers=[(-3, -3), (0, 0), (3, 3)] 
)

trainer = GMMClusteringTrainer(
    count_of_components=3, 
    max_count_of_clusters=3
)
model = trainer.fit(x)

# GMM clustering with Ignite ML (cache).
import numpy as np
from sklearn.datasets import make_blobs
from ggml.core import Ignite
from ggml.clustering import GMMClusteringTrainer

with Ignite("example-ignite.xml") as ignite:
    x, y = make_blobs(
        n_samples=2000, 
        n_features=2, 
        cluster_std=1.0, 
        centers=[(-3, -3), (0, 0), (3, 3)]
    )
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack((x, y))):
        cache.put(i, row)

    trainer = GMMClusteringTrainer(
        count_of_components=3, 
        max_count_of_clusters=3
    )
    model = trainer.fit(x)
