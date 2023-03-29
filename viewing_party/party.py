# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    static_keys = ["title", "genre","rating"]
    inputs = [title, genre, rating]
    if (type(title)) is str and (type(genre)) is str and (type(rating)) is float:
        new_movie = {k:v for k, v in zip(static_keys, inputs)}
    else:
        return None
    
    return new_movie

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    user_data["watched"] = watched_list
    return user_data


def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched_list = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            watched_list.append(movie)
            user_data["watchlist"] = watchlist
            user_data["watched"] = watched_list
            break
    return user_data
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    avg_list = [movie["rating"] for movie in watched]
    if len(avg_list) == 0:
        return 0
    avg_rating = sum(avg_list) / len(avg_list)
    return avg_rating


def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genre_freq = [movie["genre"] for movie in watched]
    if genre_freq == []:
        return None
    return max(set(genre_freq), key=genre_freq.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = set(movie["title"] for friend in user_data["friends"] for movie in friend["watched"])
    return [movie for movie in user_watched if movie["title"] not in friends_watched]

def get_friends_unique_watched(user_data):
    user_watched = set(movie["title"] for movie in user_data["watched"])
    friends_watched = [movie for friend in user_data["friends"] for movie in friend["watched"]]
    #unique_watched = [movie for movie in friends_watched if movie["title"] not in user_watched and movie not in user_data["watched"]]
    unique_watched = []
    for movie in friends_watched:
        if movie["title"] not in user_watched and movie not in user_data["watched"]:
                if movie not in unique_watched:
                    unique_watched.append(movie)
    return unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    subscriptions = user_data['subscriptions']
    recommended_movies = []
    
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['host'] in subscriptions and movie not in user_data['watched']:
                recommended_movies.append(movie)
    
    return recommended_movies

def get_available_recs(user_data):
    watched = user_data["watched"]
    subs = [subscriptions for subscriptions in user_data["subscriptions"]]
    friends_watched = [movie for friend in user_data["friends"] for movie in friend["watched"]]
    rec_movies = []

    for movie in friends_watched:
        if movie not in watched and movie["host"] in subs:
            if movie not in rec_movies:
                rec_movies.append(movie)
            
    return rec_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_freq = get_most_watched_genre(user_data)
    watched = user_data["watched"]
    friends_watched = [movie for friend in user_data["friends"] for movie in friend["watched"]]
    rec_movies = []
    if len(watched) == 0:
        return rec_movies
    for movie in friends_watched:
        if movie not in watched and movie["genre"] in genre_freq:
            if movie not in rec_movies:
                rec_movies.append(movie)
        
    return rec_movies