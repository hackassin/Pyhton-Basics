import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

sales_data = pd.read_csv(
    r"C:\Users\amlan\Documents\Git Repos\Machine Learning\Python-Basics\Machine Learning\DataQuest\WA_Fn-UseC_-Sales-Win-Loss.csv")
# print(sales_data.head())
# print(sales_data.dtypes)
# set the background colour of the plot to white
# sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
# sns.set(rc={'figure.figsize': (11.7,8.27)})
# create a countplot
"""sns.countplot('Route To Market', data=sales_data, hue='Opportunity Result')
plt.show()
sns.set(rc={'figure.figsize': (16.7,14.27)})
sns.violinplot(x="Opportunity Result", y="Client Size By Revenue", hue="Opportunity Result", data = sales_data)
plt.show()"""
# plt.plot(sales_data['Opportunity Result'],sales_data['Client Size By Revenue'],marker='.',linestyle='none')
# plt.show()
# create the Labelencoder object
le = preprocessing.LabelEncoder()
# convert the categorical columns into numeric
encoded_value = le.fit_transform(["paris", "paris", "tokyo", "amsterdam"])
print(encoded_value)
sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])

cols = [col for col in sales_data.columns if col not in ['Opportunity Number', 'Opportunity Result']]
data = sales_data[cols]
target = sales_data['Opportunity Result']
"""The fourth argument ‘random_state’ just ensures that we get reproducible results every time"""
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.30, random_state=10)
# create an object of the type GaussianNB
gnb = GaussianNB()
# train the algorithm on training data and predict using the testing data
pred_gnb = gnb.fit(data_train, target_train).predict(data_test)
print(pred_gnb)
print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred_gnb, normalize=True))

svc_model = LinearSVC(random_state=0)
pred_svc = svc_model.fit(data_train, target_train).predict(data_test)
print("LinearSVC accuracy : ", accuracy_score(target_test, pred_svc, normalize=True))

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data_train, target_train)
pred = neigh.predict(data_test)
print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))

k_list = [svc_model, gnb, neigh]
from yellowbrick.classifier import ClassificationReport

# Instantiate the classification model and visualizer
visualizer = ClassificationReport(svc_model, classes=['Won', 'Loss'])
visualizer.fit(data_train, target_train)  # Fit the training data to the visualizer
visualizer.score(data_test, target_test)  # Evaluate the model on the test data
g = visualizer.poof()  # Draw/show/poof the data
