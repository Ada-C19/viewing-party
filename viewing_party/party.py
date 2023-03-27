# ------------- WAVE 1 -------------------- 


def create_movie(title, genre, rating):
    # movies = {}
    
    # If those three attributes are truthy, then return a dictionary. This dictionary should...
    if title and genre and rating:
        # movies.update(new_movies)
        return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    else:
    # - If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`
        return None
    return movies


# Create a function named `add_to_watched`. This function should...
# take two parameters: `user_data`, `movie`
def add_to_watched(user_data, movie):
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
    user_data["watched"] = movie
    if user_data:
        user_data["watched"].update(movie)
    else:
        return None
    

    # - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
    # - ```python
    #   {
    #     "title": "Title A",
    #     "genre": "Horror",
    #     "rating": 3.5
    #   }

#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values


    # new_movie = {}
    # if title and genre and rating : 
    #     new_movie["title"] = title
    #     new_movie["genre"] = genre
    #     new_movie["rating"]= rating   
    #     # print(new_movie)
    #     return new_movie
    
    # else: 
    #     # print(None)
    #     return None
        
        
        
    


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

