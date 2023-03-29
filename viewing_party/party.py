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
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data        
    return user_data

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    
    sum = 0.0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]:
                sum += movie["rating"]
    average_rating = sum/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    genre_list = []
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    most_genre = max(genre_list, key=genre_list.count)
         
    return most_genre
        



# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    user_watched_only = []
    friends_watched = []
    unique_list = []
    for movie in user_data["watched"]:
        user_watched_only.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
                friends_watched.append(movie)
    
    for movie in user_watched_only:
        if movie not in friends_watched:
            unique_list.append(movie)
             
    return unique_list
    
                    
def get_friends_unique_watched(user_data):
    user_watched_only = []
    friends_watched = []
    unique_list = []
    for movie in user_data["watched"]:
        user_watched_only.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
                friends_watched.append(movie)
    
    for movie in friends_watched:
        if movie not in user_watched_only and movie not in unique_list:
            unique_list.append(movie)

    return unique_list    

# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    recommended_movies = []
    unique_movies = get_friends_unique_watched(user_data)
    
    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
     
    return recommended_movies
                
         

    

    
                 
    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

