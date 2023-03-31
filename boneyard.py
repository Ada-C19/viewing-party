# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

# working code Celina wrote in order to figure out how to get the tests to work
def remove_from_watchlist(user_data, movie):
    if movie in user_data["watchlist"]:
        user_data["watchlist"].remove(movie)
    return user_data

def remove_from_watched(user_data, movie):
    if movie in user_data["watched"]:
        user_data["watched"].remove(movie)
    return user_data

def watch_movie(user_data, title):
    # example used_data structure
    # user_data = {
    #     "watchlist" : [{"title" : "Ferngully", "genre": "kids", "rating": 10}],
    #     "watched" : [{"title" : "Avatar", "genre": "white savior", "rating": 1},
    #                  {"title" : "The Blind Side", "genre": "white savior", "rating": 8}]
    # }
    # so as to not modify the OG user_data as per the instructions
    modified_user_data = user_data
    for movie in modified_user_data["watchlist"]:
        if title == movie["title"]:
            add_to_watched(modified_user_data, movie)
            remove_from_watchlist(modified_user_data, movie)
            return modified_user_data
    return user_data

# A mix of the two?
def watch_movie(user_data, title):
    modified_user_data = user_data
    for movie in modified_user_data["watchlist"]:
        if title == movie["title"]:
            modified_user_data["watchlist"].remove(movie)
            modified_user_data["watched"].append(movie)
            return modified_user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# not functioning
def get_most_watched_genre(user_data):
    most_watched_genre_dict = {}
    times_watched_genre = 0
    most_watched_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched_genre_dict:
            most_watched_genre_dict[movie["genre"]] = 1
        else:
            most_watched_genre_dict[movie["genre"]] += 1
    for genre in most_watched_genre_dict:
        if most_watched_genre_dict["genre"] < times_watched_genre:
            continue
        elif most_watched_genre_dict["genre"] > times_watched_genre:
            most_watched_genre_dict["genre"] = times_watched_genre
            most_watched_genre = genre
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------