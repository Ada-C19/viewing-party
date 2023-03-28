# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movies_info = {}
    movies_info['title'] = title
    movies_info['genre'] = genre
    movies_info['rating'] = rating
    if not title or not genre or not rating:
        return None
    return movies_info

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:   
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
            # return user_data
    # If the movie is not found in the watchlist or the watchlist is empty, return the original user_data
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data.get("watched", [])
    if not watched_movies:
        return 0.0
    ratings_sum = 0.0 
    for movie_dict in watched_movies:
        ratings_sum += movie_dict.get('rating', 0.0)  
    return ratings_sum / len(watched_movies)

def get_most_watched_genre(user_data):
    genre_occur = {}
    if not user_data["watched"]:
        return None
    for movie_dict in user_data["watched"]:
        genre_occur[movie_dict["genre"]] = genre_occur.get(movie_dict["genre"], 0) + 1
    return max(genre_occur, key=genre_occur.get)





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# Create a function named `get_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies

def get_unique_watched(user_data): 
    user_watched = set()
    user_watched_dict = {}
    for movie in user_data['watched']:
        user_watched.add(movie['title'])
        user_watched_dict[movie['title']] = movie
        friends_watched = set()
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched.add(movie['title'])
    user_unique_watched = []
    for title in user_watched.difference(friends_watched):
        if title in user_watched_dict:
            user_unique_watched.append(user_watched_dict[title]) 
    return user_unique_watched



    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

