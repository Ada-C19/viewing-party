# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    # Create a movie dictionary with title, genre, and rating)
    if title and genre and rating:
        return {"title":title, "genre": genre, "rating": rating}
    else:
        return None


def add_to_watched(user_data, movie):
   # Update user's watched list with new movie
   user_data["watched"].append(movie)
   return user_data


def add_to_watchlist(user_data, movie):
    # Update user's watchlist with new movie
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    # Update user's watchlist and watched list when a movie has been seen
    for idx, movie in enumerate(user_data["watchlist"]):
        if movie["title"] == title:
            # Use .pop to reduce time complexty
            user_data["watchlist"].pop(idx)
            user_data["watched"].append(movie)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # Calculate average rating of watched movies
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    
    try:
        average_rating_watched = total_rating / len(user_data["watched"])
    except ZeroDivisionError:
        average_rating_watched = 0.0 
   
    return average_rating_watched
    

def get_most_watched_genre(user_data):
    # Return the most watched genre
    if not user_data["watched"]:
        return None
    
    # Create dictionary that tracks the frequency of genres from watched list
    genre_counter = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if not genre_counter.get(genre):
            genre_counter[genre] = 1
        else:
            genre_counter[genre] += 1

    most_watched_genre_count = 0
    most_watched_genre = ""

    # Returns the most watched genre from our genre_counter dictionary
    for genre, count in genre_counter.items():
        if count > most_watched_genre_count:
            most_watched_genre_count = count
            most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
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

def get_available_recs(user_data):
    # Return movie recommendations that haven't been watched by user, at least one friend has watched,
    # and the host is a service in user's subscriptions
    friends_watched = get_friends_unique_watched(user_data)
    movie_recs = []

    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)

    return movie_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # Find user's favorite genre
    fav_genre = get_most_watched_genre(user_data)

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
    
    fav_movie_recs = []
    for movie in user_data["favorites"]:
        if movie in friends_not_watched:
            fav_movie_recs.append(movie)

    return fav_movie_recs
