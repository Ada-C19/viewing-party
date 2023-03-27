# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # check if title, genre, or rating is falsy
    if (not title) or (not genre) or (not rating):
        # return None
        return None
    # check if title_value and genre_value are string, rating is a float
    if (not isinstance(title, str)) or (not isinstance(genre, str)) or (not isinstance(rating, float)):
        # raise ValueError("Invalid input")
        return None
    # initialize empty dictionary
    new_movie = {}

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = float(rating)

    return new_movie


create_movie("Scream 6", "Horror", 4.0)


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


movie = {
    "title": "Lion King",
    "genre": "Family",
    "rating": 5.0
}
user_data = {"watched": []}

add_to_watched(user_data, movie)
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
