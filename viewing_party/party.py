#
#  ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None

    else:
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating
    return new_movie

def add_to_watched(user_data, movie):
    for data in user_data:
        user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    for data in user_data:
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for user in user_data["watchlist"]:
        if user["title"] == title:
            user_data["watchlist"].remove(user)
            user_data["watched"].append(user)

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
        counter +=1
    
    return sum/counter
    
def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_dict = {}
    for movies in user_data["watched"]:
        if movies["genre"] not in genre_dict:
            genre_dict[movies["genre"]] = 1
        else:
            genre_dict[movies["genre"]] += 1

    largest_value = 0
    most_common_genre = ""
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

    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            friend_movies.append(movies)
    for user_movies in user_data["watched"]:
        if user_movies not in friend_movies:
            unique_movies.append(user_movies)

    return unique_movies

def get_friends_unique_watched(user_data):
    unique_movies = []
    user_movies = []

    for movies in user_data["watched"]:
        user_movies.append(movies)

    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            if movies not in user_movies and movies not in unique_movies:
                unique_movies.append(movies)
    
    print(unique_movies)

    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

