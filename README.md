# GRID INSIGHT

Grid Insight est une application web qui permet de suivre la consommation et la production d'électricité en France, par filière, à partir des données ouvertes de RTE (mises à jour toutes les 15 minutes environ).

Gris Insight is a web application that lets you follow the French electricty consumption and production, by energy source, using RTE open datas (updated every 15 minutes approximately)

[![CI](https://github.com/ThibautRouland44000/grid-insight/actions/workflows/ci.yml/badge.svg)](https://github.com/ThibautRouland44000/grid-insight/actions/workflows/ci.yml)

```mermaid
flowchart LR
    Nav["Navigateur<br/>React :5173"] -->|"fetch : requête HTTP, réponse JSON"| API["API Django REST<br/>:8000"]
    API -->|"ORM : requêtes SQL"| DB[("PostgreSQL<br/>:5432, Docker")]
```