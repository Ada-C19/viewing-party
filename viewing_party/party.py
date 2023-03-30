# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        return {"title": title, 
                "genre": genre,
                "rating": rating}
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
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
    sum = 0
    average = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]: 
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average

def create_frequency_counter(user_data):
    frequency_counter = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in frequency_counter:
            frequency_counter[movie["genre"]] = 1
        else:
            frequency_counter[movie["genre"]] += 1
    return frequency_counter

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
            return None
    frequency_counter = create_frequency_counter(user_data)
    mode = 0
    mode_genre = ""
    for genre_name, genre_frequency in frequency_counter.items():
        if genre_frequency > mode:
            mode = genre_frequency
            mode_genre = genre_name
    return mode_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_unique_watched(user_data):
    result = []
    for friends in user_data["friends"]:
        for friends_watched_movies in friends["watched"]:
            if friends_watched_movies not in user_data["watched"] and friends_watched_movies not in result:
                result.append(friends_watched_movies)
    return result

def get_unique_watched(user_data):
    result = []
    friends_movies_watch = []
    for friend in user_data["friends"]:
        for friends_watched_movie in friend["watched"]:
            friends_movies_watch.append(friends_watched_movie)
    for movie in user_data["watched"]:
        if movie not in friends_movies_watch:
            result.append(movie)
    return result

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []
    movies_to_watch = get_friends_unique_watched(user_data)
    for movies in movies_to_watch:
        if movies["host"] in user_data["subscriptions"]:
            recommendations.append(movies)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    movie_recs = []
    most_watched_genre = get_most_watched_genre(user_data)
    unique_watched_movies = get_friends_unique_watched(user_data)
    for movie in unique_watched_movies:
        if movie["genre"] == most_watched_genre:
            movie_recs.append(movie)
    return movie_recs

def get_rec_from_favorites(user_data):
    movie_recs = []
    user_unique_watched_movies = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in user_unique_watched_movies:
            movie_recs.append(movie)
    return movie_recs
