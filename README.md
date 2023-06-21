  <h1>Web Automation</h1>
  <p>
    This repository contains code that automates a repetitive computer task that has been a challenge for me: completing quizzes.
  </p>
  <p>
    After completing the same online quizzes ad nauseam, the realization struck that these could be effortlessly solved by a machine. Hence, the decision was made to develop an automated solution.
  </p>
  <h1>How It Works</h1>
  <p>
    After some research, I discovered Selenium, a powerful Python package capable of automating various networking processes.
  </p>
  <p>
    Basic proficiency in networking, web pages, and HTML code was needed to complete the code. I implemented my basic functions in "web.py."
  </p>
  <h1>Step 1</h1>
  <p>
    The first step in building the automated solution was recording the correct answers to enable the machine to score well. This was accomplished by designing a system that automatically scanned and extracted the questions and answers into a dictionary. Each question served as a key, paired with its corresponding multiple choice answers, and the resulting dictionary was stored in a JSON file. The implementation can be found in the "download_quizzes.py."
  </p>
  <h1>Step 2</h1>
  <p>
    I manually eliminated the incorrect answers. It is acknowledged that 2-3 answers within the Ancient Egypt trivia section are inaccurate. However, since achieving 9 out of 12 correct answers suffices to pass the quiz, rectifying these errors is pointless.
  </p>
  <h1>Step 3</h1>
  <p>
    After completing the previous steps, continuous refinement and iteration were undertaken to create "solve_quizzes.py." This script now reliably fulfills solves the quizzes using the answers from the json files.
  </p>
  <h1>Multithreading</h1>
  <p>
    One of the most fascinating concepts applied during this project was multithreading. This technique allowed the splitting of the automation process into multiple concurrent processes, enabling the bot to solve multiple quizzes simultaneously. For a look at the implementation, refer to "main.py."
  </p>
  <h1>Important Notes</h1>
  <p>
    IThe automation bot is unable to solve reCAPTCHAs. Consequently, manual intervention is necessary to solve these challenges for the bot to continue functioning. Additionally, using this bot may impact your Captcha3 score, potentially resulting in your IP address being flagged as bot-like or suspicious.
  </p>
  <h1>How to Use It Yourself</h1>
  <p>
    To utilize this automation code for quizzes, follow the steps outlined below:
  </p>
  <ul>
    <li>Clone the repository: <code>git clone 'https://github.com/Dan-Swarts/web_automation.git'</code></li>
    <li>Install the required dependencies: <code>pip install selenium</code></li>
    <li>Download the Selenium web driver</li>
    <li>Run the script: <code>python main.py</code></li>
  </ul>