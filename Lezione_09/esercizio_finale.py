import numpy as np

# Array di interi da 0 a 49
base_numbers = np.arange(0, 50)

# 50 numeri casuali tra 49 e 101
random_numbers = np.random.randint(49, 102, 50)

# Concatenazione dei due array
merged_array = np.concatenate((base_numbers, random_numbers))

print("Array unito:", merged_array)
print("Tipo:", merged_array.dtype)
print("Shape:", merged_array.shape)

# Conversione a float
merged_float = merged_array.astype(float)

print("Tipo dopo conversione:", merged_float.dtype)
print("Shape dopo conversione:", merged_float.shape)

# --- Slicing ---

print("Primi 10 elementi:", merged_float[:10])
print("Ultimi 7 elementi:", merged_float[-7:])
print("Elementi da 5 a 9:", merged_float[5:10])
print("Un elemento ogni 4 posizioni:", merged_float[::4])

# Modifica elementi tra posizione 10 e 14
merged_float[10:15] = 99

print("Array modificato:", merged_float)

# Indicizzazione con lista
selected_indices = [0, 3, 7, 12, 25, 33, 48]
print("Elementi selezionati:", merged_float[selected_indices])

# Maschera booleana per pari
even_values = merged_float[merged_float % 2 == 0]
print("Elementi pari:", even_values)

# Maschera booleana per valori > media
average_value = np.mean(merged_float)
print("Media:", average_value)
print("Valori superiori alla media:", merged_float[merged_float > average_value])

