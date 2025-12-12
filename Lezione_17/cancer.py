from sklearn.datasets import load_breast_cancer
import pandas as pd

# Carica il dataset
data = load_breast_cancer()

# X = features, y = target
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)
