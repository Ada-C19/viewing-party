# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if not (title and genre and rating):
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    watch_movie(user_data, title)
		if title is not in user’s watchlist
			return user_data
		else
			remove that movie from watchlist
			add it to watched
			return user_data
    """
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
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

