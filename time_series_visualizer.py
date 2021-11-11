import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")
df.index = pd.to_datetime(df.index)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18, 6))
    ax = plt.axes()
    ax.plot(df.index, df["value"], color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    #return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar["month"] = pd.Categorical(df_bar.index.strftime("%B"), categories=months, ordered=True)
    
    # Draw bar plot
    df_bar = pd.pivot_table(df_bar,	values="value",	index="year",	columns="month", aggfunc=np.mean)
    
    #print(df_bar)

    fig = plt.figure(figsize=(9, 7))
    ax = plt.axes()
    df_bar.plot(kind = "bar", ax=ax)
    fig = ax.get_figure()

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
     
    # Draw box plots (using Seaborn)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box["month"] = pd.Categorical(df_box["month"], categories=months, ordered=True)

    #print(df_box)

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    sns.boxplot(x="year", y="value", data=df_box, ax = ax1)
    sns.boxplot(x="month", y="value", data=df_box, ax = ax2)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax2.set_title("Month-wise Box Plot (Seasonality)") 
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

#draw_box_plot()