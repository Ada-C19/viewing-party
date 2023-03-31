# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not (title and genre and rating):
        return None
    else:
        movie = { "title" : title,
                    "genre" : genre,
                    "rating" : rating}
        return movie
    
def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break

    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if not user_data["watched"]:
        return 0.0
    else:
        total_rating = sum(movie["rating"] for movie in user_data["watched"])
        return total_rating / len(user_data["watched"])
    
def get_most_watched_genre(user_data):

    if not user_data["watched"]:
        return None
    
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    return max(genre_count, key=lambda genre: genre_count[genre])

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_movies = user_data["watched"]
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)

    unique_movies = []

    for user_movie in user_movies:
        if user_movie not in friend_movies and user_movie not in unique_movies:
            unique_movies.append(user_movie)

    print(f"{unique_movies = }")
    return unique_movies

    # user_movies = set([movie['title'] for movie in user_data['watched']])
    # friends_movies = set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']])
    # unique_movies = user_movies.difference(friends_movies)
    # unique_movies = [{'title': movie} for movie in unique_movies]
    # print(f"{unique_movies = }")
    # return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
            
    unique_movies = []

    for friend_movie in friend_movies:
        if friend_movie not in user_movies and friend_movie not in unique_movies:
            unique_movies.append(friend_movie)

    # print(f"{unique_movies = }")
    return unique_movies

#     user_movies = set([movie['title'] for movie in user_data['watched']])
#     friends_movies = set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']])
#     unique_movies = friends_movies.difference(user_movies)
#     return [{'title': movie} for movie in unique_movies]
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movies_not_watched = get_friends_unique_watched(user_data)
    recommendations = []
    sub_list = user_data["subscriptions"]
    for movie in movies_not_watched:
        if movie["host"] in sub_list:
                recommendations.append(movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    recommendations = []
    not_watched_yet = get_friends_unique_watched(user_data)
    fav_genre = get_most_watched_genre(user_data)

    for movie in not_watched_yet:
        if movie["genre"] == fav_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    favorites = user_data["favorites"]
    user_unique = get_unique_watched(user_data)

    for movie in user_unique:
            if movie in favorites:
                recommendations.append(movie)

    return recommendations