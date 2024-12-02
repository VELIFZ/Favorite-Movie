# name as key: genre, director, rating, year as values
# user input to add favorites   
# conditional statements to see informations or use the functions 
# use strip and lower etc to avoid duplicates



# class Movie():
#     def __init__(self):
#         pass

def add_movie():
    
    while True:
        #whole dictionary
        movie_list = {}     
        # Main key for movie_list dict
        name = input("Movie name or 'none' for no more movies")
        # avoid duplicates
        if name in movie_list:
           return f'You already added {name}.' 
        # need contitional to stop the loop    
        if name == 'none':
            break
    
        # values for nested dict
        genre = input("Which genre?") 
        director = input("Who directed?")
        year = input("What year was made?")
        rating = input("IMd or rorren tomato ratings")

        #creating nested dict
        movie_list[name] = {
        'Genre': genre,
        'Director' : director,
        'year' :year,
        'rating' : rating
        }
    

def remove_movie():
    pass


def display_movie():
    pass
    
   
