# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # Input validation
    if not title or not genre or not rating:
        return None
    
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # Return the dictionary
    return movie

def add_to_watched(user_data, movie):
    if not movie:
        return user_data

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if not movie:
        return user_data
    
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data['watchlist'])):
        title_from_dict = user_data['watchlist'][i]['title']

    # If title is in watchlist, remove that movie from watchlist
        if title_from_dict == title:
            dict_from_list = user_data['watchlist'][i]
            user_data["watchlist"].remove(dict_from_list)
            # Add that movie to "watched"
            user_data["watched"].append(dict_from_list)

    return user_data


print(watch_movie({
            "watchlist": [{
                "title": "Scooby Doo",
                "genre": "GENRE_1",
                "rating": 1
            }],
            "watched": []
        }, "Scooby Doo"))

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

