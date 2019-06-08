import quandl
import pandas

api_key = open('quandl_api_key.txt', 'r').read()
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print((df.head()))

fiddy_states = pandas.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# # this is a list
# print(fiddy_states)
# # this is a dataframe
# print(fiddy_states[0])
# # this is a column
print(fiddy_states[0][1])

for abbv in fiddy_states[0][1][1:]:
    print("FMAC/HPI_" + str(abbv))
