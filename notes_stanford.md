## nearest neighbour

L1:

d1(I_1,I_2) = sum_p(I_1 - I_2)

L2:

d2(I_1,I_2) = sqrt(sum_p(I_1^P - I_2^2))

achieve about 35% accuracy (as opposed to modern deep learning methods and humans that are about 95%)

## K nearest neighbour 

similar approach to nearest neighbour but take 5 closest neighbours and have them "vote" (?) on what the most likely outcome is



## hyper parameter tuning

use a small subsection of your data in order to tune hyper parameters (in the case of KNN, the k value.) 

cross validation(?)

## questions

how does KNN work? 

answer : https://www.kaggle.com/code/just4jcgeorge/k-nearest-neighbour-algorithm 
summary: take a group of the closest neighbours and see how many are from each class. if there are more from e.g blue, chances are the dot falls under blue rather than red. 

where are the "problems" for the standford course? i.e where do we train networks/run code etc?

How does cross validation work? how do the "folds" work (i.e 5 fold, 10 fold)