# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title is None or genre is None or rating is None:
        return None
    
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):

    if movie:
       user_data["watched"].append(movie)

    return user_data

def add_to_watchlist (user_data, movie):

    if movie:
        user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    watch_list = user_data.get("watchlist")

    for movie in watch_list:
        if title == movie.get("title"):
            watch_list.remove(movie)
            user_data["watched"].append(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    avg_rating = 0.0
    watched_list = user_data.get("watched")
    rating_sum = 0.0

    for movie in watched_list:
        current_rating = movie["rating"]
        rating_sum += current_rating

    if len(watched_list) == 0:
        return avg_rating
    
    avg_rating = rating_sum / len(watched_list)

    return avg_rating

def get_most_watched_genre(user_data):

    watched_list = user_data.get("watched")
    genre_dict = {}
    
    if not watched_list:
        return None
    
    for movie in watched_list:
        current_genre = movie["genre"]
        genre_dict[current_genre] = genre_dict.get(current_genre, 0) + 1
      
    if not genre_dict:
        return None
    
    return max(genre_dict, key=genre_dict.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
    
def get_friend_watched_list(user_data):

    friend_list = user_data.get("friends")
    friend_watched_list = []
    

    for friend in friend_list:
        for movie in friend["watched"]:
            friend_watched_list.append(movie)
        
    return friend_watched_list


def get_unique_watched(user_data): 

    watched_list = user_data.get("watched")
    friend_watched_list = get_friend_watched_list(user_data)

    unique_movie = []

    for movie in watched_list:
        if movie not in friend_watched_list:
                unique_movie.append(movie)
            
    return unique_movie


def get_friends_unique_watched(user_data):

    watched_list = user_data.get("watched")
    friend_watched_list = get_friend_watched_list(user_data)
    friends_unique_watched_list = []
    
    no_dup_friends_watched_list = [i for n, i in enumerate(friend_watched_list)
        if i not in friend_watched_list[n + 1:]]

    for movie in no_dup_friends_watched_list:
        if movie not in watched_list:
                friends_unique_watched_list.append(movie)
    
    return friends_unique_watched_list

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    subscriptions_list = user_data.get("subscriptions")
    friends_watched_list = get_friends_unique_watched(user_data)
    recommended_movie_list = []

    for movie in friends_watched_list:
        if movie["host"] in subscriptions_list:
            recommended_movie_list.append(movie)

    return recommended_movie_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre (user_data):

    recommended_movie = []
    user_watched_most_list = get_most_watched_genre(user_data)
    only_friend_watched_list = get_friends_unique_watched(user_data)
    
    if not only_friend_watched_list or not user_watched_most_list:
        return recommended_movie
    
    for movie in only_friend_watched_list:
        if movie["genre"] in user_watched_most_list:
            recommended_movie.append(movie)
    
    return recommended_movie



def get_rec_from_favorites (user_data):

    recommended_movie = []
    user_favorite_movie = user_data["favorites"]
    user_unique_watched_movie = get_unique_watched(user_data)

    if not user_favorite_movie or not user_unique_watched_movie:
        return recommended_movie

    for movie in user_unique_watched_movie:
        if movie in user_favorite_movie:
            recommended_movie.append(movie)

    return recommended_movie
