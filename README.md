# COVID-19-TweetIDs

The repository contains an ongoing collection of tweets IDs associated with the novel coronavirus COVID-19 (SARS-CoV-2), which commenced on January 28, 2020. We used the Twitter’s search API to gather historical Tweets from the preceding 7 days, leading to the first Tweets in our dataset dating back to January 22, 2020. We leveraged Twitter’s streaming API to follow specified accounts and also collect in real-time tweets that mention specific keywords. To comply with Twitter’s [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy), we are only publicly releasing the Tweet IDs of the collected Tweets. The data is released for non-commercial research use. 

The associated paper to this repository can be found here: [#COVID-19: The First Public Coronavirus Twitter Dataset](https://arxiv.org/abs/2003.07372)

## Data Organization
The Tweet-IDs are organized as follows:
* Tweet-ID files are stored in folders that indicate the year and month of the collection (YEAR-MONTH). 
* Individual Tweet-ID files contain a collection of Tweet IDs, and the file names all follow the same structure, with a prefix “coronavirus-tweet-id-” followed by the YEAR-MONTH-DATE-HOUR. 
* Note that Twitter returns Tweets in UTC, and thus all Tweet ID folders and file names are all in UTC as well. 

## Notes About the Data
A few notes about this data: 
* We are still working on processing the over 50 million Tweets that we have collected, and will be incrementally releasing all of the past Tweet IDs as the files finish processing and releasing newer Tweet IDs as the data becomes available to us.
* There may be a few hours of missing data due to technical difficulties. We have done our best to recover as many Tweets from those time frames by using Twitter’s search API. 
* We will keep a running summary of basic statistics as we upload data in each new release. 
* The file keywords.txt and accounts.txt contains the updated keywords and accounts respectively that we tracked in our data collection. Each keyword and account will be followed by the date we began tracking them. 
* Consider using tools such as the [Hydrator](https://github.com/DocNow/hydrator) and [Twarc](https://github.com/DocNow/twarc) to rehydrate the Tweet IDs. Instructions for both are in the next section. 

## How to Hydrate

### Hydrating using [Hydrator](https://github.com/DocNow/hydrator) (GUI)
Navigate to the [Hydrator github repository](https://github.com/DocNow/hydrator) and follow the instructions for installation in their README. As there are a lot of separate Tweet ID files in this repository, it might be advisable to first merge files from timeframes of interest into a larger file before hydrating the Tweets through the GUI. 

### Hydrating using [Twarc](https://github.com/DocNow/twarc) (CLI)
Many thanks to Ed Summers ([edsu](https://github.com/edsu)) for writing this script that uses [Twarc](https://github.com/DocNow/twarc) to hydrate all Tweet-IDs stored in their corresponding folders. 

First install Twarc
```
pip3 install twarc
```

Configure Twarc with your Twitter API tokens (note you must [apply](https://developer.twitter.com/en/apply-for-access) for a Twitter developer account first in order to obtain the needed tokens)
```
twarc configure
```

Run the script. The hydrated Tweets will be stored in the same folder as the Tweet-ID file, and is saved as a compressed jsonl file
```
python3 hydrate.py
```

# Data Usage Agreement
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)). By using this dataset, you agree to abide by the stipulations in the license, remain in compliance with Twitter’s [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy), and cite the following manuscript: 

Emily Chen, Kristina Lerman, and Emilio Ferrara. 2020. #COVID-19: The First Public Coronavirus Twitter Dataset.  arXiv:cs.SI/2003.07372, 2020

# Statistics Summary (v1.0)
Number of Tweets : **8,919,411**

Language Breakdown 
| Language        | ISO     | No. tweets     | % total Tweets |
|-------------    |-----    |------------    |----------------    |
| English         | en      | 5,508,304      | 61.76%             |
| Spanish         | es      | 1,167,172      | 13.09%             |
| French          | fr      | 388,481        | 4.36%              |
| Thai            | th      | 352,902        | 3.96%              |
| Italian         | it      | 219,572        | 2.46%              |
| (undefined)     | und     | 208,908        | 2.34%              |
| Indonesian      | in      | 201,821        | 2.26%              |
| Portuguese      | pt      | 169,599        | 1.9%               |
| Japanese        | ja      | 145,985        | 1.64%              |
| Turkish         | tr      | 134,173        | 1.5%               |

# Inquiries
If you have technical questions about the data collection, please contact Emily Chen at **echen920[at]usc[dot]edu**.

If you have any further questions about this dataset please contact Dr. Emilio Ferrara at **emiliofe[at]usc[dot]edu**.
