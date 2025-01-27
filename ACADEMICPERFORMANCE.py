import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from google.colab import drive
drive.mount('/content/drive')
data = pd.read_csv("Student_Mark.csv")
print(data.head(10))
print(data.isnull().sum())
figure = px.scatter(data_frame=data, x = "number_courses",
                    y = "Marks", size = "time_study",
                    title="Number of Courses and Marks Scored")
figure.show()
figure = px.scatter(data_frame=data, x = "time_study",
                    y = "Marks", size = "number_courses",
                    title="Time Spent and Marks Scored", trendline="ols")
figure.show()
correlation = data.corr()
print(correlation["Marks"].sort_values(ascending=False)) 	
x = np.array(data[["time_study", "number_courses"]])
y = np.array(data["Marks"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=42)
model = LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)
features = np.array([[6, 459]])
model.predict(features)