# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # validate_parameters (empty strings and zero evaluate to Falsy)
    if title and genre and rating:
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    movie_found = False
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            movie_found = True
            break
    if not movie_found:
        return user_data
            
    return user_data

# ****** Waves 2, 3, 4, 5: should not modify user_data ******

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_sum = 0
    if user_data["watched"] == []:
            average = 0.0
    else:
        for movie in user_data["watched"]:
            ratings_sum += movie["rating"]
        average = ratings_sum/len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
            return None
    
    genre_count_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count_dict:
            genre_count_dict[movie["genre"]] += 1
        else:
            genre_count_dict[movie["genre"]] = 1
    popular_genre = max(genre_count_dict, key=genre_count_dict.get)
    return popular_genre    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def user_movies_watched(user_data):
    """ Helper function #1 for get_unique_watched(): returns a list of movies watched by user. """
    user_watched_list = []

    watched = user_data['watched']
    for movie in watched:
        user_watched_list.append(movie)

    return user_watched_list

def friends_movies_watched(user_data):
    """ Helper function #2 for get_unique_watched(): returns a list of movies watched by user's friends. """
    friends_watched_list = []

    for each_dict in user_data['friends']:
        for watched in each_dict['watched']:
            friends_watched_list.append(watched)

    return friends_watched_list

def get_unique_watched(user_data):
    """ Return a list of movies only the user has watched. """
    user_watched = user_movies_watched(user_data)
    friends_watched = friends_movies_watched(user_data)
    user_unique_watched = []

    for movie in user_watched:
        if not movie in friends_watched:
            user_unique_watched.append(movie)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    """ Return a list of movies only the user's friends have watched. """
    user_watched = user_movies_watched(user_data)
    friends_watched = friends_movies_watched(user_data)
    friends_unique_watched = []

    for movie in friends_watched:
        if not movie in user_watched and not movie in friends_unique_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

