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

def get_unique_watched(user_data):
    watched_movies_set = set(movie['title'] for movie in user_data['watched'])
    
    friends_movie_set = set()
    for friend_dict in user_data['friends']:
        friends_movie_set.update(set(movie['title'] for movie in friend_dict['watched']))
        
    unique_set = watched_movies_set - friends_movie_set
    
    return [m for m in user_data['watched'] if m['title'] in unique_set]

def get_unique_watched_alternative(user_data):
    movie_titles_friends_watched = set()
    movies_friends_not_watched_list = []
    movies_friends_not_watched_list_dict = []

    for friend_movie in user_data["friends"]:
        for movie in friend_movie["watched"]:
            movie_titles_friends_watched.add(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] not in movie_titles_friends_watched:
            movies_friends_not_watched_list.append(movie["title"])
            movie_element = {}
            movie_element["genre"]= movie["genre"]
            movie_element["rating"] = movie["rating"]
            movie_element["title"] = movie["title"]
            movies_friends_not_watched_list_dict.append(movie_element)
                
    return movies_friends_not_watched_list_dict

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
