from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB               # yeni eklendi yeni ML algoritmamız.
from sklearn.ensemble import GradientBoostingClassifier  # yeni eklendi yeni ML algoritmamız.

# Algoritmaları tanımlayalım
classifiers = {
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(),
    'KNN': KNeighborsClassifier(),
    # Ekstra algoritmayı ekleyin
    'Gradient Boosting': GradientBoostingClassifier(),
    'Naive Bayes': GaussianNB()
}

# Doğruluk skorlarını saklamak için boş bir sözlük oluşturalım
accuracy_scores = {classifier: [] for classifier in classifiers}

# Her bir veri seti üzerinde algoritmaları uygulayalım
for dataset_name, dataset in selected_datasets.items():
    X, y = dataset.data, dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Kategorik değişkenleri sayısal değerlere dönüştürme
    X_train = pd.get_dummies(pd.DataFrame(X_train))
    X_test = pd.get_dummies(pd.DataFrame(X_test))

    for classifier_name, classifier in classifiers.items():
        classifier.fit(X_train, y_train)  # Algoritmayı eğit
        y_pred = classifier.predict(X_test)  # Test veri seti üzerinde tahmin yap
        accuracy = accuracy_score(y_test, y_pred)  # Doğruluk skorunu hesapla

        # Doğruluk skorlarını sakla
        accuracy_scores[classifier_name].append(accuracy)

# Doğruluk skorlarının ortalamasını ve standart sapmasını hesaplayalım
accuracy_means = {classifier: np.mean(scores) for classifier, scores in accuracy_scores.items()}
accuracy_stds = {classifier: np.std(scores) for classifier, scores in accuracy_scores.items()}

# Elde edilen sonuçları yazdıralım
for classifier, mean_accuracy in accuracy_means.items():
    print(f"{classifier}: Mean Accuracy: {mean_accuracy:.2f}, Standard Deviation: {accuracy_stds[classifier]:.2f}")
