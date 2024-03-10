import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for chicago, new york city, or washington city?")
    city = city.lower()
    while True: 
        if city == "chicago" or city == "new york city" or city == "washington" :
            break 
        else:
            city= input("City name is not correct, please enter a valid city name.")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    time_filter = input("Would you like to filter data by month, day, both, or not at all? Type none for no time filter.")
    time_filter = time_filter.lower()
    while True: 
        if time_filter == "month" or time_filter == "day" or time_filter == "both" or time_filter == "none" :
            break 
        else:
            time_filter= input("time filter is not correct, please enter a valid time filter.")
            
     
    month = "all" 
    day = "all" 
    if time_filter=="both":
        month = input("which month? ( january, february, ... , june) ?")
        month = month.lower()
        while True:
            if month == "january" or month == "february" or month == "march" or  month == "april" or month == "may" or month == "june":
                break 
            else:
                month = input("month is not correct, please enter a valid month.")
            
        day = input("which day? ( monday, tuesday, ..., sunday) ?")
        day = day.lower()
        while True:
            #Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday
            if day == "monday" or day == "tuesday" or day == "wednesday" or  day == "thursday" or day == "friday" or day == "saturday" or day == "sunday":
                break 
            else:
                day = input("day is not correct, please enter a valid day.")
            
    if time_filter=="month":
        month = input("which month? ( january, february, ... , june) ?")
        month = month.lower()
        while True:
            if month == "january" or month == "february" or month == "march" or  month == "april" or month == "may" or month == "june":
                break 
            else:
                month = input("month is not correct, please enter a valid month.")
            
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if time_filter=="day": 
        day = input("which day? ( monday, tuesday, ..., sunday) ?")
        day = day.lower()
        while True:
            #Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday
            if day == "monday" or day == "tuesday" or day == "wednesday" or  day == "thursday" or day == "friday" or day == "saturday" or day == "sunday":
                break 
            else:
                day = input("day is not correct, please enter a valid day.")

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df['month'].mode()[0])

    # TO DO: display the most common day of week
    print(df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print( df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print( df['Start Station'].mode()[0] )

    # TO DO: display most commonly used end station
    print( df['End Station'].mode()[0] )

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station'] 
    print( df['Trip Combination'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ( df ["Trip Duration"].sum() )
    

    # TO DO: display mean travel time
    print ( df ["Trip Duration"].mean() )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        print(df['Birth Year'].mode()[0])
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """display 5 rows of individual trip data."""
    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while view_data.lower() != "no" :
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
