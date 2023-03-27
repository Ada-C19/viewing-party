# ------------- WAVE 1 --------------------
#Wave 1- 

#user_data = {
#     watched : [{"move_1"}, "movie_2", "movie_3"}]
#}
#USER_DATA_2 = {
#     "watched": [
#         FANTASY_1, 
#         FANTASY_2, 
#         FANTASY_3, 
#         ACTION_1, 
#         INTRIGUE_1, 
#         INTRIGUE_2
#         ],    
# }

# Wave 1
# 1. Create a function named  `create_movie`. This function and all subsequent 
#functions should be in `party.py`. `create_movie` should...

# - take three parameters: `title`, `genre`, `rating`
# - If those three attributes are truthy, then return a dictionary. This dictionary should...
#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values
# - If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

# 2. Create a function named `add_to_watched`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
#     - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watched"` list inside of `user_data`
# - return the `user_data`

# 3. Create a function named `add_to_watchlist`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
#     - An empty list represents that the user has no movies in their watchlist
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watchlist"` list inside of `user_data`
# - return the `user_data`

# 4. Create a function named `watch_movie`. This function should...

# - take two parameters: `user_data`, `title`
#   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
#     - This represents that the user has a watchlist and a list of watched movies
#   - the value of `title` will be a string
#     - This represents the title of the movie the user has watched
# - If the title is in a movie in the user's watchlist:
#   - remove that movie from the watchlist
#   - add that movie to watched
#   - return the `user_data`
# - If the title is not a movie in the user's watchlist:
#   - return the `user_data`

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.

def create_movie(title, genre, rating):
    #conditional: if the three attributes (keys) exits return the key and value, if not return non
#def add_to_watched(user_data, movie):
# if title and genre and rating are true, then return dictionary and if one of them is not true, then return none

    #for movie in title:

    movies = title, genre, rating
    if all(movies):
    #if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None

#Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
#print("\nDictionary with the use of dict(): ")
#print(Dict)
         

   
        
    # pass
# def test_create_successful_movie():
#     # Arrange
#     movie_title = MOVIE_TITLE_1
#     genre = GENRE_1
#     rating = RATING_1

#     # Act
#     new_movie = create_movie(movie_title, genre, rating)

#     # Assert
#     assert new_movie["title"] == MOVIE_TITLE_1
#     assert new_movie["genre"] == GENRE_1
#     assert new_movie["rating"] == pytest.approx(RATING_1)


def add_to_watched(user_data, movie):
    pass

def add_to_watchlist(user_data, movie):
    pass

def watch_movie(user_data, title):
    pass
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

