from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_encoded, X_categories = pd.factorize(X.values.reshape(1, -1)[0])
        return X_encoded
