from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert input string to datetime object
        input_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Get current date
        current_date = datetime.today()
        
        # Convert both dates to date objects to ignore time
        input_date = input_date.date()
        current_date = current_date.date()
        
        # Calculate difference in days
        difference = current_date - input_date
        
        return difference.days
    
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'"

    

print(get_days_from_today("2023-01-01"))