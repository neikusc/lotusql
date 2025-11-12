# 🪷 LotusQL — Natural Language to SQL Chatbot Demo

## Overview
**LotusQL** is a demo chatbot application built with the **Google ADK (Agentic Development Kit)** framework.  
The chatbot allows users to query a database using natural language. It converts user queries into SQL, executes them against a SQLite database, and returns comprehensive, conversational answers — acting as an intelligent data assistant.

---

## 🧱 Setup Instructions

### 1. Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3.11 -
export PATH="/Users/kientrinh/.local/bin:$PATH"
```

### 2. Create Environment and Add Dependencies
```bash
source $(poetry env info --path)/bin/activate
poetry add google-adk notebook ipykernel
python -m ipykernel install --user --name=lotusql-py3.11
```

---

## 🧮 Data Preparation
This demo uses real estate data from Kaggle’s  
[House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data).

Download the **train.csv** file and use it as the sample dataset for your database.  
You can convert the CSV file to a `.sqlite` file for use in the chatbot’s SQL queries.

Example conversion command:
```bash
# Example: Convert train.csv to train.sqlite
# (Assuming you have pandas and sqlite3 in Python)
python -c "import pandas as pd; import sqlite3; 
df = pd.read_csv('train.csv'); 
conn = sqlite3.connect('train.sqlite'); 
df.to_sql('houses', conn, index=False, if_exists='replace'); 
conn.close()"
```

---

## 🔑 Environment Setup
Create a `.env` file in the project root folder `lotusql` with the following variables:
```
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=chatgpt-5-nano
```

Load them in Python using:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## ⚙️ Agentic Framework and Tools
Unlike traditional LLM calls, which are reactive, **agentic frameworks** empower the LLM to reason, plan, and act using a set of tools.  
In **LotusQL**, the main tool is the `data_retrieval` tool, which allows the agent to execute SQL queries and return structured results.

Each tool should:
- Return a JSON-serializable Python dictionary containing:
  - `output`: main result of the tool  
  - `status` *(optional)*: metadata, logs, or error info  
- Include a **clear docstring**, helping the agent understand when and how to use it properly.

Example structure:
```python
def data_retrieval(query: str) -> dict:
    """
    Executes a SQL query on the local SQLite database and returns the results.

    Args:
        query (str): SQL query string to execute.

    Returns:
        dict: {
            "output": query_results,
            "status": "success" or "error"
        }
    """
```

---

## 🚀 Next Steps
Once the environment is set up and your SQLite database is ready:
1. Initialize your **ADK agent**.
2. Equip it with the `data_retrieval` tool.
3. Start querying your data in natural language — and watch the chatbot translate, execute, and explain!
