import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('vacination_tweets.csv')
df.head(1)

#basic numerical analysis on all columns in the df
print(df.describe())

#make histograms for all relevant numerical variables listed in eda dict
plt.rc('xtick', labelsize=8) 
plt.rc('ytick', labelsize=8)


fig, ax = plt.subplots(2, 3, figsize=(15, 8))

ax[0,0].plot(df['user_followers'])
ax[0,0].set_title("Number of followers of a user", fontsize=8)

ax[0,1].plot(df['user_friends'])
ax[0,1].set_title("Number of friends of a user", fontsize=8)

ax[0,2].plot(df['user_favourites'])
ax[0,2].set_title("Number of favorites for a tweet", fontsize=8)

ax[1,0].plot(pd.to_datetime(df["date"]) )
ax[1,0].set_title("Date of tweet", fontsize=8)

ax[1,1].plot(df['retweets'])
ax[1,1].set_title("Number of retweets", fontsize=8)

ax[1,2].plot(df['favorites'])
ax[1,2].set_title("Number of retweets", fontsize=8)


plt.savefig("fig1.jpeg")
plt.show()


