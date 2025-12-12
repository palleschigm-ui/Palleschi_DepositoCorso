# =====================================================================
# ANALISI COMPLETA DEL DATASET "Cars Datasets 2025"
# - Pulizia tipi (stringhe -> numeri)
# - Gestione duplicati
# - Analisi valori mancanti
# - Cardinalità e coerenza categorie
# - Pulizia valuta e unità di misura
# - Gestione intervalli (range)
# - Standardizzazione nomi brand
# - Anomalie (Seats)
# - Feature engineering (price category, bang-for-buck, supercar, ecc.)
# - Normalizzazione
# - Matrice di correlazione, distribuzioni, pair plot (scatter pairwise)
# - Analisi per brand, confronto elettriche vs benzina
# - Identificazione "auto migliore" con score sintetico
# =====================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# ---------------------------------------------------------------------
# 0. CARICAMENTO DATASET E OSSERVAZIONE INIZIALE DEI TIPI
# ---------------------------------------------------------------------


# Alcuni file vengono salvati con encoding diverso da utf-8
df = pd.read_csv(
    r"C:\Users\Gianmario\Desktop\Python\Esercitazioni\Corso_GiGroup\Palleschi_DepositoCorso\Lezione_13\Cars Datasets 2025.csv",
    encoding="cp1252"
)

# Osserviamo le dimensioni originali e i tipi
print("=== DIMENSIONI ORIGINALI ===")
print(df.shape)

print("\n=== .INFO() ORIGINALE ===")
df.info()

# NOTA: Molte colonne risultano 'object' (stringhe), anche se alcune
# concettualmente sono numeriche (prezzo, cavalli, velocità, ecc.).
# Nei passi successivi convertiremo queste colonne in numeriche pulite.

# ---------------------------------------------------------------------
# 1. PULIZIA DI BASE DEL TESTO
# ---------------------------------------------------------------------

# Rimuoviamo spazi iniziali/finali in tutte le stringhe e sostituiamo
# stringhe vuote con NaN.
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].astype(str).str.strip()
    df[col] = df[col].replace({"": np.nan})

# Pulizia dei nomi colonna (rimozione spazi)
df.columns = [c.strip() for c in df.columns]

print("\n=== NOMI COLONNE DOPO PULIZIA ===")
print(df.columns.tolist())

# ---------------------------------------------------------------------
# 2. FUNZIONI AUSILIARIE PER LA PULIZIA NUMERICA
# ---------------------------------------------------------------------

def fix_weird_decimals(s: str) -> str:
    """
    Corregge casi come '5. 0 sec' -> '5.0 sec' o '10. 5' -> '10.5'.
    Utile per Performance(0 - 100) dove ci sono spazi dopo il punto.
    """
    if s is None or (isinstance(s, float) and np.isnan(s)):
        return s
    s = str(s)
    # pattern: numero . spazi numero -> numero.decimale
    s = re.sub(r'(\d+)\.\s+(\d)', r'\1.\2', s)
    return s


def parse_range_to_float(s):
    """
    Funzione generica per convertire:
      - valori singoli '963 hp', '$1,100,000', '3,982 cc', '3.2 sec'
      - intervalli '12,000-15,000', '70-85 hp', '100 - 140 Nm'
    in un float. Nel caso di intervallo, ritorna la media.
    """
    if pd.isna(s):
        return np.nan

    s = fix_weird_decimals(str(s))

    # Estraggo tutte le sottostringhe che sembrano numeri (con virgole/decimali)
    nums = re.findall(r'[\d,]+(?:\.\d+)?', s)
    if not nums:
        return np.nan

    vals = []
    for n in nums:
        try:
            v = float(n.replace(",", ""))  # rimuove separatori migliaia
            vals.append(v)
        except ValueError:
            continue

    if not vals:
        return np.nan

    # Se intervallo, prendo la media
    return float(np.mean(vals))


def parse_seats(s):
    """
    Converte la colonna 'Seats' in numero.
    Esempi:
      - '5'   -> 5
      - '2+2' -> massimo dei numeri trovati (4)
      - '2x15', '2–15' -> massimo dei numeri trovati (15)
    """
    if pd.isna(s):
        return np.nan
    s = str(s)
    nums = re.findall(r'\d+', s)
    if not nums:
        return np.nan
    vals = [int(n) for n in nums]
    return max(vals)


def extract_litres_from_engine(s):
    """
    Estrae la cilindrata in litri dalla colonna 'Engines'.
    Esempi:
      - '4.0L V8' -> 4.0
      - '1.2L Petrol' -> 1.2
      - 'I4 + ELECTRIC' -> NaN (nessun 'L' esplicito)
    """
    if pd.isna(s):
        return np.nan
    s = str(s)
    m = re.search(r'(\d+(?:\.\d+)?)\s*L', s, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return np.nan
    return np.nan


# ---------------------------------------------------------------------
# 3. CREAZIONE DI VARIABILI NUMERICHE PULITE
# ---------------------------------------------------------------------

df["price_usd"]     = df["Cars Prices"].apply(parse_range_to_float)
df["hp"]            = df["HorsePower"].apply(parse_range_to_float)
df["top_speed_kmh"] = df["Total Speed"].apply(parse_range_to_float)
df["accel_0_100_s"] = df["Performance(0 - 100 )KM/H"].apply(parse_range_to_float)
df["cc_or_kwh"]     = df["CC/Battery Capacity"].apply(parse_range_to_float)
df["torque_nm"]     = df["Torque"].apply(parse_range_to_float)
df["engine_litres"] = df["Engines"].apply(extract_litres_from_engine)
df["seats_num"]     = df["Seats"].apply(parse_seats)

numeric_cols_clean = [
    "price_usd", "hp", "top_speed_kmh", "accel_0_100_s",
    "cc_or_kwh", "torque_nm", "engine_litres", "seats_num"
]

df[numeric_cols_clean] = df[numeric_cols_clean].apply(
    pd.to_numeric, errors="coerce"
)

print("\n=== ANTEPRIMA VARIABILI NUMERICHE PULITE ===")
print(df[["Company Names", "Cars Names"] + numeric_cols_clean].head())

# ---------------------------------------------------------------------
# 4. STANDARDIZZAZIONE NOMI BRAND E FUEL TYPES
# ---------------------------------------------------------------------

df["Company Names"] = (
    df["Company Names"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

df["Fuel Types"] = df["Fuel Types"].str.strip()

fuel_standard_map = {
    "plug in hyrbrid": "Plug-in Hybrid",
    "Plug-in hybrid": "Plug-in Hybrid",
    "plug-in hybrid": "Plug-in Hybrid",
    "Hybrid (Petrol)": "Hybrid",
    "Petrol (Hybrid)": "Hybrid",
    "Hybrid (Gas + Electric)": "Hybrid",
    "Gas / Hybrid": "Hybrid",
    "Hybrid / Plug-in": "Plug-in Hybrid",
    "Petrol, Hybrid": "Hybrid",
    "Petrol/Hybrid": "Hybrid",
    "Hybrid/Electric": "Hybrid",
    "Diesel Hybrid": "Hybrid",
    "Petrol, Diesel": "Petrol/Diesel",
    "Diesel/Petrol": "Petrol/Diesel",
}

df["Fuel Types"] = df["Fuel Types"].replace(fuel_standard_map)

print("\n=== VALORI UNICI FUEL TYPES DOPO PULIZIA ===")
print(sorted(df["Fuel Types"].dropna().unique()))

# ---------------------------------------------------------------------
# 5. DUPLICATI E VALORI MANCANTI
# ---------------------------------------------------------------------

dup_count = df.duplicated().sum()
print(f"\n=== RIGHE DUPLICATE TROVATE: {dup_count} ===")

if dup_count > 0:
    dup_rows = df[df.duplicated(keep=False)].sort_values(df.columns.tolist())
    print("\nEsempi di righe duplicate:")
    print(dup_rows.head())

df = df.drop_duplicates()
print("Dimensioni dopo rimozione duplicati:", df.shape)

missing = df.isna().sum()
missing_pct = (missing / len(df)) * 100
missing_table = pd.DataFrame({
    "missing_count": missing,
    "missing_pct": missing_pct
}).sort_values("missing_pct", ascending=False)

print("\n=== VALORI MANCANTI (DOPO PULIZIA) ===")
print(missing_table)

# ---------------------------------------------------------------------
# 6. CARDINALITÀ E ANALISI DI BASE PER BRAND
# ---------------------------------------------------------------------

num_brands = df["Company Names"].nunique()
num_models = df["Cars Names"].nunique()

print(f"\nNumero di brand diversi: {num_brands}")
print(f"Numero di modelli unici: {num_models}")

brand_counts = df["Company Names"].value_counts()
print("\n=== TOP 10 BRAND PER NUMERO DI MODELLI ===")
print(brand_counts.head(10))

brand_price_stats = df.groupby("Company Names")["price_usd"].agg(
    avg_price="mean",
    price_var="var",
    count="count"
).sort_values("avg_price", ascending=False)

print("\n=== PREZZO MEDIO E VARIANZA PER BRAND (prime 15 righe) ===")
print(brand_price_stats.head(15))

# ---------------------------------------------------------------------
# 7. ANOMALIE SEATS
# ---------------------------------------------------------------------

seats_anomalies = df[(df["seats_num"] <= 0) | (df["seats_num"] > 20)]
print("\n=== ANOMALIE NELLA COLONNA SEATS (LOGICHE) ===")
print(seats_anomalies[["Company Names", "Cars Names", "Seats", "seats_num"]])

# ---------------------------------------------------------------------
# 8. FEATURE ENGINEERING PREZZO E PRESTAZIONI
# ---------------------------------------------------------------------

price_q1 = df["price_usd"].quantile(0.25)
price_q3 = df["price_usd"].quantile(0.75)

def categorize_price(p):
    if pd.isna(p):
        return np.nan
    if p <= price_q1:
        return "Economy"
    elif p <= price_q3:
        return "Premium"
    else:
        return "Luxury"

df["Price_Category"] = df["price_usd"].apply(categorize_price)

print("\n=== DISTRIBUZIONE PRICE_CATEGORY ===")
print(df["Price_Category"].value_counts(dropna=False))

df["bang_for_buck"]   = df["hp"] / df["price_usd"]
df["hp_per_litre"]    = df["hp"] / df["engine_litres"]
df["torque_per_litre"] = df["torque_nm"] / df["engine_litres"]
df["performance_index"] = df["top_speed_kmh"] / df["accel_0_100_s"]

# ---------------------------------------------------------------------
# 9. FLAG ELETTRICHE E SUPERCAR
# ---------------------------------------------------------------------

def is_electric_row(row):
    fuel = str(row["Fuel Types"]).lower()
    cc = str(row["CC/Battery Capacity"]).lower()
    if "electric" in fuel or "ev" in fuel:
        return True
    if "kwh" in cc:
        return True
    return False

df["is_electric"] = df.apply(is_electric_row, axis=1)
df["is_supercar"] = df["accel_0_100_s"].apply(
    lambda x: True if not pd.isna(x) and x < 3.5 else False
)

print("\nNumero di supercar (0-100 < 3.5s):", df["is_supercar"].sum())

# ---------------------------------------------------------------------
# 10. STATISTICHE DESCRITTIVE NUMERICHE
# ---------------------------------------------------------------------

numeric_all = numeric_cols_clean + [
    "bang_for_buck", "hp_per_litre", "torque_per_litre", "performance_index"
]

print("\n=== STATISTICHE DESCRITTIVE VARIABILI NUMERICHE ===")
print(df[numeric_all].describe().T)

# ---------------------------------------------------------------------
# 11. OUTLIER (IQR)
# ---------------------------------------------------------------------

def iqr_outlier_mask(series: pd.Series):
    """Ritorna mask di outlier e limiti (lower, upper) secondo IQR."""
    s = series.dropna()
    if s.empty:
        return pd.Series(False, index=series.index), np.nan, np.nan
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (series < lower) | (series > upper)
    return mask, lower, upper

cols_for_outliers = ["price_usd", "hp", "top_speed_kmh", "accel_0_100_s"]

print("\n=== OUTLIER (IQR) PER VARIABILI CHIAVE ===")
for col in cols_for_outliers:
    mask, lower, upper = iqr_outlier_mask(df[col])
    out_count = mask.sum()
    print(f"{col}: outlier = {out_count}, limiti [{lower:.2f}, {upper:.2f}]")

# ---------------------------------------------------------------------
# 12. NORMALIZZAZIONE HP E TORQUE (CREA SEMPRE hp_norm E torque_norm)
# ---------------------------------------------------------------------

# Normalizzazione min-max (0-1) per hp e torque_nm
for col in ["hp", "torque_nm"]:
    col_norm = col + "_norm"
    col_data = df[col].astype(float)
    if col_data.notna().sum() > 0:
        min_v = col_data.min()
        max_v = col_data.max()
        if max_v == min_v:
            # tutti i valori uguali → li mettiamo al centro (0.5)
            df[col_norm] = 0.5
        else:
            df[col_norm] = (col_data - min_v) / (max_v - min_v)
    else:
        # la colonna normalizzata viene comunque creata
        df[col_norm] = np.nan

# Stampa di controllo robusta
cols_to_show = [c for c in ["hp", "torque_nm", "hp_norm", "torque_norm"] if c in df.columns]

print("\n=== ANTEPRIMA NORMALIZZAZIONE HP E TORQUE ===")
print(df[cols_to_show].head())

# ---------------------------------------------------------------------
# 13. MATRICE DI CORRELAZIONE
# ---------------------------------------------------------------------

# numeric_all è stato definito prima come:
# numeric_all = numeric_cols_clean + ["bang_for_buck", "hp_per_litre",
#                                    "torque_per_litre", "performance_index"]

# Costruiamo corr_cols solo con le colonne che ESISTONO davvero
corr_cols = [c for c in (numeric_all + ["hp_norm", "torque_norm"]) if c in df.columns]

print("\nUseremo queste colonne per la matrice di correlazione:")
print(corr_cols)

corr = df[corr_cols].corr()

print("\n=== MATRICE DI CORRELAZIONE ===")
print(corr)

plt.figure(figsize=(10, 8))
plt.imshow(corr, interpolation="nearest")
plt.xticks(range(len(corr_cols)), corr_cols, rotation=90)
plt.yticks(range(len(corr_cols)), corr_cols)
plt.title("Matrice di correlazione (variabili numeriche)")
plt.colorbar()
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------
# 14. ANALISI PER BRAND E FUEL TYPE
# ---------------------------------------------------------------------

print("\n=== BRAND CON MAGGIOR VARIANZA DI PREZZO ===")
print(brand_price_stats.sort_values("price_var", ascending=False).head(10))

fuel_perf = df.groupby("Fuel Types")[["accel_0_100_s", "top_speed_kmh", "hp"]].mean()
print("\n=== PRESTAZIONI MEDIE PER FUEL TYPE ===")
print(fuel_perf)

if "Electric" in fuel_perf.index and "Petrol" in fuel_perf.index:
    print("\nConfronto (media accel_0_100_s):")
    print("Electric:", fuel_perf.loc["Electric", "accel_0_100_s"])
    print("Petrol :", fuel_perf.loc["Petrol", "accel_0_100_s"])

# ---------------------------------------------------------------------
# 15. DISTRIBUZIONE DEI PREZZI
# ---------------------------------------------------------------------

plt.figure()
df["price_usd"].dropna().hist(bins=40)
plt.xlabel("Price (USD)")
plt.ylabel("Frequenza")
plt.title("Distribuzione del prezzo")
plt.tight_layout()
plt.show()

price_skew = df["price_usd"].skew()
print(f"\nSkewness della distribuzione del prezzo: {price_skew:.3f}")

# ---------------------------------------------------------------------
# 16. PAIR PLOT (SCATTER PAIRWISE)
# ---------------------------------------------------------------------

pair_cols = ["price_usd", "hp", "top_speed_kmh", "accel_0_100_s", "torque_nm"]

print("\n=== SCATTER PLOT COPPIE DI VARIABILI (PAIRWISE) ===")
for i in range(len(pair_cols)):
    for j in range(i + 1, len(pair_cols)):
        x_col = pair_cols[i]
        y_col = pair_cols[j]
        sub = df[[x_col, y_col]].dropna()
        if sub.empty:
            continue
        plt.figure()
        plt.scatter(sub[x_col], sub[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"{y_col} vs {x_col}")
        plt.tight_layout()
        plt.show()

# ---------------------------------------------------------------------
# 17. SCORE SINTETICO PER "AUTO MIGLIORE"
# ---------------------------------------------------------------------

def min_max_norm(series: pd.Series):
    s = series.astype(float)
    s_non_null = s.dropna()
    if s_non_null.empty:
        return pd.Series(np.nan, index=series.index)
    min_v = s_non_null.min()
    max_v = s_non_null.max()
    if max_v == min_v:
        return pd.Series(0.5, index=series.index)
    return (s - min_v) / (max_v - min_v)

df["price_norm"] = min_max_norm(df["price_usd"])
df["speed_norm"] = min_max_norm(df["top_speed_kmh"])
df["accel_norm"] = min_max_norm(df["accel_0_100_s"])

df["car_score"] = (
    (1 - df["price_norm"]) * 0.4 +
    df["speed_norm"] * 0.3 +
    (1 - df["accel_norm"]) * 0.3
)

best_cars = df.sort_values("car_score", ascending=False)[
    [
        "Company Names",
        "Cars Names",
        "price_usd",
        "top_speed_kmh",
        "accel_0_100_s",
        "car_score",
        "bang_for_buck",
        "is_supercar",
        "Fuel Types"
    ]
].head(20)

print("\n=== TOP 20 AUTO PER SCORE SINTETICO ===")
print(best_cars.to_string(index=False))

# =====================================================================
# FINE SCRIPT
# =====================================================================

print("============================================================ FINE =================================================================")