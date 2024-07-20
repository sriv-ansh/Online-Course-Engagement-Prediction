# Student Online Course Engagement Prediction

This project aims to predict whether a student will enroll in an online course based on various features related to their engagement and interaction with the course material.

## Features
- **Course Category**
- **Time Spent On Course**
- **Number Of Videos Watched**
- **Number Of Quizzes Taken**
- **Quiz Scores**
- **Completion Rate**
- **Device Type**

## Technologies Used
- **Data Cleaning**: Pandas
- **Feature Engineering**: One_Hot_Encoder, MinMaxScaler
- **Model Selection**: GridSearchCV for Hyperparameter Tuning, Logistic Regression
- **Model Serialization**: Pickle
- **Web Development**: Flask

## Project Structure
- **data/**: Contains the dataset
- **models/**: Contains the trained model and related files
- **templates/**: HTML templates for the Flask web application
- **app.py**: Main application file for Flask

## Setup Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/online-course-engagement-prediction.git
    ```
2. Navigate to the project directory:
    ```sh
    cd online-course-engagement-prediction
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```sh
    python app.py
    ```

## Usage
1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter the required input features.
3. Click on the "Predict" button to see the prediction result.

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.
