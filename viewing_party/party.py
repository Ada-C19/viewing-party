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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

