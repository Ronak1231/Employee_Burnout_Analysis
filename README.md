
# Employee Burnout Prediction and Analysis

This project uses machine learning to predict employee burnout levels based on factors like mental fatigue score, resource allocation, and work-from-home setup. The project is implemented using **Flask** for the web interface and **Scikit-learn** for the model. The goal is to help organizations identify potential burnout risks and take preventive measures.

## Features

- **Burnout Prediction**: Predicts the burnout rate based on various features like gender, company type, mental fatigue score, and resource allocation.
- **Data Visualizations**: Provides various interactive visualizations to explore relationships between employee attributes and burnout.
- **Flask Web Application**: A simple web interface to interact with the model and view visualizations.
- **Model Persistence**: The trained model and scaler are saved as `.pkl` files to allow prediction without retraining.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contributors](#contributors)

## Project Structure

The project is organized as follows:

```
employee-burnout-analysis/
│
├── app.py                # Main application script
├── employee_burnout.xlsx # Dataset for employee burnout analysis
├── requirements.txt      # Python dependencies
├── static/               # Folder for static files (CSS, JS, Images)
│   ├── css/              # CSS files
│   ├── js/               # JavaScript files
│   └── images/           # Visualization images
├── templates/            # Folder for HTML templates
│   ├── index.html        # Home page template
│   └── visualization.html # Visualization page template
└── README.md             # Project documentation (this file)
```

- **[app.py](app.py)**: This is the main Flask application where the machine learning model is trained, evaluated, and predictions are made. It also serves the web pages.
- **[employee_burnout.xlsx](employee_burnout.xlsx)**: This is the dataset used for training the model. It contains employee information including burnout rate and other relevant attributes.
- **[requirements.txt](requirements.txt)**: Lists the required Python packages for the project. 
- **[static/](static/)**: Contains static files like CSS, JavaScript, and images for the web interface.
  - **[css/](static/css/)**: Contains the styling files for the web pages.
  - **[js/](static/js/)**: Contains the JavaScript files for client-side interactivity.
  - **[images/](static/images/)**: Stores visualizations that are dynamically generated.
- **[templates/](templates/)**: Contains the HTML templates for rendering the web pages.
  - **[index.html](templates/index.html)**: The home page where users can input their data to predict burnout rate.
  - **[visualization.html](templates/visualization.html)**: Displays the visualizations of the data and allows the user to explore them.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Ronak1231/Employee_Burnout_Analysis.git
cd employee-burnout-analysis
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure to have the **employee_burnout.xlsx** file in the project directory.

## Usage

1. Run the Flask app:

```bash
python app.py
```

2. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
   - You will see a page to input the employee data for burnout prediction.
   - Once you enter the details and click **Predict Burn Rate**, the predicted burnout rate will be displayed.
   - You can also explore various data visualizations by navigating to the **Visualizations** page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Scikit-learn** for the machine learning model and tools.
- **Flask** for creating the web interface.
- **Seaborn** and **Matplotlib** for creating the visualizations.
- Thanks to all contributors and open-source libraries that made this project possible.

## Contributors

- [Ronak Bansal](https://github.com/Ronak1231) - Project Author

Feel free to contribute to this project by opening issues or submitting pull requests. If you have any questions or suggestions, please reach out via email at [ronakbansal12345@gmail.com](mailto:ronakbansal12345@gmail.com).
