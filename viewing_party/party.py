# WAVE 1
def create_movie(title, genre, rating):
    movie = {}
    if not title or not genre or not rating:
        return None
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movies in user_data["watchlist"]:
        if title == movies["title"]:
            user_data["watched"].append(movies)
            user_data["watchlist"].remove(movies)
    return user_data

# WAVE 2
def get_watched_avg_rating(user_data):
    ratings = 0.0
    count_movies = 0
    if not user_data["watched"]:
        return ratings 
    for movie_info in user_data["watched"]:
        if isinstance(movie_info.get("rating"),float):
            ratings += movie_info.get("rating")
            count_movies += 1
    return ratings/count_movies

def get_most_watched_genre(user_data):
    favorite_genre ={}
    if not user_data["watched"]:
        return None 
    for movie_info in user_data["watched"]: 
        if movie_info["genre"] not in favorite_genre:
            favorite_genre[movie_info["genre"]] = 1
        else:
            favorite_genre[movie_info["genre"]] += 1
    return max(favorite_genre, key=favorite_genre.get)        
            
# WAVE 3
def get_unique_watched(user_data):
    friends_watched_movie = set()
    user_watched_movie = []
    unique_movie_watched = []
    # generate a set with movie titles from friend's watched lists
    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            friends_watched_movie.add(movie["title"])
   # generate a list of dictionaries with watched user movie info
    for user_movies in user_data["watched"]:
        user_watched_movie.append(user_movies)
    # Check to see if the user movie title is within the whole set of friend's watched list
    for movie_info in user_watched_movie:
        if movie_info["title"] not in friends_watched_movie:
            unique_movie_watched.append(movie_info)
    return unique_movie_watched

def get_friends_unique_watched(user_data): 
    movie_friend_watched = []
    only_friends_watched = []
    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            if movie not in movie_friend_watched:
                movie_friend_watched.append(movie)
    
    for movie_info in movie_friend_watched:
        if movie_info not in user_data["watched"]:
            only_friends_watched.append(movie_info)
    return only_friends_watched
        
# WAVE 4
def get_available_recs(user_data):
    rec_movies_by_friends = []
    friends_only = get_friends_unique_watched(user_data)
    for movie_info in friends_only: 
        if movie_info["host"] in user_data["subscriptions"]: 
            rec_movies_by_friends.append(movie_info)
    return rec_movies_by_friends

# WAVE 5
def get_new_rec_by_genre(user_data): 
    rec_by_genre = []
    fav_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    for movies in friends_watched: 
        if movies["genre"] == fav_genre: 
            rec_by_genre.append(movies)
    return rec_by_genre

def get_rec_from_favorites(user_data): 
    rec_by_favs = []
    friend_watched = []
    #generated a list of all the movies friends watched 
    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            if movie not in friend_watched:
                friend_watched.append(movie)
    #compare all the movies friends watched with favorites, 
    #if favorites are not part of movies friends watched return those movies
    for movies in user_data["favorites"]:
        if movies not in friend_watched and movies not in rec_by_favs:
            rec_by_favs.append(movies)
    return rec_by_favs
