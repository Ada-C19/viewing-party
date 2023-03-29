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

def get_friend_movies(friend_list):
    friend_watched_movies = []

    for movies in friend_list:
        for movie in movies["watched"]:
            friend_watched_movies.append(movie)
    
    return friend_watched_movies

def get_unique_watched(user_data):
    watched_movies = user_data["watched"].copy()
    friend_watched_movies = get_friend_movies(user_data["friends"])
    not_watched_by_friends = []

    fw_copy = friend_watched_movies.copy()

    for movie in watched_movies:
        if movie not in friend_watched_movies:
            not_watched_by_friends.append(movie)

    return not_watched_by_friends

def get_friends_unique_watched(user_data):
    watched_movies = user_data["watched"].copy()
    friend_watched_movies = get_friend_movies(user_data["friends"])
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
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    if len(user_data["watched"]) == 0 or len(user_data["friends"]):
        return []

    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
 
def get_new_rec_by_genre(user_data):
    recommended_movies_genre = []
    user_genre = {}
    available_recs = get_available_recs(user_data)
    friend_watch = get_friend_movies(user_data["friends"])

    if len(user_data["watched"]) == 0 or len(friend_watch) ==0:
        return []

    for movie in user_data["watched"]:
        if movie["genre"] not in user_genre:
            user_genre[movie["genre"]] = 1
        else:
            user_genre[movie["genre"]] += 1

    most_common_genre = max(user_genre, key=user_genre.get)

    for movie in available_recs:
        if movie["genre"] == most_common_genre:
            recommended_movies_genre.append(movie)
    return recommended_movies_genre

import copy

# ********************************
# *** Do Not Modify This File ****
# ********************************

# Data for Unit Tests

#----------WAVE01-------------
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

#----------WAVE02-------------
HORROR_1 = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
}
FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}
ACTION_2 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2
}
ACTION_3 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5
}
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}
USER_DATA_2 = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],    
}

USER_DATA_2b = {
    "watched": [
        INTRIGUE_1,
        FANTASY_2,
        ACTION_1,
        FANTASY_1,
        FANTASY_3,
        INTRIGUE_2,
    ]
}

#-----WAVE 3--------
USER_DATA_3 = copy.deepcopy(USER_DATA_2)
USER_DATA_3["friends"] =  [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }
    ]  

#-----WAVE 4--------

HORROR_1b = copy.deepcopy(HORROR_1)
FANTASY_1b = copy.deepcopy(FANTASY_1)
FANTASY_2b = copy.deepcopy(FANTASY_2)
FANTASY_3b = copy.deepcopy(FANTASY_3)
FANTASY_4b = copy.deepcopy(FANTASY_4)
ACTION_1b = copy.deepcopy(ACTION_1)
ACTION_2b = copy.deepcopy(ACTION_2)
ACTION_3b = copy.deepcopy(ACTION_3)
INTRIGUE_1b = copy.deepcopy(INTRIGUE_1)
INTRIGUE_2b = copy.deepcopy(INTRIGUE_2)
INTRIGUE_3b = copy.deepcopy(INTRIGUE_3)

HORROR_1b["host"] = "netflix"
FANTASY_1b["host"] = "netflix"
FANTASY_2b["host"] = "netflix"
FANTASY_3b["host"] = "amazon"
FANTASY_4b["host"] = "hulu"
ACTION_1b["host"] = "amazon"
ACTION_2b["host"] = "amazon"
ACTION_3b["host"] = "hulu"
INTRIGUE_1b["host"] = "hulu"
INTRIGUE_2b["host"] = "disney+"
INTRIGUE_3b["host"] = "disney+"

USER_DATA_4 = {
    "watched": [
        FANTASY_1b, 
        FANTASY_2b, 
        FANTASY_3b, 
        ACTION_1b, 
        INTRIGUE_1b, 
        INTRIGUE_2b
        ],  
    "friends":  [
        {
            "watched": [
                FANTASY_1b,
                FANTASY_3b,
                FANTASY_4b,
                HORROR_1b,
            ]
        },
        {
            "watched": [
                FANTASY_1b,
                FANTASY_4b,
                ACTION_1b,
                INTRIGUE_1b,
                INTRIGUE_3b,
            ]
        }  
    ]
}

USER_DATA_4["subscriptions"] = ["netflix", "hulu"]  


#----WAVE 5-----------

USER_DATA_5 = copy.deepcopy(USER_DATA_4)

USER_DATA_5["favorites"] = [
    FANTASY_1b, 
    FANTASY_2b, 
    INTRIGUE_1b,
    INTRIGUE_2b
    ]

#----Functions that return clean data for each test----

def clean_wave_2_data():
    return copy.deepcopy(USER_DATA_2)

def clean_wave_2b_data():
    return copy.deepcopy(USER_DATA_2b)

def clean_wave_3_data():
    return copy.deepcopy(USER_DATA_3)

def clean_wave_4_data():
    return copy.deepcopy(USER_DATA_4)

def clean_wave_5_data():
    return copy.deepcopy(USER_DATA_5)

get_new_rec_by_genre(USER_DATA_5)