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

    for friend in range(len(user_data["friends"])):
        for movie in range(len(user_data["friends"][friend]["watched"])):
            movie_friend_has_watched = user_data["friends"][friend]["watched"][movie]
            if movie_friend_has_watched in user_data["watched"]:
                continue
            elif movie_friend_has_watched in movie_recs:
                continue
            elif movie_friend_has_watched["host"] in user_data["subscriptions"]:
                movie_recs.append(movie_friend_has_watched)
    
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_count = []
    for movie in range(len(user_data["watched"])):
        genre_count.append(user_data["watched"][movie]["genre"])

    current_favorite_count = 0
    favorite_genre = ""
    for genre in genre_count:
        if genre_count.count(genre) > current_favorite_count:
            current_favorite_count = genre_count.count(genre)
            favorite_genre = genre
    
    recs_by_genre = []
    for friend in range(len(user_data["friends"])):
        for movie in range(len(user_data["friends"][friend]["watched"])):
            movie_to_recommend = user_data["friends"][friend]["watched"][movie]
            if movie_to_recommend in recs_by_genre:
                continue
            if movie_to_recommend in user_data["watched"]:
                continue
            elif movie_to_recommend["genre"] == favorite_genre:
                recs_by_genre.append(movie_to_recommend)

    return recs_by_genre


def get_rec_from_favorites(user_data):
    recs_by_favs = []

    for i in range(len(user_data["favorites"])):
        favorite_movie = user_data["favorites"][i]
        recs_by_favs.append(favorite_movie)
        for friend in range(len(user_data["friends"])):
            friend_watched_list = user_data["friends"][friend]["watched"]
            if favorite_movie in friend_watched_list \
            and favorite_movie in recs_by_favs:
                recs_by_favs.remove(favorite_movie)

    return recs_by_favs