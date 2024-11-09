# Diamond Price Prediction

This repository contains a machine learning application for predicting diamond prices based on various features such as carat, color, length, and width. The application is built using FastAPI for the backend and Streamlit for the frontend, allowing users to input diamond characteristics and receive price predictions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [License](#license)

## Features

- Predict diamond prices based on user input.
- User-friendly interface built with Streamlit.
- FastAPI backend for handling prediction requests.
- Dockerized application for easy deployment.

## Technologies Used

- Python 3.9
- FastAPI
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Docker

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/diamond-price-prediction.git
    cd diamond-price-prediction
    ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

3. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).

## Usage

1. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).
2. Input the diamond characteristics:
    - Carat (float)
    - Color (integer from 0 to 6)
    - Length (float)
    - Width (float)
3. Click the "Predict" button to receive the predicted price of the diamond.

## Directory Structure

