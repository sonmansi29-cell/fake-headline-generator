import random

subjects = [
    "Shahrukh Khan",
    "Salman Khan",
    "Aamir Khan",
    "Akshay Kumar",
    "Virat Kohli",
    "Sachin Tendulkar",
    "A sleepy engineering student",
    "A frustrated Python developer",
    "Mumbai cat",
    "Delhi dog",
    "Jalgaon mouse",
    "A group of monkeys",
    "An alien from Mars",
    "Prime Minister",
    "Auto Rickshaw Driver from Delhi",
    "College professor",
]

actions = [
    "accidentally launches",
    "secretly cancels",
    "dances badly with",
    "eats 25 plates of",
    "declares war on",
    "orders extra",
    "celebrates loudly with",
    "throws laptop at",
    "forgets about",
    "falls asleep during",
]

places_or_things = [
    "at Red Fort 🏰",
    "inside Mumbai local train 🚆",
    "on the moon 🌕",
    "during IPL match 🏏",
    "at India Gate 🇮🇳",
    "in college canteen 🍽️",
    "inside Python exam 🧠",
    "on Zoom meeting 💻",
    "at 3 AM coding session 😴",
]

emojis = ["😂", "🤣", "😱", "🔥", "🚨", "🤯"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)
    emoji = random.choice(emojis)

    headline = f"🚨 BREAKING NEWS {emoji}: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another funny headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\n😄 Thank you for using the Funny Fake Headline Generator. Goodbye!")
