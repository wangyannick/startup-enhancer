# Projet Big data architecture and data processing - ESIEA

### Membre du groupe :

ABENAQUI Adrien, AKYOL Olivier, WANG Yannick, ES-KOUSRI Ali, GAMBERT Lucas

## 1. La problématique que vous souhaitez traiter.

- Comment augmenter ses chances lors de la création d'une entreprise ?

- Quels sont les meilleurs paramètres à prendre en compte pour que son entreprise réussisse ?

- Comment mettre les probabilités de notre côté pour créer une entreprise pérenne ?

Ces questions nous ont amenés à nous interroger sur les facteurs qui influencent le plus le succès d'une startup. Nous avons donc décidé de nous concentrer sur les facteurs qui sont les plus importants pour un entrepreneur lorsqu'il envisage de créer une entreprise.

Les facteurs les plus importants pour un entrepreneur sont les suivants :

- La catégorie de l'entreprise

- Le pays où l'entreprise est créée

- Le montant de la levée de fonds

- Le nombre de personnes dans l'équipe de direction

- Le nombre de personnes dans l'équipe au total

- Le nombre d'investisseurs

- Le montant de la dernière levée de fonds

- La date de création de l'entreprise

- La date de la dernière levée de fonds

## 2. Le choix des composants / outils que vous avez utilisé pour répondre à votre problématique.

Le choix des composants pour répondre à la problématique a été effectué en fonction des besoins en matière de stockage, de traitement et de visualisation des données.

- PostgreSQL a été choisi pour le stockage des données en raison de sa fiabilité, de sa scalabilité et de sa puissance en matière de gestion de données relationnelles.

- Numpy et Pandas ont été choisis pour le traitement des données en raison de leur capacité à manipuler efficacement des tableaux de données numériques et à fournir des fonctionnalités de traitement de données telles que l'agrégation, la filtration et l'analyse statistique.

- Python avec une API Rest créée à l'aide du framework Flask a été choisi pour envoyer les données vers le tableau de bord en raison de sa capacité à créer rapidement des applications web et de sa facilité à intégrer des bibliothèques pour le traitement de données.

- ReactJS avec la librairie ChartJS a été choisi pour le front du tableau de bord en raison de sa popularité et de sa facilité d'utilisation pour créer des interfaces utilisateur interactives et des visualisations de données attrayantes.

En résumé, le choix de ces composants a été effectué en fonction de leur capacité à satisfaire les besoins en matière de stockage, de traitement et de visualisation des données pour répondre efficacement à la problématique.

## 3. Le détail de l'installation ou du déploiement de votre application avec Docker

Notre application a été entièrement dockerisée, ce qui signifie que tous les composants nécessaires pour son fonctionnement sont empaquetés dans des conteneurs Docker. Cela facilite la mise en place de l'application en assurant une compatibilité et une cohérence des versions entre les différents composants.

Lancer le serveur, la base de données PostgreSQL et le tableau de bord est simple grâce à Docker Compose. Il suffit de taper la commande `docker-compose up` dans un terminal pour lancer les conteneurs nécessaires.

Si c'est la première fois que le conteneur PostgreSQL est lancé, il faut attendre un certain temps pour que les données soient importées. Ce temps dépendra de la taille des données à importer, mais une fois l'import terminé, l'application est prête à être utilisée.

En utilisant Docker, nous avons rendu l'application facile à installer et à gérer, tout en assurant une compatibilité entre les composants pour une expérience utilisateur stable et fiable.

Lors du lancement des applications avec docker-compose, les différents composants sont assignés à des ports spécifiques pour leur accès. Le container PostgreSQL est accessible sur le port `5432`, le serveur Flask sur le port `3333` et le tableau de bord sur le port `5173`. Tous ces ports sont accessibles sur `localhost`, ce qui signifie qu'ils peuvent être atteints en utilisant l'adresse IP locale de la machine sur laquelle l'application est en cours d'exécution.

Toutes les combinaisons `category` et `country` ne retournent pas de données car actuellement nous utilisons des données en brutes, voici des combinaisons qui vont fonctionner avec les données qui nous sont disponibles.

> http://localhost:5173/dashboard/Media/USA

> http://localhost:5173/dashboard/Tech/USA

> http://localhost:5173/dashboard/Tech/AUS

> http://localhost:5173/dashboard/Tech/CAN

## 4. La liste des sources de données utilisées.

- [Crunchbase](https://www.crunchbase.com/)

## 5. La liste des bibliothèques et frameworks utilisés.

- [Numpy](https://numpy.org/)

- [Pandas](https://pandas.pydata.org/)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- [ReactJS](https://reactjs.org/)

- [ChartJS](https://www.chartjs.org/)

## 6. Les endpoints de l'API.

- `GET /api/categories` : Retourne la liste des catégories dans la base de données.

  ```json
  {
    "data": [
      "Curated Web",
      "Human Resources",
      "Marketplaces",
      "Recruiting",
      "Games",
      "Video on Demand",
      "Finance",
      "Software",
      "..."
    ]
  }
  ```

- `GET /api/countries` : Retourne la liste des pays dans la base de données.
- `GET /api/states/<country>` : Retourne la liste des états dans le pays spécifié.
- `GET /api/median/<country>` : Retourne la moyenne des montants de levée de fonds pour les catégories dans le pays spécifié.
- `GET /api/startups` : Retourne toutes les startups dans la base de données.
- `GET /api/startups/<category>/<country>` : Retourne les startups dans la catégorie et le pays spécifiés.
- `GET /api/startups/<category>/<country>/<state>` : Retourne les startups dans la catégorie et le pays spécifiés et dans l'état spécifié.

## 7. Les résultats que vous avez obtenu.

- Affichage d'un diagramme circulaire et d'un tableau à barres pour montrer l'état des startups dans la catégorie `Média` aux `USA`

<img  width="1792"  alt="image"  src="https://user-images.githubusercontent.com/49391108/215619619-6e96563d-d6e0-49a0-892d-f1d30335302b.png">

- Affichage d'un tableau à barres pour montrer les catégories de start-up qui ont recueilli le plus de fonds aux `USA`.

<img  width="1792"  alt="image"  src="https://user-images.githubusercontent.com/49391108/215619653-aacaeb94-0c0b-434d-bf70-26fe2d8de2a2.png">
