# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
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
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data        
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data): 
    # average_rating = 0.0
    sum = 0.0
    for movie in user_data["watched"]:
        for rating in movie:
            if rating == movie["rating"]:
                sum += rating
    average_rating = sum/len(user_data["watched"])
    return average_rating
        # else:
        #     average_rating = 0.0

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

