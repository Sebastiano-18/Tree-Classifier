## TreeType Classifier
A Machine Learning Project that classifies tree types (Maple, Oak, Pine) based on physical characteristics like heigth, trunk diameter, leaf area, bark roughness using a random forest classifier

----

## TABLE OF CONTENTS
- [Project Structure](#project-structure)
- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Requirements](#requirements)
- [License](#License)
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

## Features
-Train and Evaluate a Random Forest Classifier for tree type prediction
-Hyperparameter tuning using 'RandomizedSearchCV'.
-Confusion Matrix and classification report for performance visualization
-Save trained model for reuse 


## INSTALLATION
1. Clone the Repository
```bash
git clone https://github.com/Sebastiano-18/Tree-Classifier.git
cd Tree-Classifier
2 CREATE VIRTUAL ENVIROMENT
# for Windows OSes
python -m venv .venv
.venv\Scripts\activate
