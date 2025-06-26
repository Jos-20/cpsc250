import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Read data from file into Pandas dataframe
    df = pd.read_csv("testdata.csv")
    print(df)

    # Create a figure object
    fig, ax = plt.subplots()

    # Plot the data, with error bars, give the plot a title, and set the ylimit to zero.
    ax.errorbar(df['Temperature'],df['Pollen Count'],df['Error in Pollen Count'],df['Error in Temperature'],'o',color='blue', label='Pollen Count Data')
    ax.set_title("Basic Plotting Example")
    ax.set_ylim(0.0)
    ax.set_xlim(0.0)

    # Call the regression plotting method from Seaborn to fit the data with a second order
    # polynomial, show a 68% confidence interval error band
    sns.regplot(x='Temperature', y='Pollen Count', data=df, order=2, ci=68.0, ax=ax, label='Quadratic Fit')

    # draw a legend and show the plot
    plt.legend()
    plt.show()
