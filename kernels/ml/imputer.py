import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class NanImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.fillna('not defined')
