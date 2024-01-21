import tkinter as tk
from tkinter import scrolledtext, StringVar,PhotoImage
import random
from tkinter import ttk

def get_recommendations():
        
        select= combo_var.get()
        
        movie = {
    'Inception': 'Sci-Fi',
    'The Shawshank Redemption': 'Drama',
    'Pulp Fiction': 'Crime',
    'The Dark Knight': 'Action',
    'Forrest Gump': 'Drama',
    'The Godfather': 'Crime',
    'The Matrix': 'Sci-Fi',
    'Schindler\'s List': 'Drama',
    'Fight Club': 'Drama',
    'The Lord of the Rings: The Fellowship of the Ring': 'Fantasy',
    'The Silence of the Lambs': 'Thriller',
    'The Avengers': 'Action',
    'Titanic': 'Romance',
    'The Lion King': 'Animation',
    'Back to the Future': 'Adventure',
    'Gladiator': 'Action',
    'The Terminator': 'Sci-Fi',
    'Jurassic Park': 'Adventure',
    'Braveheart': 'Drama',
    'Avatar': 'Sci-Fi',
    'The Shining': 'Horror',
    'Casablanca': 'Romance',
    'Gone with the Wind': 'Drama',
    'Star Wars: Episode IV - A New Hope': 'Sci-Fi',
    'The Great Gatsby': 'Drama',
    'The Social Network': 'Drama',
    'Inglourious Basterds': 'War',
    'The Grand Budapest Hotel': 'Comedy',
    'La La Land': 'Musical',
    'Interstellar': 'Sci-Fi',
    'The Revenant': 'Adventure',
    'The Departed': 'Crime'
}
        
        
        selectgenre=movie[select]
        recommended_movie=[]
        for i in movie:
                if movie[i]==selectgenre and i!=select:
                        recommended_movie.append(i)
        l=len(recommended_movie)
        
        if recommended_movie!=[]:
            
            recommendation_history.insert(tk.END, f"\nAI Recommends for {select}: \n")
            for i in range (0,l):
                recommendation_history.insert(tk.END, f"{i+1} . {recommended_movie[i]}\n")
        else:
            recommendation_history.insert(tk.END, f"\nAI Recommends for {select}: \n")
            recommendation_history.insert(tk.END, "No recommendations based on your preferences.\n")
        recommendation_history.see(tk.END)


    

root = tk.Tk()
root.title("movie recommendation System")
movies = [
    'Inception', 'The Shawshank Redemption', 'Pulp Fiction', 'The Dark Knight', 'Forrest Gump',
    'The Godfather', 'The Matrix', 'Schindler\'s List', 'Fight Club', 'The Lord of the Rings: The Fellowship of the Ring',
    'The Silence of the Lambs', 'The Avengers', 'Titanic', 'The Lion King', 'Back to the Future',
    'Gladiator', 'The Terminator', 'Jurassic Park', 'Braveheart', 'Avatar', 'The Shining', 'Casablanca',
    'Gone with the Wind', 'Star Wars: Episode IV - A New Hope', 'The Great Gatsby', 'The Social Network',
    'Inglourious Basterds', 'The Grand Budapest Hotel', 'La La Land', 'Interstellar', 'The Revenant', 'The Departewod'
]

custom1=("Aerial",25)
custom2=("Aerial",40)
custom3=("Aerial",40)
root.configure(bg="red")
combo_var = tk.StringVar(value=movies[0])
combobox = ttk.Combobox(root, textvariable=combo_var, values=movies,font=custom2)
combobox.pack(pady=20)
recommend_button = tk.Button(root, text="Get Recommendations",font=custom1,command=get_recommendations)
recommend_button.pack(pady=1)
recommendation_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=100,font=custom3)
recommendation_history.pack(padx=10, pady=10)

    


    
    
