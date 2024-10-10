#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import YouTubeVideo
# First pre-lecture video: 
# "Hypothesis testing. Null vs alternative
# https://www.youtube.com/watch?v=ZzeXCKd5a18
YouTubeVideo('ZzeXCKd5a18', width=800, height=500)


# In[ ]:


from IPython.display import YouTubeVideo
# Second pre-lecture video
# "What is a p-value"
# https://www.youtube.com/watch?v=9jW9G8MO4PQ
YouTubeVideo('9jW9G8MO4PQ', width=800, height=500)


# Hypothesis is an idea and it can be tested. The hypothesis has Null Hypothesis and Alternative Hypothesis.
# We use P value to measure the consistency between experimental data and Null Hypothesis. The larger P value is, the more consistent it is. The smaller the P value, the more inconsistent it is. P value ranges from (0,1)

# Whether the idea can be quantified is a good way to judge whether it is a hypothesis, which requires specific numbers or other data. A good Null Hypothesis should be objective and testable. The null hypothesis usually states that there are no differences or effects, but the alternative hypothesis states that there are differences and effects.

# The mean of x is the mean of the sample, but μ (mu) is the mean of the population.
# When there is 0 in the lower right corner of μ, it is the population average in the null hypothesis.

# If P value is small, it means that it is very different from the Null Hypothesis, so it is absurd.

# The smaller the P value, the greater the difference from the null hypothesis, which means that we have a large degree of doubt that the null hypothesis is wrong, but we cannot be 110% sure that the null hypothesis is wrong. P value can not prove Fido's guilt or innocence, as mentioned above, we can only think Fido's guilt or innocence to a large extent, can not 100% prove Fido's guilt or innocence.

# In[1]:


import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Parameters for the binomial test
n_students = 80  # Total number of students
observed_correct = 49  # Number of correct guesses
p_guess = 0.5  # Probability of guessing correctly under the null hypothesis
num_simulations = 10000  # Number of simulations to perform

# Simulate binomial outcomes under H0 (random guessing)
simulated_correct_guesses = np.random.binomial(n_students, p_guess, size=num_simulations)

# Calculate the p-value: proportion of simulations where the number of correct guesses is >= observed_correct
p_value = np.mean(simulated_correct_guesses >= observed_correct)

# Output the p-value
p_value


# Problem Introduction
# This report analyzes a tea-tasting experiment inspired by the famous hypothesis test devised by Ronald Fisher in the 1920s. In this modern scenario, we sampled 80 students from STA130, each of whom tasted a cup of tea and stated whether they thought the milk or tea was poured first. Out of the 80 students, 49 correctly identified which was poured first. The goal of this analysis is to determine whether the students' ability to identify the order was due to random guessing or if there is evidence that they could reliably detect the difference.
# 
# Relationship between this Experiment and Fisher’s Experiment
# The inspiration for this test comes from Fisher’s experiment involving his colleague, Dr. Muriel Bristol, who claimed she could distinguish whether tea or milk was poured first in her cup. Fisher devised a hypothesis test to challenge this claim, designing an experiment in which 8 cups of tea were prepared, with 4 cups having tea poured first and the other 4 having milk poured first. Dr. Bristol correctly identified the order for all 8 cups, and Fisher conducted a statistical test to determine whether this result was due to chance.
# 
# Similarly, in this STA130 experiment, we investigate whether the students were guessing randomly or if they had a significant ability to distinguish the order of pouring. Both experiments aim to test a claim of sensory discrimination against the null hypothesis of random guessing.
# 
# Statements of the Null Hypothesis and Alternative Hypothesis
# Null Hypothesis (
# H
# 0
# H 
# 0
# ​	
#  ): The students are randomly guessing whether the tea or milk was poured first, with a 50% chance of guessing correctly.
# Alternative Hypothesis (
# H
# A
# H 
# A
# ​	
#  ): The students are not randomly guessing and are able to correctly identify the order of pouring more than would be expected by chance.
# Quantitative Analysis
# In the experiment, 49 out of 80 students correctly identified whether the milk or tea was poured first. Under the null hypothesis, we assume that each student has a 50% chance of guessing correctly, and we want to assess the likelihood of observing 49 or more correct guesses purely by chance.
# 
# To quantify this, we performed a simulation using a binomial model, where 80 trials were conducted with a 50% probability of success (correct guess) in each trial. We simulated 10,000 such trials to estimate the probability of obtaining 49 or more

# https://chatgpt.com/share/6707403f-dd14-8000-8746-7ae1efde3cab

# In[ ]:




