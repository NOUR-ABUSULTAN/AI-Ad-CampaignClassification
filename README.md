# AI Project: Ad Campaign Conversion Prediction
## Applied Machine Learning for Mobile and Intelligent Systems

### Project Overview
This project focuses on predicting whether a user will convert into a customer based on advertising campaign data. The project applies Machine Learning classification algorithms and compares their performance to identify the most suitable model for Mobile Computing applications.
The objective is to build an efficient prediction model that can run with minimal computational resources while maintaining high accuracy.

### Project Information
* **Course:** Artificial Intelligence
* **Specialization:** Mobile Computing
* **Project Type:** Tabular Classification
* **Programming Language:** Python 3.12
* **Development Environment:** Google Colab
* **Machine Learning Library:** Scikit-learn

---

### Dataset Description
The dataset contains real historical information related to digital advertising campaign performance, obtained from Kaggle and programmatically extracted within the session.

#### Target Variable
* `conversions` (Binary indicator: 1 if the user converted/purchased, 0 otherwise)

#### Features Used
* `age` - User age demographics.
* `gender` - User gender.
* `impressions` - The number of times an ad was displayed to the user.
* `clicks` - The actual number of clicks on the ad link.

> **Mobile Design Choice:** These features were strictly selected because they provide high predictive utility while completely isolating heavy or unnecessary database columns, making the final model lightweight for mobile application deployment.

---

### Project Pipeline & Methodology
1. **Data Collection:** The dataset is fetched from Kaggle and extracted from the compressed file `archive(1).zip` directly into the environment path to retrieve `ad_campaign_data.csv`.
2. **Data Preprocessing & Feature Selection:** High-dimensional and identifier columns (IDs, Dates) were removed to drastically reduce memory usage during execution on constrained edge devices.
3. **Train-Test Split:** The dataset was partitioned into an 80% training block for optimization and a 20% testing block for independent validation.
   * `test_size = 0.2`
   * `random_state = 42` (Ensuring experimental reproducibility)
4. **Model Training:** Three foundational classifiers were trained:
   * **Linear Support Vector Machine (Linear SVM)**
   * **Decision Tree Classifier**
   * **Random Forest Ensemble**

---

### Experimental Results & Model Comparison

| Algorithm Implemented | Classification Accuracy | Mobile System Suitability |
| :--- | :---: | :--- |
| **Support Vector Machine (Linear SVM)** | **100.00% (1.0)** | **Highly Recommended (Optimal)** |
| **Random Forest Classifier** | **99.84% (0.9984)** | Excessive Memory & Tree Footprint |
| **Decision Tree Classifier** | **99.74% (0.9974)** | Low Stability in Constraint Nodes |

#### Definitive Best Model Justification
The Linear SVM model achieved the highest absolute accuracy of **100%**. 
From a Mobile Computing perspective, this perfectly matches our design criteria:
* **Mathematical Simplicity:** After training, the SVM reduces to a single, lightweight linear decision equation rather than holding heavy hierarchical structures in memory.
*
