import operator

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
    if len(user_data['watched']) == 0:
        return 0.0
    
    return sum(movie['rating'] for movie in user_data['watched']) / len(user_data['watched'])

def get_most_watched_genre(user_data):
    if len(user_data['watched']) == 0:
        return None
    
    max_watched_dict = {}

    for movie in user_data['watched']:
        max_watched_dict[movie['genre']] = max_watched_dict.get(movie['genre'], 0) + 1

    max_watched_list = list(sorted(max_watched_dict.items(), key=operator.itemgetter(1), reverse=True))
    
    return max_watched_list[0][0]

# ------------- WAVE 3 --------------------

def get_watched_set_from_data(user_data):
    user_watched_movies_set = set(movie['title'] for movie in user_data['watched'])
    
    friends_watched_movie_set = set()
    for friend_dict in user_data['friends']:
        friends_watched_movie_set.update(set(movie['title'] for movie in friend_dict['watched']))

    return user_watched_movies_set, friends_watched_movie_set

def get_unique_watched(user_data):
    user_watched_movies_set, friends_watched_movie_set = get_watched_set_from_data(user_data)
    user_unique_set = user_watched_movies_set - friends_watched_movie_set
    
    return [movie for movie in user_data['watched'] if movie['title'] in user_unique_set]

def get_friends_unique_watched(user_data):
    user_watched_movies_set, friends_watched_movie_set = get_watched_set_from_data(user_data)
    friends_unique_set = friends_watched_movie_set - user_watched_movies_set

    friends_unique_list = []

    for friend_dict in user_data['friends']:
        friends_unique_list.extend(movie for movie in friend_dict['watched'] if movie['title'] in friends_unique_set if movie not in friends_unique_list)

    return friends_unique_list

# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    user_subscriptions = [host for host in user_data['subscriptions']]
    friends_unique_watched = get_friends_unique_watched(user_data)
    
    return [movie for movie in friends_unique_watched if movie['host'] in user_subscriptions]

# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    top_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    return [movie for movie in friends_unique_watched if movie['genre'] == top_genre]

def get_rec_from_favorites(user_data):
    user_unique_watched = get_unique_watched(user_data)
    
    return [movie for movie in user_unique_watched if movie in user_data['favorites']]