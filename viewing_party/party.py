# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if not (title and genre and rating):
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0 
    count = 0

    if user_data["watched"] != []:
        for i in range(len(user_data["watched"])):
            rating = user_data["watched"][i]["rating"]
            sum += rating
            count += 1
    if count > 0:
        return sum / count
    return 0.0
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# ----------------------------------------
    


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

