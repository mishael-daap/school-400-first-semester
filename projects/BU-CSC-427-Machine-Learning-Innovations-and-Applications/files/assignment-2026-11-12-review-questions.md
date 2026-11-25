# CSC 427 — Machine Learning Innovations and Applications

Assignment: Review Questions.

Source: photo of the question page, taken 12 November 2026. Questions copied word for word.
Answers to be written below each question later.

## Date

12 November 2026, 10:19

---

## Review Questions

1. Explain in your own words how machine learning is different from traditional programming.

   **Answer:** In traditional programming I write the rules and the computer follows them, in machine learning I give it examples of input and output and it finds the rules itself. Same job, different direction. So my work moves from writing logic to picking good examples and checking what it learned.

2. Give a real-life example where machine learning is used and describe how it helps in that situation.

   **Answer:** The fraud check that runs when I send money from my phone. It looks at the amount, the time and who I am paying, and holds the transfer if it does not look like me. Nobody typed those rules, it learned them from millions of past transfers, so fraud gets caught in a second instead of never.

3. What are the three key elements of machine learning, and why are they important?

   **Answer:** The three are data, model and training, and none of them works alone.

   **Data**

   What I give the computer. It can be numbers, text, images or sounds, and the more high-quality data I have, the better it can learn.

   **Importance:** it is what everything is learned from, so poor data means poor learning no matter how good the model is.

   **Model**

   The brain. It learns the pattern from the data and makes the prediction, and different tasks need different models.

   **Importance:** it is the part that actually does the thinking, so picking the wrong one means the work never gets done properly.

   **Training**

   Showing it many examples so it improves its understanding. The more training it gets, the sharper it becomes.

   **Importance:** it is how the model gets smart, and with too little training it is only guessing.

   They all have to be right together, because a good model sitting on poor data still learns rubbish and a model that never got enough training is just guessing. So the quality of my data and the amount of training is what decides whether I can trust what comes out.

4. If you wanted to build a machine learning system to predict students' exam scores, what kind of data would you collect for training?

   **Answer:** A score is a number and not a class, so this is regression. I would collect CA scores, past results, attendance, assignments submitted, study hours, whether they are repeating the course, plus the exam score itself. The school already holds the first three, so I would start there.

5. Why is the quality of data important in machine learning?

   **Answer:** The data is the teacher, so the model can only be as good as what I feed it. If the data has missing values, wrong entries or only covers one kind of example, the model learns those faults and repeats them with confidence instead of telling me it is unsure. That is why I would rather spend time cleaning and checking the data first than train a bigger model on rubbish, because bad data gives me a wrong answer that looks right.
