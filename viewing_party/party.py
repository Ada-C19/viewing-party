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
    recommended_movies = []
    for friend in user_data["friends"]: #iterate through friends
        for friend_movie in friend["watched"]: #iterate through friend movies
            is_recommended = True #flag saying movie is recommended or not
            #if the movie is in user_data["watched"]:, recommended = False
            #if the movie's "host" is not in user_data["subscriptions"] recommended = false
            # after passing these tests, if it is still recommended, append it to the list of recommended movie dictionaries
    return recommended_movies




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# title = True
# genre = True
# rating = True
# user_data = {
#     "watched": [{
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#     }, {
#         "title": "Title A",
#         "genre": "Romance",
#         "rating": 4.7}, 
#         {
#         "title": "Title A",
#         "genre": "Romance",
#         "rating": 3.5
#     }]
#     }
# get_watched_avg_rating(user_data)
# get_most_watched_genre(user_data)
# movie2 = {
#         "title": "Title B",
#         "genre": "Horror",
#         "rating": 3.5
#     }
# watch_movie(user_data, title)

# create_movie(title, genre, rating)
# add_to_watched(user_data, movie)
# add_to_watched(user_data, movie2)
# print(user_data)


# title = "MOVIE_TITLE_1"
# genre = "GENRE_1"
# rating = "RATING_1"
# create_movie(title, genre, rating)