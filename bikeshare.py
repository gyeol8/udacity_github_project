import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

print('Hello! Let\'s explore some US bikeshare data!')


def get_filters():
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the name of the city to analyze (chicago, new york city, washington): ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid city. Please enter a valid city.")

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month to filter by (all or a specific month from january to june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please enter a valid month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of the week to filter by (all or a specific day of the week): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day. Please enter a valid day.")

    print('-' * 40)
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
    # Load the data for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month != 'all':
        df = df[df['Start Time'].dt.month == ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1]

    # Filter by day if applicable
    if day != 'all':
        df = df[df['Start Time'].dt.day_name() == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    print(f"The most common month for travel is {most_common_month}.")

    # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f"The most common day for travel is {most_common_day}.")

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print(f"The most common start hour for travel is {most_common_hour}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is {most_common_start_station}.")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is {most_common_end_station}.")

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start and end station is from {most_common_trip[0]} to {most_common_trip[1]}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is {total_travel_time} seconds.")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is {mean_travel_time} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types)

    # TO DO: Display counts of gender (if 'Gender' column exists in the dataframe)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_counts)
    else:
        print("\nGender information not available in the dataset.")

    # TO DO: Display earliest, most recent, and most common year of birth (if 'Birth Year' column exists in the dataframe)
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print(f"\nEarliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print("\nBirth year information not available in the dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df, start_idx):
    """Displays 5 rows of raw data starting from the specified index."""
    print('\nDisplaying 5 rows of raw data...\n')
    print(df.iloc[start_idx:start_idx + 5])
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask user if they want to see raw data
        start_idx = 0
        while True:
            show_raw_data = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n').lower()
            if show_raw_data == 'yes':
                display_raw_data(df, start_idx)
                start_idx += 5
            elif show_raw_data == 'no':
                break
            else:
                print("Invalid input. Please enter yes or no.")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
