import pandas as pd

# Series
# temp = pd.Series([-20,-10,10,20], index=['Jan', 'Feb', 'March', 'Apr'])
# print(temp)
# print(temp[['Jan', 'Feb']])

# DataFrame
data = {
    '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '송근열'],
    '학교' : ['신림고', '신림고', '신림고', '신림고', '신림고', '디지털고', '디지털고', '디지털고'],
    '신장' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

# df = pd.DataFrame(data)
# print(df)
# df = pd.DataFrame(data, index = ['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])


# df = pd.DataFrame(data)
# df.set_index('이름', inplace=True)
# print(df)


# df = pd.DataFrame(data, index = ['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
# df.index.rename("지원번호", inplace=True)
# print(df)


# df = pd.DataFrame(data, index = ['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
# df.index.rename("지원번호", inplace=True)
# df.reset_index()
# print(df.reset_index())
# df.reset_index(drop=True, inplace=True)
# print(df.reset_index(drop=True, inplace=True))


# sort index 인덱스 정렬
df = pd.DataFrame(data)
df.set_index('이름', inplace=True)
df.sort_index(inplace=True, ascending=False)
print(df)
