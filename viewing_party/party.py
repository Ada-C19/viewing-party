from statistics import multimode,mode
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # Set initial value of sum_rating to 0
    sum_rating = 0
    # Create a new list of "watched" movies in user_data dict
    movie_list = user_data["watched"]

    # Iterate through movies in list of movies
    for movie in movie_list:
        # Find the sum of the integers in value for "rating" in the movie dict
        sum_rating += movie["rating"]
    # If the input is an empty list, return 0.0 for average
    if len(movie_list) == 0:
        return 0.0
    else:
        # Return the sum of movie ratings divided by the number of movies in input user_data dict
        return sum_rating / len(movie_list)


def get_most_watched_genre(user_data):
    genre_list = []

    # Create a new list of "watched" movies in user_data dict
    movie_list = user_data["watched"]
    # Iterate through movies in list of movies
    for movie in movie_list:
        # Append genre values to the empty list genre_list
        genre_list.append(movie["genre"])
    # If genre_list is empty, return None
    if len(genre_list) == 0:
        return None
    else:
        # It was returning as a string in a list, so I used [0] to return genre as a string
        return(multimode(genre_list)[0])


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

