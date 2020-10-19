import pandas as pd
import os

import pandas as pd

data = pd.DataFrame()

for i in range(2000,2020):
    df = pd.read_html('https://www.pro-football-reference.com/years/2019/penalties.htm')[0].set_index('Penalty')['Pen/G']
    data[str(i)] = df
data.to_csv('data.csv')
