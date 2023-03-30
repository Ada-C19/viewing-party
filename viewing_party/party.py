# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    for key, value in new_movie.items():
        if value == None:
            return None

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    add_movie = user_data
    return add_movie

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    watch_list = user_data
    return watch_list

#were we expected to use the previous functions as helper functions?

def watch_movie(user_data, title):
    new_user_data = user_data.copy()
    watchlist = new_user_data.get("watchlist", [])
    watched_list = new_user_data.get("watched", [])
    for movie in watchlist:
        if movie["title"] == title:
            if len(watchlist) > 0:
                watched_list.append(watchlist[0])
                watchlist.remove(watchlist[0])
    return new_user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0.0
    movie_count = 0 
    #another approach to accessing dictionary in list?
    for key, value in user_data.items():
        for movie in value:
            sum += movie["rating"]
            movie_count += 1

    if sum == 0.0:
        return sum
    total = sum / movie_count
    return total

def get_most_watched_genre(user_data):
    genre_dict = {}
    if user_data["watched"] == []:
        return None
    for movie in user_data["watched"]:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1

    high_genre = max(genre_dict.values())

#better way to go through the genre_dict to get high_genre?
    for key, value in genre_dict.items():
        if value == high_genre:
            return key

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched = user_data["watched"].copy()
    friends = user_data["friends"].copy()
    for friend in friends: 
        for movie in friend["watched"]: 
            if movie in watched:
                watched.remove(movie)
    return watched

def get_friends_unique_watched(user_data):
    watched = user_data ["watched"].copy()
    friends = user_data ["friends"].copy()
    unique_movies = []
    for friend in friends: 
        for movie in friend["watched"]:
            if movie not in watched and movie not in unique_movies:
                unique_movies.append(movie)
    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
#another method to the "for" for "for" maddness?
def get_available_recs(user_data):
    watched = user_data["watched"].copy()
    friends = user_data["friends"].copy()
    subscriptions = user_data["subscriptions"].copy()
    recommendations = []
    for friend in friends:
        for movie in friend["watched"]:
            if movie not in watched and movie not in recommendations:  
                if movie ["host"] in  subscriptions:
                    recommendations.append(movie)   
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    watched = user_data["watched"].copy()
    friends = user_data["friends"].copy()
    recommendations = []
    favorites = get_most_watched_genre(user_data)
            
    for friend in friends:
        for movie in friend["watched"]:
            if movie not in watched and movie not in recommendations:
                if movie["genre"] == favorites:
                    recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"].copy()
    recommendations = []
    unique = get_unique_watched(user_data)
    for movie in unique:
        if movie in favorites:
            recommendations.append(movie)
    
    return recommendations

