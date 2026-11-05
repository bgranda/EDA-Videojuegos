import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl
import matplotlib as mpl
import squarify
import plotly.express as px

archivo1 = '../data/PS4_GamesSales.csv'
df1 = pd.read_csv(archivo1, encoding='latin-1')
df1.head()

archivo2 = "../data/vgsales.csv"
df2 = pd.read_csv(archivo2)
df2.head()

archivo3 = "../data/Video_Games.csv"
df3 = pd.read_csv(archivo3)
df3.head()

archivo4 = "../data/video_games_sales.csv"
df4 = pd.read_csv(archivo4)
df4.head()

archivo5 = "../data/Video_Games_Sales_as_at_22_Dec_2016.csv"
df5 = pd.read_csv(archivo5)
df5.head()

archivo6 = "../data/VideoGames_Sales.xlsx"
df6 = pd.read_excel(archivo6)
df6.head()

archivo7 = "../data/XboxOne_GameSales.csv"
df7 = pd.read_csv(archivo7, encoding='latin-1')
df7.head()

df1['Platform'] = 'PS4'
cols = list(df1.columns)
cols.remove('Platform')
na_index = cols.index('Year')
cols.insert(na_index, 'Platform')
df1_reordered = df1[cols]
df1_reordered.head()
df1_reordered.info()

df7.drop(columns=['Pos'], inplace=True)
df7['Platform'] = 'Xbox One'
cols = list(df7.columns)
cols.remove('Platform')
na_index = cols.index('Year')
cols.insert(na_index, 'Platform')
df7_reordered = df7[cols]
df7_reordered.head()
df7_reordered.info()

df2.drop(columns=['Rank'], inplace=True)
df2.rename(columns={'Name': 'Game', 'NA_Sales': 'North America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales': 'Rest of World', 'Global_Sales': 'Global'}, inplace=True)
df2.head()
df2.info()

df3.drop(columns=['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating'], inplace=True)
df3.rename(columns={'Name': 'Game', 'Year_of_Release': 'Year', 'NA_Sales': 'North America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales': 'Rest of World', 'Global_Sales': 'Global'}, inplace=True)
df3.head()
df3.info()

df4.drop(columns=['rank'], inplace=True)
df4.rename(columns={'name': 'Game', 'platform': 'Platform', 'year': 'Year', 'genre': 'Genre', 'publisher': 'Publisher', 'na_sales': 'North America', 'eu_sales': 'Europe', 'jp_sales': 'Japan', 'other_sales': 'Rest of World', 'global_sales': 'Global'}, inplace=True)
df4.head()
df4.info()

df5.drop(columns=['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating'], inplace=True)
df5.rename(columns={'Name': 'Game', 'Year_of_Release': 'Year', 'NA_Sales': 'North America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales': 'Rest of World', 'Global_Sales': 'Global'}, inplace=True)
df5.head()
df5.info()

if df2.equals(df4):
    print("Los DataFrames df2 y df4 son iguales.")
else:
    print("Los DataFrames df2 y df4 son diferentes.")

if df3.equals(df5):
    print("Los DataFrames df3 y df5 son iguales.")
else:
    print("Los DataFrames df3 y df5 son diferentes.")

dataframes = [df1_reordered, df2, df3, df5, df7_reordered]
df_combined = pd.concat(dataframes, axis=0, ignore_index=True)
df_combined.info()
df_combined['Year'] = df_combined['Year'].astype('Int64')
df_limpio = df_combined.drop_duplicates(keep='first', ignore_index=True)

filas_nulas = df_limpio[df_limpio['Game'].isnull()]
filas_nulas
df_limpio.dropna(subset=['Game'], inplace=True)
df_limpio["Platform"] = df_limpio["Platform"].replace({"XBox One": "Xbox One","XOne": "Xbox One"})

fabricantes = {
    "PS4": "Sony",
    "Wii": "Nintendo",
    "NES": "Nintendo",
    "GB": "Nintendo",
    "DS": "Nintendo",
    "X360": "Microsoft",
    "PS3": "Sony",
    "PS2": "Sony",
    "SNES": "Nintendo",
    "GBA": "Nintendo",
    "3DS": "Nintendo",
    "N64": "Nintendo",
    "PS": "Sony",
    "XB": "Microsoft",
    "PC": "PC",
    "2600": "Atari",
    "PSP": "Sony",
    "Xbox One": "Microsoft",
    "GC": "Nintendo",
    "WiiU": "Nintendo",
    "GEN": "Sega",
    "DC": "Sega",
    "PSV": "Sony",
    "SAT": "Sega",
    "SCD": "Sega",
    "WS": "Bandai",
    "NG": "SNK",
    "TG16": "NEC",
    "3DO": "The 3DO Company",
    "GG": "Sega",
    "PCFX": "NEC"
}
df_limpio["Manufacturer"] = df_limpio["Platform"].map(fabricantes)
df_limpio[df_limpio["Manufacturer"].isna()]["Platform"].unique()

df_nuevo = df_limpio[
    [
        "Game",
        "Platform",
        "Manufacturer",
        "Year",
        "Genre",
        "Publisher",
        "North America",
        "Europe",
        "Japan",
        "Rest of World",
        "Global"
    ]
]

df_nuevo.to_csv('videojuegos.csv', index=False, encoding='utf-8')

archivo = '../data/videojuegos.csv'
df = pd.read_csv(archivo)
df.head()

df[['North America','Europe','Japan','Rest of World','Global']].describe()

game_sales = (df.groupby('Game')['Global'].sum().sort_values(ascending=False))
top10_games = game_sales.head(10).sum()
total_sales = game_sales.sum()
(top10_games / total_sales) * 100

game_sales.head(20)

df['Game'].nunique()

len(df)

games_df = (df.groupby('Game').agg({'Global': 'sum','North America': 'sum','Europe': 'sum','Japan': 'sum','Rest of World': 'sum'}).reset_index())
top_games = (games_df.sort_values(by='Global',ascending=False).head(20))
top_games

plt.figure(figsize=(12,8))
sns.barplot(
    data=top_games,
    x='Global',
    y='Game',
    palette='viridis'
)
plt.title('Top 20 videojuegos por ventas globales')
plt.xlabel('Ventas (millones)')
plt.ylabel('Videojuego')

plt.show()

for n in [10, 20]:
    
    porcentaje = (games_df.nlargest(n, 'Global')['Global'].sum()/ games_df['Global'].sum()* 100)
    
    print(f"Top {n}: {porcentaje:.2f}%")

games_df.nlargest(10,'North America')[['Game', 'North America']]
games_df.nlargest(10,'Europe')[['Game', 'Europe']]
games_df.nlargest(10,'Japan')[['Game', 'Japan']]

pareto = (games_df['Global'].sort_values(ascending=False).cumsum()/ games_df['Global'].sum()* 100)
sales = games_df['Global'].sort_values(ascending=False)
pareto = sales.cumsum() / sales.sum() * 100
videojuegos_pct = (np.arange(1, len(sales) + 1)/ len(sales)* 100)
indice_80 = np.argmax(pareto >= 80)
pct_videojuegos = ((indice_80 + 1)/ len(sales)* 100)
pct_videojuegos

plt.figure(figsize=(10,6))
plt.plot(videojuegos_pct, pareto)
plt.axhline(80,
            color='red',
            linestyle='--',
            label='80% ventas')
plt.xlabel('% de videojuegos')
plt.ylabel('% acumulado de ventas')
plt.title('Curva de Pareto de ventas de videojuegos')
plt.legend()
plt.show()

ventas_plataforma = (df.groupby('Platform')['Global'].sum().sort_values(ascending=False).reset_index())
ventas_plataforma.head(10)

plt.figure(figsize=(12,8))
sns.barplot(
    data=ventas_plataforma,
    x='Global',
    y='Platform',
    palette='viridis'
)
plt.title('Ventas globales por plataforma')
plt.xlabel('Ventas (millones)')
plt.ylabel('Plataforma')
plt.show()

df_plot = df.groupby('Platform')[['North America','Europe','Japan','Rest of World']].sum()
df_plot.plot(kind='bar',figsize=(12,6))
plt.title('Ventas por Plataforma y Región')
plt.xlabel('Plataforma')
plt.ylabel('Ventas')
plt.legend(title='Región')
plt.show()

df_plot = df.groupby('Manufacturer')[['Global','North America','Europe','Japan','Rest of World']].sum()
df_plot.plot(kind='bar',figsize=(12,6))
plt.title('Ventas por Fabricante Global y Región')
plt.xlabel('Fabricante')
plt.ylabel('Ventas')
plt.legend(title='Global y Región')
plt.show()

genre_sales = (df.groupby('Genre')['Global'].sum().sort_values(ascending=False))
genre_sales

genre_sales = (df.groupby('Genre')['Global'].sum().reset_index())

fig = px.treemap(
    genre_sales,
    path=['Genre'],
    values='Global',
    color='Global',
    color_continuous_scale='Viridis'
)

fig.update_layout(
    title='Ventas por género'
)

fig.show()

genre_sales = (df.groupby('Genre')[['North America','Europe','Japan','Rest of World','Global']].sum().sort_values('Global', ascending=False))
genre_sales

plt.figure(figsize=(10,6))
sns.barplot(
    x=genre_sales['Global'],
    y=genre_sales.index,
    palette='viridis'
)
plt.title('Ventas globales por género')
plt.xlabel('Ventas (millones)')
plt.ylabel('Género')
plt.show()

genre_pct = (genre_sales[['North America','Europe','Japan','Rest of World']].div(genre_sales[['North America','Europe','Japan','Rest of World']].sum(axis=1),axis=0)* 100)
genre_pct

n_genres = len(genre_pct)
fig, axes = plt.subplots(
    nrows=(n_genres+2)//3,
    ncols=3,
    figsize=(15, 12)
)
axes = axes.flatten()
for i, genre in enumerate(genre_pct.index):

    axes[i].pie(
        genre_pct.loc[genre],
        labels=genre_pct.columns,
        autopct='%1.0f%%',
        startangle=90,
        wedgeprops={'width':0.4}
    )

    axes[i].set_title(genre)

for j in range(i+1, len(axes)):
    fig.delaxes(axes[j])

plt.suptitle(
    'Porcentaje ventas por región según género',
    fontsize=16
)
plt.tight_layout()
plt.show()

genre_region = (df.groupby('Genre')[['North America','Europe','Japan','Rest of World']].sum().reset_index())
genre_region_long = genre_region.melt(
    id_vars='Genre',
    var_name='Region',
    value_name='Sales'
)

fig = px.treemap(
    genre_region_long,
    path=['Genre', 'Region'],
    values='Sales',
    color='Sales',
    color_continuous_scale='Blues'
)
fig.show()

genre_manufacturer = (df.groupby(['Manufacturer', 'Genre'])['Global'].sum().reset_index())
genre_manufacturer.head()

fig = px.treemap(
    genre_manufacturer,
    path=['Manufacturer', 'Genre'],
    values='Global',
    color='Global',
    color_continuous_scale='Turbo'
)
fig.show()

genre_region_manufacturer = (df.groupby(['Manufacturer','Genre'])[['North America','Europe','Japan','Rest of World']].sum())

fig, axes = plt.subplots(
    2, 2,
    figsize=(16,12)
)
regions = [
    'North America',
    'Europe',
    'Japan',
    'Rest of World'
]
for ax, region in zip(axes.flatten(), regions):

    data = (
        genre_region_manufacturer[region]
        .reset_index()
    )
    sns.barplot(
        data=data,
        x='Genre',
        y=region,
        hue='Manufacturer',
        ax=ax
    )
    ax.set_title(region)
    ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

genre_year = (df.groupby(['Year','Genre'])['Global'].sum().reset_index())
sales_80_90 = (df[(df['Year']>=1980) & (df['Year']<=1999)].groupby('Genre')['Global'].sum().sort_values())
sales_00_20 = (df[(df['Year']>=2000) & (df['Year']<=2020)].groupby('Genre')['Global'].sum().sort_values())

plt.figure(figsize=(12,8))
sales_80_90.plot(
    kind='barh',
    color='steelblue'
)
plt.title('Ventas acumuladas por género (1980-1999)')
plt.xlabel('Ventas (millones)')
plt.ylabel('Género')
plt.show()

plt.figure(figsize=(12,8))
sales_00_20.plot(
    kind='barh',
    color='darkorange'
)
plt.title('Ventas acumuladas por género (2000-2020)')
plt.xlabel('Ventas (millones)')
plt.ylabel('Género')
plt.show()

periods = pd.DataFrame({'80-99': sales_80_90,'00-20': sales_00_20}).fillna(0)
periods = periods.sort_values('00-20')

fig, ax = plt.subplots(figsize=(12,8))
ax.hlines(
    y=periods.index,
    xmin=periods['80-99'],
    xmax=periods['00-20'],
    color='lightgray'
)
ax.scatter(
    periods['80-99'],
    periods.index,
    color='blue',
    s=100,
    label='1980-1999'
)
ax.scatter(
    periods['00-20'],
    periods.index,
    color='orange',
    s=100,
    label='2000-2020'
)
ax.legend()
plt.title(
    'Evolución de las ventas por género'
)
plt.show()

def treemap_generos_region(df, region, year_start, year_end):

    sales = (
        df[
            (df['Year'] >= year_start) &
            (df['Year'] <= year_end)
        ]
        .groupby('Genre')[region]
        .sum()
        .reset_index()
    )
    fig = px.treemap(
        sales,
        path=['Genre'],
        values=region,
        color=region,
        color_continuous_scale='Viridis'
    )
    fig.update_traces(
        textinfo='label+percent root'
    )
    fig.update_layout(
        title=f'{region} ({year_start}-{year_end})'
    )
    fig.show()

treemap_generos_region(df,'North America',1980,1999)
treemap_generos_region(df,'Europe',1980,1999)
treemap_generos_region(df,'Japan',1980,1999)
treemap_generos_region(df,'Rest of World',1980,1999)

treemap_generos_region(df,'North America',2000,2020)
treemap_generos_region(df,'Europe',2000,2020)
treemap_generos_region(df,'Japan',2000,2020)
treemap_generos_region(df,'Rest of World',2000,2020)

