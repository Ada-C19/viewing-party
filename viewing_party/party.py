# ------------- WAVE 1 --------------------
import copy
'''
This function takes in 3 values: the title, genre, and rating of a movie. It uses these three parameters
and creates a dictionary that includes the title, genre, and rating for the movie. Returns none if any of
the parameters are "falsy".
'''
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    return movie    
'''
This function takes in 2 values, a dictionary called user_data, and a dictionary called movie. It adds the movie
as a value to the user_data under the key "watched", which is a list. 
'''
def add_to_watched(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watched"].append(movie)
    return user_data_copy
'''
This function takes in 2 values, a dictionary called user_data, and a dictionary called movie. It adds the movie
as a value to the user_data under the key "watchlist", which is a list. 
'''
def add_to_watchlist(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watchlist"].append(movie)
    return user_data_copy
'''
This function takes in 2 values, a dictionary called user_data, and a string called title. It checks to make sure that the movie
is in watchlist. If it is not in watchlist, we return user_data as is. If it is in watchlist, we will remove the movie from "watchlist" and 
add it to "watched".
'''
def watch_movie(user_data, title):
    user_data_copy = copy.deepcopy(user_data)
    in_watchlist = False
    movie_index = 0
    for movie in user_data_copy["watchlist"]:
        if movie["title"] == title:
            in_watchlist = True
            break
        movie_index += 1
    if not in_watchlist:
        return user_data_copy
    movie = user_data_copy["watchlist"][movie_index]
    del user_data_copy["watchlist"][movie_index]
    user_data_copy = add_to_watched(user_data_copy, movie)
    return user_data_copy
'''
This function takes in 1 value, a dictionary called user_data. It calculates the average rating for all the movies that are under
the key "watched" from user_data. 
'''
def get_watched_avg_rating(user_data):
    num_of_movies = len(user_data["watched"])
    if num_of_movies == 0:
        return 0.0
    ratings = 0
    for movie in user_data["watched"]:
        ratings += movie["rating"]
    average_rating = ratings / num_of_movies
    return average_rating   
'''
This function takes in 1 value, a dictionary called user_data. It looks at all the movies that are under the key "watched"
and figures out which genre is most watched by the user. 
'''
def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_counts = {}
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        try:
            genre_counts[movie_genre] += 1
        except KeyError:
            genre_counts[movie_genre] = 1
    max_watch_count = 0
    for genre, watch_count in genre_counts.items():
        if watch_count > max_watch_count:
            max_watch_count = watch_count
            max_genre = genre
    return max_genre
'''
This function takes in 1 value, a dictionary called user_data. We compare the movies under the key "watched" with the movies under
each friend's "watched" lists. We retun a list of movies that are unique to the user. 
'''
def get_unique_watched(user_data):
    unique_titles = []
    for movie in user_data["watched"]:
        friend_watched = False
        for friend in user_data["friends"]:
            for friends_movie in friend["watched"]:
                if friends_movie["title"] == movie["title"]:
                    friend_watched = True
                    break
        if not friend_watched:    
            unique_titles.append(movie)
    return unique_titles   
'''
This function takes in 1 value, a dictionary called user_data. We compare the movies under the key "watched" with the movies under
each friend's "watched" lists. We retun a list of movies that are unique to the friends. 
'''
def get_friends_unique_watched(user_data):
    unique_titles = []
    unique_title_names = []
    for friend in user_data["friends"]:
        for friends_movie in friend["watched"]:
            user_watched = False
            for movie in user_data["watched"]:
                if friends_movie["title"] == movie["title"]:
                    user_watched = True
                    break
            if not user_watched and friends_movie["title"] not in unique_title_names:
                unique_titles.append(friends_movie)
                unique_title_names.append(friends_movie["title"])
    return unique_titles     
'''
This function takes in 1 value, a dictionary called user_data. We use the function get_friends_unique_watched to identify
the movies unique to the friends (unwatched by the user), and then identify which of those movies are on hosts that the user is subscribed to. We return the
 movies that the user hasn't seen and also has access to. 
'''
def get_available_recs(user_data):
    rec_movies = []
    user_unwatched = get_friends_unique_watched(user_data)
    for movie in user_unwatched:
        if movie["host"] in user_data["subscriptions"]:
            rec_movies.append(movie)
    return rec_movies
'''
This function takes in 1 value, a dictionary called user_data. We use the function get_most_watched_genre to identify which genre the
user watches the most, and use the get_friends_unique_watched to identify the movies that the user has not seen. Out of the movies that are
unique to the friends, we return a list of the ones that match the most watched genre. 
'''
def get_new_rec_by_genre(user_data):
    rec_movies = []
    user_unwatched = get_friends_unique_watched(user_data)
    user_most_watched_genre = get_most_watched_genre(user_data)
    for movie in user_unwatched:
        if movie["genre"] == user_most_watched_genre:
            rec_movies.append(movie)
    return rec_movies
'''
This function takes in 1 value, a dictionary called user_data. We use the function get_unique_watched to identify which movies are unique to the user. We then
look through the user's favorite movies, and find any overlap between the unique movies and favorite movies. We return a list of the overlapping movies. 
'''
def get_rec_from_favorites(user_data):
    unique_to_user = get_unique_watched(user_data)
    fave_rec_movies = []
    for movie in unique_to_user:
        for favorite in user_data["favorites"]:
            if movie["title"] == favorite["title"]:
                fave_rec_movies.append(movie)
    return fave_rec_movies            
