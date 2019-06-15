#### Get previous weekday by day ####

from datetime import datetime, timedelta

def get_previous_byday(dayname, start_date=None):
    """
    dayname [string] e.g., Monday
    start_date [datetime] if None, then now
    -----------------------------------------------------------------------
    return [datetime] the datetime that is last dayname
    """
    weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if start_date == None:
        start_date = datetime.today()
    day_num = start_date.weekday()    # Get the weekday of start_date [int]
    day_num_target = weekday_list.index(dayname.capitalize())    # Get the weekday of the given dayname
    days_ago = (7 + day_num - day_num_target) % 7
    # To determine if it was in the last week or current week
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

if __name__ == '__main__':
    x = get_previous_byday('saturday')
    print(x)