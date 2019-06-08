import pandas

"""df = pandas.read_csv("ZILLOW-Z77006_MLPAH.csv")
print(df.head())
df.set_index('Date', inplace=True)
print(df.head())
df.to_csv("newcsv2.csv")"""

"""df = pandas.read_csv("newcsv2.csv")
#print(df.head())
df = pandas.read_csv("newcsv2.csv", index_col=0)
#print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv("newcsv3.csv")
# # for removing headers
df.to_csv("newcsv4.csv", header=False)"""
# # reading from the same csv file and adding column names with index
df = pandas.read_csv("newcsv4.csv", names=['Date', 'Austin_HPI'], index_col=0)
# # print(df.head())

df.to_html("test.html")

df.rename(columns={'Austin_HPI': '77006_HPI'}, inplace=True)
print(df.head())
