import pandas as pd
import os


def create_mapping(filename):
    df = pd.read_csv(filename)

    df = df["id"]

    return df


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "data/tracks_features.csv")
    mapping = create_mapping(filename)
    mapping.to_csv(os.path.join(dirname, "data/song_mapping.csv"), index=False)
    print(f"Success, mapping saved to {os.path.join(dirname, 'data/song_mapping.csv')}")
else:
    mapping = create_mapping("./data/tracks_features.csv")
    mapping.to_csv("./data/song_mapping.csv", index=False)
    print(f"Success, mapping saved to {os.path.join('./data/song_mapping.csv')}")
