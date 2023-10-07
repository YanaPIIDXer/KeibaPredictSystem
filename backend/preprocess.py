import pandas as pd
import numpy as np

df = pd.read_csv('./datasets/origin.csv')

# 日付
df['Date'] = '20' + df['Year'].astype(str) + '-' + df['Month'].astype(str).apply(lambda x: x.zfill(2)) + '-' + df['Day'].astype(str).apply(lambda x: x.zfill(2))
# レースIDを付与
df['RaceID'] = df['Place'] + df['Year'].astype(str) + df['Month'].astype(str) + df['Day'].astype(str) + df['RaceNo'].astype(str)

# 「阪神ダート1400」などのコース名を生成
df['Course'] = df['Place'] + df['CourseType'] + df['Distance'].astype(str)
df.drop(columns=['Place', 'CourseType'], axis=1, inplace=True)

# 欠損値の処理
# 競争除外・競争中止
df = df[df['Arrival'] != 0]

# 型を変更
df['Popular'] = df['Popular'].astype(np.int32)
df['ArrivalDiff'] = df['ArrivalDiff'].astype(np.float32)
categorical_features = ['Condition', 'Sex', 'Jockey', 'Course']
df[categorical_features] = df[categorical_features].astype('category')

print(df.head())
