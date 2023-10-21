import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('./datasets/origin.csv')

# レースID・日付
df['RaceID'] = df['Place'] + df['Year'].astype(str) + df['Month'].astype(str) + df['Day'].astype(str) + df['RaceNo'].astype(str)
df['Date'] = pd.to_datetime('20' + df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-' + df['Day'].astype(str))
cols = ['RaceID', 'Date'] + [col for col in df if col != 'RaceID' and col != 'Date']
df = df[cols]
df.drop(['Year', 'Month', 'Day'], axis=1, inplace=True)

# レース情報テーブルを生成
race_df = df[['RaceID', 'Date', 'RaceNo', 'Place', 'CourseType', 'Distance', 'Condition']].drop_duplicates().reset_index(drop=True)

# レース情報として切り出した情報を撤去
df.drop(['RaceNo', 'Place', 'CourseType', 'Distance', 'Condition'], axis=1, inplace=True)

# 欠損値を処理
df.fillna(999.9, inplace=True)

# 型を成形
df['Popular'] = df['Popular'].astype(np.int32)

# pickleファイルに保存
with open('./pickles/races.pickle', 'wb') as f:
  pickle.dump(race_df, f)
  
with open('./pickles/results.pickle', 'wb') as f:
  pickle.dump(df, f)
