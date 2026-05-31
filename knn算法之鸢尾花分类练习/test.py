import numpy as np
import joblib

model = joblib.load('knniris.model')
x_test = np.array([6.1 ,2.6 ,5.6 ,1.4]).reshape(1, -1)
y_pred = model.predict([4.6 ,3.2 ,1.4 ,0.2])
print(y_pred)
