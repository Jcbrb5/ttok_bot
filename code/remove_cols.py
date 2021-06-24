import pandas as pd
import numpy as np

def remove_cols():
        df = pd.read_csv('../out.csv') # Import the data from a csv
        # Remove unneeded columns from the dataframe
        df.drop(['id', 'secretID', 'authorMeta.id', 'authorMeta.secUid', 'authorMeta.name',
                'authorMeta.nickName', 'authorMeta.verified', 'authorMeta.signature',
                'authorMeta.avatar', 'authorMeta.following', 'authorMeta.fans',
                'authorMeta.heart', 'authorMeta.video', 'authorMeta.digg', 'musicMeta.musicId',
                'musicMeta.playUrl', 'musicMeta.coverThumb', 'musicMeta.coverMedium',
                'musicMeta.coverLarge', 'covers.default', 'covers.origin', 'covers.dynamic',
                'webVideoUrl', 'videoUrl', 'videoUrlNoWaterMark', 'videoApiUrlNoWaterMark',
                'videoMeta.height', 'videoMeta.width', 'downloaded', 'effectStickers'], inplace=True, axis=1)
        df.to_csv('../data_with_less_cols.csv', index=False) # Save the data to a csv