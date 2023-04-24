# Viewing Party

## Skills Assessed

Solving problems with...

- Conditional logic
- Lists
- Dictionaries
- Nested loops
- Nested data structures
- Pair-programming techniques

## Goal

You and your friends enjoy watching things together online. Of course, everyone has seen different things, has different favorites, and different things they want to watch.

You've been using a spreadsheet to compare everyone's watched list, favorites list, and watchlist, but it's been getting too cumbersome. In order to find things you've watched and your friends haven't watched, or things that your friends have watched and you haven't watched, you have to comb through the spreadsheet. You know that there are different ways we can get that information: we can use Python!

For this project, you and your partner will be given some data structure that represents the things you've watched, favorited, and want to watch. The directions below will lead you and your partner to create a series of functions. These functions will modify the data, and implement features like adding and removing things between different lists. Other features include creating recommendations!

### Wave 1

1. Create a function named  `create_movie`. This function and all subsequent functions should be in `party.py`. `create_movie` should...

- take three parameters: `title`, `genre`, `rating`
- If those three attributes are truthy, then return a dictionary. This dictionary should...
  - Have three key-value pairs, with specific keys
  - The three keys should be `"title"`, `"genre"`, and `"rating"`
  - The values of these key-value pairs should be appropriate values
- If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

2. Create a function named `add_to_watched`. This function should...

- take two parameters: `user_data`, `movie`
  - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
    - An empty list represents that the user has no movies in their watched list
  - the value of `movie` will be a dictionary in this format:
    - ```python
      {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
      }
      ```
- add the `movie` to the `"watched"` list inside of `user_data`
- return the `user_data`

3. Create a function named `add_to_watchlist`. This function should...

- take two parameters: `user_data`, `movie`
  - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
    - An empty list represents that the user has no movies in their watchlist
  - the value of `movie` will be a dictionary in this format:
    - ```python
      {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
      }
      ```
- add the `movie` to the `"watchlist"` list inside of `user_data`
- return the `user_data`

4. Create a function named `watch_movie`. This function should...

- take two parameters: `user_data`, `title`
  - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
    - This represents that the user has a watchlist and a list of watched movies
  - the value of `title` will be a string
    - This represents the title of the movie the user has watched
- If the title is in a movie in the user's watchlist:
  - remove that movie from the watchlist
  - add that movie to watched
  - return the `user_data`
- If the title is not a movie in the user's watchlist:
  - return the `user_data`

Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

### Wave 2

1. Create a function named `get_watched_avg_rating`. This function should...

- take one parameter: `user_data`
  - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries
    - This represents that the user has a list of watched movies
- Calculate the average rating of all movies in the watched list
  - The average rating of an empty watched list is `0.0`
- return the average rating

2. Create a function named `get_most_watched_genre`. This function should...

- take one parameter: `user_data`
  - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
    - This represents that the user has a list of watched movies. Each watched movie has a genre.
    - The values of `"genre"` is a string.
- Determine which genre is most frequently occurring in the watched list
- return the genre that is the most frequently watched
- If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.

### Wave 3

1. Create a function named `get_unique_watched`. This function should...

- take one parameter: `user_data`
  - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
    - This represents that the user has a list of watched movies and a list of friends
    - The value of `"friends"` is a list
    - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
    - Each movie dictionary has a `"title"`.
- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
- Return a list of dictionaries, that represents a list of movies

2. Create a function named `get_friends_unique_watched`. This function should...

- take one parameter: `user_data`
  - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
    - This represents that the user has a list of watched movies and a list of friends
    - The value of `"friends"` is a list
    - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
    - Each movie dictionary has a `"title"`.
- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
- Return a list of dictionaries, that represents a list of movies

### Wave 4

1. Create a function named `get_available_recs`. This function should...

- take one parameter: `user_data`
  - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
    - This represents the names of streaming services that the user has access to
    - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
- Determine a list of recommended movies. A movie should be added to this list if and only if:
  - The user has not watched it
  - At least one of the user's friends has watched
  - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
- Return the list of recommended movies

### Wave 5

1. Create a function named  `get_new_rec_by_genre`. This function should...

- take one parameter: `user_data`
- Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
  - The user has not watched it
  - At least one of the user's friends has watched
  - The `"genre"` of the movie is the same as the user's most frequent genre
- Return the list of recommended movies

2. Create a function named  `get_rec_from_favorites`. This function should...

- take one parameter: `user_data`
  - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
    - This represents the user's favorite movies
- Determine a list of recommended movies. A movie should be added to this list if and only if:
  - The movie is in the user's `"favorites"`
  - None of the user's friends have watched it
- Return the list of recommended movies
