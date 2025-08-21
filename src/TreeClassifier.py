from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_predict, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt 
import pandas as pd
import joblib, os

def load_data(path="data/trees.csv"):
    """
    Load dataset and separate features and target.
    """
    df = pd.read_csv(path)
    X = df.drop("TreeType", axis=1)
    y = df["TreeType"]
    return X, y


def get_param_grid():
    """
    Return a parameter grid for RandomizedSearchCV.
    """
    return {
        'classifier__n_estimators': [100, 200, 500],
        'classifier__max_depth': [None, 10, 20, 30],
        'classifier__min_samples_split': [2, 5, 10],
        'classifier__min_samples_leaf': [1, 2, 4],
        'classifier__max_features': ['sqrt', 'log2', None],
        'classifier__bootstrap': [True, False]
    }

def create_pipeline():
    """
    Create a machine learning pipeline with preprocessing and a classifier.
    """
    pipe = Pipeline([
        ('scaler', RobustScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    return pipe

def train_model(X, y, pipe, param_grid, n_iter=30, cv_splits=5):
    """
    Train Random Forest with RandomizedSearchCV and StratifiedKFold.
    """
    skf = StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=42)
    rd = RandomizedSearchCV(pipe, param_grid, cv=skf, scoring='accuracy',
                            verbose=1, n_iter=n_iter, random_state=42)
    rd.fit(X, y)
    return rd, skf


def evaluate_model(model, X, y, skf):
    """
    Evaluate the model using cross_val_predict, print classification report,
    and plot confusion matrix.
    """
    y_pred = cross_val_predict(model, X, y, cv=skf)
    print("CLASSIFICATION REPORT:\n", classification_report(y, y_pred))

    return y_pred

def plot_confusion_matrix(y, y_pred, save_path="results/confusion_matrix.png"):
    labels = ['Maple', 'Oak', 'Pine']
    cm = confusion_matrix(y, y_pred)
    disp = ConfusionMatrixDisplay(cm, display_labels=labels)
    disp.plot(cmap='Blues')
    plt.title("Confusion Matrix of the Classifier")
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()
    print(f"Confusion matrix saved to {save_path}")
    return cm



def save_model(model, folder="models",filename="random_forest_model.pkl"):
    """
    Save the trained model
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, filename)
    joblib.dump(model, filepath)
    print(f"Model saved as {filepath}")


def main():
    X, y = load_data()
    pipe = create_pipeline()
    param_grd = get_param_grid()
    rd, skf = train_model(X, y, pipe, param_grd)

    print("THE BEST PARAMS ARE:\n", rd.best_params_)
    print("THE BEST SCORE IS:\n", round(rd.best_score_, 2))

    best_model = rd.best_estimator_
    y_pred = evaluate_model(best_model, X, y , skf)
    plot_confusion_matrix(y, y_pred)

    save_model(best_model)

if __name__ == "__main__":
    main()