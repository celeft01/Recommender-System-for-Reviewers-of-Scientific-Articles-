# Recommender System for Reviewers of Scientific Articles (Bachelor Thesis)

This repository contains the implementation of a recommender system designed to assist in assigning reviewers for scientific articles. The project was developed as part of my Bachelor thesis and utilizes a combination of machine learning, web technologies, and data processing techniques.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Files and Structure](#files-and-structure)
5. [Future Work](#future-work)

---

## Introduction

Reviewing scientific articles requires matching reviewers with expertise relevant to the article’s content. This recommender system automates this process by:

- Identifying suitable reviewers based on keywords and previous publications.
- Utilizing clustering and similarity measures for recommendations.

The system was built with the goal of improving the efficiency and accuracy of the peer review process.

---

## Features

- **Reviewer Recommendation**:
  - Recommends reviewers based on keywords extracted from the article.
  - Suggests reviewers with prior co-author relationships.

- **Interactive Web Interface**:
  - Search by author names and keywords.
  - Configure the number of recommendations.

- **Backend Processing**:
  - Implements k-nearest neighbors (k-NN) for similarity measurement.
  - Leverages TF-IDF for keyword extraction.

---

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - Bootstrap for responsive design

- **Backend**:
  - Python for data processing and machine learning
  - PHP for server-side scripting

- **Data Science Libraries**:
  - pandas, scikit-learn, NumPy, scipy

---

## Files and Structure

- **`index.html`**: The main web interface for the system.
- **`thesis.js`**: JavaScript logic for user interaction and data display.
- **`thesis-booktitles.py`**: Python script for data processing and generating recommendations (old version).
- **`thesis-booktitles-senond-option.py`**: Python script for data processing and generating recommendations.
- **`thesis-journals.py`**: Python script for data processing and generating recommendations (old version).
- **`thesis-journals-second-option.py`**: Python script for data processing and generating recommendations.
- **`thesis-booktitlesANDjournals.py`**: Python script for data processing and generating recommendations (old version).
- **`thesis-booktitlesANDjournals-second-option.py`**: Python script for data processing and generating recommendations.
- **`requirements.txt`**: List of required Python dependencies.
- **`thesis.css`**: Stylesheet for the web interface.
- **`newParsing.py`**: Python script for parsing purposes.
- **`tesingAll.py`**: Python script for testing purposes.
- **`testingCJ.py`**: Python script for testing purposes.
- **`thesis.php`**: PHP script.

---

## Future Work

1. Expand the dataset to include more publications and reviewers.
2. Improve recommendation algorithms for better precision.
3. Add support for multi-language input.
4. Integrate real-time updates using modern frameworks like React or Angular.

---

## Acknowledgements

Special thanks to:

- The professors and mentors who guided the development of this thesis.
- Open-source libraries and their contributors for the tools used in this project.

