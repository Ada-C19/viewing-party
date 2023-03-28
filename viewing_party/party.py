# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #create and empty dictionary to store title, genre and rating of the movie
    movie_dictionary = {}
    #this if statement evaluate that title, genre and rating
    #have some value different from None
    #besides checking if this parameters are truthy we also evaluate that they're the 
    #appropiate type of data
    if type(title) == str and type(genre) == str and type(rating) == float:
        #if the parameters are truthy then we add title,genre and rating
        #to movie_dictionary
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
        return movie_dictionary
    return None

def add_to_watched(user_data, movie):
    #append movie dictionary to the key "watched" in user_data dictionary
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    #append movie dictionary to the key "watchlist" in user_data dictionary
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    #nested for loop to loop through the outer dictionary first "user_data"
    #and look for the key "watchlist"
    for watch in user_data.keys():
        if watch == "watchlist":
            #inner for loop check if the title of the movie is in the list of dictionaries
            #stored in "watchlist key"
            for movie in user_data[watch]:
                if movie["title"] == title:
                    temp_movie = user_data[watch].pop()
                    add_to_watched(user_data, temp_movie)
                    
    return user_data
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

