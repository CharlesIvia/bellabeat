# IMPORT REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn theme
# sns.set_style("darkgrid")
sns.set_palette("hls")

# READ-IN DATA

# Activity data
activity_df = pd.read_csv("./data/dailyActivity_merged.csv")
print(activity_df.info())
print(activity_df.columns)
print(f"Activity Dataframe \n {activity_df}")


# PROCESS DATA

# Convert the ActivityDate column into  a datetime
activity_df["ActivityDate"] = pd.to_datetime(activity_df["ActivityDate"])
print(activity_df.info())

# Check for null values

print(activity_df.isnull().sum())

# From the output, the activity dataframe does not have null values.

# Next, check for duplicated rows

print(activity_df.duplicated().sum())

# The activity dataframe does not have duplicated rows.

# Next, get summary of the data

print(activity_df.describe())

# Key stats from the summary

# Average number of steps is 7637.91steps, with a maximum of 36019.00
# Average distance by an individual is 5.49km with a min of 0 and a maximum of 28.03

# Average amount of calories burned is 2303.61 with a minimum of 0 and a maximum of 4900.00

# ANALYZE DATA

# Establish the relationship between Total Steps and Calories burned

# First, get the correlation

total_steps_calories_corr = activity_df["TotalSteps"].corr(activity_df["Calories"])
print(total_steps_calories_corr)

# pearson correlation is 0.5916
# This shows that there is a large positive correlation between total steps taken and calories burned.

# Plot data in a scatterplot
plt.figure(figsize=(10, 4.94), dpi=100)
plt.title("Calories Burned vs Total Steps", pad=20, loc="left")
sns.scatterplot(data=activity_df, x="TotalSteps", y="Calories")
plt.show()

# Total Steps and Calories exhibit a linear relationship as shown above.
