# 🍷 Wine Quality Prediction with AWS SageMaker
*An End-to-End Machine Learning Pipeline for Regression*

## 📌 Overview
This project predicts the quality of red wines (on a scale of 0-10) using chemical properties like acidity, pH, and alcohol content. Built on AWS SageMaker, it demonstrates a complete ML workflow from data preprocessing to model deployment, showcasing industry best practices in MLOps and cloud computing.

**Dataset:** UCI Wine Quality Dataset (1,599 samples, 11 features).

## 🔍 Key Features
- **Regression Model:** XGBoost predicts wine quality with an RMSE of 0.68 (≈ ±0.68 score error).
- **Cloud Pipeline:**
  - **Data Storage:** Raw/training data versioned in AWS S3.
  - **Training:** Managed XGBoost training on SageMaker (```ml.m5.large``` instances).
  - **Deployment:** Real-time predictions via SageMaker endpoints.
- **Scalability:** Automated workflows handle large datasets and retraining.

## 🛠️ Technical Components
### Model Development
- **Preprocessing:** Label-first CSV formatting, train-test splits.
- **Hyperparameters:**
``` python
{  
    "max_depth"=5,
    "eta"=0.2,
    "gamma"=4,
    "min_child_weight"=6,
    "subsample"=0.8,
    "verbosity"=0,
    "objective"="reg:squarederror",
    num_round=500,
}
``` 
- **Evaluation:** RMSE, MAE, R², Explained Variance and MAPE scores.

### AWS Integration
- **S3:** Data versioning and storage.
- **SageMaker:**
  - Training jobs with spot instances (cost optimization).
  - _Endpoint deployment for REST API inference.
  - _Integration with AWS Lambda for serverless workflows.

## 🚀 Deployment
- **Endpoint:** Predictions using the lambda function.
- **Input Example:**
``` json
{
  "body": "7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4",
  "headers": {
    "Content-Type": "text/csv"
  }
}
```
- **Output:** Predicted quality: 5.15.

## 🎯 Challenges & Solutions
1. **Data Formatting:**
- _Issue:_ SageMaker expected LIBSVM format by default.
- _Fix:_ Explicit CSV serialization with label-first ordering.
2. **Endpoint Conflicts:**
- _Issue:_ Duplicate endpoint configurations.
- _Fix:_ Automated cleanup scripts + unique endpoint naming.

## 📈 Results
**Metric** | **Value**
--- | ---
RMSE| 0.591
MAE| 0.469
R²| 0.466
Explained Variance| 0.467
MAPE (%)| 8.419

**Interpretation:** 
- **RMSE (Root Mean Squared Error):** The model's predictions deviate from the true values by ~0.59 units on average
- **MAE (Mean Absolute Error):** Predictions are ~0.47 units away from actual values on average.
- **R² (R-Squared):** The model explains ~46.6% of the variance in the target variable, indicating moderate predictive power.
- **MAPE (Mean Absolute Percentage Error):** Predictions are ~8.4% off from true values on average

## 🌟 Future Enhancements
- **Hyperparameter Tuning:** SageMaker Automatic Model Tuning (AMT).
- **Monitoring:** SageMaker Model Monitor for data drift detection.
- **CI/CD:** AWS CodePipeline for automated retraining.

## 🛠️ Installation & Setup
#### Prerequisites 
- Python 3.8+
- AWS Account with SageMaker/S3 access
- AWS CLI configured with IAM credentials
#### Clone the Repository
```bash
git clone https://github.com/your-profile/wine-quality-prediction.git  
cd wine-quality-prediction
```  
#### Install Dependencies
```bash
pip install -r requirements.txt
```
