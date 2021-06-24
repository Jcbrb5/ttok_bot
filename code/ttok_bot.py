'''
RUN THIS SCRIPT TO TEST OUT OUR PROJECT
'''

import bool_to_bin
import calculate_engagement_metric
import vectorize_text
import vectorize_hashtags
import clean_hashtags
import remove_cols
import nn_v2
from Naked.toolshed.shell import execute_js

if __name__ == '__main__':
    success = execute_js('./tiktok_scrape.js') # Run TikTok scraping script
    if success:
        remove_cols.remove_cols() # Remove unnecessary columns from data
        clean_hashtags.clean_hashtags() # Remove unnecessary data from hashtags
        vectorize_hashtags.vectorize_hashtags() # Vectorize hashtags
        vectorize_text.vectorize_other_text() # Vectorize the rest of the textual data
        calculate_engagement_metric.calculate_engagement_metric() # Calculate the engagement metric for each video
        bool_to_bin.bool_to_bin() # Convert boolean values to 1 or 0 (1 = true , 0 = false)
        nn_v2.run_neural_net() # Build, train, & test the neural network

    else:
        print('Unexpected Error: Failed to run tiktok_scraper.') # If the TikTok scraper does not successfully run print this error