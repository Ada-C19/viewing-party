# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if  title and genre and rating: 
        return {
            "title": title,
            "genre": genre,
            "rating": rating 
        }
    return None

def add_to_watched(user_data, movie): 
    if movie.items():
        user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title): 
    if title not in [movie["title"] for movie in user_data["watchlist"]]:
        return user_data
    for value in user_data.values():
        for movie in value: 
            if movie["title"] == title: 
                user_data["watched"].append(movie)
                user_data["watchlist"].remove(movie)
                return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 
    sum = 0
    rating_average = 0
    for watched in user_data["watched"]: 
        sum += watched["rating"]
        rating_average = sum / len(user_data["watched"])
    return rating_average

def get_most_watched_genre(user_data):
    genres = []
    if user_data["watched"]:
        for movie in user_data["watched"]:
            genres.append(movie["genre"])
        return max(genres, key=genres.count)
    return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    movies_user_watched = []
    for movies in user_data["watched"]:
        movies_user_watched.append(movies)
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            if film in movies_user_watched:
                movies_user_watched.remove(film)
    return movies_user_watched

def get_friends_unique_watched(user_data):
    movies_friends_watched = []
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            if film not in movies_friends_watched:
                movies_friends_watched.append(film)
    for movie in user_data["watched"]:
        if movie in movies_friends_watched:
            movies_friends_watched.remove(movie)
    return movies_friends_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data): 
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for film in friends_unique_movies: 
        if film["host"] in user_data["subscriptions"] and film not in recommended_movies:
                recommended_movies.append(film)
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    fav_genre_movies = get_most_watched_genre(user_data)
    for film in friends_unique_movies:
        if film not in recs_by_genre and film["genre"] == fav_genre_movies:
            recs_by_genre.append(film)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    recommended_movies = []
    user_unique_movies = get_unique_watched(user_data)
    for user_favorite_movie in user_data["favorites"]: 
        if user_favorite_movie in user_unique_movies: 
            recommended_movies.append(user_favorite_movie)
    return recommended_movies