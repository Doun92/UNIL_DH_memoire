# UNIL_DH_memoire
Le code mis à disposition a été écrit dans le cadre de mon mémoire de Master en Humanités Numériques à l'Université de Lausanne. Il est un annexe de mon travail écrit et propose une illustration des propos qui y sont amenés.

## Résumé du code informatique
Nous avons écrit un algorithme expert d'intelligence atificielle. Il a pour but intial de repérer des termes issus de dialectes dans un texte écrit en ancien français. Pour ce faire, nous y avons implémenté les règles d'évolution phonétique et nous demandons à  l'algorithme de faire l'évolution de l'étymon latin de chaque terme et d'ensuite comparer sa sortie avec celle du texte. Si les deux sont égales alors le mot est considéré comme faisant partie de la langue normée, le cas contraire, le mot est vu comme faisant partie d'autre chose.

## Comment l'utiliser
### 1ère étape
La première étape consiste à traiter le texte afin qu'il deviennent computationable. Pour ce faire, le texte doit être écrit dans un document en .txt. 
### 2ième étape
Une fois le texte choisi et copié, il doit être dépouillé de signes de ponctuation et des nombres afin de ne laisser que des lettres. Pour que ce soit fait, il suffit de lancer le petit script normaliseur.py
### 3ième étape
Une fois que le texte est dépouillé de tout ce qui n'entre pas dans l'évolution phonétique, il faut le réduire à une seule ligne afin que l'algorithme puisse bien traiter chaque mot. Pour cela, il faut lancer le script one_string.
### 4ième étape
Puis, il faut répartir les mots dans un dictionnaire vide avec create_dict.py
Le dictionnaire devra être rempli "à la main".
### 5ième étape
Une fois toutes ces étapes accomplies, il suffit de lancer main.py pour avoir trois documents textes qui se crééent. Le premier catch.txt recouvre tous les mots identiques, le second dont_catch.txt montre les mots qui diffèrent les uns des autres et, finalement, every_word montre la lsite de tous les mots du texte avec leur étymon et l'évolution selon l'algorithme.

## Pour aller plus loin
Ce code pourrait être optimiser soit en emplyoant de séléments d'apprentissage machine, soit en tentant de prendre en compte plus d'éléments que simplement l'étymon, en prenant en compte certaines évolutions dues à des analogies avec d'autres mots en ancien français ou encore à l'évolution  savante parallèle à l'évolution populaire.
