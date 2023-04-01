# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
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
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)            
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_sum = 0
    if not user_data["watched"]:
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

def friends_movies(user_data):
    friends_movie_data = []
    for movies_dict in user_data["friends"]:
        for movies in movies_dict["watched"]: 
            friends_movie_data.append(movies) 
    return (friends_movie_data)

def get_unique_watched(user_data):
    user_unique_movies =[]
    for movie in user_data["watched"]:
        if movie not in friends_movies(user_data):
            user_unique_movies.append(movie)
    return(user_unique_movies)

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    filter_out_dupes = []
    for movie in friends_movies(user_data):
        if movie not in user_data["watched"]:
            friends_unique_movies.append(movie)

    for movie in friends_unique_movies:
        if movie not in filter_out_dupes:
            filter_out_dupes.append(movie)
    return (filter_out_dupes)

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    rec_based_on_genre = []
    most_freq_genre = get_most_watched_genre(user_data)
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == most_freq_genre:
            rec_based_on_genre.append(movie)
    return rec_based_on_genre

def get_rec_from_favorites(user_data):
    rec_based_on_favorites = []
    for movie in get_unique_watched(user_data):
        if movie in user_data["favorites"]:
            rec_based_on_favorites.append(movie)
        else:
            rec_based_on_favorites = []
    return rec_based_on_favorites