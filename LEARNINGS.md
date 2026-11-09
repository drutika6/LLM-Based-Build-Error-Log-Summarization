
# Assignment Learnings
## Topic: LLM-Based Build/Error-Log Summarization

### 1. Introduction
In this assignment, I learned how Large Language Models can be used to summarize software build and error logs.

### 2. Understanding the Problem
Build logs contain many messages, warnings and errors. Finding the main error manually can take time. LLMs can simplify this process by identifying important errors and explaining them.

### 3. Tools Used
- Python: Used to develop the application.
- OpenAI API: Used to connect the application with an LLM.
- GitHub: Used to store and manage the project.

### 4. Steps Followed

**Step 1: Repository Creation**

Created a public GitHub repository to store the assignment files and maintain the project.

**Step 2: Python Implementation**

Created app.py to read the build log and send it to the LLM using the OpenAI API.

**Step 3: Sample Log Creation**

Created sample_build.log containing a Maven compilation error.

**Step 4: Dependency Installation**

Created requirements.txt and added the OpenAI Python package required for API integration.

**Step 5: Prompt Engineering**

Designed a prompt instructing the LLM to identify the main error, possible cause and suggested solution in simple language.

**Step 6: Log Processing**

The Python program reads the log file and sends its contents to the LLM for analysis.

**Step 7: Error Summarization**

The LLM analyzes the input and generates an understandable summary of the build failure.

**Step 8: GitHub Documentation**

Created README.md and LEARNINGS.md to explain the project, implementation steps and learning outcomes.

### 5. Working Principle

Input: Build/Error Log

Processing: Python + OpenAI API + LLM

Output: Simple Error Summary and Suggested Solution

### 6. Key Learnings
- Understood the basic working of LLMs.
- Learned how APIs connect Python applications with AI models.
- Understood prompt engineering.
- Learned how to process software error logs.
- Practiced creating and managing GitHub repositories.

### 7. Limitations
- Requires an internet connection.
- Requires a valid API key.
- AI-generated suggestions should be verified.
 
### 8. Conclusion
Through this assignment, I understood how LLMs can be integrated with Python to simplify software debugging. This project demonstrates how AI can reduce the time required to understand build errors.
