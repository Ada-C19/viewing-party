import pytest
from viewing_party.party import *
from tests.test_constants import *

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    else:
        return None

    return movie_dict


def add_to_watched(user_data , movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    for i in range(0,len(user_data["watchlist"])):
        if title in user_data["watchlist"][i]["title"]:
            removed_movie = user_data["watchlist"].pop(i)
            user_data["watched"].append(removed_movie)

    return user_data

        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_rating = 0.0
    for dict in user_data["watched"]:
        sum_rating += dict["rating"]
    
    try:
        avg_rating = sum_rating / len(user_data["watched"])
    except ZeroDivisionError:
        return 0.0

    return avg_rating


def get_most_watched_genre(user_data):
    genre_dict = {}

    if len(user_data["watched"]) == 0:
        return None
    
    for dict in user_data["watched"]:
        if not dict["genre"] in genre_dict:
            genre_dict[dict["genre"]] = 1

        elif dict["genre"] in genre_dict:
            genre_dict[dict["genre"]] += 1
    
    most_watched = ["", 0]

    for key,value in genre_dict.items():
        if value > most_watched[1]:
            most_watched[0] = key
            most_watched[1] = value

    return most_watched[0]

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_list = []
    friends_list = []
    final_list = []

    for dict in user_data["watched"]:
        user_list.append(dict["title"])
        
    for movie_dict in user_data["friends"]:
        for i in range(len(user_data["friends"])):
            for movie_dict in user_data["friends"][i]["watched"]:
                friends_list.append(movie_dict["title"])

    user_set = set(user_list)
    friends_set = set(friends_list)

    unique_movies = user_set - friends_set
    unique_movies_list = list(unique_movies)

    for movie_dict in user_data["watched"]:
        for unique_movie in unique_movies_list:
            if unique_movie in movie_dict["title"]:
                final_list.append(movie_dict)
            
    return final_list


    
def get_friends_unique_watched(user_data):
    user_list = []
    friends_list = []
    final_list = []

    for dict in user_data["watched"]:
        user_list.append(dict["title"])
        
    for movie_dict in user_data["friends"]:
        for i in range(len(user_data["friends"])):
            for movie_dict in user_data["friends"][i]["watched"]:
                print(movie_dict["title"])
                friends_list.append(movie_dict["title"])

    user_set = set(user_list)
    friends_set = set(friends_list)

    unique_movies = friends_set - user_set
    unique_movies_list = list(unique_movies)

    for movie_dict in user_data["friends"]:
        for i in range(len(user_data["friends"])):
            for movie_dict_2 in user_data["friends"][i]["watched"]:
                for unique_movie in unique_movies_list:
                    if unique_movie in movie_dict_2["title"] and not movie_dict_2 in final_list:
                        final_list.append(movie_dict_2)
                            
        
    return final_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    user_list = []
    friends_list = []
    final_list = []

    for dict in user_data["watched"]:
        user_list.append(dict["title"])
        
    for movie_dict in user_data["friends"]:
        for i in range(len(user_data["friends"])):
            for movie_dict in user_data["friends"][i]["watched"]:
                print(movie_dict["title"])
                friends_list.append(movie_dict["title"])

    user_set = set(user_list)
    friends_set = set(friends_list)

    unique_movies = friends_set - user_set
    unique_movies_list = list(unique_movies)

    for movie_dict in user_data["friends"]:
        for i in range(len(user_data["friends"])):
            for movie_dict_2 in user_data["friends"][i]["watched"]:
                for unique_movie in unique_movies_list:
                    if unique_movie in movie_dict_2["title"] and not movie_dict_2 in final_list:
                        final_list.append(movie_dict_2)
    
    final_list_subscribed = []
    for movie_dict in final_list:
        if movie_dict["host"] in user_data["subscriptions"]:
            final_list_subscribed.append(movie_dict)
        
    return final_list_subscribed

amandas_data = clean_wave_4_data()
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    rec_list = []

    for movie_dict in friends_unique_watched:
        if movie_dict["genre"] == most_watched:
            rec_list.append(movie_dict)

    return rec_list

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    favorites = user_data["favorites"]
    
    rec_favorite_list = []

    for movie_dict in unique_watched:
        if movie_dict in favorites:
            rec_favorite_list.append(movie_dict)

    return rec_favorite_list

