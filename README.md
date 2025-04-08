# AI-Driven Fraud Detection in Financial Transactions using Azure OpenAI

## Introduction

In an era of rapidly growing digital financial systems, fraud has become a sophisticated and persistent threat — costing institutions billions annually. Traditional rule-based systems often fall short due to their inability to adapt to evolving fraud tactics and complex behavioral patterns.

To address this challenge, our project leverages **Microsoft Fabric’s modern data architecture**, the **powerful language reasoning capabilities of Azure OpenAI's GPT-4 model**, and **interactive data visualization with Power BI** to create a smart, explainable fraud detection system.

Using a public transaction dataset from **Kaggle** as a proxy for real financial data, we simulate a production-grade fraud detection pipeline. The architecture is built on the **Lakehouse Medallion model (Bronze → Silver → Gold)** for organized data processing, feature engineering, and AI insights. The **GPT-4 model** (accessed through Azure OpenAI) analyzes each transaction and provides two outputs:
- A concise, human-like explanation of whether the transaction seems fraudulent or not.
- A **fraud risk score** (`Low`, `Medium`, or `High`) to flag suspicious records.

This AI-enhanced approach doesn't just detect fraud — it **communicates the rationale**, empowering analysts to understand *why* a transaction may be risky.

The final fraud intelligence is surfaced through **Power BI dashboards**, offering visual summaries, risk distribution, and GPT-generated fraud insights in a business-friendly format.

---

## Problem Statement

As digital banking and online payments expand, fraudsters continue to develop more complex, real-time attack strategies. Existing fraud detection methods — often built on rigid rules or traditional supervised models — struggle to detect novel fraud patterns or adapt to changing behavior.

This project responds to this problem by introducing a **generative AI-based fraud detection model** that:
- Thinks like a human fraud analyst.
- Understands the context behind each transaction.
- Flags anomalies based on behavioral reasoning — not just mathematical thresholds.

By combining **Microsoft Fabric** for structured data processing and **GPT-4** for intelligent transaction analysis, we aim to build a flexible, scalable system capable of detecting both known and unknown fraud behaviors.

---

## Objectives

### 3.1 Main Objective  
To develop an AI-powered fraud detection system that can intelligently evaluate financial transactions, assign risk levels, and provide human-readable fraud justifications — using Azure OpenAI and Microsoft Fabric.

### Specific Objectives

- Ingest and process transactional data using the Lakehouse architecture (Bronze → Silver → Gold).
- Analyze financial transactions to extract behavioral and contextual patterns.
- Leverage **Azure OpenAI GPT-4** to classify transactions by risk level and generate fraud analysis summaries.
- Visualize flagged transactions and fraud trends using Power BI.
- Showcase explainable AI as a tool to support fraud analysts in real-world decision-making.

---

## Data Methods

- **Data Analysis**: Process and clean financial transaction data using **Microsoft Fabric’s Lakehouse architecture**.
- **Fraud Detection**: Use **Azure OpenAI GPT-4** to assess transactions, identifying potential fraud and generating risk summaries.
- **Fraud Visualization**: Develop an interactive **Power BI** dashboard to display fraud risk insights.
- **Scalable System**: Build a solution that can detect fraud efficiently as data grows.

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
