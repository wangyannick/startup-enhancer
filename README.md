# Startup-Enhancer

### Membre du groupe :

ABENAQUI Adrien, AKYOL Olivier, WANG Yannick, ES-KOUSRI Ali, GAMBERT Lucas

## 1. La problématique que vous souhaitez traiter.

- Comment augmenter ses chances lors de la création d'une entreprise ?
- Quels sont les meilleurs paramètres à prendre en compte pour que son entreprise réussisse ?
- Comment mettre les probabilités de notre côté pour créer une entreprise pérenne ?

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

Lors du lancement des applications avec docker-compose, les différents composants sont assignés à des ports spécifiques pour leur accès. Le container PostgreSQL est accessible sur le port `5432`, le serveur Flask sur le port `3333` et le tableau de bord sur le port `5173`. Tous ces ports sont accessibles sur localhost, ce qui signifie qu'ils peuvent être atteints en utilisant l'adresse IP locale de la machine sur laquelle l'application est en cours d'exécution.

## 4. Les résultats que vous avez obtenu.
