# Spotify-5

This repo is the model creator for a spotify recommender. In the first iterations, the recommender is based on [KNearestNeighbor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier).

In order to create the model you need to:

1. Clone this repo
   - `git clone git@github.com:spotify-recommender/model.git`
2. Provide conforming spotify data
   - Data should be placed in the `spotify/data` folder and saved as `tracks_features.csv`
3. Run the create_baseline.py code
   - Enter spotify directory
   - `python create_baseline.py`


To use the baseline model, it is recommended that you save and move the baseline model into your own project. Then you can load the model using pickle like this:
```
knn = pickle.load(open("./baseline", "rb"))
knn.predict(X=[[0.121, 0.23]])
```

