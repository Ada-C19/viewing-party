# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if  title and genre and rating: 
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating 
        }
        return new_movie
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
    movies_friends_watched = []
    for movies in user_data["watched"]:
        movies_user_watched.append(movies)
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            movies_friends_watched.append(film)
    unique_movies = []
    for movies in movies_user_watched:
        if movies not in movies_friends_watched:
            unique_movies.append(movies)
    return unique_movies


def get_friends_unique_watched(user_data):
    movies_user_watched = []
    movies_friends_watched = []
    for movies in user_data["watched"]:
        movies_user_watched.append(movies)
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            movies_friends_watched.append(film)
    friend_unique_movies = []
    for movies in movies_friends_watched:
        if movies not in movies_user_watched:
            if movies not in friend_unique_movies:
                friend_unique_movies.append(movies)
    return friend_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data): 
    # recommended_movies = []
    # friends_watched = []
    # friends_movies = []
    # for friend in user_data["friends"]: 
    #     for movie in friend["watched"]:
    #         friends_watched.append(movie)
    #         if movie not in user_data["watched"]:
    #             friends_movies.append(movie)

    # for movie in user_data["watched"]:
    #     user_host = movie["host"]
    #     for film in friends_movies: 
    #         if film["host"] in user_host: 
    #             if film not in recommended_movies:
    #                 recommended_movies.append(film)

    # return recommended_movies
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in user_data["watched"]:
        user_host = movie["host"]
        for film in friends_unique_movies: 
            if film["host"] in user_host: 
                if film not in recommended_movies:
                    recommended_movies.append(film)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
