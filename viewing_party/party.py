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

def get_most_watched_genre(user_data):
    user_genres = {}
    most_watched = None
    times_watched = 0

    # Returns None if watched list is empty
    if not user_data["watched"]:
        return None
    
    # Iterates through each movie in watched list and adds 
    # each genre to a user_genres dictionary with an initial value of 1. 
    # If the genre already exists in user_genres, it +1 to the value.
    for movie in user_data["watched"]:
        if movie["genre"] not in user_genres:
            user_genres[movie["genre"]] = 1
        else:
            user_genres[movie["genre"]] += 1
    
    # Iterates through the genres in user_genres to find most watched
    for genre in user_genres:
        if user_genres[genre] > times_watched:
            most_watched = genre
            times_watched = user_genres[genre]
    
    return most_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
