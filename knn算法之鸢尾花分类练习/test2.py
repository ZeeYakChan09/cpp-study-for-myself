import joblib
import numpy as np
#加载模型
knn=joblib.load(filename='knniris.model')
#制作测试数据集
x_test = np.array([4.6 ,3.2 ,1.4 ,0.2]).reshape(1, -1)
knn.predict(x_test)
#预测
y_pred = knn.predict(x_test)
print(y_pred)
