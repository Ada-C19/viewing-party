
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None

    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_movie = user_data['watched']
    movie_to_watchlist = user_data['watchlist']

    for item in movie_to_watchlist:
        if title == item['title']:
            watched_movie.append(item)
            movie_to_watchlist.remove(item)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0
    number_movies = len(user_data["watched"])

    if len(user_data["watched"]) == 0:
        return 0.0
    
    for i in range(len(user_data["watched"])):
            total_ratings += user_data["watched"][i]["rating"]
            average_rating = total_ratings / number_movies
    return average_rating



def get_most_watched_genre(user_data):
    genre_options = []

    if user_data["watched"] == []:
        return None    
    
    for i in range(len(user_data["watched"])):
        genre_options.append(user_data["watched"][i]["genre"])
        highest_watched = (max(set(genre_options), key=genre_options.count))
    return highest_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data): 
    unique_watch = []
    friends_movies_watched = []

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_movies_watched.append(movie)
 
    for movie in user_data["watched"]:
        if movie not in friends_movies_watched:
            unique_watch.append(movie)
    return unique_watch

  
def get_friends_unique_watched(user_data):
    unique_watch = []
    no_duplicate_unique_watch = []
   

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"]:
                    unique_watch.append(movie)

    for movie in unique_watch:
        if movie not in no_duplicate_unique_watch:
            no_duplicate_unique_watch.append(movie)
    return no_duplicate_unique_watch


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_recs = []
    friends_movies_recs = get_friends_unique_watched(user_data)

    for i in range(len(friends_movies_recs)):
        if friends_movies_recs[i]["host"] in user_data["subscriptions"]:
            available_recs.append(friends_movies_recs[i])
    return available_recs
        

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass