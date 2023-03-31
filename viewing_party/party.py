# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    """Create a single movie dictionary to store title, genre, and rating."""
    if title and genre and rating:
        movie = {
        "title": title,
        "genre": genre,
        "rating": rating
        }
        return movie
    return None


def add_to_watched(user_data, movie):
    """Store the user's watched movies in a list contained by the key 'watched'."""
    user_data["watched"] += [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    """Store movies the user would like to watch 
    in a list contained by the key 'watchlist.'"""
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    """Relocate the movie from "watchlist" to "watched" if the user has watched the movie."""
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """Return the average rating for the user's watched movies."""
    ratings = 0
    movie_count = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            ratings += (movie["rating"])
            movie_count += 1
        avg_rating = ratings/movie_count
        return avg_rating
    return ratings


def get_genre_counts(user_data):
    """Return a dictionary of the occurrences of genres for each movie the user has watched."""
    genre_frequencies = {}
    if user_data["watched"]:
        for movie in user_data["watched"]:
            genre_frequencies[movie["genre"]] = 0
        for movie in user_data["watched"]:
            genre_frequencies[movie["genre"]] += 1
    return genre_frequencies


def get_most_watched_genre(user_data):
    """Return the genre with the highest occurrence out of movies the user has watched."""
    genre_frequencies = get_genre_counts(user_data)
    most_watched_genre, highest_count = None, 0
    for genre, count in genre_frequencies.items():
        if count > highest_count:
            most_watched_genre, highest_count = genre, count
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def make_friends_watched_list(user_data):
    """Make a list of the movies a user's friends have watched."""
    friends_movies = []
    for friend in user_data["friends"]:
        friends_movies +=friend["watched"]
    return friends_movies
    

def get_unique_watched(user_data):
    """Return a list of the movies watched by the user and not by their friends."""
    unique_movies = []
    friends_movies = make_friends_watched_list(user_data)
    for movie in user_data["watched"]:
        if not movie in friends_movies:
            unique_movies.append(movie)
    return unique_movies


def get_friends_unique_watched(user_data):
    """Return a list of movies watched by the user's friends and not by the user."""
    friends_unique_movies = []
    friends_movies = make_friends_watched_list(user_data)
    for movie in friends_movies:
        if not movie in user_data["watched"]:
            if not movie in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """Return a list of movies the user has not watched out of their 
    friends' watchlists that fall into the user's subscription access."""
    movie_recommendations = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"] and movie not in movie_recommendations:
            movie_recommendations.append(movie)
    return movie_recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    """Return a list of movies watched by the user's 
    friends that belong to the user's most watched genre."""
    top_genre = get_most_watched_genre(user_data)
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["genre"] == top_genre and movie not in recommended_movies:
            recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    """Return a list of the user's favorite movies that the friends have not seen."""
    recommended_movies = []
    user_unique_movies = get_unique_watched(user_data)
    for movie in user_unique_movies:
        if movie in user_data["favorites"]:
            recommended_movies.append(movie)
    return recommended_movies

    