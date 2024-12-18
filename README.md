
# Employee Burnout Analysis and Prediction

This project is a Flask-based web application designed to analyze employee burnout based on factors like gender, company type, WFH setup, and resource allocation. It provides predictions for burnout rates and includes dynamic visualizations for data insights.

---

## Project Structure

### 1. **Application Files**
- **`app.py`**: The main Flask application script. It handles routes, predictions, and dynamic visualizations.  
  [View `app.py` on GitHub](https://github.com/your-github-repo/app.py)

### 2. **Data Files**
- **`employee_burnout.xlsx`**: The dataset used for training and visualizations.  
  [View `employee_burnout.xlsx` on GitHub](https://github.com/your-github-repo/employee_burnout.xlsx)

### 3. **Templates**
Contains HTML files for rendering the web pages.
- **`index.html`**: The homepage for inputting employee details and viewing predictions.
- **`visualization.html`**: Displays dynamic visualizations based on the dataset.

### 4. **Static**
Contains static assets for the web application, such as CSS, JavaScript, and images.
- **`static/css/`**: Folder for CSS files.
- **`static/js/`**: Folder for JavaScript files.
- **`static/images/`**: Folder for images used in the app.

---

## Steps to Run the Project

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment
```bash
python -m venv env
```

### 3. Activate the Virtual Environment
- **Windows**: 
  ```bash
  .\env\Scriptsctivate
  ```
- **Linux/Mac**:
  ```bash
  source env/bin/activate
  ```

### 4. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

### 6. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Prerequisites
- Python 3.7 or above
- pip

---

## Key Features
- User-friendly interface for input and predictions.
- Visualizations to analyze burnout trends.

---

**Download the complete project folder below:**

[Download Project Files](./employee_burnout_analysis.zip)
