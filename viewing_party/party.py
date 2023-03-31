# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(title, genre, rating):
    movies = title, genre, rating
    if all(movies):
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
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            watched.append(movie)
            return user_data 
    return user_data   

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie in user_data["watched"]:
        total_rating += movie["rating"]  
    average_rating = total_rating / len(user_data["watched"]) 
    return average_rating

def get_most_watched_genre(user_data):
    list_genre = []
    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        list_genre.append(movie["genre"])
    genre_watched = max(list_genre, key=list_genre.count)
    return genre_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched =[]
    for movie in user_data['watched']:
        user_watched.append(movie)

    friends_watched =[]
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched.append(movie['title'])

    unique_watched =[]
    for movie in user_watched:
        if movie['title'] not in friends_watched: #['title']
            already_added = False
            for unique_movie in unique_watched:
                if unique_movie['title'] == movie['title']:
                    already_added = True
                    break 
            if not already_added:
                unique_watched.append(movie)          
    return unique_watched

def get_friends_unique_watched(user_data):
    user_watched =[]
    friends_watched =[]
    friends_unique_watched =[]

    for movie in user_data['watched']:
        user_watched.append(movie)

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched.append(movie)

    for movie in friends_watched:
        if movie not in user_watched and movie not in friends_unique_watched: #['title']
            friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movie =[]
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie['host'] in user_data['subscriptions']:
            recommended_movie.append(movie)
    return recommended_movie

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    watched_genres = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in watched_genres:
            watched_genres[genre] += 1
        else:
            watched_genres[genre] = 1
    if len(watched_genres) == 0:
        return []
    most_frequent_genre = max(watched_genres, key=watched_genres.get)

    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_frequent_genre and movie not in recommended_movies and movie not in user_data["watched"]:
                recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    favorite_movies = user_data["favorites"]
    recommended_movies = []
    for movie in favorite_movies:
        has_watched = False
        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                has_watched = True
                break
        if not has_watched:
            recommended_movies.append(movie)
    return recommended_movies
