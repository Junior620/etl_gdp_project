# 🌍 ETL Project: Countries by GDP (FMI)

## 📘 Description

Ce projet consiste à construire un pipeline **ETL** (Extract - Transform - Load) automatisé qui extrait la liste des pays classés par leur **PIB (Produit Intérieur Brut)**, telle que publiée par le **Fonds Monétaire International (FMI)**.

L'objectif est de permettre à une entreprise d'accéder en continu à ces données pour orienter ses décisions d'expansion à l'international.

---

## 🎯 Objectifs

- Extraire les données à partir d’une page web contenant le **PIB par pays**.
- Transformer les données (nettoyage, arrondi à 2 décimales).
- Charger dans :
  - un fichier JSON : `Countries_by_GDP.json`
  - une base SQLite : `World_Economies.db`, table `Countries_by_GDP`
- Filtrer les pays dont le PIB > 100 milliards USD.
- Journaliser les étapes dans `etl_project_log.txt`

---

## 🧱 Structure du projet

```
etl_gdp_project/
├── etl_project_gdp.py
├── Countries_by_GDP.json
├── World_Economies.db
├── etl_project_log.txt
├── README.md
```

---

## 🛠️ Technologies utilisées

- Python 3.10+
- pandas
- requests
- beautifulsoup4
- sqlite3
- json
- logging

---

## ▶️ Instructions

```bash
pip install pandas requests beautifulsoup4
python etl_project_gdp.py
```

---

## 📊 Requête SQL utilisée

```sql
SELECT * FROM Countries_by_GDP WHERE GDP_USD_billion > 100;
```

---

## 📈 Exemple de données

```json
[
  { "Country": "United States", "GDP_USD_billion": 26700.00 },
  { "Country": "China", "GDP_USD_billion": 17900.00 }
]
```

---

## 🗒️ Journalisation

Toutes les étapes sont enregistrées dans `etl_project_log.txt`.

---

## ✅ Résultat

Un fichier JSON, une base SQLite, et une table filtrée des pays avec un PIB > 100 milliards.
