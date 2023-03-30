from collections import Counter


# ------------- WAVE 1 --------------------


# creates a movie 
# returns dictionary

def create_movie(title, genre, rating):

    if title == None or genre == None  or rating == None:
        movie_dict = None
    else:
        movie_dict = {"title":title,"genre":genre,"rating":rating}

    return movie_dict


# builds watched movies list in user_data dictionary

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data


# builds movie watchlist in user_data dictionary

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data


# moves movie from watchlist to watched in user_data dictionary

def watch_movie(user_data, title):
    
    for index in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][index].values():
            res = user_data["watched"].insert(0, user_data["watchlist"].pop(index))
        else:
            continue

    return user_data  

# -----------------------------------------
# ------------- WAVE 2 --------------------


# calculates average rating of movies
# returns int

def get_watched_avg_rating(user_data):
    
    average_rate = 0

    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie_dict in user_data["watched"]:
        average_rate += movie_dict["rating"]

    return average_rate / len(user_data["watched"])
    

# finds most popular genre in user_data
# returns string

def get_most_watched_genre(user_data):
    
    if user_data["watched"] == []:
        return None
    else: 
        genres_dict = {}

        for index in range(len(user_data["watched"])):
            movie_genre = user_data["watched"][index]["genre"]
            if movie_genre in genres_dict:
                genres_dict[movie_genre] += 1
            else:
                genres_dict[movie_genre] = 1

        most_popular = max(genres_dict, key = genres_dict.get)

        return most_popular


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# returns tuple (movies watched user not friends, movies watched friends not user)

def set_comparison(user_data):

    friends_watched_set = set()
    user_watched_set = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])

    for i in range(len(user_data["watched"])):
        user_watched_set.add(user_data["watched"][i]["title"])
    
    return user_watched_set.difference(friends_watched_set),friends_watched_set.difference(user_watched_set)


# returns list of movie dictionaries that user has watched + friends haven't watched

def get_unique_watched(user_data):

    unique_movies = [movie for movie in user_data["watched"] if movie["title"] in set_comparison(user_data)[0]]

    return unique_movies


# returns list of movie dictionaries that friends have watched but user has not

def get_friends_unique_watched(user_data):

    friends_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in set_comparison(user_data)[1] and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


# returns list of movie dictionaries that user has not watched, but friends have watched based on whether or not the user has a subscription to that movie's host

def get_available_recs(user_data):

    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    

    for watchlist in user_data["friends"]:
        for movie in watchlist["watched"]:
            if movie["host"] in user_data["subscriptions"] and (movie in friends_unique_watched and movie not in recommended_movies):
                recommended_movies.append(movie)       
                    
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


# returns list of movie dictionaries that user has not watched but friends have watched based on user's most watched genre

def get_new_rec_by_genre(user_data):

    recommended_movies_by_genre = [movie for movie in get_friends_unique_watched(user_data) if movie["genre"] == get_most_watched_genre(user_data)]

    return recommended_movies_by_genre


# returns list of movie dictionaries that user has watched but friends have not based on users favorite movies

def get_rec_from_favorites(user_data):
    
    recommended_movies_by_favorites = [movie for movie in user_data["favorites"] if movie in get_unique_watched(user_data)]
    
    return recommended_movies_by_favorites
