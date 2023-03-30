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
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0 
    count = 0

    if user_data["watched"] != []:
        for i in range(len(user_data["watched"])):
            rating = user_data["watched"][i]["rating"]
            sum += rating
            count += 1
    if count > 0:
        return sum / count
    return 0.0
    

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_counting_dict = {}
    for i in range(len(user_data["watched"])):
        genre_to_count = user_data["watched"][i]["genre"]
        if genre_to_count not in genre_counting_dict:
            genre_counting_dict[genre_to_count] = 1
        else:
            genre_counting_dict[genre_to_count] += 1

    most_watched_genre = ""
    most_watched_count = 0

    for genre, count in genre_counting_dict.items():
        if count > most_watched_count:
            most_watched_genre = genre
            most_watched_count = count

    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# ----------------------------------------

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    user_title = []

    for i in range(len(user_data["watched"])):
        user_title.append(user_data["watched"][i]["title"])
    
    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j]["title"] not in user_title \
                and user_data["friends"][i]["watched"][j] not in friends_unique_movies:
                friends_unique_movies.append(user_data["friends"][i]["watched"][j])
    
    print(friends_unique_movies)
    return friends_unique_movies

def get_unique_watched(user_data):
    unique_watched = user_data["watched"].copy()

    for friend in range(len(user_data["friends"])): 
        for movie in range(len(user_data["friends"][friend]["watched"])):
            if user_data["friends"][friend]["watched"][movie] in unique_watched:
                unique_watched.remove(user_data["friends"][friend]["watched"][movie])

    return unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recs = []

    if user_data['watched'] == []:
        return movie_recs

    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j] in user_data["watched"]:
                continue
            elif user_data["friends"][i]["watched"][j] in movie_recs:
                continue
            elif user_data["friends"][i]["watched"][j]["host"] in\
            user_data["subscriptions"]:
                movie_recs.append(user_data["friends"][i]["watched"][j])
    
    return movie_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_count = []
    for i in range(len(user_data["watched"])):
        genre_count.append(user_data["watched"][i]["genre"])
    current_favorite_count = 0
    favorite_genre = ""
    for genre in genre_count:
        if genre_count.count(genre) > current_favorite_count:
            current_favorite_count = genre_count.count(genre)
            favorite_genre = genre
    
    recs_by_genre = []
    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j] in\
            recs_by_genre:
                continue
            if user_data["friends"][i]["watched"][j] in\
            user_data["watched"]:
                continue
            elif user_data["friends"][i]["watched"][j]["genre"] ==\
            favorite_genre:
                recs_by_genre.append(user_data["friends"][i]["watched"][j])

    return recs_by_genre


def get_rec_from_favorites(user_data):
    recs_by_favs = []

    for i in range(len(user_data["favorites"])):
        favorite_movie = user_data["favorites"][i]
        recs_by_favs.append(favorite_movie)
        for j in range(len(user_data["friends"])):
            if favorite_movie in user_data["friends"][j]["watched"] \
            and favorite_movie in  recs_by_favs:
                recs_by_favs.remove(favorite_movie)
    print(recs_by_favs)
    return recs_by_favs