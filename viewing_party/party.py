# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if not title or not genre or not rating:
        return None
    else:
        movie.update({"title" : title, "genre" : genre, "rating" : rating})
        return movie


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    print(user_data)
    watchlist_list_of_dict = user_data.get("watchlist")
    print(watchlist_list_of_dict)

    for watchlistDict in watchlist_list_of_dict:
        if watchlistDict.get("title") == title:
            watchlist_list_of_dict.remove(watchlistDict)
            user_data["watched"].append(watchlistDict)
            print(user_data)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------


def get_unique_watched(user_data):

    user_unique_movies = []  # a list of dictionaries
    movies_titles_friends_watched = []  # a list of strings

    for item in user_data.get("friends"):
        for x in item.get("watched"):
            movies_titles_friends_watched.append(x.get("title"))
    
    for item in user_data.get("watched"):
        movie_user_has_watched = item
        if movie_user_has_watched.get("title") not in movies_titles_friends_watched:
                user_unique_movies.append(movie_user_has_watched)

    return user_unique_movies


def get_friends_unique_watched(user_data):

    friends_movies = [] # a list of dictionaries
    movies_titles_user_watched = [] # a list of strings

    for item in user_data.get("watched"):
        movies_titles_user_watched.append(item.get("title"))

    for item in user_data.get("friends"):
        for x in item.get("watched"):
            if x.get("title") not in movies_titles_user_watched:
                friends_movies.append(x)

    new_list = []
    for dictionary in friends_movies:
        if dictionary not in new_list:
            new_list.append(dictionary)
    
    return new_list

    
    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

