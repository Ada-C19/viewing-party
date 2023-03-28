# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass # can you
=======
def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        return {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
    
    return None



# user data is a dict and it has a key "watched" --> list 
# add movie to this list 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data



    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched_movies = {movie['title']: movie for movie in user_data['watched']}
    friends_watched_movies = set()

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movies.add(movie['title'])

    unique_watched_movies = set(user_watched_movies.keys()).difference(friends_watched_movies)
    return [user_watched_movies[movie] for movie in unique_watched_movies]


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

