import pandas as pd                  # I'm importing pandas so I can work with tables (DataFrame)
import matplotlib.pyplot as plt      # I need matplotlib to make charts and visualize data

# 1. Load the data from my CSV file into a pandas DataFrame
df = pd.read_csv(r"C:\Users\HassanKassar\Downloads\KASSAR Hassan - bank_loans.csv")  # reading the file I downloaded

# 2. Peek at the data to understand what I'm working with
print("First 5 rows:")               # letting me see a sample of the top rows
print(df.head())                     # show first five rows so I know the column names and some values
print("\nData Info:")                # label for the info section
print(df.info())                     # shows me data types and how many values in each column

# 3. Clean up the column names because I want to type them easily later
df.columns = (
    df.columns
      .str.strip()                   # remove unwanted spaces around names
      .str.lower()                   # convert everything to lowercase so it's consistent
      .str.replace(' ', '_')         # replace spaces with underscores for valid Python names
)

# 4. Remove columns with too many missing values so they won't mess up my analysis
half_count = len(df) * 0.5           # compute what half the number of rows is
# drop columns that don't have at least half of the rows filled
df = df.dropna(axis=1, thresh=half_count)

# 5. Get some quick stats on the remaining numeric columns to see ranges and averages
print("\nSummary stats:")            # label for summary statistics
print(df.describe())                 # gives me count, mean, std, min, max, quartiles

# 6. Create FIVE charts to visualize key parts of the data

# Chart 1: How loan amounts are distributed across all loans
plt.figure()                         # start a new figure to keep things separate
df['loan_amount'].hist(bins=20)      # histogram with 20 bins to show frequency spread
plt.title('Distribution of Loan Amount')  # gives context to what I'm plotting
plt.xlabel('Loan Amount')            # x-axis label so reader knows units
plt.ylabel('Frequency')              # y-axis label for counts
plt.show()                           # display the plot on screen

# Chart 2: Count of loans for each grade to see which grades are most common
plt.figure()
df['grade'].value_counts().sort_index().plot(kind='bar')  # count each grade and draw a bar chart
plt.title('Number of Loans by Grade')
plt.xlabel('Grade')
plt.ylabel('Count')
plt.show()

# Chart 3: Boxplot of loan amounts grouped by grade to compare distributions
plt.figure()
df.boxplot(column='loan_amount', by='grade')  # boxplot gives median, quartiles, and outliers info
plt.title('Loan Amount by Grade')
plt.suptitle('')                     # remove default subtitle since pandas adds one by default
plt.xlabel('Grade')
plt.ylabel('Loan Amount')
plt.show()

# Chart 4: Scatter plot to check if larger loans have different interest rates
plt.figure()
plt.scatter(df['loan_amount'], df['interest_rate'])  # x-axis is loan_amount, y-axis is interest_rate
plt.title('Interest Rate vs Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Interest Rate (%)')
plt.show()

# Chart 5: Correlation matrix to find out which numeric columns move together
plt.figure(figsize=(6,6))            # making it a bit larger to read labels
numeric = df.select_dtypes(include='number')  # only pick numeric columns for correlation
corr = numeric.corr()                # compute correlation coefficients
plt.matshow(corr, fignum=1)          # draw the correlation matrix as colored squares
plt.xticks(range(len(corr)), corr.columns, rotation=90)  # label x-axis with column names
plt.yticks(range(len(corr)), corr.columns)              # label y-axis
plt.colorbar()                       # add the color legend so we know what values mean
plt.title('Correlation Matrix', y=1.15)  # title above the plot
plt.show()

# 7. Write down some simple insights I found from the data and visuals
print("\nInsights:")
print("- I see most loans are on the smaller side from the histogram.")
print("- Grades B, C, and D have the highest number of loans from the bar chart.")
print("- The boxplot shows that A- and B-grade loans have less spread in amounts.")
print("- The scatter plot doesn’t show a clear straight-line pattern between loan size and rate.")
print("- The correlation matrix confirms that funded_amount and investor_amount are very strongly correlated.")
