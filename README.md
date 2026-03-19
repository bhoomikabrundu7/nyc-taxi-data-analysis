#  NYC Taxi Data Pipeline (Jan 2024)

### Project Overview
A Python-based data pipeline designed to process and analyze NYC Yellow Taxi trip data. This project automates data ingestion, cleaning, and statistical visualization.

### Methodology
* **Ingestion:** Loading `.parquet` files via `TaxiPipeline` class.
* **Cleaning:** Handling null values in `passenger_count` and filtering `fare_amount` outliers.
* **Analysis:** Exploratory Data Analysis (EDA) using Seaborn and Matplotlib.
* **Geospatial:** Mapping pickup density using Folium HeatMaps.

### Key Findings
* Most trips are short-haul (under 5 miles).
* Peak demand occurs during evening rush hours.
* Pricing shows a strong linear correlation with distance.