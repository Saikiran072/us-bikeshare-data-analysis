import time
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def handle_empty_df(df):
    """Checks if DataFrame is empty and prints a message."""
    if df.empty:
        print("No data available for the selected filters.")
        print("-" * 40)
        return True
    return False


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = (
            input("Enter city (Chicago, New York City, Washington): ").strip().lower()
        )
        if city in CITY_DATA:
            break
        print("Invalid city. Please try again.")

    # get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        month = input(
            "Enter month (all, january, february, march, april, may, june):"
        ).lower()
        if month in months:
            break
        print("Invalid month. Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = [
        "all",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    while True:
        day = (
            input(
                "Enter day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): "
            )
            .strip()
            .lower()
        )
        if day in days:
            break
        print("Invalid day. Please try again.")
    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data into dataframe

    df = pd.read_csv(CITY_DATA[city])

    # Convert start time to datetime

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract useful columns

    df["month"] = df["Start Time"].dt.month
    df["day_name"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    # filter by month

    if month != "all":
        month_index = ["january", "february", "march", "april", "may", "june"].index(
            month
        ) + 1
        df = df[df["month"] == month_index]

    # filter by day

    if day != "all":
        df = df[df["day_name"] == day.title()]

    return df


def display_raw_data(df):
    """Displays raw data in chunks of 5 rows upon usser request."""
    start = 0
    while True:
        choice = (
            input("\nWould you like to see 5 rows of raw data? Enter yes or no: ")
            .strip()
            .lower()
        )
        if choice != "yes":
            break
        print(df.iloc[start : start + 5])
        start += 5

        if start >= len(df):
            print("\nNo more data to display.")
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    if handle_empty_df(df):
        return

    # display the most common month

    print("Most Common Month:", df["month"].mode().iloc[0])

    # display the most common day of week

    print("Most Common Day of Week:", df["day_name"].mode().iloc[0])

    # display the most common start hour

    print("Most Common Start Hour:", df["hour"].mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    if handle_empty_df(df):
        return

    # display most commonly used start station

    print("Most common Start Station:", df["Start Station"].mode()[0])

    # display most commonly used end station

    print("Most common End Station:", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip

    df["trip"] = df["Start Station"] + " -> " + df["End Station"]
    print("Most Frequent Trip:", df["trip"].mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    if handle_empty_df(df):
        return

    # display total travel time

    total_hours = df["Trip Duration"].sum() / 3600
    print(f"Total Travel Time:{total_hours:.2f} hours")

    # display mean travel time

    avg_minutes = df["Trip Duration"].mean() / 60
    print(f"Average Travel Time:{avg_minutes:.2f} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    if handle_empty_df(df):
        return

    # Display counts of user types

    print("\nUser Types:")
    print(df["User Type"].value_counts())

    # Display counts of gender

    if "Gender" in df.columns:
        print("\nGender:")
        print(df["Gender"].value_counts())
    else:
        print("\nGender data not available.")

    # Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:
        print("\nEarliest Birth Year:", int(df["Birth Year"].min()))
        print("Most Recent Birth Year:", int(df["Birth Year"].max()))
        print("Most Common Birth Year:", int(df["Birth Year"].mode()[0]))
    else:
        print("\nBirth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = (
            input("\nWould you like to restart? Enter yes or no.\n").strip().lower()
        )
        if restart.lower() != "yes":
            print("\nThank you for exploring US Bikeshare data!")
            break


if __name__ == "__main__":
    main()
