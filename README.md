# Gen_AI_app

## Introduction

Gen_AI_app est une application de machine learning qui utilise Flask pour le backend et Streamlit pour le frontend. Ce projet inclut un modèle de machine learning entraîné pour faire des prédictions basées sur des données d'avocat.

## Prérequis

- Python 3.8 ou supérieur
- Anaconda ou Miniconda
- Un environnement virtuel (recommandé)


## Installation

### 1. Cloner le dépôt

Clonez ce dépôt sur votre machine locale :

git clone https://github.com/votre_utilisateur/Gen_AI_app.git
cd Gen_AI_app
Créer un environnement virtuel
Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet. Vous pouvez créer un environnement virtuel avec Anaconda :


conda create --name gen_ai_env python=3.8
conda activate gen_ai_env
### 3. Installer les dépendances
Installez les dépendances nécessaires en utilisant le fichier requirements.txt :


pip install -r application/model/requirements.txt
### 4. Préparer le modèle
Assurez-vous que le fichier your_model.pkl est présent dans le répertoire application/model/. Si ce n'est pas le cas, vous pouvez générer le modèle en exécutant le script your_script.py :


cd application/model
python your_script.py
Utilisation
1. Démarrer le backend
Naviguez jusqu'au répertoire back et démarrez le serveur Flask :


cd application/back
python back.py
Le serveur Flask devrait démarrer et être accessible à l'adresse http://localhost:5000.

2. Démarrer le frontend
Naviguez jusqu'au répertoire application et démarrez l'application Streamlit :


cd application
streamlit run app.py
L'application Streamlit devrait démarrer et être accessible à l'adresse http://localhost:8501.

Tests
Vous pouvez tester l'API en utilisant des outils comme curl ou Postman. Voici un exemple de requête curl pour tester l'endpoint de prédiction :
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"input": [valeur1, valeur2, valeur3]}'

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails
