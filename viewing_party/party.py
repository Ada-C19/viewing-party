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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

