import os
import glob
import pandas as pd
import json
def get_all_ids(basedir='millionsongdataset_echonest\\',ext='.json') :
    df = pd.DataFrame(columns=['trackID', 'SpotifyID'])
    df.to_csv('spotifyIDs.csv')

    try:
        for root, dirs, files in os.walk(basedir):
            files = glob.glob(os.path.join(root,'*'+ext))
            print('Files:', len(files))
            for f in files:
                print('Starting file', f)
                with open(f, 'r') as current:
                    data = json.load(current)
                    if(len(data['response']['songs']) > 0):
                        for i in range(len(data['response']['songs'][0]['tracks'])):
                            id = data['response']['songs'][0]['id']
                            if('spotify' in data['response']['songs'][0]['tracks'][i]['foreign_id']):
                                df = df.append({'trackID': id, 'SpotifyID': data['response']['songs'][0]['tracks'][i]['foreign_id']}, ignore_index=True)
                                print('\tAdded', data['response']['songs'][0]['tracks'][i])
                print('Finished file', f)

            df.to_csv('spotifyIDs.csv', mode='a', header=False)
            df = pd.DataFrame(columns=df.columns)

    except Exception as e:
        print(e)
        return

    return df

get_all_ids()