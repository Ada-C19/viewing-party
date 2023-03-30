# ------------- WAVE 1 --------------------

# Let's start
# Hola, Laura!

def create_movie(title, genre, rating):
    title_check = isinstance(title, str)
    genre_check = isinstance(genre, str)
    rating_check = isinstance(rating, float)
    if not title_check or not genre_check or not rating_check:
        return None
    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie
    

def add_to_watched(user_data, movie):
    user_data_watched_list = user_data["watched"]
    user_data_watched_list.append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data_watchlist = user_data["watchlist"]
    user_data_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):

    # if title not in user_data["watchlist"]:
    #     return user_data
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    lengh_list = len(user_data["watched"])
    if lengh_list < 1:
        return 0.0
    rating_added = 0
    for element in user_data["watched"]:
        rating_added += element["rating"]
    average_rating = rating_added/lengh_list
    return float(average_rating)


def get_most_watched_genre(user_data):
    count_watched_genres = {}
    if user_data["watched"] == []:
        return None
    for element in user_data["watched"]:
        if element["genre"] not in count_watched_genres:
            count_watched_genres[element["genre"]] = 1
        count_watched_genres[element["genre"]] += 1
    sorted_dict = sorted(count_watched_genres.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict[0][0]

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_set = set()
    unique_watched = []
    user_data_watched = user_data["watched"]
    user_data_friends_list = user_data["friends"]
    
    for friend in user_data_friends_list:
        for i in range(len(friend["watched"])):
            title = friend["watched"][i]["title"]
            unique_set.add(title)
    
    for my_movie in user_data_watched:
        if my_movie["title"] not in unique_set:
            unique_watched.append(my_movie)
        
    
    return unique_watched



# Consider the movies that the user has watched, 
# and consider the movies that their friends have watched. 
# Determine which movies at least one of the user's friends have watched,
# but the user has not watched.
# Return a list of dictionaries, that represents a list of movies
def did_user_watch_this_title(user_data, title):
    for movie in user_data["watched"]:
        if movie["title"] == title:
            return True
    return False

def get_dictionary_of_friends_movies(user_data):
    dictionary_friends_watched = {}
    for friend in user_data["friends"]:
        for i in range(len(friend["watched"])):
            title = friend["watched"][i]["title"]
            movie_dict = friend["watched"][i]
            dictionary_friends_watched[title] = movie_dict
    
    return dictionary_friends_watched

def get_friends_unique_watched(user_data):
    
    friends_watch_dictionary = get_dictionary_of_friends_movies(user_data)
   
    list_of_movies = []
    
    for k, v in friends_watch_dictionary.items():
        if not did_user_watch_this_title(user_data, k):
            list_of_movies.append(v)

    return list_of_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# Determine a list of recommended movies. 
# A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"
# Return the list of recommended movies
def check_user_suscriptions(user_data):
    list_of_suscriptions = user_data["subscriptions"]
    return list_of_suscriptions

def get_available_recs(user_data):
    recomendations_for_user = []
    user_suscriptions = check_user_suscriptions(user_data)
    # list of dictionaries:
    friends_unique_watched = get_friends_unique_watched(user_data)
    # search in list of dict for host == users'host:
    for movie in friends_unique_watched:
        if movie["host"] in user_suscriptions:
            recomendations_for_user.append(movie)
    return recomendations_for_user


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


