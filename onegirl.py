# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:10:00 2015

@author: breiche

One Girl Child

In the far future, the Queen of Earth is worried about falling birth rates and 
the continuation of humanity. 
She decrees that every couple has at least one female child or face a fine.

-What will the male:female ratio look like after one generation?

-How many generations (if ever) will it take for humans to become extinct?
"""

import random
import math

def CalculateChildbearingCouples(num_males, num_females, \
                                male_reluctance, female_reluctance):
    '''
    calculates the number of childbearing couples, given
    a number of men and a number of women.
    
    Assumes a random percentage of males and females (maximum specified by 
    male_reluctance and female_reluctance) do not want or 
    cannot have children, or are #foreveralone.
    '''
    min_willing_females = math.floor(num_females * (1 - female_reluctance))
    min_willing_males = math.floor(num_males * (1 - male_reluctance))
    
    willing_females = random.randrange(min_willing_females, num_females)
    willing_males = random.randrange(min_willing_males, num_males)
        
    return min(willing_females, willing_males)

def ProduceAnotherGeneration(num_couples):
    '''
    Given the number of childbearing *couples*,
    Returns the number of (female, male) children that these couples produce.
    
    -Assumes 50/50 chance of having a male and female baby
    -Assumes each couple keeps trying until they have a girl.
    -Assumes a hard limit of 10 pregnancies per couple. Jeez.
    '''
    male_babies = 0
    female_babies = 0
    for couple in range(num_couples):
        for pregnancy in range(10):
            its_a_girl = random.choice([True, False])
            if its_a_girl:
                female_babies += 1
                break
            if its_a_girl == False:
                male_babies += 1
                
    return (female_babies, male_babies)
    
    
def RunSimulation():
    '''
    Called by main(). Runs the simulation.
    '''
    num_males = 100
    num_females= 100
    male_reluctance = 0.05
    female_reluctance = 0.05
    
    g = 0
    while True:
        print "Generation", str(g), "has", num_females, "females and", \
            num_males, "males."
            
        num_couples = CalculateChildbearingCouples(num_males, num_females,\
                                                male_reluctance, female_reluctance)
        print "Generation", str(g), "forms", num_couples, "couples."
        
        (female_children, male_children) = ProduceAnotherGeneration(num_couples)        
        print "Generation", str(g), "produces", female_children, "female children and", \
            male_children, "male children."
            
        num_males = male_children
        num_females = female_children
        
        if num_females == 0 or num_males == 0:
            print "Humanity has died after", str(g), "generations."
            return
        
        g += 1
            
    
if __name__ == '__main__':
    RunSimulation()
    