
# LLM-Based Build/Error-Log Summarization

## 1. Introduction
This project uses a Large Language Model (LLM) to summarize software build and error logs in simple language.

## 2. Objective
The main objective is to help developers understand build errors quickly and identify possible solutions.

## 3. Technologies Used
- Python
- OpenAI API
- Large Language Model (LLM)
- GitHub

## 4. Working
1. A build log is provided as input.
2. Python reads the log file.
3. The log is sent to the LLM through the OpenAI API.
4. The LLM analyzes the errors.
5. A simple summary with possible causes and solutions is generated.

## 5. Example
Input: Maven build log containing a compilation error.

Error: Cannot find symbol - variable userName.

Expected summary: The build failed because the variable userName could not be found. Check whether the variable is declared correctly and spelled properly.

## 6. Benefits
- Saves debugging time.
- Makes error messages easier to understand.
- Helps beginners identify errors.
- Improves developer productivity.

## 7. Conclusion
This project demonstrates how LLMs can help developers understand and summarize technical build logs.
