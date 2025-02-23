from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        # Convert birthday string to date object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Get birthday this year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If birthday has passed this year, look at next year's birthday
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate days until birthday
        delta_days = (birthday_this_year - today).days
        
        # Check if birthday is within next 7 days
        if 0 <= delta_days <= 7:
            # Get day of the week (0 is Monday, 6 is Sunday)
            day_of_week = birthday_this_year.weekday()
            
            # Define congratulation date
            congratulation_date = birthday_this_year
            
            # If birthday falls on weekend
            if day_of_week >= 5:  # 5 is Saturday, 6 is Sunday
                # Move to next Monday
                congratulation_date += timedelta(days=(7 - day_of_week))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Test the function
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)