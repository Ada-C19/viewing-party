# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    if movie:
       user_data["watched"].append(movie)
    return user_data

def add_to_watchlist (user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watch_list = user_data.get("watchlist")
    for movie in watch_list:
        if title == movie.get("title"):
            watch_list.remove(movie)
            user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    watched_list = user_data.get("watched")
    sum = 0.0
    for movie in watched_list:
        current_rating = movie["rating"]
        sum += current_rating
    if len(watched_list) == 0:
        return 0.0
    avg_rating = sum / len(watched_list)

    return avg_rating

def get_most_watched_genre(user_data):
    watched_list = user_data.get("watched")
    most_watched_count = 0
    most_watched = None
    genre_dict = {}
    
    for movie in watched_list:
        current_genre = movie["genre"]
        if current_genre in genre_dict.keys():
            genre_dict[current_genre] += 1
        else:
            genre_dict[current_genre]= 1
    for genre, frequency in genre_dict.items():
        if most_watched_count < frequency:
            most_watched_count = frequency
            most_watched = genre
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

