# 🌳 TreeType Classifier
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)](https://scikit-learn.org/stable/)  
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

## 📌 Project Overview
This repository contains an **end-to-end Machine Learning project** that predicts the type of tree (Maple, Oak, Pine) based on physical characteristics.  

The workflow includes:
- Data loading & preprocessing with `pandas` and `RobustScaler`.
- Training a **Random Forest Classifier** inside a `Pipeline`.
- **Hyperparameter tuning** using `RandomizedSearchCV` with stratified K-Fold CV.
- **Evaluation** with accuracy, precision, recall, F1-score, and confusion matrix.
- **Model saving** for reproducibility.
- Full documentation and environment setup.

 ----
## Project Structure
TreeType_Classfier/
├──.venv # PYTHON VIRTUAL ENVIROMENT
├──data/# LOCAL FOLDER FOR DATASET (IGNORED IN GIT)
 └──TREES.CSV
├──models/# LOCAL FOLDER FOR TRAINED MODELS (IGNORED IN GIT)
  └──RANDOM_FOREST_TRAINED_MODEL.pkl
├──src/
    └──TreeClassifier.py # Main ML Code
├──.gitignore # Files/Folders IGNORED BY GIT
├──README.md # Project Documentation
├──requirements.txt# Python Dependencies
├──LICENSE# LICENSE FILE

> **NOTE** 'data/' and 'models/' folders are ignored in Git, so they need to be created locally before running the project
----

## INSTALLATION
1. Clone the Repository
```bash
git clone https://github.com/Sebastiano-18/Tree-Classifier.git
cd Tree-Classifier
2 CREATE VIRTUAL ENVIROMENT
# for Windows OSes
python -m venv .venv
.venv\Scripts\activate
# for macOS/Linux
python -m venv .venv
source .venv/bin/activate
3 Install Dependencies
pip install -r requirements.txt
# USAGE
python src/TreeClassifier.py
```
## RESULTS
The Random Forest Classifier achieved around 92% of accuracy.
See `results.md` for detailed classification report and confusion matrix 
