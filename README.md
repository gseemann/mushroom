# Mushroom Classification
## The Data
Uses data scraped from wikipedia. This provides data for name, hymeniumType, capShape, whichGills, stipeCharacter, sporePrintColor, ecologicalType, and genus.

## The goal
The goal of this project was to classify edible/inedible base off other mushroom features.


## Initial EDA 

### Distribution of features 
![Hymenium Type](graphs/hymeniumType.png)
![Cap Shape](graphs/capShape.png)
![Gill type](graphs/whichGills.png)
![Stipe Character](graphs/stipeCharacter.png)
![Spore Print Color](graphs/sporePrintColor.png)
![Ecological Type](graphs/ecologicalType.png)

### Distribution of target 
#### Edibility of mushroom
![Edibility](graphs/howEdible.png)


## Models Used
After initial EDA, I ran a decision tree, random forest, XGBoost, and  GridsearchCV models. Of all these, random forest gave the best prediction results.

