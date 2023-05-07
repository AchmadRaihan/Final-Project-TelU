# Implementation Prophet's Method on River Water Level Forecast

## Introduction
Flooding is one of the incidents that result in a major adverse impact, causing the inactivity of various sectors of human life. In overcoming it, there are various ways that have been done, such as developing a river water level prediction system using machine learning. However, based on the research, the system does not make predictions into the future. In addition, it does not have a dashboard that can display the results of river water level prediction. This Final Project proposes to implement the prophet method on river water level prediction. Then, the system can display the results of river water level prediction in a dashboard. Furthermore, the data set used for flood prediction is only the results of river water level measurements every 1 hour by ignoring the factors that affect it. 

## System Design
### Prophet Modelling
Prophet modeling is done by hyperparameter tuning. Hyperparameter tuning is done by setting values based on parameters that can be used to support the performance of the river water level prediction system. Hyperparameter tuning is done 3 times with different data sets. The first data set contains river water levels from January 1, 2020 to June 30, 2020. The second data set contains river water levels from July 1, 2020 to December 31, 2020. The third data set contains river water levels from April 1, 2020 to September 30, 2020. Then, evaluation is carried out using theil's u to determine the best model by looking at the smallest error. After that, the best model can be determined to be implemented into the dashboard for river water level prediction.
### Dashboard Modelling River Water Level Forecast
#### Deploy the Best Prophet Model
The best prophet model would be deploy to Streamlit aims to be able to display performance in the form of a dashboard. Integrating the best model into Streamlit locally is a step where the backend is the best model resulting from hyperparameter tuning and the frontend using the Streamlit library package which is put together as a whole but its performance can only be seen by developers. Next, place the locally integrated file into a GitHub repository. There are 3 files that must be placed into a GitHub repository, they are app.py, requirements.txt, and data set. Integrating the GitHub repository into Streamlit is the last step in deploying.
#### Dashboard Flowchart
There are 3 steps in the dashboard work process, they are upload data, forecast to future, and display. Upload data can be referred to as the data set input to the dashboard. However, if you do not have a data set in the form of river water levels, users can press the 'Use sample data set' button to see the dashboard performance without uploading data. Forecast to future is a step where users can set the time range to make predictions to the future. Display is a step where the dashboard displays river water level data.

## Conclusion
Evaluation after hyperparameter tuning with 3 different data using Theil's U has shown the smallest average error that is 0.187044. The dashboard can predict and display data directly after uploading. Then, the dashboard has sample data that can be used to see the performance in making predictions.

Note:
Dashboard
https://achmadraihan-ptas-app-47m035.streamlit.app/
