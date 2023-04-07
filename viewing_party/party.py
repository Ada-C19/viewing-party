# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None
    
    movie_dict = {}
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
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            break
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    sum = 0 
    for movie in user_data["watched"]:
        rating = movie["rating"]
        sum += rating

    return sum / len(user_data["watched"])
    

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_counting_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_counting_dict:
            genre_counting_dict[movie["genre"]] = 1
        else:
            genre_counting_dict[movie["genre"]] += 1
    
    most_watched_genre = max(genre_counting_dict, key=genre_counting_dict.get)

    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# ----------------------------------------

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    user_title = []

    for movie in user_data["watched"]:
        user_title.append(movie["title"])
    
    for friend in user_data["friends"]:
        for movie_my_friend_watched in friend["watched"]:
            if movie_my_friend_watched["title"] not in user_title \
                    and movie_my_friend_watched not in friends_unique_movies:
                friends_unique_movies.append(movie_my_friend_watched)
    
    return friends_unique_movies

def get_unique_watched(user_data):
    unique_watched = user_data["watched"].copy()

    for friend in user_data["friends"]: 
        for movie_to_check in friend["watched"]:
            if movie_to_check in unique_watched:
                unique_watched.remove(movie_to_check)

    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recs = []

    if user_data['watched'] == []:
        return movie_recs

    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)
    
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    favorite_genre = get_most_watched_genre(user_data)
    
    recs_by_genre = []
    for friend in user_data["friends"]:
        for movie_to_recommend in friend["watched"]:
            is_movie_in_recs = movie_to_recommend in recs_by_genre
            is_movie_in_watched = movie_to_recommend in user_data["watched"]
            is_movie_favorite_genre = movie_to_recommend["genre"] == favorite_genre
            if not is_movie_in_recs and not is_movie_in_watched \
                    and is_movie_favorite_genre:
                recs_by_genre.append(movie_to_recommend)

    return recs_by_genre


def get_rec_from_favorites(user_data):
    recs_by_favs = []

    for favorite_movie in user_data["favorites"]:
        if favorite_movie in get_unique_watched(user_data):
            recs_by_favs.append(favorite_movie)

    return recs_by_favs