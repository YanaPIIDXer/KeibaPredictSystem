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

# 「阪神芝1200」のようなコースを表すカテゴリ変数を生成
df['Course'] = df['Place'] + df['CourseType'] + df['Distance'].astype(str)

# 欠損値を処理
df.dropna(inplace=True)

# 型を成形
feature_columns = ['Jockey', 'Condition', 'Course']
df[feature_columns] = df[feature_columns].astype('category')
df['Popular'] = df['Popular'].astype(np.int32)

# 件数を絞る
df = df[(df['Date'] >= '2022/01/01') & (df['Date'] <= '2023/12/31')]
