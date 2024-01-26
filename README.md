**README**

## LinkPad: Academic Project
#### Project Start and End Dates: October 2023 - Present
#### Status: Under Development

## Overview

“Building an Alumni Network for Institutes to Improve Networking, Career Opportunities, and Institutional Growth leveraging the trends of AI and ML”

#### Objective: 
The objective of this project is to develop a web-based alumni network for institutes that will provide a platform for alumni to connect with each other, network with industry professionals, and find job opportunities. The network will also allow institutes to track the progress of their alumni and gain valuable insights into their career paths.
#### Problem Statement:
Currently, there is no platform for alumni to connect with each other or with industry professionals of their colleges. This makes it difficult for alumni and students to connect, collaborate, learn and mentor and also to find job opportunities and to stay up-to-date on the latest industry trends. Additionally, institutes have no way to track the progress of their alumni or to gain valuable insights into their career paths. 

#### Solution:
LinkPad is an alumni portal that addresses these problems with a fake information classifier that uses Django and NLP to identify fake information articles on the platform. The classifier utilizes a Bi-directional RNN model with an accuracy of over 92%. It focuses on the College and institutional growth by helping students to get mentorships, skills, career paths and guidance and also helps staff to know latest industry standards, career paths and technological trends.

LinkPad also has a feature that explains the model's predictions and generates counter-arguments to fake information articles. This feature allows users to better understand why the model classified an article as fake and to develop their own arguments against the misinformation.

## Technical Terms

* Django: A Python web framework for backend
* ReactJS: A javascript framework for frontend
* NLP: Natural language processing
* Bi-directional RNN: A type of recurrent neural network that can process data in both directions
* Accuracy: A measure of how often a model correctly predicts the outcome of a given input

## How to Run

To run LinkPad, you will need to have the following installed:

* Python 3.8 or higher
* Django 3.2 or higher
* TensorFlow 2.9 or higher

Once you have all of the required dependencies installed, you can run LinkPad by following these steps:

1. Clone the LinkPad repository:

```
git clone https://github.com/adarshmarvel22/LinkPad.git
```

2. Navigate to the LinkPad directory:

```
cd LinkPad
```

3. Create a virtual environment:

```
python3 -m venv env
```

4. Activate the virtual environment:

```
source env/bin/activate
```

5. Install the LinkPad dependencies:

```
pip install -r requirements.txt
```

6. Create a database:

```
python manage.py migrate
```

7. Run the LinkPad development server:

```
python manage.py runserver
```

LinkPad will now be running on http://localhost:8000/. You can access the admin interface at http://localhost:8000/admin.

## Other Stuff

LinkPad is still under development, but it is already a useful tool for connecting the Alumni Students and Staff of a college, identifying and combating fake information, finding jobs and participating in discussion forums. The fake information classifier is highly accurate, and the feature that explains the model's predictions and generates counter-arguments is very helpful for understanding and combating misinformation.

I hope you find LinkPad useful. Please feel free to contribute to the project or to submit feedback.
