# ------------- WAVE 1 --------------------
"""Create and modify movie data"""


def create_movie(title, genre, rating):
    """create a movie dictionary"""
    if title is None or genre is None or rating is None:
        return None
    return {"title": title, "genre": genre, "rating": rating}


def add_to_watched(user_data, movie):
    """append movie dictionary to user_data "watched" list"""
    user_data["watched"].append(
        create_movie(movie["title"], movie["genre"], movie["rating"])
    )
    return user_data


def add_to_watchlist(user_data, movie):
    """append movie dictionairy to user_data "watchlist" list"""
    user_data["watchlist"].append(
        create_movie(movie["title"], movie["genre"], movie["rating"])
    )
    return user_data


def watch_movie(user_data, title):
    """Move a movie from user_data "watchlist" list to "watched" list"""

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    """Return the user's average movie rating"""
    rating = 0
    try:
        for movie in user_data["watched"]:
            rating += movie["rating"]
        return rating / len(user_data["watched"])
    except ZeroDivisionError:
        return 0.0


def get_most_watched_genre(user_data):
    """Return the user's most frequently watched genre"""
    genre_list = []
    try:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])

        sorted_genre_list = sorted(genre_list, key=genre_list.count, reverse=True)
        return sorted_genre_list[0]
    except IndexError:
        return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    """Return movies the user has watched that their friends have not watched."""
    user_movies_watched = user_data["watched"]  # list of dicts of movies
    user_movie_titles = [
        movie["title"].lower() for movie in user_movies_watched
    ]  # list of titles only

    friends_movies_watched = []  # list of dicts of movies (all friends combined)
    for friend in user_data["friends"]:
        friends_movies_watched.extend(friend["watched"])
    friend_movie_titles = [
        movie["title"].lower() for movie in friends_movies_watched
    ]  # list of titles only

    user_unique_movie_titles = set(user_movie_titles) - set(friend_movie_titles)
    user_unique_movies = []

    for movie in user_movies_watched:
        if movie["title"].lower() in user_unique_movie_titles:
            user_unique_movies.append(movie)

    return user_unique_movies


def get_friends_unique_watched(user_data):
    """Return movies the user's friends have watched that the user has not watched."""
    user_movies_watched = user_data["watched"]  # list of dicts of movies
    user_movie_titles = [
        movie["title"].lower() for movie in user_movies_watched
    ]  # list of titles only

    friends_movies_watched = []  # list of dicts of movies (all friends combined)
    for friend in user_data["friends"]:
        friends_movies_watched.extend(friend["watched"])
    friend_movie_titles = [
        movie["title"].lower() for movie in friends_movies_watched
    ]  # list of titles only

    friend_unique_movie_titles = set(friend_movie_titles) - set(user_movie_titles)
    friend_unique_movies = []

    for movie in friends_movies_watched:
        if (
            movie["title"].lower() in friend_unique_movie_titles
            and movie not in friend_unique_movies
        ):
            friend_unique_movies.append(movie)

    return friend_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    """Return recommended movies that the user subscribes to."""
    recommended_movies = []
    friends_unique = get_friends_unique_watched(user_data)

    for movie in friends_unique:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    """Return recommended movies of the user's most frequently watched genre."""
    most_watched_genre = get_most_watched_genre(user_data)
    movies_not_watched = get_friends_unique_watched(user_data)

    recommended_by_genre = []

    for movie in movies_not_watched:
        if (
            most_watched_genre
            and movie["genre"].capitalize() == most_watched_genre.capitalize()
        ):
            recommended_by_genre.append(movie)

    return recommended_by_genre


def get_rec_from_favorites(user_data):
    """Return movies the user recommends in favorites"""
    unique_movies = get_unique_watched(user_data)
    recommended_favorites = []

    for movie in user_data["favorites"]:
        if movie in unique_movies:
            recommended_favorites.append(movie)

    return recommended_favorites
