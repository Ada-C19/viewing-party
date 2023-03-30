# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if (not title) or (not genre) or (not rating):
        return None
      
    if not all((isinstance(title, str), isinstance(genre, str),
               isinstance(rating, float))):
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


def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
   
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            move_movie = movie
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(move_movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    sum = 0
    if not user_data["watched"]:
        return 0.0

    for movie in user_data["watched"]:
        sum += movie["rating"]

    return sum/len(user_data["watched"])


def get_most_watched_genre(user_data):
    genre_list = []

    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    # Returns the first instance of a most-watched genre
    return max(genre_list, key=genre_list.count)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    friend_watched = {movie_dict["title"] for friend_dict in user_data["friends"]
                      for movie_dict in friend_dict["watched"]}

    user_watched = [user_dict for user_dict in user_data["watched"]
                    if user_dict["title"] not in friend_watched]

    return user_watched


def get_friends_unique_watched(user_data):
    friend_watched = []
    friend_watched_titles = []
    
    user_watched = [user_dict["title"] for user_dict in user_data["watched"]]

    for friend_dict in user_data["friends"]:
        for movie_dict in friend_dict["watched"]:
            friend_movie_title = movie_dict["title"]
            if (friend_movie_title not in friend_watched_titles and
                    friend_movie_title not in user_watched):
                friend_watched_titles.append(friend_movie_title)
                friend_watched.append(movie_dict)

    return friend_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_only_watched = get_friends_unique_watched(user_data)

    recommendations = [movie for movie in friend_only_watched
                       if movie["host"] in user_data["subscriptions"]]

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friend_only_watched = get_friends_unique_watched(user_data)

    recommendations = [movie for movie in friend_only_watched
                       if movie["genre"] == most_watched_genre]

    return recommendations


def get_rec_from_favorites(user_data):
    only_user_watched = get_unique_watched(user_data)

    recommendations = [fav_movie for fav_movie in user_data['favorites']
                       for movie in only_user_watched
                       if movie["title"] == fav_movie["title"]]

    return recommendations

