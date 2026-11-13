from cmath import nan
from tempfile import NamedTemporaryFile

import pandas as pd
Cleaning_Data_Movies_TVShows = pd.read_csv(r'C:\Users\Alicja\PycharmProjects\Movie_TV_Shows_Explorer\data\raw\netflix_titles.csv')
print(Cleaning_Data_Movies_TVShows.head())
Movie_TV_Shows_cleaning_data = Cleaning_Data_Movies_TVShows.copy()
Movie_TV_Shows_cleaning_data['date_added'] = Movie_TV_Shows_cleaning_data['date_added'].str.strip()
Movie_TV_Shows_cleaning_data['date_added'] = pd.to_datetime(Movie_TV_Shows_cleaning_data['date_added'], errors='coerce')
print(Movie_TV_Shows_cleaning_data['date_added'])
Movie_TV_Shows_cleaning_data['date_added'].info()
print('\nIS NULL')
print(Movie_TV_Shows_cleaning_data['date_added'].isnull().sum())
Movie_TV_Shows_cleaning_data.to_csv(r'data\processed\netflix_clean.csv', index=False)



