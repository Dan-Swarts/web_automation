
<div>
  <h1>A Repetitive task</h1>
  <p>
    I am very fond of this project, as it is not for school or work. This repository contains code that automates a repetitive task that has been a personal challenge for me: completing quizzes for a daily reward. I completed these quizzes for my free crowns EVERY DAY. While Experiencing the mind-numbing, boring, tedious, and repetitive task once again, the realization struck that these could be effortlessly solved by a machine.
  </p>
</div>

<div>
  <h1>Selenium</h1>
  <p>
    After some research, I discovered Selenium, a powerful Python package capable of automating various networking processes.
  </p>
  <p>
    Basic proficiency in networking, web pages, and HTML code was needed to complete the code. I implemented my basic functions in "web.py."
  </p>
</div>

<div>
  <h1>Multithreading</h1>
  <p>
    One of the most fascinating concepts applied during this project was multithreading. This technique allowed the splitting of the automation process into multiple concurrent processes, enabling the bot to solve multiple quizzes simultaneously. For a look at the implementation, refer to "main.py."
  </p>
</div>

<div>
  <h1>Recording the Answers</h1>
  <p>
    The first step in building the automated solution was recording the correct answers to enable the machine to score well. This was accomplished by designing a system that automatically scanned and extracted the questions and answers into a dictionary. Each question served as a key, paired with its corresponding multiple choice answers, and the resulting dictionary was stored in a JSON file. The implementation can be found in the "download_quizzes.py."
  </p>
</div>

<div>
  <h1>Manual Review</h1>
  <p>
    I manually eliminated the incorrect answers. It is acknowledged that 2-3 answers within the Ancient Egypt trivia section are inaccurate. However, since achieving 9 out of 12 correct answers suffices to pass the quiz, rectifying these errors is pointless.
  </p>
</div>

<div>
  <h1>Solving the Quizzes</h1>
  <p>
    After completing the previous steps, continuous refinement and iteration were undertaken to create "solve_quizzes.py." This script now reliably fulfills solves the quizzes using the answers from the json files.
  </p>
</div>

<div>
  <h1>Important Notes</h1>
  <p>
    The automation bot is unable to solve ReCAPTCHAs. Consequently, manual intervention is necessary to solve these challenges for the bot to continue functioning. Additionally, using this bot may impact your Captcha3 score, potentially resulting in your IP address being flagged as bot-like or suspicious.
  </p>
</div>

<div>
  <h1>Ethics</h1>
  <p>
    Using this software may be unethical. The online quizzes were meant for educational purposes; not to be gamed by automation for free rewards. Additionally, the ReCAPTCHAs are proof that the owners do not want bots on their site.
  </p>
</div>

<div>
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
</div>