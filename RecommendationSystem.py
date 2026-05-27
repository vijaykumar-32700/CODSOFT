import random

print("====Movie Recommendation System=====")

movies={
    "action": [("Avengers",9), ("Batman",8), ("John Wick",9)],
    "comedy": [("Mr Bean",8), ("The Mask",9), ("Jumanji",8)],
    "horror": [("Conjuring",9), ("Insidious",8), ("Annabelle",7)],
    "romance": [("Titanic",9), ("Notebook",8), ("La La Land",8)]
}

print("\nAvailable Genres:")
for genre in movies:
    print("-",genre)

choice=input("\nChoose Genre: ").lower()

if choice in movies:

    print("\nRecommended Movies:")

    for movie, rating in movies[choice]:
        print(f"{movie}  {rating}/10")

    surprise = random.choice(movies[choice])

    print("\nSurprise Pick For You:")
    print(f"{surprise[0]} co {surprise[1]}/10")

else:
    print("Sorry! Genre not available.")