import csv
import random

cities = ['Buenos Aires', 'New York', 'San Francisco', 'London', 'Madrid', 'Paris', 'Berlin', 'Dubai', 'Lima', 'Sidney', 'Toronto', 'Tokyo', 'Beijing']
corps = ['Google', 'Apple', 'Facebook', 'Amazon', 'Tesla', 'Tencent']
events = 1000

with open('Events.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, quotechar="'", quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['City', 'Corps', 'Attendants'])
    for event in range(events):
        attendants = str(random.randint(10000,25000))
        spamwriter.writerow([random.choice(cities)] + [random.choice(corps)] + [attendants])