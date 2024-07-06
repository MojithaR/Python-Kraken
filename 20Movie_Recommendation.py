# Movie_Recommendation.py

movies = {
    "Inception": ["sci-fi", "thriller"],
    "The Matrix": ["sci-fi", "action"],
    "Titanic": ["romance", "drama"],
    "The Godfather": ["crime", "drama"],
    "Toy Story": ["animation", "family"]
}

def recommend_movie(genre):
    recommendations = [title for title, genres in movies.items() if genre in genres]
    if recommendations:
        return f"Recommended movies: {', '.join(recommendations)}"
    else:
        return "No movies found for this genre."

if __name__ == "__main__":
    genre = input("Enter a genre (e.g., sci-fi, drama): ").lower()
    print(recommend_movie(genre))
