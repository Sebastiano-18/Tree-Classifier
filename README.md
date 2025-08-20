## TreeType Classifier
A Machine Learning Project that classifies tree types (Maple, Oak, Pine) based on physical characteristics like heigth, trunk diameter, leaf area, bark roughness using a random forest classifier

----

## Features 
-Preprocessing with Robust Scaler 
-Random Forest model with hyperparameter tuning via 'RandomizedSearchCV'
-Stratified K-fold cross-validation
-Confusion Matrix and classification report visualization
-Save and load models locally (not tracked in Git)

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

> **NOTE** 'data/' and 'models/' folders are ignored in Git, so they need to be create locally before running the project 
