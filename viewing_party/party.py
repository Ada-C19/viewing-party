import copy

MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

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

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None

    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_movie = user_data['watched']
    movie_to_watchlist = user_data['watchlist']

    for item in movie_to_watchlist:
        if title == item['title']:
            watched_movie.append(item)
            movie_to_watchlist.remove(item)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0
    number_movies = len(user_data["watched"])

    if len(user_data["watched"]) == 0:
        return 0.0
    
    for i in range(len(user_data["watched"])):
            total_ratings += user_data["watched"][i]["rating"]
            average_rating = total_ratings / number_movies
    return average_rating



def get_most_watched_genre(user_data):
    genre_options = []

    if user_data["watched"] == []:
        return None    
    
    for i in range(len(user_data["watched"])):
        genre_options.append(user_data["watched"][i]["genre"])
        highest_watched = (max(set(genre_options), key=genre_options.count))
    return highest_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data): 
    unique_watch = []
    friends_movies_watched = []

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_movies_watched.append(movie)
 
    for movie in user_data["watched"]:
        if movie not in friends_movies_watched:
            unique_watch.append(movie)
    return unique_watch

  
def get_friends_unique_watched(user_data):
    unique_watch = []
    no_duplicate_unique_watch = []
   

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"]:
                    unique_watch.append(movie)

    for movie in unique_watch:
        if movie not in no_duplicate_unique_watch:
            no_duplicate_unique_watch.append(movie)
    return no_duplicate_unique_watch


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # user_data = {
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

    user_data["subscriptions"] = ["netflix", "hulu"] 

    available_recs = []

    friends_movies_recs = get_friends_unique_watched(user_data)

    for i in range(len(friends_movies_recs)):
        if friends_movies_recs[i]["host"] in user_data["subscriptions"]:
            available_recs.append(friends_movies_recs[i])
    return available_recs
        
        

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass