# **Media Spend Cost Optimization | Marketing Mix Modeling (MMM)**  

## **Team Members**  
- **Aditya Sanjay Pawar**: [GitHub](https://github.com/aspawarsyredu)  
- **Himanshu Hegde**: [GitHub](https://github.com/himanshu-hegde-syr) (Point of Contact)  
- **Keerthi Krishna Aiyappan**: [GitHub](https://github.com/KeerthiKrishna-Aiyappan)  
- **Sri Venkata Subhramanya Abhishek Namana**: [GitHub](https://github.com/snamana)  

---

## **Project Overview**  
This project focuses on optimizing **media spend costs** by analyzing the effectiveness of various marketing channels using **Marketing Mix Modeling (MMM)**. The objective is to measure the impact of media investments across channels such as **TV, social media, digital ads, and traditional advertising** to optimize budget allocation for **maximum sales and revenue generation**. We leverage **Bayesian models and SHAP (Shapley Additive Explanations)** to determine the **marginal contribution** of each channel and understand factors like **diminishing returns, ad-stock effect, and cost savings** from optimized spending strategies.

### **Key Goals**  
1. **Assess Media Channel Effectiveness** – Quantify the impact of each media channel on sales.  
2. **Evaluate Ad-Stock Effects** – Analyze the lag between ad spend and consumer response.  
3. **Measure Diminishing Returns** – Identify saturation points where additional spending does not yield proportional returns.  
4. **Optimize Budget Allocation** – Create an optimized **media spending strategy** based on data-driven insights.  

---

## **Why This Project Matters?**  
Companies invest **millions in media marketing**, and understanding **where and how to allocate these funds efficiently** can lead to **higher ROI and reduced wastage**. Traditional MMM models rely on **Generalized Linear Models (GLM) and Bayesian statistics**, but we explore the use of **Shapley values** for a more nuanced, game-theoretic approach to **media spend contribution analysis**.

---

## **Dataset**  
The dataset used in this study consists of **4 years of weekly data** on marketing spend for a **shampoo advertiser** provided by **Neustar MarketShare**. It includes:  
- **Sales Volume Data** – Weekly product sales in ounces.  
- **Media Spend Data** – Budgets for **TV, newspapers, social media, YouTube, search ads, and digital ads**.  
- **Control Variables** – Includes **discounts, economic factors, seasonality, and competitor pricing**.  

### **Categories of Data Variables**  
| **Category**          | **Variables Included** |
|----------------------|----------------------|
| **Media Variables**  | TV, digital ads, social media, search ads, newspaper, etc. |
| **Control Variables** | Macroeconomic indicators, retail holidays, discounts. |
| **Target Variable**  | Weekly product sales in dollars. |

---

## **Methodology & Approach**  

### **1. Data Preprocessing & EDA**  
- Handle missing values and outliers.  
- Normalize and standardize variables.  
- Perform correlation analysis between **sales and media spend**.  

### **2. Model Selection & Analysis**  
#### **Bayesian Marketing Mix Model (MMM)**  
- Implements **Bayesian Structural Time Series (BSTS)** for robust marketing mix analysis.  
- Captures **prior knowledge about seasonality, competitor pricing, and ad-stock effects**.  

#### **SHAP-Based Model (Shapley Additive Explanations)**  
- Uses **game-theoretic methods** to quantify the marginal contribution of each media channel.  
- Provides **individual-level and aggregated feature impact analysis**.  

### **3. Optimizing Budget Allocation**  
- Perform simulations to **maximize Return on Ad Spend (ROAS)**.  
- Identify budget reallocation strategies that **increase sales while reducing costs**.  
- Use **SciPy Optimization** to create optimal spend recommendations.

---

## **Key Findings & Insights**  

📌 **Marketing Spend Effectiveness**  
- **TV ads contributed 20% to sales revenue**, while **social media contributed 10%**.  
- **Diminishing returns** were observed for **social media spending above $10,000**, with no further increase in sales.  
- **Optimizing media allocation** resulted in **4% higher sales while reducing total spend by 10%**.  

📌 **Ad-Stock & Lag Effect**  
- **TV ads take ~2 weeks to influence sales**, while **newspaper ads take ~1 week**.  
- **Sales response to digital ads was immediate**, making them a strong short-term driver.  

📌 **Budget Optimization Outcomes**  
- **Reallocating budget to high-impact channels (TV, digital ads, SEM)** led to **higher sales efficiency**.  
- **Newspaper & radio ad spend was reduced** due to **lower marginal contribution to revenue**.  

---

## **Technologies Used**  
🛠 **Python Stack:**  
- **Pandas, NumPy** – Data cleaning and transformation.  
- **Matplotlib, Seaborn** – Data visualization.  
- **LightweightMMM, Py-McMarketing** – Bayesian MMM modeling.  
- **SHAP (Shapley Values)** – Feature impact analysis.  
- **Scikit-learn, XGBoost** – Model training and evaluation.  
- **SciPy Optimization** – Budget reallocation and ROAS maximization.  

📊 **Business Intelligence Tools:**  
- **Tableau, Power BI** – Sales & marketing performance visualization.  

---

## **How to Run the Project**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/Media-Spend-Optimization.git
cd Media-Spend-Optimization
