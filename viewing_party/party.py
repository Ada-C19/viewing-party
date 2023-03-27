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
    pass





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# USER_DATA_4 = {
#     "watched": [
#         FANTASY_1b, 
#         FANTASY_2b, 
#         FANTASY_3b, 
#         ACTION_1b, 
#         INTRIGUE_1b, 
#         INTRIGUE_2b
#         ],  
#     "friends":  [
#         {
#             "watched": [
#                 FANTASY_1b,
#                 FANTASY_3b,
#                 FANTASY_4b,
#                 HORROR_1b,
#             ]
#         },
#         {
#             "watched": [
#                 FANTASY_1b,
#                 FANTASY_4b,
#                 ACTION_1b,
#                 INTRIGUE_1b,
#                 INTRIGUE_3b,
#             ]
#         }  
#     ]
# }

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

    # users_movies = set(tuple(movie) for movie in movies_user_watched)
    # friends_movies = set(tuple(movie) for movie in movies_friends_watched)
    # return users_movies - friends_movies
    
def get_friends_unique_watched(user_data):
    pass
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

