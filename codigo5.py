# gui.py
import tkinter as tk

from codigo2 import get_movie_details


def search_movie():
    movie_title = entry.get()
    if not movie_title:
        return

    movie_data = get_movie_details(movie_title)

    # Limpa a área de exibição
    movie_info_label.config(text="")
    poster_label.config(image="")

    if "Erro" in movie_data:
        movie_info_label.config(text="Filme não encontrado!")
    else:
        info_text = f"Título: {movie_data['Título']}\n"
        info_text += f"Ano: {movie_data['Ano']}\n"
        info_text += f"Gênero: {movie_data['Gênero']}\n"
        info_text += f"Diretor: {movie_data['Diretor']}\n"
        info_text += f"Atores: {movie_data['Atores']}\n"
        info_text += f"Nota IMDb: {movie_data['Nota IMDb']}"

        movie_info_label.config(text=info_text)


# Criando a interface gráfica
root = tk.Tk()
root.title("Recomendador de Filmes")

# Campo de entrada
entry = tk.Entry(root, width=40)
entry.pack()

# Botão de busca
search_button = tk.Button(root, text="Buscar Filme", command=search_movie)
search_button.pack()

# Label para exibir informações do filme
movie_info_label = tk.Label(root, text="", justify="left")
movie_info_label.pack()

# Label para exibir o pôster do filme (opcional)
poster_label = tk.Label(root)
poster_label.pack()

# Executar a interface gráfica
root.mainloop()