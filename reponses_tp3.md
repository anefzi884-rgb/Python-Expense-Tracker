# TP3 — Questions de compréhension

## 1. Quelle est la différence entre `git switch` et `git merge` ?

`git switch` permet de changer de branche et de sélectionner la branche sur laquelle on souhaite travailler. `git merge` permet d'intégrer les modifications d'une branche source dans la branche active.

## 2. Quelle est la différence entre `git merge` et une Pull Request ?

`git merge` est une commande Git qui réalise une fusion. Une Pull Request est une fonctionnalité de GitHub qui permet de proposer une fusion, examiner les modifications, commenter le code et approuver son intégration avant la fusion.

## 3. Que représentent `base` et `compare` ?

`base` est la branche de destination qui reçoit les modifications. `compare` est la branche source qui contient les modifications proposées.

## 4. Pourquoi vérifier le code avant la fusion ?

Pour vérifier que la fonctionnalité demandée est présente, que les anciennes fonctionnalités sont conservées et que les modifications ne provoquent pas de problème dans l'application.

## 5. Pourquoi exécuter `git pull` après une fusion sur GitHub ?

Pour récupérer dans la copie locale les modifications qui ont été fusionnées sur GitHub et synchroniser la branche locale avec la version distante.

## 6. Une PR modifie-t-elle `main` dès sa création ?

Non. La création d'une Pull Request propose une fusion, mais ne modifie pas automatiquement `main`. La fusion doit être effectuée après la vérification et l'approbation.

## 7. Pourquoi la deuxième fusion peut-elle provoquer un conflit ?

Parce que les deux étudiants ont ajouté une option 5 différente dans le même menu au TP2. Les modifications peuvent donc concerner les mêmes lignes du fichier et Git peut avoir besoin d'une résolution manuelle.
