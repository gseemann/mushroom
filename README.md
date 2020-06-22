# Mushroom Classification
## The Data
Uses data scraped from wikipedia. This provides data for name, hymeniumType, capShape, whichGills, stipeCharacter, sporePrintColor, ecologicalType, and genus.

## The goal
The goal of this project was to classify edible/inedible base off other mushroom features.


## Initial EDA 

### Distribution of features 
![Hymenium Type](graphs/hymeniumType_edibility_dist.png)
![Cap Shape](graphs/capShape_edibility_dist.png)
![Gill type](graphs/whichGills_edibility_dist.png)
![Stipe Character](graphs/stipeCharacter_edibility_dist.png)
![Spore Print Color](graphs/sporePrintColor_edibility_dist.png)
![Ecological Type](graphs/ecologicalType_edibility_dist.png)

### Distribution of target 
#### Edibility of mushroom
![Edibility](graphs/howEdible.png)


## Models Used
After initial EDA, I ran a decision tree, random forest, XGBoost, and  GridsearchCV models. Of all these, random forest gave the best prediction results.

