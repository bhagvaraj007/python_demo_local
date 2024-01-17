import pandas as pd

# PEP 8
hello = [1, 2, 3, 4, 5, 6]
dict_lists = {"name":["Ajitesh", "Shailesh", "Seema", "Nidhi"],
               "weight":[84, 79, 67, 52],
               "height":[183, 186, 158, 155],
               "smoke_or_not":["no", "yes", "no", "no"]}

# df = pd.DataFrame(dict_lists)
# for i, r in df.iterrows():
#     print(i, r)

for i in hello:
    print(i)

for k, v in dict_lists.items():
    print(k, v)

for k in dict_lists.keys():
    print(dict_lists[k])


# r = open('text.txt', "r")
# print(r.read())

# r = open('test.csv', "r")
# print(r.read())

df = pd.read_csv('test.csv')
df = df.dropna(axis=0, how='all')
df1 = df[['Date', 'PAYEMS', 'JTSJOL']]
# df = df.fillna()
print(df)
