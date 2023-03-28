# ------------- WAVE 1 --------------------

#Create definition to store movie
def create_movie(title, genre, rating):
    #create empty dictionary to store the movie
    movie = { "title": "", "genre" : "", "rating" : 0}

    #Check for edge case of one item being empty 
    if title is False or genre is False or rating is False:
        return None
    else:
        movie["title"]= title
        movie["genre"]= genre
        movie["rating"]= rating

    return movie

def add_to_watched(user_data, movie):
    pass
    
def add_to_watchlist(user_data, movie):
    pass




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # average_rating = 0.0
    # sum_rating = 0
    # for movies in user_data:
    #     sum_rating += sum(["rating"])
    #     average_rating = sum_rating / len(movies)

    # return average_rating
    sum_rating = 0
    average_rating = 0.0
    watched_movies = user_data.get("watched")
    if not watched_movies:
        return 0.0
    for movie in watched_movies:
        sum_rating += movie.get("rating", 0)
    average_rating = sum_rating / len(watched_movies)
    return average_rating 

def get_most_watched_genre(user_data):
    most_watched_genre = None
    # genre_list = user_data.get("watched")

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# def get_unique_watched(user_data):


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

