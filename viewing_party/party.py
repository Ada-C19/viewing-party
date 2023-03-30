#
#  ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}

#   Check to see if there is a title, genre, rating
    if not title or not genre or not rating:
        return None
    else:
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating

    return new_movie

def add_to_watched(user_data, movie):
#   Add movie to user's watched list
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
#   Add movie to user's watchlist list
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
#   Check to see if movie's in watchlist, and put into watched
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    counter = 0

    if not user_data['watched']:
        return 0.0
    
    for movies in user_data['watched']:
        sum += movies['rating']
        counter += 1
    
    return sum/counter
    
def get_most_watched_genre(user_data):
    genre_dict = {}
    largest_value = 0
    most_common_genre = ""

    if not user_data["watched"]:
        return None
    
#   Count frequency of genre
    for movies in user_data["watched"]:
        if movies["genre"] not in genre_dict:
            genre_dict[movies["genre"]] = 1
        else:
            genre_dict[movies["genre"]] += 1

#   Find the most common genre
    for genre, freq in genre_dict.items():
        if freq > largest_value:
            largest_value = freq
            most_common_genre = genre
    
    return most_common_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = []
    friend_movies = []

#   Create a list of movies that friends have
    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            friend_movies.append(movies)

#   Check to see if there are common movies between user movies and friends movies
#   Adds uncommon movies for user
    for user_movies in user_data["watched"]:
        if user_movies not in friend_movies:
            unique_movies.append(user_movies)

    return unique_movies

def get_friends_unique_watched(user_data):
    unique_movies = []
    user_movies = []

#   Create a list of movies that users have
    for movies in user_data["watched"]:
        user_movies.append(movies)

#   Check to see if there are common movies between user movies and friends movies
#   Adds uncommon movies for friends
    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            if movies not in user_movies and movies not in unique_movies:
                unique_movies.append(movies)

    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended = []
    unique_movies = get_friends_unique_watched(user_data)

#   Recommend movies with matching host and subscription
    for subscription in user_data["subscriptions"]:
        for movies in unique_movies:
            if subscription == movies["host"]:
                recommended.append(movies)
    return recommended


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_by_genre = []
    unique_movies = get_friends_unique_watched(user_data)
    most_common_genre = get_most_watched_genre(user_data)

#   Recommends movies from friends unique list based on most common genre
    for movie in unique_movies:
        if movie["genre"] == most_common_genre:
            recommended_by_genre.append(movie)
    
    return recommended_by_genre

def get_rec_from_favorites(user_data):
    friend_movies = []
    recommendations = []
    
#   Create list of friends movies
    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            friend_movies.append(movies)

#   Recommend movies in user favorites but not in friends movies
    for favorites in user_data["favorites"]:
        if favorites not in friend_movies:
            recommendations.append(favorites)
    
    return recommendations
