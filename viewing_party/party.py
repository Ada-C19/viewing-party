# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]

    if not watched: return 0

    return sum([watched[i]["rating"] for i in range(len(watched))]) / len(watched)

def get_most_watched_genre(user_data):
    watched = user_data["watched"]

    if not watched: return None
    
    genre_list = [watched[i]["genre"] for i in range(len(watched))]
    return max(genre_list, key=genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

