import pandas as pd
import os

import pandas as pd

data = pd.DataFrame()

for i in range(2000,2020):
    df = pd.read_html(f'https://www.pro-football-reference.com/years/{i}/penalties.htm')[0].set_index('Penalty')['Pen/G']
    data[str(i)] = df
data.to_csv('data.csv')
