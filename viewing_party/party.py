# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        new_movie = None
    else:
        new_movie = {"title": title, "genre": genre, "rating": rating}
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

def watch_movie(user_data, movie):
    # look up movie in watchlist
    tracker_dict = None
    for movie_dict in user_data["watchlist"]:
        if movie == movie_dict["title"]:
            add_to_watched(user_data, movie_dict)
            tracker_dict = movie_dict
    if tracker_dict:
        user_data["watchlist"].remove(tracker_dict)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 
    sum = 0 

    if len(user_data["watched"]) != 0:
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        average_rating = sum / len(user_data["watched"])
        return average_rating
    
    else:
        return 0.0

def get_most_watched_genre(user_data):
    genre_list = []
    counter = 0

    if len(user_data["watched"]) == 0:
        return None
    
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"]) 
        for i in genre_list:
            frequency = genre_list.count(i)
            if (frequency > counter):
                counter = frequency
                genre = i

    return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_movie_titles(user_data):
    friends_movies = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    
    return friends_movies

def get_unique_watched(user_data):
    friends_movies = get_friends_movie_titles(user_data)
    unique_movies = []
    
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            unique_movies.append(movie)

    return unique_movies        

def get_friends_unique_watched(user_data):
    friends_movie_titles = get_friends_movie_titles(user_data)
    user_movie_titles = set()

    for movie in user_data["watched"]:
        user_movie_titles.add(movie["title"])

    friends_unique = friends_movie_titles - user_movie_titles
    friends_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friends_unique:
                if movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)

    return friends_unique_movies    

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_watched = get_friends_unique_watched(user_data)
    # If user data has a subscriptions key
    if "subscriptions" in user_data:
        user_subs = user_data["subscriptions"]
        recs = []

        for movie in friends_watched:
            if movie["host"] in user_subs:
                recs.append(movie)

        return recs
    
    else:
        return []

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_recs = []
    full_recs = get_available_recs(user_data)

    if len(user_data["watched"]) != 0:
        genre = get_most_watched_genre(user_data)
        for rec in full_recs:
            if rec["genre"] == genre:
                genre_recs.append(rec)
    return genre_recs

def get_rec_from_favorites(user_data):
    friends_watchlist = []
    recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watchlist.append(movie)
    favorites = user_data["favorites"]
    for favorite in favorites:
        if favorite not in friends_watchlist:
            recs.append(favorite)
    return recs