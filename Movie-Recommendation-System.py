import tkinter as tk
from tkinter import scrolledtext, StringVar,PhotoImage
import random
from tkinter import ttk

def get_recommendations():
        
        select= combo_var.get()
        recommended_movie=[]
        with open("E:/code/movie2.txt") as f:
                l=f.readlines()
                for r in l:
                        if r.find(select)!=-1:
                                selectgenres=r.split(':')[-1]
                selectgenre=[]
                for i in selectgenres.split():
                        selectgenre.append(i)
                full=len(selectgenre)
                for r in l:
                        rank=0
                        for sel in selectgenre:
                                if r.find(sel)!=-1 and r.find(select)==-1 :
                                        rank+=1
                                        if rank==full:
                                                recommended_movie.append(r.split(':')[0])
                                                
                
        if recommended_movie!=[] and len(recommended_movie)>=5:
            
            recommendation_history.insert(tk.END, f"\nAI Recommends for {select}: \n")
            for i in range (0,5):
                recommendation_history.insert(tk.END, f"{i+1} . {recommended_movie[i]}\n")
        else:
            for r in l:
                rank=1
                for sel in selectgenre:
                        if r.find(sel)!=-1 and r.find(select)==-1 :
                                rank+=1
                                if rank==full:
                                        recommended_movie.append(r.split(':')[0])
            recommendation_history.insert(tk.END, f"\nAI Recommends for {select}: \n")
            for i in range (0,5):
                recommendation_history.insert(tk.END, f"{i+1} . {recommended_movie[i]}\n")
            
        recommendation_history.see(tk.END)
root = tk.Tk()
root.title("movie recommendation System")
with open("E:/code/movie2.txt") as f:
        l=f.readlines()
        movies=[]
        for r in l:
                movies.append(r.split(':')[0])
custom1=("Aerial",25)
custom2=("Aerial",40)
custom3=("Aerial",30)
root.configure(bg="red")
combo_var = tk.StringVar(value=movies[0])
combobox = ttk.Combobox(root, textvariable=combo_var, values=movies,font=custom2)
combobox.pack(pady=20)
recommend_button = tk.Button(root, text="Get Recommendations",font=custom1,command=get_recommendations)
recommend_button.pack(pady=1)
recommendation_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=100,font=custom3)
recommendation_history.pack(padx=10, pady=10)
