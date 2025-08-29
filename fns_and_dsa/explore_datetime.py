from datetime import datetime, timedelta


def display_current_datetime():
    # get the current date and time
    current_date = datetime.now()
    # print in the required format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(days_to_add):
    # get today's date and add the number of days
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    # print in the required format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1
    display_current_datetime()

    # Part 2
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for days.")


if __name__ == "__main__":
    main()