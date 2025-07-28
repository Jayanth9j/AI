1. ## Data Science
Data Science is the process of extracting knowledge and insights from structured, semi-structured, and unstructured data using scientific methods, algorithms, processes, and systems.

## Why Interdisciplinary?
It combines multiple domains:
Mathematics & Statistics → for patterns and predictions
Computer Science → for coding, algorithms, databases
Domain Knowledge (Healthcare) → to interpret results correctly
Business Understanding → to solve relevant problems

Example (Hospital Dataset):
Using patient data (age, BMI, cholesterol, medication count, diagnosis), predict:
Length of hospital stay,Risk of readmission,Probability of home discharge.

## Why RDBMS is not directly suited for Data Science?
RDBMS (like MySQL, PostgreSQL): Stores structured data with a fixed schema.
Fails when: Data comes from different sources, Relational DBs assume one rigid schema—great for transactions, brittle for analytics with multisource data (IoT JSON, doctor notes, CRM tables).
Schemas are inconsistent (column names/types vary).

Data scientists work across structured, semi-structured (JSON, XML), and unstructured (text, images) data.

Analytics needs “schema-on-read” flexibility; that’s why data lakes/lake-houses or hybrid warehouses are favored for data-science pipelines.

Hospital Example:
CRM Data: Appointment logs, billing records (structured).
IoT Data: Heart rate sensors, oxygen monitors (semi-structured or time-series).
Doctor's Notes: Free text (unstructured).
You can't directly combine them in RDBMS; you need feature extraction & transformation.

2. ## Types of Data Format-
Structured Data: Tabular data with a fixed schema (e.g., CSV, Excel, relational databases)
Semi-structured Data: Data with some structure, but not all data is in a fixed format.
Unstructured Data: Data without a predefined structure (e.g., text, images, audio, video).

| Type                | Essence                      | Typical Tooling                   |
| ------------------- | ---------------------------- | --------------------------------- |
| **Structured**      | Rows & columns               | SQL, Pandas                       |
| **Semi-Structured** | Nested key–value (JSON, XML) | Spark, NoSQL, `pd.json_normalize` |
| **Unstructured**    | Free text, images, audio     | NLP, CV, embeddings               |

3. ## Data Wrangling -
Data Wrangling is the process of transforming data from its raw form into a format that is suitable for 
analysis. It involves cleaning, transforming, and preparing the data for use in data science tasks.

| Task     | **Data Cleaning**                                              | **Data Wrangling**                                            |
| -------- | -------------------------------------------------------------- | ------------------------------------------------------------- |
| Purpose  | Fix errors                                                     | Reshape data                                                  |
| Includes | Handling missing values, correcting typos, removing duplicates | Merging datasets, transforming formats, pivoting, aggregating |
| Example  | Fill NaNs in `bmi`                                             | Combine CRM + IoT data into one DataFrame                     |

4. ## Steps in Data Science -

| **Step**                   | **Description**             | **Example**                                        |
| -------------------------- | --------------------------- | -------------------------------------------------- |
| **1. Data Collection**     | Scraping, APIs, databases   | API for patient vitals, scrape public health data  |
| **2. Data Wrangling**      | Merge, reshape, clean       | Combine CRM + IoT + billing data                   |
| **3. Feature Engineering** | Select meaningful variables | Create `Senior_LongStay` = age>65 & LOS>5          |
| **4. Model Selection**     | Choose ML models            | Logistic Regression for readmission prediction     |
| **5. Model Evaluation**    | Metrics                     | Accuracy, Precision, Recall                        |
| **6. Deployment**          | API, dashboards             | Build app to predict patient discharge probability |
| **7. Interpretation**      | Understand output           | Age and BMI influence length of stay               |

5. ## Data Extraction (Ingestion) - 
Data ingestion is the process of collecting data from various sources and bringing it into a centralized location for analysis.

APIs – governed, versioned; best when offered.
Scraping – last resort when no API.
DB Connectors – classic SQL dumps.
Streaming (Kafka, MQTT) – for high-frequency events.
Reasoning: Choose the least brittle method that meets latency, completeness, and compliance needs.