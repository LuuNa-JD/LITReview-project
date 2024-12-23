# LitReview

## Description

Ma nouvelle application permet de demander ou publier des critiques de livres ou d’articles. L’application présente trois cas d’utilisation principaux :

- la publication des critiques de livres ou d’articles ;
- la demande des critiques sur un livre ou sur un article particulier ;
- la recherche d’articles et de livres intéressants à lire, en se basant sur les critiques des autres.

## Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez le repository :

   ```bash
   git clone https://github.com/LuuNa-JD/LITReview-project.git
   cd LITReview-project
   ```

2. Créez un environnement virtuel :

   ```bash
   python -m venv venv
   ```

   Activez l'environnement virtuel :

   - Sur Windows :

     ```bash
     venv\Scripts\activate
     ```

   - Sur macOS et Linux :

     ```bash
     source venv/bin/activate
     ```

   Pour désactiver l'environnement virtuel, exécutez la commande suivante :

   ```bash
   deactivate
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Créez un fichier `.env` à la racine de votre projet et ajoutez-y votre clé secrète.
   Exemple de contenu `.env` :
   ```plaintext
   SECRET_KEY='votre_clé_secrète'
   ```
    Pour obtenir la clé secrete, vous pouvez me la demander par mail.

5. La base de données SQLite `db.sqlite3` est incluse dans ce projet.
    Si vous souhaitez utiliser une nouvelle base de données, vous pouvez la créer en exécutant les commandes suivantes :

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Créez un superutilisateur :

    Pas besoin de créer un superutilisateur si vous utilisez la base de données SQLite fournie.
   ```bash
   python manage.py createsuperuser
   ```

   Suivez les instructions pour créer un superutilisateur.

## Démarrer l'application

1. Démarrez le serveur :
    - Activez votre environnement virtuel si ce n'est pas déjà fait.
   ```bash
   python manage.py runserver
   ```

2. Accédez à l'application : `http://127.0.0.1:8000/`

## Comptes de test

Pour tester l'application, vous pouvez utiliser les comptes suivants :

1. **Utilisateur Administrateur**
   - Nom d'utilisateur : `Admin`
   - Mot de passe : `Azerty123*`

2. **Utilisateur Simple**
   - Nom d'utilisateur : `Harry`
   - Mot de passe : `Azerty123*`

Ces comptes vous permettront de vous connecter et d'explorer les fonctionnalités de l'application.
