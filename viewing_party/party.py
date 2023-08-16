# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = { 
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data.get("watchlist", [])
    watched = user_data.get("watched", [])

    found_movie = None

    for movie in watchlist:
        if movie["title"] == title:
            found_movie = movie
            watchlist.remove(movie)
            watched.append(movie)
            
        
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    if not watched_movies:
        return 0.0
    
    total_ratings = sum(movie.get("rating", 0) for movie in watched_movies)
    average_rating = total_ratings / len(watched_movies)
    return average_rating

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    if not watched_movies:
        return None
    
    genre_count = {}
    for movie in watched_movies:
        genre = movie.get("genre")
        if genre:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    
    most_watched_genre = max(genre_count, key=genre_count.get)
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    friends_watched_list = []
    friends_watched_set = None
    friends_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
            friends_watched_set = set(friends_watched_list)

    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_set and movie not in friends_list:
            friends_list.append(movie)

    return friends_list


def get_friends_unique_watched(user_data):

    user_watched = set([movie["title"] for movie in user_data["watched"]])
    friends_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie not in friends_list:
                friends_list.append(movie)

    return friends_list



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    unseen_by_user = get_friends_unique_watched(user_data)
    user_subscriptions = user_data["subscriptions"]
    available_recs = []

    for movie in unseen_by_user:
        if movie["host"] in user_subscriptions:
            available_recs.append(movie)
    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    user_watched = set([movie["title"] for movie in user_data["watched"]])
    friends_unique_watched = get_friends_unique_watched(user_data)

    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1
    best_genre = None
    best_genre_count = 0
    for genre, count in genre_count.items():
        if count > best_genre_count:
            best_genre = genre
            best_genre_count = count

    recommended_movies = []
    for movie in friends_unique_watched:
        if movie["title"] not in user_watched and movie["genre"] == best_genre:
            recommended_movies.append(movie)

    return recommended_movies


# 2ND function in Wave 5
def get_rec_from_favorites(user_data):
    
    user_favorites = user_data["favorites"]
    recommended_movies = []

    if user_data["friends"] == []:
        return user_favorites
    else:
        unseen_by_friends = get_unique_watched(user_data)
        for movie in unseen_by_friends:
            if movie in user_favorites:
                recommended_movies.append(movie)
    return recommended_movies