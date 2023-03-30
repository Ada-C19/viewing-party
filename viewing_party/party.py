
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title":title, "genre": genre, "rating": rating}
    else:
        return None

def add_to_watched(user_data, movie):
   user_data["watched"].append(movie)
   return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    if not user_data["watched"]: # or if empty string
        return 0.0
    
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    average_rating_watched = total_rating / len(user_data["watched"])
    print(average_rating_watched)
    return average_rating_watched
    
def get_most_watched_genre(user_data):

    if user_data["watched"] == []:
        return None
    
    genre_counter = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_counter:
            genre_counter[genre] += 1
        else:
            genre_counter[genre] = 1
    print(genre_counter)

    most_watched_genre_count = 0
    most_watched_genre = ""
    # add a new variable to put the key in. Initialize to None or empty string
    for key, value in genre_counter.items():
        if value > most_watched_genre_count:
            most_watched_genre_count = value
            most_watched_genre = key
    print(most_watched_genre)
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    """
    user_data: dict with "watched" list of dictionaries and "friends" list of dictionaries
    """

    # Create list of all friends' watched movies
    friends_watched = []
    for friend in user_data["friends"]:
        friends_watched += friend["watched"]
    
    # Create list of movies that only user_data has watched
    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_watched.append(movie)
    
    return unique_watched
    
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    
    return friends_unique_watched

            
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

<<<<<<< HEAD
def get_available_recs(user_data):
    
    subscriptions = user_data["subscriptions"] # list of strings
    watched_list = user_data["watched"] # list of dicts of watched movies
=======
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genres = []
    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    # Determine most frequent genre from watched list   
    try:
        fav_genre = max(genres, key=genres.count)
    # Capture exception for when user_data's watched list is empty
    except ValueError:
        fav_genre = None

    movie_recs = []
    # Create a list of all the movies friends have watched that user_data has not
    friends_movies = get_friends_unique_watched(user_data)
    
    for movie in friends_movies:
        if movie["genre"] == fav_genre:
            movie_recs.append(movie)
    
    return movie_recs

def get_rec_from_favorites(user_data):
    # Create list of movies only watched by user, not by friends
    friends_not_watched = get_unique_watched(user_data)
    
    # Create list of movies from favorites that have not been watched by friends
    fav_movie_recs = [movie for movie in user_data["favorites"] if movie in friends_not_watched]
 
    return fav_movie_recs

>>>>>>> dd04daac08bae9f850bcdef65c46d8ddc2e35f6c

    movie_recs = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie in friend["watched"] and movie["host"] in subscriptions:
                movie_recs.append(movie)
        return movie_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
