# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # validate_parameters (empty strings and zero evaluate to Falsy)
    if title and genre and rating:
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    movie_found = False
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            movie_found = True
            break
    if not movie_found:
        return user_data
            
    return user_data

# ****** Waves 2, 3, 4, 5: should not modify user_data ******

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_sum = 0
    if user_data["watched"] == []:
            average = 0.0
    else:
        for movie in user_data["watched"]:
            ratings_sum += movie["rating"]
        average = ratings_sum/len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
            return None
    
    genre_count_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count_dict:
            genre_count_dict[movie["genre"]] += 1
        else:
            genre_count_dict[movie["genre"]] = 1
    popular_genre = max(genre_count_dict, key=genre_count_dict.get)
    return popular_genre    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

