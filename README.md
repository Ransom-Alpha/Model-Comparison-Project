# **Comparing Traditional Asset Pricing Models with Machine Learning for Equity Valuation**

## **Project Overview**
This project compares traditional financial models, such as the Capital Asset Pricing Model (CAPM) and its extensions, with machine learning (ML) models for equity valuation. The goal is to evaluate their predictive accuracy using identical datasets and variables. Additionally, sectoral segmentation is applied to analyze model robustness and adaptability across different industries. The findings will help determine which approach provides superior predictions and under what conditions each model performs best.

## **Methodology**
The project follows a structured approach, including **data collection, feature engineering, model implementation, and performance evaluation**.

### **Traditional Models**
The following traditional **asset pricing models** are included in the analysis:

- **CAPM (Capital Asset Pricing Model)**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_i (E(R_m) - R_f)
    \]
  - Factors:  
    - \( R_m \) = Market Return  
    - \( R_f \) = Risk-Free Rate  
    - \( \beta_i \) = Beta (Systematic Risk)

- **Black CAPM**
  - Formula:  
    \[
    E(R_i) = \beta_i E(R_m)
    \]
  - Factors:  
    - \( \beta_i \) = Beta (Market Sensitivity)

- **Fama-French Three-Factor Model**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_m (R_m - R_f) + \beta_{SMB} + \beta_{HML}
    \]
  - Factors:  
    - Size Factor (SMB)  
    - Value Factor (HML)

- **Carhart Four-Factor Model**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_m (R_m - R_f) + \beta_{SMB} + \beta_{HML} + \beta_{UMD}
    \]
  - Factors:  
    - Momentum Factor (UMD)

- **Fama-French Five-Factor Model**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_m (R_m - R_f) + \beta_{SMB} + \beta_{HML} + \beta_{RMW} + \beta_{CMA}
    \]
  - Factors:  
    - Investment Factor (CMA)  
    - Profitability Factor (RMW)

- **Pastor-Stambaugh Liquidity Model**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_m (R_m - R_f) + \beta_{SMB} + \beta_{HML} + \beta_{LIQ}
    \]
  - Factors:  
    - Liquidity Factor (LIQ)

- **Q-Factor Model**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_m (R_m - R_f) + \beta_{ME} + \beta_{I} + \beta_{ROE}
    \]
  - Factors:  
    - Return on Equity (ROE)  
    - Investment (I)  
    - Market Equity (ME)

- **Consumption CAPM (CCAPM)**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_C E(\Delta C / C)
    \]
  - Factors:  
    - Consumption Growth (\(\Delta C / C\))

- **Intertemporal CAPM (ICAPM)**
  - Formula:  
    \[
    E(R_i) = R_f + \beta_m (R_m - R_f) + \sum \beta_k Z_k
    \]
  - Factors:  
    - Additional State Variables (\( Z_k \))

- **Stochastic Discount Factor Models (SDF)**
  - Formula:  
    - Various macroeconomic and financial indicators incorporated into a general pricing framework.

### **Machine Learning Models**
The following **ML models** are used for comparison:
- **Ordinary Least Squares (OLS) Regression**
- **Support Vector Regression (SVR)**
- **Random Forest Regression**
- **Gradient Boosting Machines (GBM)**
- **Quantile Regression**
- **Quantile Regression Forests**
- **Neural Networks (NNs)**

Each ML model is trained using the same factors as traditional models to ensure a controlled comparison.

## **Data Sources**
- **WRDS (Wharton Research Data Services)**: Financial data, stock returns, and factor loadings.
- **Additional Market Data**: Macroeconomic indicators, liquidity measures, and industry-specific data.
- **Preprocessing Steps**:
  - Data cleaning, normalization, and factor creation.
  - Transforming data into a time-series structure for modeling.

## **Project Structure**
