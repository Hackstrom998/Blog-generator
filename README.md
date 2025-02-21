Blog Generator Using LLaMA 2 & Streamlit
Overview
This project is a blog generator built using LLaMA 2 and Streamlit. It takes user input and generates blog content using AI.

Features
Generates blog content based on prompts
Simple and interactive UI with Streamlit
Backend powered by a pre-trained LLaMA 2 model
Setup & Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/blog-generator.git
cd blog-generator
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Download the LLaMA Model
Since the model file is too large for GitHub, download it from:
[Google Drive / OneDrive / Dropbox Link]

After downloading, place the model file in the models/ directory:

python
Copy
Edit
blog-generator/
│── app.py
│── test.py
│── models/
│   └── llama-2-q4.bin
│── requirements.txt
│── README.md
4. Run the Application
bash
Copy
Edit
streamlit run app.py
Project Structure
bash
Copy
Edit
blog-generator/
│── app.py        # Frontend (Streamlit UI)
│── test.py       # Backend logic
│── models/       # Folder for the LLaMA model
│── requirements.txt  # Python dependencies
│── README.md     # Project documentation
Contributors
Navadeep (Backend & AI Model Setup)
Shanmukh (Frontend stramlit)
Harika
Shivani
Madhupriya
