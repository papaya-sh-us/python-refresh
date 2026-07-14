def add_bonus(score):
    score = score + 10
    return score
score = 50
new_score = add_bonus(score)
print(score)        #should be 50, because it is outside the scope of the function
print(new_score)    #should print 60