# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    #  user data is a dictionary where the key is watched and the value is a list of movies
    # add the movie paramater to theblist of movies
    
    # for movie in user_data:
    #     if movie not in user_data:

    user_data["watched"].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):
    
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # for movie_info in user_data["watchlist"]:
    #   if movie_info["title"] == title:
    #     user_data["watched"].append(movie_info)
    #     # test passes if I add the title instead of the entire movie dictionary user_data["watched"].append(movie_info["title"])
    #     del user_data["watchlist"][0]
    # return user_data

    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    pass
    


def get_most_watched_genre(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    pass


def get_friends_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass
