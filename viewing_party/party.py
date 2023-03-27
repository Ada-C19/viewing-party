# ------------- WAVE 1 --------------------

# Let's start
# Hola, Laura!


def create_movie(title, genre, rating):
    title_check = isinstance(title, str)
    print(title_check)
    genre_check = isinstance(genre, str)
    rating_check = isinstance(rating, float)
    if not title_check or not genre_check or not rating_check:
        return None
    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie
    
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5
# movie_title = "Title A"
# genre = None
# rating = 3.5
# movie_title = MOVIE_TITLE_1
# genre = GENRE_1
# rating = RATING_1
print(create_movie(MOVIE_TITLE_1, GENRE_1, RATING_1))


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

