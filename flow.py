print("\033c\033[43;30m\narray?")

import tensorflow as tf
import numpy as np

# 1️⃣ Dados de treino
x_train = np.array([n for n in range(20)], dtype=float)
y_train = np.array([n * 4 for n in range(20)], dtype=float)

print("Entradas (x):", x_train)
print("Saídas (y):", y_train)

# 2️⃣ Modelo simples
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# 3️⃣ Compilar
model.compile(optimizer='adam', loss='mean_squared_error')

# 4️⃣ Treinar
print("\nTreinando modelo...")
model.fit(x_train, y_train, epochs=300, verbose=0)

# 5️⃣ Testar
print("\nTreino completo!")
test_value = 10.0
prediction = model.predict(np.array([[test_value]]))
print(f"Predição para x={test_value}: y≈{prediction[0][0]:.2f}")

# 6️⃣ Mostrar pesos
weights = model.layers[0].get_weights()
print(f"\nPeso aprendido: {weights[0][0][0]:.4f}, viés: {weights[1][0]:.4f}")
