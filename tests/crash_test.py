from tests.test_constants import *

def get_new_rec_by_genre(user_data):
    genre_count = []

    for i in user_data["watched"]:
        genre_count.append(user_data["watched"][i]["genre"])
    
    current_favorite_count = 0
    current_favorite = ""

    for genre in genre_count:
        if genre_count.count(genre) > current_favorite_count:
            current_favorite_count = genre_count.count(genre)
            current_favorite = genre
    
    print(current_favorite)



sonyas_data = clean_wave_5_data()
get_new_rec_by_genre(sonyas_data)
