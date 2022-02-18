import random

import pandas as pd
from surprise import Dataset, Reader, SVDpp, KNNBasic
from surprise.model_selection import train_test_split
import pickle


class DVrecommender:
    model = None
    triplets_df = None
    surprise_ds = None
    train = None
    test = None
    scale = 1

    def __init__(
            self,
            triplets_path='../data/raw/TasteProfile/train_triplets.txt',
            n_rows=100000,
            max_play_scaling=None
    ):
        self.triplets_path = triplets_path
        self.n_rows = n_rows
        self.max_play_scaling = max_play_scaling

        self.triplets_df = pd.read_csv(self.triplets_path, sep='\t', names=['user', 'item', 'rating'], nrows=n_rows)

        if max_play_scaling is not None:
            # Escala entre max_play_scaling
            self.scale = max(self.triplets_df['rating']) / self.max_play_scaling
            self.triplets_df['rating'] = self.triplets_df['rating'].apply(lambda x: x / self.scale)

        max_ratings = max(self.triplets_df['rating'])
        min_ratings = min(self.triplets_df['rating'])

        reader = Reader(rating_scale=(min_ratings, max_ratings))
        self.surprise_ds = Dataset.load_from_df(self.triplets_df, reader)

    def init_model(self, test=False):
        """
        Makes a new model from scratch
        :param test: if True it will generate a test. if False, it will train with the whole dataset
        """
        if test:
            self.train, self.test = train_test_split(self.surprise_ds, test_size=0.25, random_state=42)
        else:
            self.train = self.surprise_ds.build_full_trainset()

        #svd = SVDpp()
        sim_options = {'name': 'cosine', 'user_based': False}
        svd = KNNBasic(k=20, min_k=2, sim_options=sim_options)
        svd.fit(self.train).compute_similarities()
        self.model = svd

    def dump_model(self, pickle_path='', pickle_name='model.pickle'):
        pickle_file = open(pickle_path + pickle_name, 'wb')
        pickle.dump(self.model, pickle_file)
        pickle_file.close()

    def load_model(self, pickle_path='', pickle_name='model.pickle'):
        file = open(pickle_path + pickle_name, 'rb')
        self.model = pickle.load(file)

    def get_estimation(self, userId, songID):
        return round(self.model.predict(userId, songID)[3] * self.scale)

    def get_top_recommendations(self, userID, n_recs):
        recs = pd.DataFrame(columns=['songID', 'r_ui', 'est', 'details'])
        songs = self.triplets_df[self.triplets_df['user'] != userID]['item'].unique()

        for i in range(len(songs)):
            prediction = self.model.predict(userID, songs[i])

            recs = recs.append({'songID': prediction[1], 'r_ui': prediction[2], 'est': round(prediction[3] * self.scale), 'details': prediction[4]},
                               ignore_index=True)

            if i == n_recs:
                break

        return recs.sort_values('est', ascending=False)

    def unique_songs(self):
        return self.triplets_df['item'].unique()

    def unique_users(self):
        return self.triplets_df['user'].unique()

    def test_model(self):
        return self.model.test(self.test)

    def max_rating(self):
        return max(self.triplets_df['rating'])

    def min_rating(self):
        return min(self.triplets_df['rating'])




def test():
    test = DVrecommender()
    test.load_model(pickle_name='model_small.pickle')
    preds = test.get_top_recommendations('b80344d063b5ccb3212f76538f3d9e43d87dca9e', 5)
    preds


