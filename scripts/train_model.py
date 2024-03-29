from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
 
df = pd.read_csv('/home/diza/airflow_plus_mlflow_pipeline/datasets/data_train.csv', header=None)
df.columns = ['id', 'counts']
 
model = LinearRegression()
model.fit(df['id'].values.reshape(-1,1), df['counts'])
 
with open('/home/diza/airflow_plus_mlflow_pipeline/models/data.pickle', 'wb') as f:
    pickle.dump(model, f)
 


