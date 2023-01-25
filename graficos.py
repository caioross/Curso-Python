import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

df.head()

df.tail()

"""## 1. Gráfico de Barras"""

df_agrupado_pelo_dia = df.groupby('day', sort=False).agg({ 'total_bill': np.sum }).reset_index()

df_agrupado_pelo_dia

px.bar(df_agrupado_pelo_dia, x='day', y='total_bill')

df_agrupado_pelo_dia_e_sexo = df.groupby(['day', 'sex'], sort=False).agg({ 'total_bill': np.sum }).reset_index()

df_agrupado_pelo_dia_e_sexo

px.bar(df_agrupado_pelo_dia_e_sexo, x='day', y='total_bill', color='sex', barmode='group')

px.bar(df_agrupado_pelo_dia_e_sexo, x='total_bill', y='day', color='sex', barmode='group', orientation='h')

"""## Gráfico de Dispersão"""

px.scatter(df, x='total_bill', y='tip', color='day', hover_name='time')

"""## Gráfico de Pizza"""

quantidade_pedidos_por_dia = df['day'].value_counts()

quantidade_pedidos_por_dia

quantidade_pedidos_por_dia.index

quantidade_pedidos_por_dia.values

px.pie(names=quantidade_pedidos_por_dia.index, values=quantidade_pedidos_por_dia.values)

