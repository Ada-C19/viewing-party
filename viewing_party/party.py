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
    movie = user_data['watched']    # dictionary: movie
    user_watched_titles = []   # empty list

    for element in movie:
        title = movie.get('title', 'N/A')
        user_watched_titles.append(title)
    
    return user_watched_titles

def user_movies_watched(user_data):
    """ Helper function for get_unique_watched(): returns a list of movie titles watched by user. """
    watched_list = user_data['watched']
    user_watched_titles = []

    for movie in watched_list:
        for key in movie:
            if key == 'title':
                title = movie.get(key)
                user_watched_titles.append(title) 
    
    return user_watched_titles

def friends_movies_watched(user_data):
    """ Helper function #2 for get_unique_watched(): returns a list of movie titles watched by user's friends. """
    friends_watched_titles = []

    for watched_dict in user_data['friends']:
        watched_list = watched_dict['watched']
        for movie in watched_list:
            for key in movie:
                if key == 'title':
                    title = movie.get(key)
                    friends_watched_titles.append(title)

    return friends_watched_titles

def get_unique_watched(user_data):
    # (x) 1 - create a list of movies user has watched: helper fx: user_watched
    # ( ) 2 - create a list of movies friends have watched: helper fx: friends_watched
    # ( ) 3 - initiate empty list: user_unique_watched
    # ( ) 4 - for each movie in user_watched:
    # ( ) 5 - if the movie from user_watched is in friends_watched: keep looping.
    # ( ) 6 - else: user_unique_watched.append(movie)
    # ( ) 7 - return user_unique_watched

    # user_data = {'watched': [{'TITLE': "I See You", 'genre': 'Horror', 'rating': 5.0}],
    #             'friends': [{'watched': [{'TITLE': 'You', 'genre': 'Suspense', 'rating': 4.8}]}]}

    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

