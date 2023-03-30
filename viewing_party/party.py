# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Sets up a dictionary for a new movie that contials title, genre, and rating. 
    """   
    new_movie = {}
    if not (title and genre and rating):
        return None 
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating 
    return new_movie    

def add_to_watched(user_data, movie):
    """
    Adds a movie dictionary to the users list of dictionaries containing watched movies. 
    """ 
    user_data['watched'].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    """
    Add the movie to the users the watchlist which is a list of dictionaries.
    """ 
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    Searches for title in user's list of dictionaries containing watchlis movies.
    Removes movie from watchlist and adds it to watched list. 
    """ 
    for movie in user_data['watchlist']:
        if movie['title'] == title:  
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    Calculate the average rating of all movies in the watched list.
    """
    sum = 0.0
    average = 0.0 
    for movies in user_data["watched"]:
        if not movies["rating"]:
           return average
        sum += movies["rating"]
    if len(user_data["watched"]) > 0:
        average = sum / len(user_data["watched"])      
        
    return average
            
def get_most_watched_genre(user_data):
    """
    Returns a string of most watched genre by searching in user's list of watched movies. 
    """ 
    genre_freq = {}

    if not user_data['watched']:
        return None 
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in genre_freq:
            genre_freq[genre] += 1
        else:
            genre_freq[genre] = 1
    
    max_frequency = max(genre_freq.values())
    most_common_genre = None   
    for genre, frequency in genre_freq.items():
        if frequency == max_frequency:
            most_common_genre = genre
            break

    return most_common_genre  


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_user_titles(user_data):
    """
    Helper function that returns list of strings movie titles from user watched list.
    """
    user_titles  = []
    for movie in user_data["watched"]:
        user_titles.append(movie["title"])
    return user_titles

def get_friend_titles(user_data):
    """
    Helper function that returns list of strings containing the tiles that the friends have watched. 
    """ 
    friend_movie_titles = []
    for friend_movies in user_data["friends"]:
        for watched_movie in friend_movies['watched']:
            friend_movie_titles.append(watched_movie["title"])
    return friend_movie_titles

def get_unique_watched(user_data):
    """
    Get the movies that user has watched, but none of their friends have watched.
    """
    user_titles = get_user_titles(user_data)
    friend_titles = get_friend_titles(user_data)
    
    only_user_watched = []
  
    only_user_titles = set(user_titles) - set(friend_titles)
   
    for movie in user_data["watched"]:
        for title in only_user_titles:
            if movie["title"] == title:
                only_user_watched.append(movie)
    return only_user_watched

def get_friends_unique_watched(user_data):
    """
    Returns list of dictionaries with movies that at least one of the user's friends have watched, 
    but the user has not watched.
    """
    user_titles = get_user_titles(user_data)
    friend_titles = get_friend_titles(user_data)
    
    only_friends_titles = set(friend_titles) - set(user_titles)
    
    all_friend_watched_movies = {}
    #Make a dictionary that contains all of the friends watched,key is title of movie, and value is movie dictionary.
    for friend in user_data["friends"]:
        for movie in friend['watched']:
            all_friend_watched_movies[movie["title"]]= (movie)
    
    only_friends_watched = []
    #Make a list of dictionaries by comparing titles only friends have watched to keys in all friends watched dictionary
    for title in all_friend_watched_movies.keys():
        if title in only_friends_titles:
            only_friends_watched.append(all_friend_watched_movies[title]) 
    
    return only_friends_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
#Call get_friends_unique_watched on user data and assign to user_not_watched
    user_not_watched = get_friends_unique_watched(user_data)
    movie_recs = []
#Check if movie from friends_unique_watched == host in user_data 
    for movie in user_not_watched:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie) 

    return movie_recs 


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    most_common_genre = get_most_watched_genre(user_data)
    unique_movies = get_friends_unique_watched(user_data)
    for movie in unique_movies:
        if movie["genre"] == most_common_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    recs_from_faves= []
    user_unique_recs = get_unique_watched(user_data)

    favorites = []
    for movie in user_data["favorites"]:
        favorites.append(movie["title"])
    
    for favorite_title in favorites:
        for movie in user_unique_recs:
            if movie["title"] == favorite_title:
                recs_from_faves.append(movie)



    return recs_from_faves