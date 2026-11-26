# Rapport — TP3 : Fusion des branches et Pull Requests

**Application :** Python Expense Tracker  
**Module :** Git et GitHub  
**Étudiant :** Amine Nefzi

## 1. Objectif du TP

L'objectif de ce TP est de réunir les fonctionnalités développées dans des branches indépendantes dans la branche `main`, en utilisant les Pull Requests de GitHub.

## 2. Branches utilisées

- `main` : application initiale et version finale.
- `feature-delete` : fonctionnalité de suppression d'une dépense.
- `feature-average` : fonctionnalité de calcul de la moyenne.

## 3. Fonctionnalités finales

L'application permet de :
- ajouter une dépense ;
- afficher les dépenses ;
- afficher le total ;
- supprimer une dépense à partir de son numéro ;
- calculer la moyenne des dépenses.

## 4. Tests à effectuer

Les tests demandés dans le TP sont les suivants :

| Action | Résultat attendu |
|---|---|
| Ajouter Coffee : 10 | Dépense ajoutée |
| Ajouter Sandwich : 20 | Dépense ajoutée |
| Ajouter Transport : 30 | Dépense ajoutée |
| Afficher les dépenses | 3 dépenses |
| Afficher le total | 60.00 |
| Calculer la moyenne | 20.00 |
| Supprimer la dépense n° 2 | Sandwich supprimé |
| Afficher le total | 40.00 |
| Calculer la moyenne | 20.00 |

Ces opérations doivent être effectuées dans une même exécution, car les dépenses sont conservées uniquement en mémoire.

## 5. Conclusion

Ce TP permet de pratiquer la synchronisation des branches, la création de Pull Requests, la revue du code et la fusion des contributions dans `main`.
