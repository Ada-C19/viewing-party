# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if title != None and genre != None and rating != None:
        movies= {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movies
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


    # user_data = {
    #     "watched": [
    #         movie
    #         ]
    #     }

    # user_data["watched"] += movie
    # print(user_data)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    #we want to move the movies (title, genre, rating) into the user_data["watch"]

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

