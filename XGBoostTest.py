import xgboost
import pandas as pd

dataR = pd.read_excel("training_dataset.xlsx")
X_train = []
y_train = []
for i in range(len(dataR['Оценка'])):
    X_train.append([dataR['Частота'][i], dataR['Амплитуда'][i], dataR['Смещение'][i], dataR['Повторение'][i]])
    y_train.append(dataR['Оценка'][i])

model = xgboost.XGBClassifier(
 learning_rate =0.0998,
 n_estimators=300,
 max_delta_step = 0.005,
 max_depth=5,
 min_child_weight=1,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 objective= 'binary:logistic')

model.fit(X_train, y_train)
model.save_model("trained_model.txt")

print("Model is trained and saved")





