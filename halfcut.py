from datetime import datetime, timedelta

def add_time1(time_str):
    try:
        time_obj = datetime.strptime(time_str, "%I:%M %p")
        new_time_obj = time_obj + timedelta(hours=2, minutes=30)  # Add 2.5 hours
        new_time_str = new_time_obj.strftime("%I:%M %p")
        return new_time_str
    except ValueError:
        return None

def main1():
    try:
        num_times = int(input("Enter the number of times to loop: "))
        print("")
        time_str = input("Enter the time you cut the 1st tree (e.g 12:30 PM) : ")
        print("")
        for _ in range(num_times):
            new_time_str = add_time1(time_str)
            if new_time_str:
                print("Come back in ", new_time_str)
                time_str = new_time_str
            else:
                print("Please enter a valid time in the specified format.")
                break
    except ValueError:
        print("Please enter a valid number.")
