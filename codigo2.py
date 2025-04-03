def get_movie_details(title):
    """ Busca informações de um filme pelo título na API OMDb """
    import requests
    from config import API_KEY, BASE_URL

    url = f"{BASE_URL}?apikey={API_KEY}&t={title}"
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()

        if movie_data.get("Response") == "True":
            return {
                "Título": movie_data.get("Title"),
                "Ano": movie_data.get("Year"),
                "Gênero": movie_data.get("Genre"),
                "Diretor": movie_data.get("Director"),
                "Atores": movie_data.get("Actors"),
                "Nota IMDb": movie_data.get("imdbRating"),
                "Poster": movie_data.get("Poster")
            }
        else:
            return {"Erro": "Filme não encontrado!"}
    else:
        return {"Erro": "Falha na requisição!"}