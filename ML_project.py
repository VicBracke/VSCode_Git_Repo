### option 1

# import pandas as pd

# # Load the dataset from UCI repository
# url = "http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
# column_names = ["ID", "thickness", "cell_size", "cell_shape", "adhesion", 
#                 "epithelial_size", "bare_nuclei", "bland_chromatin", 
#                 "normal_nucleoli", "mitoses", "class"]

# # Load the dataset into a pandas dataframe
# cancer = pd.read_csv(url, header=None, names=column_names)

# # Display the first few rows of the dataset
# print(cancer.head())

### option 2

from ucimlrepo import fetch_ucirepo, list_available_datasets

# check which datasets can be imported
# list_available_datasets()

# import dataset
breast_biopsy  = fetch_ucirepo(id=17)
# alternatively: fetch_ucirepo(name='Heart Disease')

# access data
X = breast_biopsy .data.features
y = breast_biopsy .data.targets
# train model e.g. sklearn.linear_model.LinearRegression().fit(X, y)

# access metadata
print(breast_biopsy .metadata.uci_id)
print(breast_biopsy .metadata.num_instances)
print(breast_biopsy .metadata.additional_info.summary)

# access variable info in tabular format
print(breast_biopsy .variables)
