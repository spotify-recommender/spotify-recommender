import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os


def create_baseline_model(filename):
    df = pd.read_csv(filename)

    df = df[["id", "danceability", "liveness"]]

    X = df[["danceability", "liveness"]].to_numpy()
    y = df[["id"]].values.ravel()

    # """Using NearestNeighbors, which does not accept any labels"""
    # nn = NearestNeighbors()
    # nn.fit(X)

    # testdata = np.reshape((0.321, 0.23), (1, 2))
    # _, neigh_ind = nn.kneighbors(testdata, n_neighbors=11)

    """Using KNeighborsClassifier, fit with labels"""
    knn = KNeighborsClassifier(n_neighbors=11)
    knn.fit(X, y)
    # example
    # knn_ind = knn.kneighbors([[0.121, 0.23]], return_distance=False)
    return knn
    # pickle.dump(knn, open(os.path.join("./baseline"), "wb"))


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "data/tracks_features.csv")
    baseline = create_baseline_model(filename)
    pickle.dump(baseline, open(os.path.join(dirname, "models/baseline"), "wb"))
    print(f"Success, model saved to {os.path.join(dirname, 'models/baseline')}")
else:
    baseline = create_baseline_model("./data/tracks_features.csv")
    pickle.dump(baseline, open(os.path.join("./models/baseline"), "wb"))
    print(f"Success, model saved to {os.path.join('./models/baseline')}")
