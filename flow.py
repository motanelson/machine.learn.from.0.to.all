print("\033c\033[43;30m\narray?")
import tensorflow as tf
import numpy as np

# 1️⃣ Criar dados
x_train = np.array([n for n in range(20)], dtype=float)
y_train = np.array([n * 4 for n in range(20)], dtype=float)

# Normalizar
x_train_n = x_train / np.max(x_train)
y_train_n = y_train / np.max(y_train)

# 2️⃣ Modelo
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

# 3️⃣ Compilar
model.compile(optimizer='adam', loss='mean_squared_error')

# 4️⃣ Treinar
print("\nTreinando modelo...")
model.fit(x_train_n, y_train_n, epochs=1000, verbose=0)

# 5️⃣ Testar
test_value = 10.0
prediction = model.predict(np.array([[test_value / np.max(x_train)]]))
prediction_real = prediction[0][0] * np.max(y_train)
print(f"\nPredição para x={test_value}: y≈{prediction_real:.2f}")

# 6️⃣ Mostrar pesos
weights = model.layers[0].get_weights()
print(f"Peso aprendido: {weights[0][0][0]:.4f}, viés: {weights[1][0]:.4f}")
