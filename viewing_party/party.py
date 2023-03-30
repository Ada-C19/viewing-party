# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {}
    
    if not title or not genre or not rating:
        return None
    
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):

    user_data["watched"] += [movie]

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"] += [movie]

    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]

    for i in range(len(watchlist)):
        if title == watchlist[i]["title"]:
            user_data["watched"] += [watchlist[i]]
            watchlist.pop(i)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    watched = user_data["watched"]

    if not watched:
        return 0
    
    sum = 0

    for i in range(len(watched)):
        sum += watched[i]["rating"]

    # average = sum(values) / len(user_data)
    avg_rating = sum / len(watched)

    return avg_rating

def get_most_watched_genre(user_data):
    pass
    # What is deemed most popular? By rating? By count?
    watched = user_data["watched"]

    genre_dict = {}

    if len(watched) == 0:
        return None
    
    # watched[0]["genre"] == "Fantasy"
    for movie in watched:
        genre_dict[movie["genre"]] = 1
        
    for movie in watched:
        if genre_dict[movie["genre"]] >= 1:
            genre_dict[movie["genre"]] += 1


    # max(d, key = d.get)
    most_watched = max(genre_dict, key = genre_dict.get)
    
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

# Consider the movies that the user has watched, 
# and consider the movies that their friends have watched. 
# Determine which movies the user has watched, 
# but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies

    user_watched = user_data["watched"]
    friends = user_data["friends"]

    user_unique_movies = []

    friends_movie_watched = []

    # Big O notation of O(n^2), try to refactor
    for friend in friends:
        for i in range(len(friend["watched"])):
            friends_movie_watched.append(friend["watched"][i]) 

    for movie in user_watched:
        if movie not in friends_movie_watched:
            if movie not in user_unique_movies:
                user_unique_movies.append(movie)

    return user_unique_movies

def get_friends_unique_watched(user_data):
    
# Consider the movies that the user has watched, 
# and consider the movies that their friends have watched. 
# Determine which movies at least one of the user's friends have watched, 
# but the user has not watched.
# Return a list of dictionaries, that represents a list of movies
    
    user_watched = user_data["watched"]
    friends = user_data["friends"]

    friends_unique_movies = []

    friends_movie_watched = []

    # Big O notation of O(n^2), try to refactor
    for friend in friends:
        for i in range(len(friend["watched"])):
            friends_movie_watched.append(friend["watched"][i]) 

    for movie in friends_movie_watched:
        if movie not in user_watched:
            if movie not in friends_unique_movies:
                friends_unique_movies.append(movie)

    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

# Determine a list of recommended movies. 
# A movie should be added to this list if and only if:
# - The user has not watched it
# - At least one of the user's friends has watched
# - The `"host"` of the movie is a service that is in 
# - the user's `"subscriptions"`
# Return the list of recommended movies

    recommendations = []
    
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    
# Consider the user's most frequently watched genre. 
# Then, determine a list of recommended movies. 
# A movie should be added to this list if and only if:
# - The user has not watched it
# - At least one of the user's friends has watched
# - The `"genre"` of the movie is the same as the user's most frequent genre
# Return the list of recommended movies

    recommendations = []

    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):

# Determine a list of recommended movies. 
# A movie should be added to this list if and only if:
# - The movie is in the user's `"favorites"`
# - None of the user's friends have watched it
# Return the list of recommended movies
    
    recommendations = []

    for movie in user_data["favorites"]:
        if movie in get_unique_watched(user_data):
            recommendations.append(movie)

    return recommendations