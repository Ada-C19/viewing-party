# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if not title or not genre or not rating:
        return None
    
    movie["title"], movie["genre"], movie["rating"] = title, genre, rating
    
    return movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if title != movie['title']:
            continue
        user_data['watched'].append(movie)
        user_data['watchlist'].remove(movie)

    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0.0

    sum = 0
    
    for movie in user_data['watched']:
        sum += movie['rating']

    avg_rating = sum / len(user_data['watched'])
    
    return avg_rating

# Method 2
def get_watched_avg_rating_alternative(user_data):
    avg_rating = sum(int(movie['rating']) for movie in user_data['watched'])/len(user_data['watched'])

    return avg_rating


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
