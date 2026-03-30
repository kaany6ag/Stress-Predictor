                                         STUDENT STRESS LEVEL PREDICTOR 

1) OVERVIEW :
This project predicts whether a student is stressed based on study hours and sleep hours using a Machine Learning model.

2) PROBLEM STATEMENT :
Students often experience stress due to academic workload and poor lifestyle habits. This project aims to predict stress levels early using basic inputs.

3) SOLUTION :
A Logistic Regression model is trained to classify stress levels:
 0 → Low Stress
 1 → High Stress

4) TECHNOLOGIES USED : 
 Python
 Pandas
 Scikit-learn

5) DATASET :
A small dataset was manually created with:
- Study Hours
- Sleep Hours
- Stress Level

6) HOW IT WORKS :
1. Data is created using pandas
2. Features and labels are separated
3. Data is split into training and testing sets
4. Model is trained using Logistic Regression
5. Predictions are made on test data



                                                STEP-BY-STEP SETUP GUIDE 

STEP 1) INSTALL PYTHON 
Ensure Python is installed on your system.

STEP 2) CLONE REPOSITORY 
git clone https://github.com/YOUR-USERNAME/Stress-Predictor

STEP 3) NAVIGATE TO PROJECT FOLDER 
cd Stress-Predictor

STEP 4) INSTALL DEPENDENCIES 
pip install -r requirements.txt

STEP 5) RUN THE PROJECT 
python model.py



--SAMPLE OUTPUT --
Accuracy: 0.5  
Prediction: High Stress



--LIMITATIONS--
 Small dataset
 Limited features

--FUTURE SCOPES--
 Use real dataset
 Add more features
 Build web interface

AUTHOR:
Kaanya Agrawal