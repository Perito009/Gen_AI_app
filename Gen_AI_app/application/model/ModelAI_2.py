# application/model/ModelAI_2.py

import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Charger le fichier CSV localement
df = pd.read_csv('avocado.csv')

# Supprimer les colonnes inutiles
df = df.drop(columns=['Unnamed: 0', 'Total Volume', 'Total Bags'])

# Renommer les colonnes
df = df.rename(columns={'4046': 'Quality1', '4225': 'Quality2', '4770': 'Quality3'})

# Convertir les dates
df['Date'] = pd.to_datetime(df['Date'])

# Vérification des données
print(df.isnull().sum())  # Identifier les valeurs manquantes
print(df.duplicated().sum())  # Vérifier l'existence de doublons
df = df.drop_duplicates()  # Supprimer les doublons

# Afficher les premières lignes pour vérification
print(df.head())

# Exemple de modèle de régression linéaire
X = df[['Quality1', 'Quality2', 'Quality3']]
y = df['AveragePrice']

model = LinearRegression().fit(X, y)

# Sauvegarder le modèle en tant que fichier pickle
with open('avocado_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
