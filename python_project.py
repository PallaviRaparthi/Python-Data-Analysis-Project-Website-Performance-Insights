import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Website Performance Analysis dataset.xlsx" , sheet_name = "data-export")
print(df.columns)
print(df.head)

df.columns = ['Channel Group',
       'DateHour', 'Users', 'Sessions', 'Engaged sessions',
       'Avg Engagement Time', 'Engaged sessions per user',
       'Events per session', 'Engagement rate', 'Event count']
print(df['Events per session'].max())
df["Hour"] = df["DateHour"].astype(str).str[-2:].astype(int)

numeric_df = df.select_dtypes(include=[float, int])

#Calculating Mean of Users
users_mean = np.mean(df['Users'])
print(f"Mean number of users: {users_mean}")


#Calculating Stabdard Deviation 
users_std = np.std(df['Users'])
print(f"Standard deviation of Users: {users_std}")

#Calculate min, max, and range for the 'Event count'
event_count_min = np.min(df['Event count'])
event_count_max = np.max(df['Event count'])
event_count_range = np.ptp(df['Event count'])  
print(f"Event Count - Min: {event_count_min}, Max: {event_count_max}, Range: {event_count_range}")


# (1) pie chart --- top 10 Events per session and top 10 Event count

y = df["Events per session"].head(10)
y1 = df["Event count"].head(10)
color = ["lightgreen","g","pink","r","b","Teal" , "lightcoral" , "skyblue","yellow" , "orange"]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.pie(y1,labels = y , autopct = "%1.2f%%" , colors = color)
plt.savefig("Top 10 Event Count Distribution.png")

plt.show()



# (2) Scatterplot ---- Event Count vs Avg Engagement Time

plt.figure(figsize=(8, 6))
sns.scatterplot(data = df , x = "Event count", y = "Avg Engagement Time" , color = 'k')
plt.title("Event Count vs Avg Engagement Time")
plt.xlabel("Event Count")
plt.ylabel("Avg Engagement Time")
plt.tight_layout()
plt.savefig("event_vs_engagement.png")
plt.show()



# (3)bar plot  ----  the average number of Users per Channel


avg_users = df.groupby('Channel Group')['Users'].mean().sort_values(ascending = False)
colors = sns.color_palette("plasma", 10)
plt.figure(figsize = (8,10))
plt.bar(avg_users.index, avg_users.values,color = colors)
plt.xlabel("Channel" , fontsize = 100)
plt.ylabel("average number of Users")
plt.title("average number of Users per Channel")
plt.xticks(rotation=45)
plt.savefig("average number of Users per Channel.png")
plt.show()




# (4) line plot --- Sessions by Hour

plt.figure(figsize = (8,10))
hours = df.groupby('Hour')['Sessions'].mean()
sns.lineplot(x=hours.index,y=hours.values,color = "darkblue",marker="s",linewidth=4)
plt.title("Average Sessions by Hour")
plt.xlabel("Hours")
plt.ylabel("Average Sessions")
plt.xticks(range(0, 24))
plt.savefig("Sessions by Hour.png")
plt.show()



# (5)Box Plot ----- Engagement Time per Channel

plt.figure(figsize = (10,12))
sns.boxplot(x = "Channel Group" , y = "Avg Engagement Time" ,data = df , color = "brown")
plt.title("Average Engagement Time per Channel")
plt.xlabel("Channel Group")
plt.ylabel("Avg Engagement Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Engagement Time per Channel")
plt.show()



# (6)Histogram ---- Engagement Rate Distribution

plt.figure(figsize=(10,12))
sns.histplot(data=df , x = "Engagement rate",color = "r",bins=30,kde=True)
plt.title("Engagement Rate Distribution")
plt.xlabel("Engagement Rate")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Engagement Rate Distribution.png")
plt.show()


# (7) ViolinPlot --- Engaged Sessions per User across Channel Groups

plt.figure(figsize=(10,8))
sns.violinplot(x="Channel Group" ,y="Engaged sessions per user" ,hue="Channel Group", data=df,
               palette="pastel")
plt.title("Engaged Sessions per User across Channel Groups")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Engaged Sessions per User.png")
plt.show()


# (8) Heatmap --- Correlation Heatmap of Website Performance Data

correlation = numeric_df.corr()
plt.figure(figsize = (10,6))
sns.heatmap(correlation , annot = True ,fmt = '.2f' , cmap ="Blues",linewidth = 0.5 )
plt.title("Correlation Heatmap of Website Performance Data")
plt.savefig("heatmap.png")
plt.show()



# (9) Histogram --- Histogram of Avg Engagement Time

plt.figure(figsize=(16,6))
plt.subplot(1, 2, 1)
plt.hist(df['Sessions'], bins=20, color='green', edgecolor='black')
plt.title("Histogram of Avg Engagement Time")
plt.xlabel("Avg Engagement Time")
plt.ylabel("Frequency")
plt.savefig("Histogram of Avg Engagement Time.png")
plt.show()






