# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating: 
        return { "title": title, "genre": genre, "rating": rating}
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            watched.append(movie)
            return user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0
    if len(user_data["watched"]) < 1:
        return 0.0
    for movie in user_data["watched"]:
        rating_sum += movie["rating"]
        rating_sum = float(rating_sum)
    avg_rating = rating_sum / len(user_data["watched"])
    return avg_rating


def get_most_watched_genre(user_data):
    genre_list = []
    if len(user_data["watched"]) < 1:
        return None
    for movie in user_data["watched"]:
        genre = movie.get("genre")
        genre_list.append(genre)
    genre_count = max(set(genre_list), key=genre_list.count)
    return genre_count

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    my_unique_movies = []
    for my_movies in user_data["watched"]:
        unique_movie = True
        for friend in user_data["friends"]:
            for friends_movies in friend["watched"]:
                if my_movies["title"] == friends_movies["title"]:
                    unique_movie = False
        if unique_movie is True:
            my_unique_movies.append(my_movies)
    return my_unique_movies


def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for friends_movies in friend["watched"]:
            unique_movie = True
            for my_movies in user_data["watched"]:
                if friends_movies["title"] == my_movies["title"]:
                    unique_movie = False
            if unique_movie is True:
                movie_already_in_list = False
                for movie in friends_unique_movies:
                    if friends_movies["title"] == movie["title"]:
                        movie_already_in_list = True
                if movie_already_in_list is False:
                    friends_unique_movies.append(friends_movies)
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    subscriptions = user_data["subscriptions"]
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    recommended_movies = []
    user_watched_titles = [movie["title"] for movie in user_watched]
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_titles and movie["host"] in subscriptions:
                if movie not in recommended_movies:    
                    recommended_movies.append(movie)
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    print(most_watched_genre)
    movie_recs = []
    friends_movies = get_friends_unique_watched(user_data)
    for movie in friends_movies:
        if movie["genre"] == most_watched_genre:
            movie_recs.append(movie)
    return movie_recs


def get_rec_from_favorites(user_data):
    friends_movie_recs = []
    favorites = user_data["favorites"]
    unique_watched = get_unique_watched(user_data)
    for movie in favorites:
        if movie in unique_watched:
            friends_movie_recs.append(movie)
    return friends_movie_recs
