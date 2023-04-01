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
            movie = watched
            friends_watched_list.append(movie)

    return friends_watched_list

def get_unique_watched(user_data):
    pass
    # user_watched = user_movies_watched(user_data)   # returns a list of user movies watched(dict)
    # friends_watched = friends_movies_watched(user_data) # returns a list of friend's movies watched(dict)
    # user_unique_watched = []


    # (x) 1 - create a list of movies user has watched: helper fx: user_watched
    # (x) 2 - create a list of movies friends have watched: helper fx: friends_watched
    # (x) 3 - create variables to hold user and friends watch_lists
    # (x) 4 - initiate empty list: user_unique_watched
    # (x) 5 - for each movie_title in user_watched:
    # (x) 6 - if the movie from user_watched is in friends_watched: keep looping.
    # ( ) 7 - else: user_unique_watched.append(movie)
    # ( ) 8 - return user_unique_watched

    # user_data = {'watched': [{'TITLE': "I See You", 'genre': 'Horror', 'rating': 5.0}],
    #             'friends': [{'watched': [{'TITLE': 'You', 'genre': 'Suspense', 'rating': 4.8}]}]}

    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

