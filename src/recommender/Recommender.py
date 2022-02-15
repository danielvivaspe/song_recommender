import numpy as np
import pandas

class Recommender():
    def __init__(self, train_data):
        self.user_id = 'userID'
        self.item_id = 'songID'
        self.train_data = train_data
        self.cooccurence_matrix = None

    # Get unique songs corresponding to a given user
    def get_user_items(self, user):
        user_data = self.train_data[self.train_data[self.user_id] == user]
        user_items = list(user_data[self.item_id].unique())

        return user_items

    # Get unique users for a given song
    def get_item_users(self, item):
        item_data = self.train_data[self.train_data[self.item_id] == item]
        item_users = set(item_data[self.user_id].unique())

        return item_users

    # Get unique songs in the training data
    def get_all_items_train_data(self):
        all_items = list(self.train_data[self.item_id].unique())

        return all_items

    # Construct cooccurence matrix
    def construct_cooccurence_matrix(self, user_songs, all_songs):

        # 1 - Get users who have listened to the same songs the current user have listened to
        user_songs_users = []
        for i in range(0, len(user_songs)):
            user_songs_users.append(self.get_item_users(user_songs[i]))

        # 2 - Create song cooccurence matrix with size nº songs listened by the user and nº users
        cooccurence_matrix = np.matrix(np.zeros(shape=(len(user_songs), len(all_songs))), float)

        # 3 - Calculate similarity between user songs and all unique songs in training data
        for i in range(0, len(all_songs)):

            # Calculate unique users listeners of song i
            songs_i_data = self.train_data[self.train_data[self.item_id] == all_songs[i]]
            users_i = set(songs_i_data[self.user_id].unique())

            for j in range(0, len(user_songs)):

                # Get unique listeners (users) of song (item) j
                users_j = user_songs_users[j]

                # Calculate intersection of listeners of songs i and j
                users_intersection = users_i.intersection(users_j)

                # Calculate cooccurence_matrix[i,j] as Jaccard Index
                if len(users_intersection) != 0:
                    # Calculate union of listeners of songs i and j
                    users_union = users_i.union(users_j)

                    cooccurence_matrix[j, i] = float(len(users_intersection)) / float(len(users_union))
                else:
                    cooccurence_matrix[j, i] = 0

        return cooccurence_matrix

    # Use the cooccurence matrix to make top recommendations
    def generate_top_recommendations(self, user, cooccurence_matrix, all_songs, user_songs, n_recs):
        print("Non zero values in cooccurence_matrix :%d" % np.count_nonzero(cooccurence_matrix))

        # 1 - Calculate a weighted average of the scores in cooccurence matrix for all user songs
        user_sim_scores = cooccurence_matrix.sum(axis=0) / float(cooccurence_matrix.shape[0])
        user_sim_scores = np.array(user_sim_scores)[0].tolist()

        # 2 - Sort the indices of user_sim_scores based upon their value
        #     Also maintain the corresponding score
        sort_index = sorted(((e, i) for i, e in enumerate(list(user_sim_scores))), reverse=True)

        # 3 - Create a dataframe from the following
        columns = ['user_id', 'song', 'score', 'rank']
        df = pandas.DataFrame(columns=columns)

        # 4 - Fill the dataframe with top song recommendations
        rank = 1
        for i in range(0, len(sort_index)):
            if ~np.isnan(sort_index[i][0]) and all_songs[sort_index[i][1]] not in user_songs and rank <= n_recs:
                df.loc[len(df)] = [user, all_songs[sort_index[i][1]], sort_index[i][0], rank]
                rank = rank + 1

        # 4.1 - Handle the case where there are no recommendations
        if df.shape[0] == 0:
            print("The current user has no songs for training the item similarity based recommendation model.")
            return -1
        else:
            return df

    # Make recommendations
    def recommend(self, user):

        # 1- Get all unique songs for this user
        user_songs = self.get_user_items(user)

        # 2- Get all unique songs in training data
        all_songs = self.get_all_items_train_data()

        # 3-  Create song cooccurence matrix with size nº songs and nº users
        cooccurence_matrix = self.construct_cooccurence_matrix(user_songs, all_songs)

        # 4- Use the cooccurence matrix to make recommendations
        df_recommendations = self.generate_top_recommendations(user, cooccurence_matrix, all_songs, user_songs, n_recs=10)

        return df_recommendations

    # Get similar items to given items
    def get_similar_items(self, item_list):

        user_songs = item_list

        # 1 -  Get all unique songs in training data
        all_songs = self.get_all_items_train_data()

        # 2 - Create song cooccurence matrix with size nº songs listened by the user and nº songs
        cooccurence_matrix = self.construct_cooccurence_matrix(user_songs, all_songs)

        # 3 -  Use the cooccurence matrix to make recommendations
        user = ""
        df_recommendations = self.generate_top_recommendations(user, cooccurence_matrix, all_songs, user_songs, n_recs=10)

        return df_recommendations