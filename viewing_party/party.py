# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

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
def get_watched_avg_rating(user_data):
    running_total = 0
    number_of_movies = 0
    for movie in user_data["watched"]:
        running_total += movie["rating"]
        number_of_movies += 1
    avg = running_total / number_of_movies
    return avg

def get_most_watched_genre(user_data):
    most_watched_genre_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched_genre_dict:
            most_watched_genre_dict["genre"] = 1
        else:
            most_watched_genre_dict["genre"] += 1


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

