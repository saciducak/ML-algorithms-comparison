# %%
# UCI Machine Learning Repository'den veri setleri indirmek fetch_openml fonksiyonu ve sklearn.datasets modülünü kullandık.
from sklearn.datasets import fetch_openml


# %%
# Uygun veri setlerini seçme ve yükleme
iris = fetch_openml(name='iris', version=1)
breast_cancer = fetch_openml(name='breast-cancer', version=1)
diabetes = fetch_openml(name='diabetes', version=1)
vehicle = fetch_openml(name='vehicle', version=1)
ionosphere = fetch_openml(name='ionosphere', version=1)
glass = fetch_openml(name='glass', version=1)
segment = fetch_openml(name='segment', version=1)
wine_quality = fetch_openml(name='wine-quality-red', version=1)
yeast = fetch_openml(name='yeast', version=1)
ecoli = fetch_openml(name='ecoli', version=1)


# %%

# Seçilen veri setlerini bir sözlükte saklama
selected_datasets = {
    'Iris': iris,
    'Breast Cancer': breast_cancer,
    'Diabetes': diabetes,
    'Vehicle': vehicle,
    'Ionosphere': ionosphere,
    'Glass': glass,
    'Segment': segment,
    'Wine Quality': wine_quality,
    'Yeast': yeast,
    'Ecoli': ecoli,
}


