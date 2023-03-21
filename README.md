# Implementation of Prophet's Method on River Water Level Forecast

## Introduction
Flooding is one of the incidents that result in a major adverse impact, causing the inactivity of various sectors of human life. In overcoming it, there are various ways that have been done, such as developing a river water level prediction system using machine learning. However, based on the research, the system does not make predictions into the future. In addition, it does not have a dashboard that can display the results of river water level prediction. This Final Project proposes to implement the prophet method on river water level prediction. Then, the system can display the results of river water level prediction in a dashboard. Furthermore, the data set used for flood prediction is only the results of river water level measurements every 1 hour by ignoring the factors that affect it. 

## System Design
### Prophet Modelling
Prophet modeling is done by hyperparameter tuning. Hyperparameter tuning is done by setting values based on parameters that can be used to support the performance of the river water level prediction system. Hyperparameter tuning is done 3 times with different data sets. The first data set contains river water levels from January 1, 2020 to June 30, 2020. The second data set contains river water levels from July 1, 2020 to December 31, 2020. The third data set contains river water levels from April 1, 2020 to September 30, 2020. Then, evaluation is carried out using theil's u to determine the best model by looking at the smallest error. After that, the best model can be determined to be implemented into the dashboard for river water level prediction.

## Conclusion
Evaluation after hyperparameter tuning with 3 different data using Theil's U has shown the smallest average error that is 0.187044. The dashboard can predict and display data directly after uploading. Then, the dashboard has sample data that can be used to see the performance in making predictions.
