# ML Algorithm Comparison

This repository contains a comprehensive comparison of various machine learning algorithms using datasets fetched from the UCI Machine Learning Repository. The algorithms compared include Decision Tree, Random Forest, SVM, KNN, Gradient Boosting, and Naive Bayes.

## Datasets Used
The following datasets from the UCI Machine Learning Repository were used for this comparison:

- Iris
- Breast Cancer
- Diabetes
- Vehicle
- Ionosphere
- Glass
- Segment
- Wine Quality (Red)
- Yeast
- Ecoli

## Algorithms Compared
The machine learning algorithms compared in this project are:

- Decision Tree
- Random Forest
- SVM (Support Vector Machine)
- KNN (K-Nearest Neighbors)
- Gradient Boosting
- Naive Bayes

## Project Structure
- **data_fetching.ipynb**: Jupyter notebook for fetching and processing the datasets.
- **algorithm_comparison.ipynb**: Jupyter notebook for training the models and comparing their performance.
- **visualization.ipynb**: Jupyter notebook for visualizing the results and confusion matrices.

## Usage
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ML-Algorithm-Comparison.git
    cd ML-Algorithm-Comparison
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the notebooks in the following order:
    - `data_fetching.ipynb`
    - `algorithm_comparison.ipynb`
    - `visualization.ipynb`

## Results
The accuracy and training time for each algorithm were recorded and compared. The results are visualized using matplotlib and seaborn.

### Accuracy Comparison
The mean accuracy and standard deviation for each algorithm across the datasets are calculated and displayed.

### Training Time Comparison
The mean training time for each algorithm is calculated and visualized.

### Confusion Matrices
Confusion matrices for each algorithm are plotted to visualize the classification performance.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
