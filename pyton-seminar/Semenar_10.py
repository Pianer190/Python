import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

encoder = OneHotEncoder()
values = np.array(data['whoAmI']).reshape(-1, 1)
encoder.fit(values)

one_hot = encoder.transform(values).toarray()

one_hot_df = pd.DataFrame(one_hot, columns=encoder.get_feature_names(['whoAmI']))

data = pd.concat([data, one_hot_df], axis=1)

data = data.drop('whoAmI', axis=1)

print(data.head())