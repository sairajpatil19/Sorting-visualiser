📊 Sorting Visualizer
This is a web-based Sorting Algorithm Visualizer built using HTML/CSS/JavaScript for the frontend and Python (Flask) for the backend. It helps users visually understand how different sorting algorithms work by animating each step.

🚀 Features
Visualizes the sorting process of:

Bubble Sort

Selection Sort

Insertion Sort

Merge Sort

Smooth animations and an aesthetic UI

Responsive, fast, and interactive

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python with Flask

Communication: REST API (/sort)

Styling: Custom CSS + Google Fonts

CORS Enabled: To allow frontend-backend communication

📂 File Structure
bash
Copy
Edit
├── app.py           # Flask backend handling sorting logic
├── index.html       # Frontend UI
├── README.md        # Project documentation (you are here!)
▶️ How to Run the Project
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/sorting-visualizer.git
cd sorting-visualizer
2. Set Up and Run Backend
Make sure Python and pip are installed.

bash
Copy
Edit
pip install flask flask-cors
python app.py
The Flask server will run at: http://127.0.0.1:5000

3. Open Frontend
Open index.html in any web browser.

🔁 How It Works
A random array is generated.

User selects a sorting algorithm.

Frontend sends the array and algorithm to the Flask backend.

Backend returns a list of "steps" in sorting.

Frontend animates each step as vertical bars.

🧠 Educational Use Case
This project is ideal for:

Learning and teaching sorting algorithms

Visual learners

Coding portfolios

📸 Screenshot
(Add a screenshot of the site here for better appeal on GitHub)

📬 Contributing
Want to add more algorithms like Quick Sort or Heap Sort?
Feel free to fork the repo and open a pull request!

📜 License
MIT License — feel free to use and modify.
