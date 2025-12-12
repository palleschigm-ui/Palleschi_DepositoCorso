import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.metrics import r2_score, mean_squared_error

# ==============================
# 1. Caricamento dati
# ==============================

df = pd.read_csv("california_housing_data.csv")
print("Osservazioni iniziali:", len(df))

# ==============================
# 2. Pulizia valori impossibili
# ==============================

cond = (
    (df["MedInc"] > 0) &
    (df["HouseAge"] >= 0) &
    (df["AveRooms"] > 0) &
    (df["AveBedrms"] > 0) &
    (df["Population"] > 0) &
    (df["AveOccup"] > 0) &
    (df["MedHouseVal"] > 0)
)

df = df[cond].copy()
df = df.dropna()

print("Dopo rimozione valori impossibili:", len(df))

# ==============================
# 3. Feature engineering
# ==============================

df["BedroomsPerRoom"] = df["AveBedrms"] / df["AveRooms"]
df["PersonsPerRoom"] = df["AveOccup"] / df["AveRooms"]
df["MedInc_sq"] = df["MedInc"] ** 2
df["DistToCoast"] = (df["Longitude"] + 120).abs()

# ==============================
# 4. Rimozione outliers 20–80%
# ==============================

cols_to_clean = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "BedroomsPerRoom",
    "PersonsPerRoom",
    "MedHouseVal"
]

for col in cols_to_clean:
    p20 = df[col].quantile(0.20)
    p80 = df[col].quantile(0.80)
    df = df[(df[col] >= p20) & (df[col] <= p80)]

print("Dopo rimozione outliers 20–80%:", len(df))

# ==============================
# 5. Train-test split
# ==============================

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

print("Train size:", len(train_df))
print("Test size:", len(test_df))

# ==============================
# 6. Definizione X e y (senza log!)
# ==============================

y_train = train_df["MedHouseVal"].values
y_test = test_df["MedHouseVal"].values

X_train = train_df.drop(columns=["MedHouseVal"])
X_test = test_df.drop(columns=["MedHouseVal"])

feature_names = X_train.columns.to_numpy()

X_train = X_train.values
X_test = X_test.values

# ==============================
# 7. Standardizzazione
# ==============================

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==============================
# 8. Ridge Regression
# ==============================

alphas_ridge = np.logspace(-3, 3, 13)
ridge = RidgeCV(alphas=alphas_ridge, cv=5)
ridge.fit(X_train_scaled, y_train)

y_pred_ridge = ridge.predict(X_test_scaled)

ridge_r2 = r2_score(y_test, y_pred_ridge)
ridge_mse = mean_squared_error(y_test, y_pred_ridge)
ridge_rmse = np.sqrt(ridge_mse)

print("\n===== RISULTATI RIDGE =====")
print("Alpha scelto:", ridge.alpha_)
print("R2 test:", round(ridge_r2, 4))
print("MSE test:", round(ridge_mse, 2))
print("RMSE test:", round(ridge_rmse, 2))

# ==============================
# 9. Lasso Regression
# ==============================

alphas_lasso = np.logspace(-3, 1, 50)
lasso = LassoCV(alphas=alphas_lasso, cv=5, max_iter=10000, random_state=42)
lasso.fit(X_train_scaled, y_train)

y_pred_lasso = lasso.predict(X_test_scaled)

lasso_r2 = r2_score(y_test, y_pred_lasso)
lasso_mse = mean_squared_error(y_test, y_pred_lasso)
lasso_rmse = np.sqrt(lasso_mse)

print("\n===== RISULTATI LASSO =====")
print("Alpha scelto:", lasso.alpha_)
print("R2 test:", round(lasso_r2, 4))
print("MSE test:", round(lasso_mse, 2))
print("RMSE test:", round(lasso_rmse, 2))

print("\nVariabili eliminate dal Lasso:")
coef_zero = feature_names[lasso.coef_ == 0]
print(coef_zero)

