# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {"title": title, "genre": genre, "rating": rating}
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    average_rating = 0.0

    if not user_data["watched"]:
        return average_rating
    
    for movie in user_data["watched"]:
        average_rating += movie["rating"]
    average_rating = average_rating / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    max_count = 0

    genres = count_genres(user_data)

    for count in genres.values():
        if count > max_count:
            max_count = count

    for key, value in genres.items():
        if value == max_count:
            return key
        
def count_genres(user_data):
    genres = {}

    for movie in user_data["watched"]:
        if movie["genre"] not in genres:
            genres[movie["genre"]] = 1
        else:
            genres[movie["genre"]] += 1

    return genres

# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    user_watched = []
    friend_watched = []
    friend_not_watched = []

    for movie in user_data["watched"]:
        user_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)

    for movie in user_watched:
        if movie not in friend_watched:
            friend_not_watched.append(movie)
    return friend_not_watched

def get_friends_unique_watched(user_data):
    user_watched = []
    friend_watched = []
    user_not_watched = []

    for movie in user_data["watched"]:
        user_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)

    for movie in friend_watched:
        if movie not in user_watched and movie not in user_not_watched:
            user_not_watched.append(movie)
    return user_not_watched

# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = [movie for movie in unique_movies if movie["host"] in user_data["subscriptions"]]

    return recommended_movies

# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    recommended_movies = [movie for movie in friends_watched if movie["genre"] == most_watched_genre]

    return recommended_movies

def get_rec_from_favorites(user_data):
    friends_not_watched = get_unique_watched(user_data)
    recommended_movies = [movie for movie in user_data["favorites"] if movie in friends_not_watched]

    return recommended_movies