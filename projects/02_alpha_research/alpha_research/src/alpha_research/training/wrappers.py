from __future__ import annotations
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier


class RegimeSpecialistHGB:
    """Stable wrapper kept in module namespace for pickle compatibility.

    The current implementation is intentionally simple but accepts standard HGB
    hyperparameters so randomized search can tune it without storing classes as
    __main__.
    """
    def __init__(self, random_state=42, max_iter=200, learning_rate=0.05,
                 max_leaf_nodes=31, l2_regularization=0.05, min_samples_leaf=20, **kwargs):
        self.random_state = random_state
        self.params = dict(
            max_iter=max_iter,
            learning_rate=learning_rate,
            max_leaf_nodes=max_leaf_nodes,
            l2_regularization=l2_regularization,
            min_samples_leaf=min_samples_leaf,
            random_state=random_state,
        )
        self.params.update(kwargs)
        self.model = HistGradientBoostingClassifier(**self.params)

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def predict(self, X):
        return self.model.predict(X)


class RankHGB(RegimeSpecialistHGB):
    """Ranking-oriented HGB wrapper.

    For now it is a calibrated binary classifier wrapper. Its behavior differs at
    the pipeline level: evaluation uses precision@k/daily top-k rather than a
    fixed 0.5 threshold.
    """
    pass
