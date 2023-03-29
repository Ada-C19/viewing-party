# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating}
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if user_data["watchlist"][index]["title"] == title:
            add_to_watched(user_data, user_data["watchlist"][index])
            del user_data["watchlist"][index]
            break

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if user_data["watched"]:
        watched_list = user_data["watched"]
        ratings_total = 0

        for movie in watched_list:
            ratings_total += movie["rating"]
        
        avg = ratings_total / len(watched_list)

        return avg
    return 0.0


def get_most_watched_genre(user_data):
    # first validate that user_data["watched"] is truthy, else return None
    if not user_data["watched"]:
        return None
        
    # store the nested list in its own variable for ease of access
    watched_list = user_data["watched"]

    # declare counter variables for the amount of movies in each genre
    num_fantasy_movies = 0
    num_action_movies = 0
    num_intrigue_movies = 0

    # iterate through the watched list movies to increment the corresponding genre count
    for movie in watched_list:
        if movie["genre"] == "Fantasy":
            num_fantasy_movies += 1
        elif movie["genre"] == "Action":
            num_action_movies += 1
        elif movie["genre"] == "Intrigue":
            num_intrigue_movies += 1

    most_watched = max(num_action_movies, num_fantasy_movies, num_intrigue_movies)

    # find the corresponding genre to the most_watched amount
    if num_action_movies == most_watched:
        return "Action"
    elif num_fantasy_movies == most_watched:
        return "Fantasy"
    elif num_intrigue_movies == most_watched:
        return "Intrigue"

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    recommended_movies = []

    # evaluate if there is data in the user's watched list
    if not user_data["watched"]:
        return recommended_movies
    
    # retrieve the most watched genre for that user
    most_watched_genre = get_most_watched_genre(user_data)

    # create an initial recommended_movies list based on
    # all of the movies the friends have watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre and movie not in recommended_movies:
                recommended_movies.append(movie)
    
    # evaluate if recommended movies is truthy, else return the empty list
    if not recommended_movies:
        return recommended_movies

    # remove any movies from recommended_movies that the user has already seen
    for movie in user_data["watched"]:
        if movie in recommended_movies:
            recommended_movies.remove(movie)
    
    return recommended_movies


def get_rec_from_favorites(user_data):

    # establish empty lists to hold our movie data
    friend_watched_list = []
    recommended_movies = []

    # get the movies in from friends watched lists:
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_watched_list:
                friend_watched_list.append(movie)

    # compare each movie from the user's favorites to the friend watched list:
    for movie in user_data["favorites"]:
        if movie not in friend_watched_list:
            recommended_movies.append(movie)

    return recommended_movies

    