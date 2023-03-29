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


# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    # initialize emoty list
    # nested dictionary - friends - watched
    # append list

    friends_list = []

    for each_friend_dict in user_data.get("friends", []):
        for each_movie_dict in each_friend_dict.get("watched", []):
            friends_list.append(each_movie_dict)

# initialize a set of friend's list title
# loop through the friends_list:
# get value of title
# if title is existent, add the title to the set -

    friends_titles = set()
    for each_movie_dict in friends_list:
        title = each_movie_dict.get("title")
        if title:
            friends_titles.add(title)

# loop through the user_data["watched"]

    unique_movies = []
    for each_movie_dict in user_data["watched"]:
        title = each_movie_dict.get("title", [])
        # if title is not in friends's list then add the dictionary to the unique list
        if title and title not in friends_titles:
            unique_movies.append(each_movie_dict)

    return unique_movies


def get_friends_unique_watched(user_data):
    user_titles = set()
    friends_titles = set()
    unique_watched = []

    for movie in user_data["watched"]:
        user_titles.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles.add(movie["title"])

    unique_titles = friends_titles - user_titles

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_titles and movie not in unique_watched:
                unique_watched.append(movie)

    return unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
