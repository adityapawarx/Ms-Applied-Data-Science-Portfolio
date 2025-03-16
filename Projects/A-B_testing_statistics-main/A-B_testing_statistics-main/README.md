# **A/B Testing for Player Retention in Cookie Cats**

## **Project Overview**  
This project analyzes an **A/B test** conducted in the popular mobile puzzle game **Cookie Cats**, developed by **Tactile Entertainment**. The test was designed to determine the **optimal placement of an in-game gate**, which forces players to either wait or make an in-app purchase to continue playing. The experiment involved **moving the gate from level 30 to level 40** and measuring the impact on **player retention rates** over **1-day and 7-day periods**. Using **Python, Pandas, and statistical analysis techniques**, the project explores **user behavior, retention trends, and engagement metrics** to derive data-driven recommendations for game design improvements.

---

## **Table of Contents**  
1. [Project Background](#project-background)  
2. [Dataset Information](#dataset-information)  
3. [Analysis & Methodology](#analysis--methodology)  
4. [Key Findings](#key-findings)  
5. [Technologies Used](#technologies-used)  
6. [Results & Conclusion](#results--conclusion)  
7. [How to Run](#how-to-run)  
8. [Future Improvements](#future-improvements)  

---

## **Project Background**  
Cookie Cats is a **"connect three"-style puzzle game** where players clear tiles to progress through levels. Periodic in-game **gates** are designed to **control the pace of gameplay and encourage in-app purchases**. The experiment aimed to **test whether moving the first gate from level 30 to level 40 impacts player retention** by evaluating two groups:
- **Control Group (gate_30):** Players encountered the gate at level 30.
- **Test Group (gate_40):** Players encountered the gate at level 40.

The goal was to determine **which placement maximizes player retention** and engagement.

---

## **Dataset Information**  
The dataset contains **90,189 player records**, each assigned to either **gate_30 or gate_40**. The key variables include:
- `userid` → Unique player identifier  
- `version` → Player's assigned group (`gate_30` or `gate_40`)  
- `sum_gamerounds` → Total game rounds played in the first week  
- `retention_1` → Whether the player returned the next day (`True/False`)  
- `retention_7` → Whether the player returned after seven days (`True/False`)  

---

## **Analysis & Methodology**  
The project follows a structured data analysis approach:
1. **Data Cleaning & Exploration** – Checking for missing values, summarizing player activity, and understanding data distributions.  
2. **Behavioral Analysis** – Examining the number of game rounds played, player drop-off rates, and possible outliers.  
3. **Retention Comparison** – Evaluating **1-day and 7-day retention rates** across both groups.  
4. **Statistical Significance Testing** – Using **bootstrapping** to measure confidence levels in observed retention differences.  
5. **Data Visualization** – Generating **box plots, density plots, and retention comparison charts** to interpret results.  

---

## **Key Findings**  
- **1-day retention:** Players in the **gate_30 group (44.8%)** were slightly more likely to return than those in the **gate_40 group (44.2%)**.  
- **7-day retention:** The difference was more pronounced, with **gate_30 (19.0%)** retaining more players than **gate_40 (18.2%)**.  
- **Statistical confidence:** Bootstrapping confirmed a **96.8% probability** that 1-day retention was higher for **gate_30** and a **99.8% probability** that 7-day retention was also higher.  

---

## **Technologies Used**  
- **Python** (Pandas, NumPy) for data analysis  
- **Matplotlib & Seaborn** for data visualization  
- **Statistical methods** (Bootstrapping, A/B testing techniques)  
- **Jupyter Notebook** for interactive analysis  

---

## **Results & Conclusion**  
The findings indicate that **keeping the gate at level 30 improves both short-term and long-term retention**. This aligns with the **theory of hedonic adaptation**, where periodic forced breaks maintain player engagement. The recommendation for game developers is to **maintain the gate at level 30 rather than moving it to level 40**, as doing so may lead to **higher drop-off rates and lower overall retention**.

---

## **How to Run**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/AB-Testing-Cookie-Cats.git
   cd AB-Testing-Cookie-Cats
