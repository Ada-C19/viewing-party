# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    for key, value in new_movie.items():
        if value == None:
            return None

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    add_movie = user_data
    return add_movie

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    watch_list = user_data
    return watch_list

def watch_movie(user_data, title):
    # Create a new copy of the user_data dictionary to avoid modifying the original
    new_user_data = user_data.copy()
    # Get the current watchlist and watched lists from the new_user_data dictionary,
    # or create empty lists if they don't exist
    watchlist = new_user_data.get("watchlist", [])
    watched_list = new_user_data.get("watched", [])
    # Check each movie in the watchlist to see if it matches the given title
    for movie in watchlist:
        if movie["title"] == title:
            if len(watchlist) > 0:
                watched_list.append(watchlist[0])
                watchlist.remove(watchlist[0])
            else:
            # If a match is found, remove the movie from the watchlist and add it to the watched list
                watchlist.remove(movie)
                watched_list.append(movie)
            # Update the new_user_data dictionary with the modified watchlist and watched list
                new_user_data["watchlist"] = watchlist
                new_user_data["watched"] = watched_list
            # Return the updated new_user_data dictionary
                return new_user_data
    # If no match is found, return the original user_data dictionary unchanged
    return new_user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0.0
    movie_count = 0 
    for key, value in user_data.items():
        for movie in value:
            sum += movie["rating"]
            movie_count += 1

    if sum == 0.0:
        return sum
    total = sum / movie_count
    return total

def get_most_watched_genre(user_data):
    genre_dict = {}
    if user_data["watched"] == []:
        return None
    for key, value in user_data.items():
        for movie in value:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1

    high_genre = max(genre_dict.values())

    for key, value in genre_dict.items():
        if value == high_genre:
            return key

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched = user_data["watched"].copy()
    friends = user_data["friends"].copy()
    for friend in friends: 
        for movie in friend["watched"]: 
            if movie in watched:
                watched.remove(movie)
    return watched

def get_friends_unique_watched(user_data):
    watched = user_data ["watched"].copy()
    friends = user_data ["friends"].copy()
    unique_movies = []
    for friend in friends: 
        for movie in friend["watched"]:
            if movie not in watched and movie not in unique_movies:
                unique_movies.append(movie)
    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

