# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies_dict = {}
    if not title or not genre or not rating:
        return None
    else:
        movies_dict["title"] = title
        movies_dict["genre"] = genre
        movies_dict["rating"] = rating 
    return movies_dict

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    is_valid = True

    ### checking that watched_list is not empty
    if watched_list:
    ### checking that title is not already in watched_list keys
        for movie_dict in watched_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to watched_list
    if is_valid:
        watched_list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):  
    want_to_watch_list = user_data["watchlist"]
    is_valid = True

    ### checking that want_to_watch_list is not empty
    if want_to_watch_list:
    ### checking that title is not already in want_to_watch_list keys
        for movie_dict in want_to_watch_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to want_to_watch_list
    if is_valid:
        want_to_watch_list.append(movie)

    return user_data

def watch_movie(user_data, title):
    want_to_watch_list = user_data["watchlist"]
    watched_list = user_data["watched"]
    ##iterating through want_to_watch_list to see if title is present
    for movie_dict in want_to_watch_list:
        ##if title present, remove from want_to_watch list and add to watched_list
        if movie_dict["title"] == title:
            watched_list.append(movie_dict)
            want_to_watch_list.remove(movie_dict)
        ##tried to account for if title not in want_to_watch_list or watched_list
        ## else:
             ##if title not present in want_to_watch_list, just add to watched_list
             ##watched_list.append(movie_dict)
    return user_data






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------



def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    avg_rating = 0.0
    ##empty watch list is 0.0 avg rating
    if len(watched_list) == 0:
        return avg_rating
    else:
        ##iterate through watched_list, add all ratings and then divide by length of watched_list
        for movie_dict in watched_list:
            avg_rating += movie_dict["rating"]
        avg_rating = avg_rating/len(watched_list)
    return avg_rating



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

