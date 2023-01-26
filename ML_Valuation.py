import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from matplotlib import pyplot

# %matplotlib inline

dfNY = pd.read_csv("https://www.dropbox.com/s/8i2nw6bd5ha7vny/listingsNY.csv?dl=1")
dfRJ = pd.read_csv("https://www.dropbox.com/s/yyg8hso7fbjf1ft/listingsRJ.csv?dl=1")

"""id – O número de identificação do imóvel.
name – Nome da propriedade anunciada.
hot_id – O número de identificação do proprietário (anfitrião) do imóvel.
neighbourhood_group – É um conjunto de grupos de bairros.
latitude – Coordenada de Latitude do imóvel.
longitude – Coordenada de Longitude do imóvel.
room_type – O tipo de quarto oferecido.
pric – Preço por pernoite do imóvel a ser alugado na moeda local.
minimum_nights – Noites mínimas para locação.
number_of_reviews – Quantidade de avaliações que o imóvel recebeu.
last_review – Data da última avaliação.
reviews_per_month – Quantidade de avaliações por mês.
calculated_host_listings_count – Quantidade de imóveis do mesmo anfitrião.
availability_365 – Número total de dias em que o anúncio está disponível durante o ano.
number_of_reviews_ltm – Quantidade de avaliação nos últimos 12 meses.
license – Esta coluna não contém nenhum valor válido.
"""

display(dfNY.head(5))
display(dfRJ.head(5))

print(f'New York\nEntradas: {dfNY.shape[0]}\nVariáveis: {dfNY.shape[1]}\n')
print(f'Rio de Janeiro\nEntradas: {dfRJ.shape[0]}\nVariáveis: {dfRJ.shape[1]}\n')

display(dfNY.dtypes)

dfNY.last_review = pd.to_datetime(dfNY.last_review, format="%Y-%m-%d")
dfRJ.last_review = pd.to_datetime(dfRJ.last_review, format="%Y-%m-%d")

import datetime as dt

dfNY['year'] = dfNY.last_review.dt.year
dfNY.price = dfNY.price.mask(dfNY.year <= 2011, (dfNY.price * 1.674))
dfNY.price = dfNY.price.mask(dfNY.year == 2012, (dfNY.price * 1.954))
dfNY.price = dfNY.price.mask(dfNY.year == 2013, (dfNY.price * 2.157))
dfNY.price = dfNY.price.mask(dfNY.year == 2014, (dfNY.price * 2.353))
dfNY.price = dfNY.price.mask(dfNY.year == 2015, (dfNY.price * 3.331))
dfNY.price = dfNY.price.mask(dfNY.year == 2016, (dfNY.price * 3.489))
dfNY.price = dfNY.price.mask(dfNY.year == 2017, (dfNY.price * 3.190))
dfNY.price = dfNY.price.mask(dfNY.year == 2018, (dfNY.price * 3.654))
dfNY.price = dfNY.price.mask(dfNY.year == 2019, (dfNY.price * 3.943))
dfNY.price = dfNY.price.mask(dfNY.year == 2020, (dfNY.price * 5.155))
dfNY.price = dfNY.price.mask(dfNY.year == 2021, (dfNY.price * 5.352))

variaveis = ['id',
      'name',
      'host_id',
      'host_name',
      'neighbourhood_group',
      'neighbourhood',
      'latitude',
      'longitude',
      'room_type',
      'price',
      'minimum_nights',
      'number_of_reviews',
      'last_review',
      'reviews_per_month',
      'calculated_host_listings_count',
      'availability_365',
      'number_of_reviews_ltm',
      'license']

vz = []
dado = []

for i in variaveis:
  dado.append(dfNY[i].isnull().sum() / dfNY[i].shape[0])
  dado.append(dfRJ[i].isnull().sum() / dfRJ[i].shape[0])
  vz.append(dado[:])
  dado.clear()
vz  

pd.DataFrame(vz, columns=['New York', 'Rio de Janeiro'], index=variaveis)

dfNY_clean = dfNY.dropna(subset=['name', 'host_name'], axis=0)
dfRJ_clean = dfRJ.dropna(subset=['name', 'host_name'], axis=0)

rpm_ny_median = dfNY_clean.reviews_per_month.median()
dfNY_clean = dfNY_clean.fillna({"reviews_per_month": rpm_ny_median})
lr_ny_median = dfNY_clean['last_review'].astype('datetime64[ns]').quantile(0.5, interpolation="midpoint")
dfNY_clean = dfNY_clean.fillna({"last_review": lr_ny_median})
rpm_rj_median = dfRJ_clean.reviews_per_month.median()
dfRJ_clean = dfRJ_clean.fillna({"reviews_per_month": rpm_rj_median})
lr_rj_median = dfRJ_clean['last_review'].astype('datetime64[ns]').quantile(0.5, interpolation="midpoint")
dfRJ_clean = dfRJ_clean.fillna({"last_review": lr_ny_median})

dx0 = ['price', 'minimum_nights']


for n in dx0:
    data_a = dfNY_clean[n]
    data_b = dfRJ_clean[n]
    data_2d=[data_a,data_b]
    plt.boxplot(data_2d, vert=False, labels=["New York", "Rio de Janeiro"])
    plt.title(n)
    plt.show()

# New York

dfNY_clean[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']].describe()




# Rio de Janeiro

dfRJ_clean[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']].describe()

# New York




dfNY_out = dfNY_clean.copy()





dfNY_out.drop(dfNY_out[dfNY_out.price > 1100].index, axis=0, inplace=True)





dfNY_out.drop(dfNY_out[dfNY_out.minimum_nights > 65].index, axis=0, inplace=True)





# Rio de Janeiro





dfRJ_out = dfRJ_clean.copy()





dfRJ_out.drop(dfRJ_out[dfRJ_out.price > 600].index, axis=0, inplace=True)





dfRJ_out.drop(dfRJ_out[dfRJ_out.minimum_nights > 4].index, axis=0, inplace=True)

var = ['Entire home/apt',
       'Private room',
       'Shared room',
       'Hotel room']

dado_var = {}
for i in var:
  dado_var[i] = [dfNY_out.loc[dfNY_out.room_type == i].shape[0] / dfNY_out.room_type.shape[0] , dfRJ_out.loc[dfRJ_out.room_type == i].shape[0] / dfRJ_out.room_type.shape[0]]

ima = pd.DataFrame(dado_var, index=['New York', 'Rio de Janeiro'])
ima.plot(kind="barh",stacked=True,figsize=(6,4), color=['c', 'm', 'y', 'orange'])
plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()

#lugares mais caros
dfNY_out.groupby(['neighbourhood']).price.mean().sort_values(ascending=False)[:10]

import folium
import branca

colormap = branca.colormap.linear.YlOrRd_09.scale(0, 1100)
colormap = colormap.to_step(index = [0, 275, 550, 825, 1100])
colormap.caption = 'Preços dos imóveis'

m = folium.Map(location=[40.691895, -73.902734], tiles="stamentoner", zoom_start=11)

lon = []
lat = []
value = []

data= {'lon': lon, 'lat': lat, 'value': value}
for n in range(0, dfNY_out.shape[0]):
  lon.append(dfNY_out.longitude.values[n])
  lat.append(dfNY_out.latitude.values[n])
  value.append(dfNY_out.price.values[n])

for i in range(0, 16000):
  preco = data['value'][i]
  if preco <= 275:
    print = '#f1f8d0'
  elif preco > 275 and preco <= 550:
    print = '#efc271'
  elif preco > 825 and preco <= 1100:
    print = '#e35d4d'
  else:
    print = '#8b2a40'
  folium.CircleMarker(
      location=[data['lat'][i], data['lon'][i]],
      radius= 2,
      popup='Laurelhurst Park',
      color= print,
      line_color= print,
      fill_color=print,
      fill=True).add_to(m)
colormap.add_to(m)
m
