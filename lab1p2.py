#1
movie_name:str = "Room"
movie_rate:int = 3
popularity_score: float = 72.65

if movie_rate <= 4 and popularity_score > 80:
    print ("Highly recommended")
elif movie_rate <= 3 and popularity_score > 70:
    print("I recommended it. It is good")
elif movie_rate >= 2 and popularity_score > 60: 
    print("You should cehck it out!")
else:
    print("Don't watch it. It is a waste of time")
     





