import tensorflow as tf
import pandas as pd

model = new_model = tf.keras.models.load_model(
    "../StripTheText-Backend-2.0/models/classifier/classification_rnn_2.0_TESTING")

test_data = """
We propose and implement an interpretable machine learning classification model for Explainable AI (XAI) based on expressive Boolean formulas.
Potential applications include credit scoring and diagnosis of medical conditions. The Boolean formula defines a rule with tunable complexity (or interpretability),
according to which input data are classified. Such a formula can include any operator that can be applied to one or more Boolean variables, thus providing higher expressivity
compared to more rigid rule-based and tree-based approaches. The classifier is trained using native local optimization techniques, efficiently searching the space of feasible formulas.
Shallow rules can be determined by fast Integer Linear Programming (ILP) or Quadratic Unconstrained Binary Optimization (QUBO) solvers, potentially powered by special purpose hardware or quantum devices.
"""
print(model.summary())

pred = model.predict(pd.DataFrame([test_data]))

print(pred)
print(pred.argmax(axis=1))
