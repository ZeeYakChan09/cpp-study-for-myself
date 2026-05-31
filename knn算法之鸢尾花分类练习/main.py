#鸢尾花的训练
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV #数据集划分
from sklearn.neighbors import KNeighborsClassifier #knn算法分类
import joblib
#1.加载数据集
data = load_iris()
print(data)

features = data.data    #得到特征
target = data.target    #得到标签


print(type(data))

#2.数据集进行划分
#x_train 训练集的特征
#y_train 训练集的标签
#x_test 测试集的特征
#y_test 测试集的标签
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.3,shuffle = True)

print(x_test)
print(y_test)

#3.定义knn算法的实例
knn = KNeighborsClassifier(n_neighbors=9)


#4.训练
# knn.fit(x_train, y_train)
#
# #5.评估
# score = knn.score(x_test, y_test)
# print(score)

#保存模型
# joblib.dump(value=knn, filename='knniris.model')

#k:[3,5,7,9,11,13]
#weights:['uniform','distance']
#p:[1,2,3,4,5]

# #方法一
# best_score = 0
# best_k = 0
# for k in range(3,14,2):
#     for w in ['uniform','distance']:
#         for p in range(1,6):
#             knn = KNeighborsClassifier(n_neighbors=k,weights=w,p=p)
#             knn.fit(x_train,y_train)
#             score = knn.score(x_test,y_test)
#             if score > best_score:
#                 best_score = score
#                 best_k = k
#                 best_w = w
#                 best_p = p
#
# print(best_k)
# print(best_w)
# print(best_p)
# print(best_score)

#方法二 超参调参-网格搜索
knn = KNeighborsClassifier()
param_grid = [{'weights': ['uniform', 'distance'],
               'n_neighbors': [i for i in range(1, 14, 2)],
               'p': [p for p in range(1, 6)]}]
knncv = GridSearchCV(knn, param_grid=param_grid)
knncv.fit(x_train, y_train)
print(knncv.best_estimator_)
print(knncv.best_score_)
print(knncv.best_params_)

