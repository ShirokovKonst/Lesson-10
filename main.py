import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data_onehot = data['whoAmI'].apply(lambda x: pd.Series([int(x == 'human'), int(x == 'robot')], index=['human', 'robot']))
data_onehot.head()