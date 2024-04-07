# Technical Crew AI

---

## Description

This Streamlit application simulates a technical crew for software development projects. It utilizes the CrewAI library to manage a team of development agents and execute various development tasks. The project scope can be provided as input, and upon running the development crew, the result of the crew's execution will be displayed.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/technical-crew-ai.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    - Create a `.env` file in the root directory of the project.
    - Add the required environment variables:

        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```

4. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

---

## Usage

1. Enter the project scope in the provided text area.
2. Click the "Run Development Crew" button to initiate the development crew.
3. View the result of the development crew's execution.

---

## Dependencies

- Streamlit
- CrewAI
- LangChain_OpenAI
- Dotenv

---

## File Structure

- `app.py`: Main Streamlit application code.
- `agents.py`: Definition of development agents.
- `tasks.py`: Definition of development tasks.
- `README.md`: Project documentation.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variable configuration file.

---

## About

This application is developed by Rizwan Coder. It is part of a project to explore AI-driven project management and software development automation.

For any questions or inquiries, please contact rizwaniscoder@gmail.com

