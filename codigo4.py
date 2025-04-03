# recommendation_model.py
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Exemplo de dados: ID do filme e suas características (features)
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'feature_1': [0.1, 0.2, 0.1, 0.4, 0.5],
    'feature_2': [0.5, 0.3, 0.6, 0.1, 0.8],
    'feature_3': [0.3, 0.7, 0.4, 0.2, 0.9]
}

df = pd.DataFrame(data)

# Extraindo as características
X = df[['feature_1', 'feature_2', 'feature_3']]

# Ajustando o modelo KNN
knn = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
knn.fit(X)

# Recomendando filmes similares ao filme com ID 1
movie_index = 0  # ID 1
distances, indices = knn.kneighbors([X.iloc[movie_index]])

# Exibindo as recomendações
print("Recomendações para o filme ID 1:")
for i in indices[0]:
    print(f"Filme recomendado ID: {df['movie_id'][i]}")