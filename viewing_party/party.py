# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if not title or not genre or not rating:
        return None

    return movie


def add_to_watched(user_data, movie):
    '''GOAL: passing in user_data and movie
    add movie to user_data

    append dictionary to list of watched'''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    # Iterates through every movie dict stored in watchlist
    for i in range(len(user_data["watchlist"])):
        # Checks to see if the title is in the user's watchlist. If it is,
        # it adds movie dict to watched, and removes it from watchlist.
        if title == user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            del user_data["watchlist"][i]

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):

    if not user_data["watched"]:
        return 0.0

    total = 0

    for movie_dict in user_data["watched"]:
        movie_rating = movie_dict.get("rating", 0.0)
        total += movie_rating

    average = total/len(user_data["watched"])

    return average

    # looping the watched_list
    # get rating value
    # compare values
    # count number

    # calculate average


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
