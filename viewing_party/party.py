# ------------- WAVE 1 --------------------
#---Wave_1_function_1---
def create_movie(title, genre, rating):

    movie_dict = {}

    if not title:
        return None
    elif not genre:
        return None
    elif not rating:
        return None
    else: 
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating

    return movie_dict

create_movie("Title", "Genre", "Rating")


# #---Wave_1_function_2---
def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

add_to_watched({"watched": []}, {
        "title": "MOVIE_TITLE_1",
        "genre": "GENRE_1",
        "rating": "RATING_1"})


# #---Wave_1_function_3---
def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data



#---Wave_1_function_4---
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title != (movie["title"]):
            continue
        else:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            print (user_data)
            return user_data
    return user_data

# ------------- WAVE 2 --------------------
# ---Wave_2_function_1---

def get_watched_avg_rating(user_data):

    ratings = []
    
    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie in user_data["watched"]:
        ratings.append((movie["rating"]))
    
    ratings_sum = sum(ratings)
    ratings_average = (ratings_sum) / len(ratings)

    return ratings_average


# ---Wave_2_function_2---
def get_most_watched_genre(user_data):

    movie_genre_dict = {}

    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:

        
        title = movie["title"]
        genre = movie["genre"]
        
        if genre not in movie_genre_dict:
            movie_genre_dict[genre] = []
        
        movie_genre_dict[genre].append(title)

    max_genre = None
    max_count = 0

    for genre in movie_genre_dict:
        genre_length = len(movie_genre_dict[genre])
        if genre_length >= max_count:
            max_genre = genre
            max_count = len(movie_genre_dict.values())

    return max_genre

# ------------- WAVE 3 --------------------

#---Wave_3_function_1---

def get_unique_watched(user_data):
    user_unique_movies = []
    movies_friends_watched = []
    movies_user_watched = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movies_friends_watched.append(movie)
    
    for movie in movies_user_watched:
        if movie not in movies_friends_watched:
            user_unique_movies.append(movie)

    return user_unique_movies

#---Wave_3_function_2---

def get_friends_unique_watched(user_data):

    movies_user_watched = user_data["watched"]
    unique_movies_friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie not in unique_movies_friends_watched) and (movie not in movies_user_watched):
                unique_movies_friends_watched.append(movie)
    
    # returns list of movie dictionaries
    return unique_movies_friends_watched

# ------------- WAVE 4 --------------------
#---Wave_4_function_1---

def get_available_recs(user_data):

    friends_unique_movie_list = get_friends_unique_watched(user_data)

    # figure out if host is in user's subscriptions
    recommended_movies = []
    for movie in friends_unique_movie_list:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies

# ------------- WAVE 5 --------------------
# ---Wave_5_function_1---
def get_new_rec_by_genre(user_data):
    rec_by_genre = []

    users_watched = user_data["watched"]
    friends_watched = get_friends_unique_watched(user_data)
    users_most_freq_genre = get_most_watched_genre(user_data)

    if len(users_watched) == 0:
        return rec_by_genre

    if len(friends_watched) == 0:
        return rec_by_genre

    for movie in friends_watched:
        if movie["genre"] == users_most_freq_genre:
            rec_by_genre.append(movie)
    
    return rec_by_genre
            
# ---Wave_5_function_2---
def get_rec_from_favorites(user_data):
    recommended = []

    users_unique_movies = get_unique_watched(user_data)
    users_favorites = user_data["favorites"]

    for movie in users_unique_movies:
        if movie in users_favorites:
            recommended.append(movie) 
        
    return recommended
