from statistics import mean

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): 
    # if any of the vars are None, return None
    if not title or not genre or not rating:
        return None
    
    # create new dict
    new_movie = {
        "title": title,
        "genre": genre,
        "rating":rating,
    }

    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    # Parse through the movies in watchlist
    for movie in user_data["watchlist"]:

        # if title == the movie title then operate on it
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    # return modified user_data
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
#create function get_watched_avg_rating(user_data)
        # user data is dict with 'watched' [{}]
    if user_data["watched"] == []:
        average_rating = 0.0
        return average_rating

    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie['rating'])
    average_rating = mean(ratings)
    return average_rating

def get_most_watched_genre(user_data):
    # handles empty watchlist
    if user_data["watched"] == []:
        return None
    
    genres = []
    # iterate through user-data to fine movie value for watched
    for movie in user_data["watched"]:
        # add value of genre to variable genres
        genres.append(movie["genre"])
        
    # use count to find which genres repeat most and delete others
    popular_genre = max(set(genres), key = genres.count)
    
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # get all the titles for users_watched
    user_watched_titles = set([movie["title"] for movie in user_data['watched']])

    # build set of all friends watched
    friends_watched_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.append(movie["title"])
    friends_watched_titles = set(friends_watched_titles)

    # find unique user watched
    unique_user_watched_titles = user_watched_titles.difference(friends_watched_titles)
    unique_user_watched_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_user_watched_titles:
            unique_user_watched_movies.append(movie)

    return unique_user_watched_movies    


def get_friends_unique_watched(user_data):
    # get all the titles for users_watched
    user_watched_titles = {movie["title"] for movie in user_data["watched"]}
    
    # build set of all friends watched
    friends_watched_titles = {movie["title"] for friend in user_data["friends"] for movie in friend["watched"]}
    
    # find unique friends watched
    friends_unique_watched_titles = friends_watched_titles - user_watched_titles
    
    # create non duplicated list of all the movies friends have watched and user
    # has not.  Use a seperate list added_titles to be sure of no dups.
    friends_unique_watched_movies = []
    added_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friends_unique_watched_titles:
                if movie["title"] not in added_titles:
                    friends_unique_watched_movies.append(movie)
                    added_titles.append(movie["title"])

    return friends_unique_watched_movies    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # set up and get user-watched and subscriptions as sets
    subscriptions = set(user_data["subscriptions"])
    user_watched_titles = {movie['title'] for movie in user_data['watched']}

    # initialize the recommended and already added movie titles
    # then loop through the friends watched movies and add the 
    # un-watched by user movies to the recommened list.
    recommended = []
    added_titles = []
    for friend in user_data['friends']:
        for movie in friend["watched"]:
            if movie['title'] not in user_watched_titles and movie['host'] in subscriptions:
                if movie['title'] not in added_titles:
                    recommended.append(movie)
                    added_titles.append(movie['title'])

    return recommended

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

