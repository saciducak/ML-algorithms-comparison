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

## Confusion Matrixs
Here, SVM and KNN have identified too many positive values as negative, a bad feature for this algorithm. However, the Decision tree and Random forest ratings are not as high as KNN and SVM and are relatively more successful. 
FP: FP (it can be thought as if we said we have something that is not really there.) 
To the person who is not sick means this person. 
!! System is a misleading result. 

![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/b5cca92a-49e3-4048-a1bd-90d3027e0623)
![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/a370b131-ffc4-44a3-9de9-0c928843fb7b)
![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/0cf2144e-5284-4ab1-84b4-a59fddc0310a)
![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/6f2d2b52-c5c2-495c-9b0a-64edd0657302)

KNN and SVM have lower values than other algorithms. however, the Decision tree(especially this is too much) and Random forest values have a fairly high FP value, which means that the DT and RF ‚ actually obtained incorrect results from FP values.

### Accuracy Comparison

![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/83ec2949-392f-41f2-8fd8-d3e4733bab46)

### Training Time Comparison

![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/f638a510-3d14-4b2e-a268-6f6c058ff878)
![image](https://github.com/saciducak/ML-algorithms-comparison/assets/84833816/b1113712-5ea1-4ec8-ae30-b630831e0fa7)

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
