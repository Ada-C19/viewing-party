# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    
    return None

def add_to_watched(user_data, movie):
    if movie not in user_data.get("watched"):
        user_data.get("watched").append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if movie not in user_data.get("watchlist"):
        user_data.get("watchlist").append(movie)

    return user_data

def watch_movie(user_data, title):
    movies = user_data.get("watchlist")

    for movie in movies:
        if title == movie["title"]:
            movies.remove(movie)
            user_data.get("watched").append(movie)
    
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = []
    try:
        for movie in user_data["watched"]:
            rating.append(movie["rating"])
        return sum(rating) / len(rating)
    except ZeroDivisionError:
        return 0.0
    except KeyError: # Incase the key "watched" is missing
        return None

def get_most_watched_genre(user_data):
    genre = {}

    try:
        for movie in user_data.get("watched"):
            if movie["genre"] not in genre:
                genre[movie["genre"]] = 1

            genre[movie["genre"]] += 1
            print(genre)
    except TypeError:
        return None
    
    if genre:
        return max(genre, key=genre.get)
    
    return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# ------------------------------------------
def get_unique_watched(user_data):
    user_data = {
        "watched": [{movie}, {movie}, ..],
        "friends": [{watched: [{movie}]}, {watched}, {watched}]
    }
    
    watched = set()
    friends_watched = set()

    for movie in user_data.get("watched"):
        watched.add(movie)
    
    for friend in user_data.get("friends"):
        friends_watched.extend(friend.get("watched"))
    
    return list(watched - friends_watched)

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

