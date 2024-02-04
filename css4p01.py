# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:44:04 2024

@author: 2012011520
"""

import pandas as pd
# import matplotlib.pyplot as plt
# from ydata_profiling import ProfileReport

#load the data
movie_df = pd.read_csv("movie_dataset.csv")

# Replace 'Revenue' with the actual column name you want to delete
movie_df = movie_df.drop('Rank', axis=1)

#Get general info
# print(movie_df.info())

#Droping deplicate if any
movie_df.drop_duplicates(inplace=True)

#There are 128, and 64 missing values in revenue and Meascore columns, respectively. 
# the next step either we can drop the row of these missing values or we can fill them
# with the mean of either column.

# fill the missing values in Revenue with the mean of the revenue values.

revenue_avg = movie_df['Revenue (Millions)'].mean()
movie_df['Revenue (Millions)'].fillna(revenue_avg, inplace=True)

# fill the missing values inMetascore with the mean of the metascore values.
#calcalating the average revenue of the movies in all dataset
metascore_avg = movie_df['Metascore'].mean()
movie_df['Metascore'].fillna(metascore_avg, inplace=True)

#check if done
print(movie_df.info())

# Overall Descriptive statistics
print(movie_df.describe())
print(movie_df['Rating'].describe())

# Exploratory Data Analysis
# look into the histogram to to get idea of how variables are distrubuted
movie_df.hist(color='DarkBlue',figsize= (10,10))

# Get the t highest rated movies 
highest_rating = movie_df.nlargest(1, 'Rating')
#average revenue of movies between from 2015 to 2017.

filtered_df_2015 = movie_df[(movie_df['Year'] >= 2015) & (movie_df['Year'] <= 2017)]

averag_rev2015_2017 = filtered_df_2015['Revenue (Millions)'].mean()

#average revenue of movies between from 2007 to 2015.

filtered_df = movie_df[(movie_df['Year'] > 2006) & (movie_df['Year'] < 2016)]

averag_rev2006_2015 = filtered_df['Revenue (Millions)'].mean()

#calulating the number of movies released in 2016

released_2016 = movie_df[movie_df['Year']==2016]
num_released_2016 = len(released_2016)

# Replace 'Director' with the actual column name representing movie directors
christopher_movies = movie_df[movie_df['Director'].str.contains('Christopher Nolan', case=False, na=False)]

# Calculate the number of movies directed by Christopher
num_christopher_movies = len(christopher_movies)


# Alternatively, you can use the shape attribute to get the number of rows directly
# num_christopher_movies = christopher_movies.shape[0]

# calculating the mediam rading of the movies directed by Christopher Nolan

christopher_movies_median = christopher_movies['Rating'].median()

# print("Number of movies directed by Christopher:", num_christopher_movies)
# Replace 'Rating' with the actual column name representing movie ratings
high_rated_movies_8 = movie_df[movie_df['Rating'] >= 8]

# Calculate the number of movies with a rating of at least 8 using shape this time
num_high_rated_movies_8 = len(high_rated_movies_8)

#calculating the year with the highest average ratings

Year_highest_rating = movie_df['Year']

# Replace 'Year' and 'Rating' with the actual column names
average_ratings_by_year = movie_df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
max_avg_rating_year = average_ratings_by_year.idxmax()
max_avg_rating = average_ratings_by_year.max()

print(f"The year with the highest average rating is {max_avg_rating_year} with an average rating of {max_avg_rating:.2f}")

# Replace 'Year' with the actual column name representing movie release years
movies_2006 = movie_df[movie_df['Year'] == 2006]
movies_2016 = movie_df[movie_df['Year'] == 2016]

# Calculate the number of movies in 2006 and 2016
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print(f"The percentage increase in the number of movies between 2006 and 2016 is: {percentage_increase:.2f}%")

# If the 'Actors' column contains strings with actor names separated by commas, you may need to split them first
all_actors = movie_df['Actors'].str.split(',').explode().str.strip()

# Find the most common actor
most_common_actor = all_actors.mode().iloc[0]

print("The most common actor in all movies is:", most_common_actor)
#unique genres

unique_genres = movie_df['Genre'].str.split(',').explode().unique()
num_unique_genres = len(unique_genres)


# Replace 'Year', 'Rating', and other column names with your actual numerical features
numerical_features = movie_df[['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)















