# 데이터 분석 및 시각화

# 1차원 Series / 2차원 DataFrame
# [] 리스트 구조 / 데이터 분석에 용이하게 만든 라이브러리

import pandas as pd

# Series 변환
temp = pd.Series([-20,-10,10,20])
print(temp)
# print(type(temp))
# print(type(1))
# print(type([1,2,3,4,5]))
print(temp[0])

# index 추가
temp = pd.Series([-20,-10,10,20], index = ['Jan', 'Feb', 'March', 'Apr'])
print(temp)
