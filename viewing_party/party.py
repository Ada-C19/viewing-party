# ------------- WAVE 1 --------------------
import pprint

def create_movie(title, genre, rating):
    """Create dictionary containing title, genre, and rating of a movie
    
    Keyword arguments:
    title -- the title of the movie
    genre -- the genre of the movie
    rating -- the rating of the movie
    """
    # Return None if any parameter is falsy
    if not title or not genre or not rating:
        return None
        
    movie = {
        "title": title, 
        "genre": genre,
        "rating": rating
    }

    return movie

def add_to_watched(user_data, movie):
    """Add a movie to watched list.
    
    Keyword arguments:
    user_data -- dictionary containing movies user has and wants to watch
    movie -- dictionary containing title, genre, and rating
    """
    # Check movie isn't empty and is a dictionary
    # Try to add movie to watched, otherwise give error message
    if movie and isinstance(movie, dict):
        try:
            user_data["watched"].append(movie)
        except KeyError:
            print("'Watched' key does not exist; could not add movie")
    
    return user_data

def add_to_watchlist(user_data, movie):
    """Add a movie to a watchlist.
    
    Keyword arguments:
    user_data -- dictionary containing movies user has and wants to watch
    movie -- dictionary containing title, genre, and rating
    """
    # Check movie isn't empty and is a dictionary
    # Try to add movie to watchlist, otherwise give error message
    if movie and isinstance(movie, dict):
        try:
            user_data["watchlist"].append(movie)
        except KeyError:
            print("'Watchlist' key does not exist; could not add movie")
    
    return user_data

def watch_movie(user_data, title):
    """Move movie if in watchlist to watched
    
    Keyword arguments:
    user_data -- dictionary containing movies user has and wants to watch
    title -- the movie title 
    """
    # Check title is a string and not empty, otherwise return user_data
    if not isinstance(title, str) or not title:
        return user_data

    # Check if movie with title in watchlist
    # If it is, append movie to watched and remove from watchlist
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """Return average rating of all movies in watched list.
    
    Keyword arguments:
    user_data -- dictionary containing movies user has and wants to watch
    """
    # Empty watched list
    if not user_data["watched"]:
        return 0.0
    
    sum_of_ratings = 0 
    for movie in user_data["watched"]:
        sum_of_ratings += movie.get("rating") # Add to sum
    
    # Calculate and return average
    return sum_of_ratings / len(user_data["watched"])

def get_most_watched_genre(user_data):
    """Return most watched genre in watched list.
    
    Keyword arguments:
    user_data -- dictionary containing movies user has and wants to watch
    """
    # Empty watched list
    if not user_data["watched"]:
        return None
    
    # Track each genre and its count
    most_watched_genres = {}
    for movie in user_data["watched"]:
        genre = movie.get("genre")
        if not genre in most_watched_genres:
            most_watched_genres[genre] = 1
        else:
            most_watched_genres[genre] += 1
    
    # Determine first instance of genre in dictionary with highest count
    most_watched_genre = max(most_watched_genres, key=most_watched_genres.get)
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    """Return list of dictionaries of movies only the user watched.
    
    Keyword arguments:
    user_data -- dictionary containing movies user and friends has watched
    """
    # Create unique list of friends' movies watched
    friends_watched = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    
    # Check if each of user's movies is in friends' watched list
    # If not, add to unique list if not already in it
    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_watched and movie not in unique_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    """Return list of dictionaries of movies only friends watched.
    
    Keyword arguments:
    user_data -- dictionary containing movies user and friends has watched
    """  
    # Check if each friends' movie is in user's watched list
    # If not, add to unique list if not already in it
    unique_watched = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if (movie not in user_data["watched"]
                    and movie not in unique_watched):
                unique_watched.append(movie)
    
    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """Return list of dictionaries of movies recommended for user.
    
    Keyword arguments:
    user_data -- dictionary containing movies user and friends has watched
    """  
    # Check if each friends' movie is in user's watched list
    # If not, add to movie recs list if not already in it 
    # and user has subscription
    movie_recs = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if (movie not in user_data["watched"]
                    and movie not in movie_recs 
                    and movie["host"] in user_data["subscriptions"]):
                movie_recs.append(movie)
            
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """Return list of dictionaries of movies recommended for user by genre.
    
    Keyword arguments:
    user_data -- dictionary containing movies user and friends has watched
    """  
    # Check if each friends' movie is in user's watched list
    # If not, add to genre recs list if not already in it 
    # and matches user's most watched genre
    most_watched_genre = get_most_watched_genre(user_data)

    genre_recs = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if (movie not in user_data["watched"]
                    and movie not in genre_recs 
                    and movie["genre"] == most_watched_genre):
                genre_recs.append(movie)
    
    return genre_recs

def get_rec_from_favorites(user_data):
    """Return list of dictionaries of movies recommended from user favorites.
    
    Keyword arguments:
    user_data -- dictionary containing movies user and friends has watched
    """
    # Create unique list of friends' movies watched
    friends_watched = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    
    # Check if each of user's movies is in friends' list
    # If not, add to favorite recs list if not already in it
    favorite_recs = []
    for movie in user_data["favorites"]:
        if movie not in friends_watched and movie not in favorite_recs:
            favorite_recs.append(movie)

    return favorite_recs
