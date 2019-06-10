import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100, 8), index=dates, columns=list('ABCDEFGH'))
print(df.head())
sns.set()
sns.relplot(x='A', y='B', data=df)
plt.show()
plt.plot(x=df['A'], y=df['B'], marker='.', linestyle='none')
plt.show()
