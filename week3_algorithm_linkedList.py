import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SubscriptionPackage:
    def __init__(self, package_type, start_date):
        self.package_type = package_type
        self.start_date = start_date
        try:
            self.end_date = start_date + datetime.timedelta(days=30)  # For 30 days subscription
        except TypeError:
            print("Error: Please provide a valid start date.")
        self.head = None
        self.tail = None
        self.pickup_dates = []
        self.generate_pickup_schedules()

    def generate_pickup_schedules(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            self.pickup_dates.append(current_date)
            if self.package_type == "standard":
                current_date += datetime.timedelta(days=8)  # Standard package has pickup once a week
            elif self.package_type == "premium":
                current_date += datetime.timedelta(days=4)  # Premium package has pickup twice a week
            elif self.package_type == "VIP":
                current_date += datetime.timedelta(days=3)  # VIP package has pickup three times a week

    def display_pickup_schedules_forward(self):
        print(f"Pickup Schedules for {self.package_type} Package:")
        for date in self.pickup_dates:
            print(date, end=' -> ')
        print('None')

    def display_pickup_schedules_backward(self):
        print(f"Pickup Schedules for {self.package_type} Package (Backward):")
        for date in reversed(self.pickup_dates):
            print(date, end=' -> ')
        print('None')


# Example usage.  
start_date = datetime.date(2023, 12, 1)  # Start date is 1st of the month
standard_package = SubscriptionPackage("standard", start_date)
standard_package.display_pickup_schedules_forward()
standard_package.display_pickup_schedules_backward()


premium_package = SubscriptionPackage("premium", start_date)
premium_package.display_pickup_schedules_forward()
standard_package.display_pickup_schedules_backward()


vip_package = SubscriptionPackage("VIP", start_date)
vip_package.display_pickup_schedules_forward()
standard_package.display_pickup_schedules_backward()
