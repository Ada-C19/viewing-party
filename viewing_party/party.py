
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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    subscriptions = user_data["subscriptions"] # list of strings
    watched_list = user_data["watched"] # list of dicts of watched movies

    movie_recs = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie in friend["watched"] and movie["host"] in subscriptions:
                movie_recs.append(movie)
        return movie_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
