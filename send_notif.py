from pushbullet import Pushbullet
API_KEY = 'your api key'
file = 'schedule.txt'

with open(file, 'r') as f:
    text = f.read()
pb = Pushbullet(API_KEY)
pb.push_note('Follow IT!', text)

