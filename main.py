import xgboost
import pandas as pd
from process_of_all_data import create_data_set

csv_file = pd.read_csv("test.csv")
create_data_set(csv_file,"test_dataset")

dataR = pd.read_excel("test_dataset.xlsx")
X_test = []
for i in range(len(dataR['Частота'])):
    X_test.append([dataR['Частота'][i], dataR['Амплитуда'][i], dataR['Смещение'][i], dataR['Повторение'][i]])

model2 = xgboost.XGBClassifier()
model2.load_model("trained_model.txt")

y_pred = model2.predict(X_test)

columns = { 'Class': y_pred}

df = pd.DataFrame(columns)

df.rename_axis('id', inplace=True)

df.to_csv('алгоритмы.csv')

print("Model is tested")