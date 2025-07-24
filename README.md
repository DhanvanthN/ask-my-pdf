
# Ask My PDF

A lightweight Python app that lets users ask questions about any PDF using the power of OpenAI's LLMs. Upload a PDF, ask anything, and get intelligent answers.

## Features

- Upload any PDF and extract text from it  
- Ask questions in natural language  
- Get context-aware answers powered by OpenAI's API  
- Simple command-line interface  
- Modular and easy to extend  

## Project Structure



ask-my-pdf/
├── app.py              # Main application logic
├── requirements.txt    # Python dependencies
├── .gitignore          # Files ignored by Git
└── .env                # API keys (not pushed to GitHub)



## Setup Instructions

### 1. Clone the Repository

bash
git clone https://github.com/DhanvanthN/ask-my-pdf.git  
cd ask-my-pdf  


### 2. Create a Virtual Environment

bash
python -m venv venv  
source venv/bin/activate    # On Windows: venv\Scripts\activate  


### 3. Install Dependencies

bash
pip install -r requirements.txt  


### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

env
OPENAI_API_KEY=your_api_key_here


### 5. Run the App

bash
python app.py  


## Example

bash
PDF loaded successfully  
Ask a question about the PDF: What is the main topic discussed in the document?  
Answer: The document primarily discusses...  


## Requirements

* Python 3.8+
* OpenAI API Key


