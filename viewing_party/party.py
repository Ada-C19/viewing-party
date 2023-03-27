# ------------- WAVE 1 --------------------
import copy
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating    }
    return movie    

def add_to_watched(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watched"].append(movie)
    return user_data_copy

def add_to_watchlist(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watchlist"].append(movie)
    return user_data_copy

def watch_movie(user_data, title):
    user_data_copy = copy.deepcopy(user_data)
    in_watchlist = False
    movie_index = 0
    for movie in user_data_copy["watchlist"]:
        if movie["title"] == title:
            in_watchlist = True
            break
        movie_index += 1
    if not in_watchlist:
        return user_data_copy
    movie = user_data_copy["watchlist"][movie_index]
    del user_data_copy["watchlist"][movie_index]
    user_data_copy["watched"].append(movie)
    return user_data_copy


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    num_of_movies = len(user_data["watched"])
    if num_of_movies == 0:
        return 0.0
    ratings = 0
    for movie in user_data["watched"]:
        ratings += movie["rating"]
    average_rating = ratings / num_of_movies
    return average_rating   

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_counts = {}
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        try:
            genre_counts[movie_genre] += 1
        except KeyError:
            genre_counts[movie_genre] = 1
    max_watch_count = 0
    for genre, watch_count in genre_counts.items():
        if watch_count > max_watch_count:
            max_watch_count = watch_count
            max_genre = genre
    return max_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_titles = []
    for movie in user_data["watched"]:
        friend_watched = False
        for friend in user_data["friends"]:
            for friends_movie in friend["watched"]:
                if friends_movie["title"] == movie["title"]:
                    friend_watched = True
                    break
        if not friend_watched:    
            unique_titles.append(movie)
    return unique_titles   

def get_friends_unique_watched(user_data):
    unique_titles = []
    unique_title_names = []
    for friend in user_data["friends"]:
        for friends_movie in friend["watched"]:
            user_watched = False
            for movie in user_data["watched"]:
                if friends_movie["title"] == movie["title"]:
                    user_watched = True
                    break
            if not user_watched and friends_movie["title"] not in unique_title_names:
                unique_titles.append(friends_movie)
                unique_title_names.append(friends_movie["title"])

    return unique_titles     

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

