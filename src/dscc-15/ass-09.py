import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

# Create user-movie rating matrix
user_movie_matrix = ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating"
).fillna(0)

# Select any two users
user1 = 1
user2 = 2

# Get rating vectors
vector1 = user_movie_matrix.loc[user1].values
vector2 = user_movie_matrix.loc[user2].values

# Compute dot product
dot_product = np.dot(vector1, vector2)

# Compute Euclidean norms
norm1 = np.linalg.norm(vector1)
norm2 = np.linalg.norm(vector2)

# Compute Euclidean distance
distance = np.linalg.norm(vector1 - vector2)

# Compute cosine similarity
cosine_sim = dot_product / (norm1 * norm2)

# Display results
print("User 1 Vector:\n", vector1)
print("User 2 Vector:\n", vector2)

print("\nDot Product:", dot_product)
print("Norm of User 1:", norm1)
print("Norm of User 2:", norm2)
print("Euclidean Distance:", distance)
print("Cosine Similarity:", cosine_sim)

# Find similarity among all users
similarity_matrix = cosine_similarity(user_movie_matrix)

# Convert similarity matrix to DataFrame
similarity_df = pd.DataFrame(
    similarity_matrix,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)

# Find most similar users for user1
similar_users = similarity_df[user1].sort_values(ascending=False)

print("\nMost Similar Users to User", user1)
print(similar_users.head())

# Find movies liked by similar user
most_similar_user = similar_users.index[1]

user1_movies = set(
    ratings[
        (ratings["userId"] == user1) &
        (ratings["rating"] >= 4)
    ]["movieId"]
)

similar_user_movies = set(
    ratings[
        (ratings["userId"] == most_similar_user) &
        (ratings["rating"] >= 4)
    ]["movieId"]
)

# Recommend unseen movies
recommended_movies = similar_user_movies - user1_movies

# Convert movie IDs to movie names
recommended_movie_names = movies[
    movies["movieId"].isin(recommended_movies)
]["title"]

print("Top 10 Recommended Movies for User", user1)

for movie in recommended_movie_names.head(10):
    print("  -", movie)
