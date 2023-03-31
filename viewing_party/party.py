# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    movie = {}
    if not title or not genre or not rating:
        return None
    else:
        movie.update({"title" : title, "genre" : genre, "rating" : rating})
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    print(user_data)
    watchlist_list_of_dict = user_data.get("watchlist")
    print(watchlist_list_of_dict)

    for watchlistDict in watchlist_list_of_dict:
        if watchlistDict.get("title") == title:
            watchlist_list_of_dict.remove(watchlistDict)
            user_data["watched"].append(watchlistDict)
            print(user_data)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    running_total = 0
    number_of_movies = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]:
        running_total += movie["rating"]
        number_of_movies += 1
    avg = running_total / number_of_movies
    return avg

def get_most_watched_genre(user_data):
    most_watched_genre_dict = {}
    times_watched_genre = 0
    most_watched_genre = ""
    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched_genre_dict:
            most_watched_genre_dict[movie["genre"]] = 1
        else:
            most_watched_genre_dict[movie["genre"]] += 1
    for genre in most_watched_genre_dict:
        if most_watched_genre_dict["genre"] < times_watched_genre:
            continue
        elif most_watched_genre_dict["genre"] > times_watched_genre:
            most_watched_genre_dict["genre"] = times_watched_genre
            most_watched_genre = " "

            
            


# -----------------------------------------
# ------------- WAVE 3 --------------------


def get_unique_watched(user_data):

    user_unique_movies = []  # a list of dictionaries
    movies_titles_friends_watched = []  # a list of strings

    for item in user_data.get("friends"):
        for x in item.get("watched"):
            movies_titles_friends_watched.append(x.get("title"))
    
    for item in user_data.get("watched"):
        movie_user_has_watched = item
        if movie_user_has_watched.get("title") not in movies_titles_friends_watched:
                user_unique_movies.append(movie_user_has_watched)

    return user_unique_movies


def get_friends_unique_watched(user_data):

    friends_movies = [] # a list of dictionaries
    movies_titles_user_watched = [] # a list of strings

    for item in user_data.get("watched"):
        movies_titles_user_watched.append(item.get("title"))

    for item in user_data.get("friends"):
        for x in item.get("watched"):
            if x.get("title") not in movies_titles_user_watched:
                friends_movies.append(x)

    new_list = []
    for dictionary in friends_movies:
        if dictionary not in new_list:
            new_list.append(dictionary)
    
    return new_list



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    friends_unique_watched = get_friends_unique_watched(user_data)
    print(friends_unique_watched)

    movie_recommendations = []

    for x in friends_unique_watched:
        if x.get("host") in user_data.get("subscriptions"):
            movie_recommendations.append(x)

    return movie_recommendations



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    # Consider the user's most frequently watched genre.

    frequently_watched_genre = []
    for item in user_data.get("watched"):
        frequently_watched_genre.append(item.get("genre"))
    
    # Here I converted from list to set, then again to list to get rid of the duplicates
    frequently_watched_genre_set = set(frequently_watched_genre)
    frequently_watched_genre_list = list(frequently_watched_genre_set)

        
    friends_recommendations_list_of_dict = get_friends_unique_watched(user_data)


    movie_recommendations_genre = []
    for i in friends_recommendations_list_of_dict:
        if i.get("genre") == frequently_watched_genre_list:
            movie_recommendations_genre.append(i)
            

    return movie_recommendations_genre

