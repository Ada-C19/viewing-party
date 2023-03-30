# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if bool(title) and bool(genre) and bool(rating) == True:
        user_data = {}
        user_data['title'] = title
        user_data['genre'] = genre
        user_data['rating'] = rating
        return user_data
    
    return None

def add_to_watched(user_data, movie):

    user_data['watched'].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, title):

    for movie_data in user_data['watchlist']:
        if title == movie_data['title']:
            user_data['watchlist'].remove(movie_data)
            user_data['watched'].append(movie_data)
            return user_data
    
    if title not in user_data['watchlist']:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
avg_rating = 0
ratings = []
def get_watched_avg_rating(user_data):
    
    if len(user_data["watched"]) > 0:
        for movie_data in user_data["watched"]:
            if "rating" in movie_data:
                ratings.append(movie_data["rating"])
                avg_rating = sum(ratings) / len(ratings)
    else:
        avg_rating = 0.0 

    return avg_rating

def get_most_watched_genre(user_data):
    genres = []
   
    if len(user_data["watched"]) > 0:
        for movie_data in user_data["watched"]:
            if "genre" in movie_data:
                genres.append(movie_data["genre"])
                most_watched_genre = max(set(genres), key = genres.count)
    else:
        return None
    
    return most_watched_genre

def get_watched_avg_rating(user_data):
     
    rating_sum = 0
    num_of_ratings = []

    if len(user_data['watched']) > 0:
        for movie_data in user_data['watched']:
        
            if 'rating' in movie_data:
                num_of_ratings.append(movie_data['rating'])
                rating_sum += movie_data['rating']
                average_rating = rating_sum / len(num_of_ratings)

    else:
        average_rating = float(0)


    return float(average_rating)


def get_most_watched_genre(user_data):
    genres = []
    if len(user_data['watched']) > 0:
        for movie_data in user_data['watched']:
            if 'genre' in movie_data:
                genres.append(movie_data['genre'])
                most_watched_genre = (max(set(genres), key = genres.count))

    else:
        return None
    
    return most_watched_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_unique = []
    for user_watched in user_data['watched']:
        if not user_watched in user_unique:
            user_unique.append(user_watched)

    for friends in user_data['friends']:
        for watched in friends['watched']:
            if watched in user_unique:
                user_unique.remove(watched)

    return user_unique

def get_friends_unique_watched(user_data):
    unique = []
    for friends in user_data["friends"]:
        for watched in friends["watched"]:
            if watched not in unique:
                unique.append(watched)

    for movie_data in user_data["watched"]:
        if movie_data in unique:
            unique.remove(movie_data)
    return unique


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    user_movies = []
    for user in user_data['watched']:
        user_movies.append(user['title'])

    recommend_movies = []
    for friends in user_data['friends']:
        for watched in friends['watched']:
           if not watched['title'] in user_movies and watched['host'] in user_data['subscriptions'] and not watched['title'] in recommend_movies:
               recommend_movies.append(watched)

    return recommend_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

