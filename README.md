# Web Automation

This repo stores code which automates a repetative computer task which has plaugued me for months-doing quizzes. 

I've done these same online quizzes dozens of times and often i think "this is so simple a robot could do it. so i finally decided to try and make just that-a robot to do these quizzes. 

# how it works 

I discovered selerium; a python package which can automate simple networking processes. first i downloaded the selerium web driver, then i startd coding.

this requiered a basic knowledge of networking, web pages, and html code, but i was able to figure it out quickly. 

# step 1

The first thing i had to do was record all the correct answers, so that the machine was able to answer the quizzes. to do this, i created a system which would automatically read go through, read the questions and anwsers into a dictionary, where the question keys to the answers, and then writes the dict to a json file. 

I manually went through and deleted all the wrong answers, leaving a dictionary where questions keyed to the correct answer instead of the possible answers. 

# step 2 

once that was over i iterated on my designs for the quiz-solving bot. eventually it worked perfectly.

# Multithreading

this project gave me a unique opportunity to implement one of the coolest things i've ever learned but almost never use; multithreading. this lets me split my process into multiple seperate processes which all do a portion of the work. bassically, this bot can solve multiple different quizzes at the same time. 