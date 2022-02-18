import pandas as pd
from surprise import Reader, Dataset, SVDpp
from surprise.model_selection import train_test_split
import pickle

def train_model():
    print('Script started')

    triplets = pd.read_csv('../data/raw/TasteProfile/train_triplets.txt', sep='\t',
                           names=['userID', 'songID', 'playCount'])

    print('Triplets loaded')

    reader = Reader()
    data = Dataset.load_from_df(triplets, reader)

    print('Data converted')

    train, test = train_test_split(data, test_size=0.25, random_state=42)

    print('Train test division made')

    svd = SVDpp()
    svd.fit(train)

    print('Model trained')

    pickle_file = open('model.pickle', 'wb')
    pickle.dump(svd, pickle_file)
    pickle_file.close()
    
    print('Script finished')

def read_model():
    file = open('model.pickle', 'rb')
    model = pickle.load(file)
    print(model)


train_model()