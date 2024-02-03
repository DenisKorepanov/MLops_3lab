from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
 
df = pd.read_csv('/home/mike/airflow_plus_mlflow_pipeline/datasets/data_test.csv', header=None)
df.columns = ['id', 'counts']
 
model = LinearRegression()
with open('/home/mike/airflow_plus_mlflow_pipeline/models/data.pickle', 'rb') as f:
    model = pickle.load(f)
 
score = model.score(df['id'].values.reshape(-1,1), df['counts'])
print("score=", score)
 

