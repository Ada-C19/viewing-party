# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    movie_ratings = {}

    if not title or not genre or not rating:
        return None
    
    movie_ratings["title"] = title
    movie_ratings["genre"] = genre
    movie_ratings["rating"] = rating
    
    return movie_ratings


def add_to_watched(user_data, movie):

    watched = user_data["watched"]
    watched.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    watch_list = user_data["watchlist"]
    watch_list.append(movie)

    return user_data

def watch_movie(user_data, title):
    # list of dictionaries(each dictionary has title, genre, rating)
    watch_list = user_data["watchlist"]
    # list of watched movies
    watched = user_data["watched"]

    for movie in watch_list:
        if title in movie["title"]:
            watch_list.remove(movie)
            watched.append(movie)   
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0
    
    watched = user_data["watched"]
    
    for movie in watched:
        rating = movie["rating"]
        total_rating += rating

    try:
        average_rating = total_rating / len(watched)
    except ZeroDivisionError:
        average_rating = 0.0

    return average_rating


    
def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    
    #return None if watched list is empty
    if len(watched) == 0:
        return None
    
    genre_list = []

    for movie in watched:
        genre = movie["genre"]
        genre_list.append(genre)
    
    max_genre = max((genre_list), key = genre_list.count)
    
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    #user_data = {watched: [{}], friends: [{watched: [{}] }]}

    watched = user_data["watched"]
    friends = user_data["friends"]

    unique_movies = []
    friends_movies = []

    for films in friends:
        for film in films["watched"]:
            friend_title = film["title"]
            friends_movies.append(friend_title)

    for movie in watched:
        title = movie["title"]
        if not title in friends_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    watched = user_data["watched"]
    friends = user_data["friends"]

    friend_unique_movies = []
    user_movies = []

    for movie in watched:
        title = movie["title"]
        user_movies.append(title)

    for films in friends:
        for film in films["watched"]:
            friend_title = film["title"]
            if friend_title not in user_movies and (film not in friend_unique_movies):
                friend_unique_movies.append(film)
    
    return friend_unique_movies
            

    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # list of subscriptions
    user_subscriptions = user_data["subscriptions"]
    # watched dictionary
    friends = user_data["friends"]

    unique_movies = get_friends_unique_watched(user_data)

    recommended_movies = []
    
    for movie in unique_movies:
        friend_host = movie["host"]
        if friend_host in user_subscriptions:
            recommended_movies.append(movie)
    
    return recommended_movies
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

