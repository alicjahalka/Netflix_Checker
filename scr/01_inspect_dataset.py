import pandas as pd
netflix_titles_dataset = pd.read_csv(r'C:\Users\Alicja\PycharmProjects\Movie_TV_Shows_Explorer\data\raw\netflix_titles.csv')
print(netflix_titles_dataset.head())
print(netflix_titles_dataset.describe())
netflix_titles_dataset.info()


print('\nISNA SUMMARY')
print(netflix_titles_dataset.isnull().sum())
print('\nDUPLICATED SUMMARY')
print(netflix_titles_dataset.duplicated().sum())
print(netflix_titles_dataset.isnull().sum().sum())
print(netflix_titles_dataset['type'].unique())
print(netflix_titles_dataset['listed_in'].unique())