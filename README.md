# AI-Driven Fraud Detection in Financial Transactions using Microsoft Fabric and Microsoft Azure OpenAI

![Fraud Detection](https://rtslabs.com/wp-content/uploads/2024/04/fraud-detection1.jpeg)

## Introduction
![Fraud Detection GIF](https://i.pinimg.com/originals/06/d4/59/06d459148136cb42ae10c78c2dca9ebe.gif)

Video demo - https://drive.google.com/drive/folders/1Pyj3NvFOziMivPQ-oszDg78iF8R_kF_-?usp=drive_link

In an era of rapidly growing digital financial systems, fraud has become a sophisticated and persistent threat — costing institutions billions annually. Traditional rule-based systems often fall short due to their inability to adapt to evolving fraud tactics and complex behavioral patterns.

To address this challenge, our project leverages **Microsoft Fabric’s modern data architecture**, the **powerful language reasoning capabilities of Azure OpenAI's GPT-4 model**, and **interactive data visualization with Power BI** to create a smart, explainable fraud detection system.

Notebooks:
1. Fraud_detection (Bronze-Silver layer) - https://github.com/simonMakumi/Fraud_Detection_System/blob/main/Notebooks/Fraud_detection%20(Bronze%20-%20silver%20layer)%20(1).ipynb
2. EDA (silver layer) - https://github.com/simonMakumi/Fraud_Detection_System/blob/main/Notebooks/EDA%20(Silver%20Layer)%20(1).ipynb
3. Statistical Analysis (Silver) - https://github.com/simonMakumi/Fraud_Detection_System/blob/main/Notebooks/Statistical%20Analysis%20(Silver)%20(1)%20(1).ipynb
4. Fraud_detection_Azure_OpenAI - https://github.com/simonMakumi/Fraud_Detection_System/blob/main/Notebooks/Fraud_detection_AzureOpenAI.ipynb
5. Gold - https://github.com/simonMakumi/Fraud_Detection_System/blob/main/Notebooks/Gold.ipynb
6. PowerBI Dashboard - https://github.com/simonMakumi/Fraud_Detection_System/blob/main/Fraud_detection_Dashboard.pbix

Using a public transaction dataset from **Kaggle** as a proxy for real financial data, we simulate a production-grade fraud detection pipeline. The architecture is built on the **Lakehouse Medallion model (Bronze → Silver → Gold)** for organized data processing, feature engineering, and AI insights. The **GPT-4 model** (accessed through Azure OpenAI) analyzes each transaction and provides two outputs:
- A concise, human-like explanation of whether the transaction seems fraudulent or not.
- A **fraud risk score** (`Low`, `Medium`, or `High`) to flag suspicious records.

This AI-enhanced approach doesn't just detect fraud — it **communicates the rationale**, empowering analysts to understand *why* a transaction may be risky.

The final fraud intelligence is surfaced through **Power BI dashboards**, offering visual summaries, risk distribution, and GPT-generated fraud insights in a business-friendly format.

---

## Problem Statement

![Preventing Credit Card Fraud](https://www.wexinc.com/wp-content/uploads/2017/10/Preventing-credit-card-fraud-on-the-road.png)

As digital banking and online payments expand, fraudsters continue to develop more complex, real-time attack strategies. Existing fraud detection methods — often built on rigid rules or traditional supervised models — struggle to detect novel fraud patterns or adapt to changing behavior.

This project responds to this problem by introducing a **generative AI-based fraud detection model** that:
- Thinks like a human fraud analyst.
- Understands the context behind each transaction.
- Flags anomalies based on behavioral reasoning — not just mathematical thresholds.

<img width="796" alt="Screenshot 2025-04-10 at 20 38 33" src="https://github.com/user-attachments/assets/3de86b3e-dddd-4c9a-8b9c-b76cd64eabef" />

<img width="739" alt="Screenshot 2025-04-10 at 20 35 06" src="https://github.com/user-attachments/assets/86514a10-d7bd-47e7-a7d0-ab52c677b6de" />

<img width="737" alt="Screenshot 2025-04-10 at 20 47 00" src="https://github.com/user-attachments/assets/b36a6c6d-558e-45cc-96e6-ad569b2c0bb0" />

<img width="734" alt="Screenshot 2025-04-10 at 20 47 11" src="https://github.com/user-attachments/assets/826b97eb-17d3-4fee-813e-544fbd10800a" />

By combining **Microsoft Fabric** for structured data processing and **GPT-4** for intelligent transaction analysis, we aim to build a flexible, scalable system capable of detecting both known and unknown fraud behaviors.

---

## Objectives

![Microsoft Fabric GenAI](https://robkerr.ai/content/images/2024/01/fabric_doc_genai.png)

### 3.1 Main Objective  
To develop an AI-powered fraud detection system that can intelligently evaluate financial transactions, assign risk levels, and provide human-readable fraud justifications — using Azure OpenAI and Microsoft Fabric.

<img width="1434" alt="Screenshot 2025-04-09 at 05 23 58" src="https://github.com/user-attachments/assets/ae4e0797-a287-4dea-a6ae-3174a803745f" />

<img width="1424" alt="Screenshot 2025-04-10 at 17 19 39" src="https://github.com/user-attachments/assets/c794332c-71e1-4a06-b9dd-380478ad5596" />

### Specific Objectives

- Ingest and process transactional data using the Lakehouse architecture (Bronze → Silver → Gold).
- Analyze financial transactions to extract behavioral and contextual patterns.
- Leverage **Azure OpenAI GPT-4** to classify transactions by risk level and generate fraud analysis summaries.
- Visualize flagged transactions and fraud trends using Power BI.
- Showcase explainable AI as a tool to support fraud analysts in real-world decision-making.

---

## Data Methods

![Microsoft Fabric](https://lytix.be/wp-content/uploads/2024/09/Microsoft-Fabric-visual.png)

- **Data Analysis**: Process and clean financial transaction data using **Microsoft Fabric’s Lakehouse architecture**.
- **Fraud Detection**: Use **Azure OpenAI GPT-4** to assess transactions, identifying potential fraud and generating risk summaries.
- **Fraud Visualization**: Develop an interactive **Power BI** dashboard to display fraud risk insights.
- **Scalable System**: Build a solution that can detect fraud efficiently as data grows.
  
<img width="1228" alt="Screenshot 2025-04-09 at 05 41 46" src="https://github.com/user-attachments/assets/01d23d37-0b66-4a3d-80dc-eb39d5db7f31" />

---

## Key Achievements

- Created a robust **AI-driven fraud detection system** using **Azure OpenAI** and **Microsoft Fabric**.
- Analyzed financial transaction data, generating fraud risk insights with **GPT-4**.
- Developed an interactive **Power BI dashboard** to visualize fraud patterns and risk levels.
- Showcased this innovative solution at the **Microsoft Fabric Data + AI Kenya Hackathon**, with **real-world applications** in financial institutions.

---

## Experimental Design

- **Data Collection**: Utilized transaction data with features like **TransactionID**, **TransactionAmount**, **TransactionType**, etc.
- **Data Preprocessing**: Cleaned and transformed the data, handling missing values and outliers.
- **Modeling**: Used **GPT-4** to analyze each transaction, producing a fraud risk level and summary.
- **Deployment**: Integrated the fraud detection model with **Microsoft Fabric** and **Power BI** for real-time analysis.

---

## Technologies Used

![Azure Blog Post](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/08/8.2-social-image.png)

- **Azure OpenAI GPT-4**: For natural language understanding and fraud risk analysis.
- **Microsoft Fabric**: For handling the data pipeline using the **Lakehouse architecture**.
- **Power BI**: For creating a user-friendly dashboard to visualize fraud insights.
- **Python**: For data preprocessing, model integration, and fraud detection workflows.

---

## Data Understanding

The dataset consists of transaction records with key features:

| Feature           | Description                              |
|-------------------|------------------------------------------|
| **TransactionID**  | Unique identifier for each transaction   |
| **AccountID**      | Unique account identifier                |
| **TransactionAmount** | Amount of the transaction               |
| **Location**       | Geographic location of the transaction   |
| **TransactionType**| Credit or Debit                         |
| **DeviceID**       | Identifier for the device used          |
| **IP Address**     | IP address linked to the transaction    |
| **MerchantID**     | Identifier for the merchant             |
| **TransactionDuration** | Time taken for the transaction      |

---

## Hackathon Achievements

- Successfully implemented an **AI-driven fraud detection system** using **Azure OpenAI** for fraud analysis and **Microsoft Fabric** for scalable data processing.
- Demonstrated how **AI models** can provide detailed **fraud risk assessments** for transactions without requiring labeled fraud data.
- Created an interactive **Power BI dashboard** for presenting fraud trends, risk distributions, and GPT-generated insights.
- Participated in the **Microsoft Fabric Data + AI Kenya Hackathon**, applying data science techniques to real-world challenges and advancing fraud detection capabilities with modern AI technologies.

---
