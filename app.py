from flask import Flask, request, render_template, redirect, url_for
import pickle
import pandas as pd


app = Flask(__name__)

# Load the models and encoders
with open('feature engineering model/MMS_SCALER.pkl', 'rb') as mms_file:
    mms = pickle.load(mms_file)

with open('feature engineering model/OneHot.pkl', 'rb') as mms_file:
    one_hot = pickle.load(mms_file)


with open('model_file/MODEL.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Route for the index page
@app.route('/')
def index():
    return render_template('web_page.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    
    # Retrieve form data
    course_category = request.form.get('CourseCategory')
    time_spent = float(request.form.get('TimeSpentOnCourse'))
    videos_watched = float(request.form.get('NumberOfVideosWatched'))
    quizzes_taken = float(request.form.get('NumberOfQuizzesTaken'))
    quiz_scores = float(request.form.get('QuizScores'))
    completion_rate = float(request.form.get('CompletionRate'))
    device_type = request.form.get('DeviceType')

    # Convert device type to integer
    device_type = device_type.lower()
    if device_type == 'laptop':
        device_type = 0
    elif device_type == 'mobile':
        device_type = 1
    else:
        return "Invalid device type. Please enter 'Laptop' or 'Mobile'."

    # Create input data DataFrame
    input_data = pd.DataFrame({
        'CourseCategory': [course_category],
        'TimeSpentOnCourse': [time_spent],
        'NumberOfVideosWatched': [videos_watched],
        'NumberOfQuizzesTaken': [quizzes_taken],
        'QuizScores': [quiz_scores],
        'CompletionRate': [completion_rate],
        'DeviceType': [device_type]
    })
    temp_df = input_data[['CourseCategory']]

    # Transform categorical features using pd.get_dummies()
    encoded_category_df = pd.DataFrame(one_hot.transform(temp_df).toarray(),
                                       columns = ['CourseCategory_Arts','CourseCategory_Business', 
                                                  'CourseCategory_Health','CourseCategory_Programming',
                                                    'CourseCategory_Science'],
                                       index = temp_df.index)

    # Combine all features into a single DataFrame
    input_data = input_data.drop('CourseCategory', axis=1).join(encoded_category_df)


    # Scale features using MinMaxScaler
    input_data.iloc[:,:5] = mms.transform(input_data.iloc[:,:5])


    
    # Make prediction using loaded model
    prediction = model.predict(input_data)

    # Process prediction result
    if prediction[0] == 1:
        result = "Student Will Enroll 🤩"
    else:
        result = "Student Will Not Enroll 😥😣"

    # Redirect to result page with prediction
    return redirect(url_for('show_result', result=result))



# Route to display result
@app.route('/result')
def show_result():
    result = request.args.get('result', type=str)
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
