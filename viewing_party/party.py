# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    return movie_dict

def add_to_watched(user_data, movie):
    #  user data is a dictionary where the key is watched and the value is a list of movies
    # add the movie paramater to theblist of movies
    
    # for movie in user_data:
    #     if movie not in user_data:

    
     user_data["watched"].append(movie)
     return user_data



def add_to_watchlist(user_data, movie):
    pass

def watch_movie(user_data, title):
    pass
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    pass


def get_most_watched_genre(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    pass


def get_friends_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass
