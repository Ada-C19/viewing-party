import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None

    movie = {
        "title" : title, 
        "genre" : genre, 
        "rating" : rating
    }

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    new_user_data = {
        "watchlist" : user_data["watchlist"].copy(),
        "watched" : user_data["watched"].copy()
    }
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            new_user_data["watchlist"].remove(movie)
            new_user_data["watched"].append(movie)

    return new_user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Barbara
def get_watched_avg_rating(user_data):
    sum_rating = 0
    watched_movies = user_data["watched"]
    if len(watched_movies) == 0: return 0.0
    for movie in watched_movies:
        sum_rating += movie["rating"]
    average_rating = sum_rating / len(watched_movies)
    return average_rating


# Alycia
def get_most_watched_genre(user_data):
    genre_dict = {}
    highest_num = 0
    highest_genre = ""
    watched_movies = user_data["watched"]

    if len(watched_movies) == 0: return None

    for movie in watched_movies:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1

    for genre, num in genre_dict.items():
        if num > highest_num:
            highest_num = num
            highest_genre = genre
    
    return highest_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # user_data = {
    #     "watched" : [{"title" : "movie1"},{"title" : "movie2"}],
    #     "friends": {"watched":[{"title" : "movie1"}, {"title" : "movie2"}]}
    # }
    watched_movies = user_data["watched"].copy()
    friend_watched_movies = []
    not_watched_by_friends = []
    
    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            friend_watched_movies.append(movie)

    fw_copy = friend_watched_movies.copy()

    for movie in watched_movies:
        if movie not in friend_watched_movies:
            not_watched_by_friends.append(movie)

    # print(watched_movies)
    # print(len(watched_movies))
    # print(friend_watched_movies)
    # print(len(friend_watched_movies))
    # print(not_watched_by_friends)


    return not_watched_by_friends

def get_friends_unique_watched(user_data):
    watched_movies = user_data["watched"].copy()
    friend_watched_movies = []
    not_watched_by_user = []
    
    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            friend_watched_movies.append(movie)

    fw_copy = friend_watched_movies.copy()

    for movie in friend_watched_movies:
        if movie not in watched_movies and movie not in not_watched_by_user:
            not_watched_by_user.append(movie)   

    return not_watched_by_user

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # user_data["subscriptions"] = ["netflix", "hulu", "disney+"]
    # user_data["friends"] = {"watched":
                # [{"title" : "movie1", "host": "hulu"}, 
                # {"title" : "movie2", "host" : "disney+"}]}
    # append to recommended_movies if: 
    #   movie not in user_data["watched"]
    #   movie in user_data[friends]--[watched]
    #   movie["host"] in user_data["subscriptions"]
    recommended_movies = []
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
