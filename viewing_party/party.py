# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movie={}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie ["rating"] = rating
        return movie
    else:
        return None 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie (user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie) 
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_total = 0.0 

    if user_data["watched"] == []:
        return 0.0 
    
    for each_movie in user_data["watched"]:
        rating_total += each_movie["rating"]
        
    rating_average = rating_total/len(user_data["watched"])

    return rating_average

def get_most_watched_genre(user_data):

    frequency_dict = {}
    if user_data["watched"] == []:
        return None 
    
    for movie in user_data["watched"]:
        if movie['genre'] in frequency_dict:
            frequency_dict[movie['genre']] += 1
        else:
            frequency_dict[movie['genre']] = 1           
    winner = max(frequency_dict, key=frequency_dict.get)
    return winner


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_movies (user_data):

    friends_movie_title = [movies for movies_dict in user_data["friends"] for movies in movies_dict["watched"]]
    return friends_movie_title
    # This is what Line 64 is doing: 
    # friends_movie_title = []
    # for movies_dict in user_data["friends"]:
    #     for movies in movies_dict["watched"]: 
    #         friends_movie_title.append(movies) 
    # return (friends_movie_title)


def get_unique_watched(user_data):
    # user_unique_movies =[]
    
    # for movie in user_data["watched"]:
    #     if movie not in get_friends_movies(user_data):
    #         user_unique_movies.append(movie)
    # return(user_unique_movies)

    user_unique_movie = [movie for movie in user_data["watched"] if movie not in get_friends_movies(user_data)]
    return user_unique_movie
    

def get_friends_unique_watched(user_data):
    # friends_data= get_friends_movies(user_data)
    friends_result= []
    
    # for movie in get_friends_movies (user_data):
    #     if movie not in user_data["watched"]:
    #         friends_unique_movies.append(movie)
    friends_unique_movies =[movie for movie in get_friends_movies(user_data) if movie not in user_data["watched"]]
    
    [friends_result.append(movie) for movie in friends_unique_movies if movie not in friends_result]
    return friends_result 


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    subscription_list = user_data["subscriptions"]
    friend_unique_watched = get_friends_unique_watched(user_data)
    recommended_list = []

    for movie in friend_unique_watched:
        host = movie["host"]
        if host in subscription_list:
            recommended_list.append(movie)

    return recommended_list
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    recommended_movies = []
    unique_watched_friend_movies = get_friends_unique_watched(user_data)

    if genre is None or unique_watched_friend_movies ==[]: 
        return []
    
    for movie in unique_watched_friend_movies:
        if genre in movie["genre"]:
            recommended_movies.append(movie) 
    return recommended_movies

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    recommended_movies =[]
    user_movies= get_unique_watched(user_data)


    for movie in user_movies: 
        if movie in favorites:
            recommended_movies.append(movie)
    return recommended_movies