# EXPRESSO CHURN FLASK

- The data is from the Zindi Epresso Churn Competition

- The SQL data is loaded from CSV files in a path with permission, for my sql it is as such "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/", it will vary depending on what you are using e.g. Postgres etc. Alternatively, you could alter the file priviledges to read from different folders.

- For Tensorflow serving , use the [Docker image on Docker Hub](https://hub.docker.com/r/tensorflow/serving) to orchastrate and serve the model locally on your PC. Have it running at the same time as the Flask App, the ports will/should be different.
- The model was trained initially and saved, for more details check [here](https://github.com/AsetaShadrach/Expresso-Churn-Prediction/blob/main/Expresso%20Churn%20Pred%20with%20TF%20Functional%20API.ipynb)
- I run my docker container eith the following command :: 
docker run -t -p 8505:8505 --mount type=bind,source='/{path to folder}',target=/models/saved_model -e MODEL_NAME=saved_model tensorflow/serving
- Replace {path to folder} with the actual path to the folder with your model


- For the employee login, initially add a user ID and Email manually on your SQL server(simulate an admin situation), I avoided adding the whole idea of acces levels, atleast for now, but if you are familiar with it feel free to do so.

