### Assignment 4: Probability and Utility

#### Due April 27, at the start of class.

To turn in: For the written portions, please prepare one document with the answers for each question noted within.

For parts 2 and 3, please provide your answers in separate, easy to find files. (for part 4, use the provided file.)

Part 1. Probability and utility.

(10 points) Consider two medical tests, A and B, for a disease. 
Test A is 95% effective at recognizing the disease when it is present, 
but has a 10% false positive rate (indicating that the disease is present, when it is not). 
Test B is 90% effective at recognizing the disease, but has a 5% false positive rate. 
The two tests use independent methods of identifying the disease. 
1% of the population has this disease.

Suppose that we are particularly interested in minimizing false positives - that is, we do not want 
cases in which someone who does not have the disease to test positive.

Which test would we prefer? Justify your answer using Bayes' rule.

(5 points) Suppose that our agent has a choice of three routes it can take to deliver a package. 
- Route 1 is guaranteed to take 30 minutes.
- Route 2 takes 20 minutes 50% of the time, and 50 minutes 50% of the time, due to traffic.
- Route 3 takes 10 minutes 25% of the time, and 35 minutes 75% of the time, due to traffic.

Which route should our agent choose if it wants to minimize expected travel time. Show your work.

(5 points) Suppose that our agent has access to a camera that shows it the traffic on route 2. It can check the camera,
know whether there is traffic or not, and then make a decision. Does this change its strategy? Explain your answer.

(10 points) Suppose that the camera for route 2 is slow to start up, and the agent needs to wait in order to get 
traffic information. How long should the agent be willing to wait? 


(25 points) Part 2: Text classification with sklearn.

In this question, you'll get some experience using sklearn's built-in tools to classify text with the Naive Bayes algorithm.

To begin, please review [this tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
), which shows how to use sklearn's text processing tools.


The tutorial shows how to read in data using the 'bag of words' model, how to score word counts using TF-IDF, and how to 
construct a pipeline to train a classifier. 

One common text classification task  is *sentiment analysis*. This is the problem of determining the emotion (or sentiment) behind a text.
The [sklearn GitHub repo](https://github.com/scikit-learn/scikit-learn/blob/main/doc/tutorial/text_analytics/solutions/exercise_02_sentiment.py)
illustrates how to do this with their movie review dataset. They use an algorithm called a linear classifier to separate 
reviews into positive and negative.

You should do two things:
1. Change this example to instead use the Naive Bayes classifier. Print out the confusion matrix that is generated.

2. One way to potentially improve the performance of 'bag-of-words' classifiers is to remove features that are not helpful in classifying. The example
does this with tokens based on frequency. An additional approach is to remove stopwords. The TFIDFVectorizer can 
   remove these for you if you provide it a list. Change the code to also use the stopword list from the Terrier package (found [here](https://github.com/kavgan/stop-words/blob/master/terrier-stop.txt)); remove all of these words from the dataset before classifying.
   Compare the performance with and without removing stopwords.
   

(25 points) Part 3: Hidden Markov Models with Pomegranate. In this problem, you'll be using the [Pomegranate](https://pomegranate.readthedocs.io/en/latest/) package to build
a simple Hidden Markov Model. As with question 2, this is more about setting up the problem and using the software than it is about writing a ton of code.

You;ll want to use [this tutorial](https://github.com/jmschrei/pomegranate/blob/master/tutorials/B_Model_Tutorial_3_Hidden_Markov_Models.ipynb
) as an example:

For this problem, let's assume that we want to build an agent that can predict the season, based on whether it's sunny or rainy. We'll keep this pretty small; the goal is just to give you some practice with HMMs.

To begin, create two DiscreteDistributions: summerDist and winterDist. In summer, it's sunny 90% of the time and rainy 10% of the time.
In winter, it's sunny 50% of the time and rainy 50% of the time.

Next, create two States, summer and winter, using the appropriate distributions.

Next, create a HiddenMarkovModel and add your two states.

Now we need to add transitions. Assume that 90% of the time we stay in the same season and 10% of the time we change seasons. Add these transitions
to your HMM and bake it.

Now you're ready to make a prediction. Create a list of the form ['sun','rain','sun','sun'] and call model.predict(). It should print out the most likely 
set of states that generated these observations.

Last, let's make a small program to generate test cases. Build yourself a test program that can:
- generate a list of random States
- call state.distribution.sample to get observations for those states
- use that as input to your HMM to predict the actual states from the observation
- count the percentage of properly predicted states

Try this for sequences of 10, 20, 50 and 100 observations. Create a table that shows the percentage of states correctly predicted for each sequence.

(20 points) Part 4. Markov Decision Processes. 
   For this problem, you will implement the value iteration and policy iteration algorithms. 

I've provided a representation for states, a map, and the setup for two problems - the one shown in R&N (and done in class), and a larger problem, the map of which can be found in the file p2.jpg. In this second problem, the agent moves in the intended direction with P=0.7, and in each of the other 3 directions with P=0.1.

Your task is to implement the value iteration and policy iteration algorithms and verify that they work with both problems. (I'd suggest doing the R&N problem first.)


Here's an example of what the code looks like running in the Python interpreter with gamma=0.8, r=-0.04 and error=0.0001:

```
>>> import mdp
>>> m = mdp.Map()
>>> m.getMapFromFile("rnGraph")
>>> m.valueIteration()
>>> [(s.coords, s.utility, s.policy) for s in m.states.values()]
>>> [(s.coords, s.utility, s.policy) for s in m.states.values()]
[('11', -1.0, None), ('10', 1.0, None), ('1', 0.36897400368491667, 'right'), ('3', 0.73239206253199807, 'right'), ('2', 0.55800509251153152, 'right'), ('5', 0.42253248924235004, 'up'), ('4', 0.28095459542448692, 'up'), ('7', 0.2270923185711371, 'right'), ('6', 0.21512107599383087, 'up'), ('9', 0.12044027474165538, 'left'), ('8', 0.29822340058012747, 'up')]
```

(20 points) Part 5. (686 students only) Please read [this article](https://www.theatlantic.com/magazine/archive/2013/11/the-man-who-would-teach-machines-to-think/309529/)
about Douglas Hofstadter, which also serves as a nice summary of the history of AI and the debates over 
the value of developing machines that think like humans. (As an aside: If you have not read Hofastadter's book [Godel, Escher, Bach](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach), I strongly recommend it.)

Prepare a summary or critique of this article that addresses the following questions:

- Hofstadter is particularly interested in understanding the way humans think. What sorts of reasoning mechanisms does he study?
- The article includes a quote from our text: “The quest for ‘artificial flight’ succeeded when the Wright brothers and others stopped imitating birds and started … learning about aerodynamics,” What does this mean? Why is it relevant to AI?
- What was Candide? Why did it change the way we thought about machine translation? 
- The article also contains a quote from the last chapter of AIMA: perhaps AI has become too much like the man who tries to get to the moon by climbing a tree: “One can report steady progress, all the way to the top of the tree.” What does this mean? How does it 
  relate to Candide and the ways in which big data and machine learning have changed AI?
