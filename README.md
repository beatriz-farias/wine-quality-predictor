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
  "objective": "reg:squarederror",  
  "num_round": 100,  
  "max_depth": 5,  
  "eta": 0.2  
}
``` 
- **Evaluation:** RMSE, R² score.

### AWS Integration
- **S3:** Data versioning and storage.
- **SageMaker:**
  - Training jobs with spot instances (cost optimization).
  - _Endpoint deployment for REST API inference -- in progress_
  - _Integration with AWS Lambda for serverless workflows. -- in progress_

## 🚀 Deployment
- **Endpoint:** Real-time predictions via HTTP API.
- **Input Example:**
``` json
{  
  "fixed acidity": 7.4,  
  "volatile acidity": 0.7,  
  "citric acid": 0.0,  
  "residual sugar": 1.9,  
  "chlorides": 0.076,  
  "free sulfur dioxide": 11.0,  
  "total sulfur dioxide": 34.0,  
  "density": 0.9978,  
  "pH": 3.51,  
  "sulphates": 0.56,  
  "alcohol": 9.4  
}
```
- **Output:** Predicted quality (e.g., 5.8/10).

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
RMSE	| 0.68
R²	| 0.38

**Interpretation:** The model explains 38% of variance in wine quality, with predictions averaging ±0.68 points from actual scores.

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
#### Install Dependencies -- in progress
```bash
pip install -r requirements.txt
```
