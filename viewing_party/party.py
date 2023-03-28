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


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

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