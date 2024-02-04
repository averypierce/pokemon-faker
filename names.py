from faker import Faker
import random


# Create a list of Faker instances
fakers = [
    Faker('en_IN'),
    Faker('en_US'),
    Faker('pt_PT')
]


with open('trainers.txt', 'r') as f:
    trainer_classes = f.readlines()

# Now 'lines' is a list where each element is a line from the file

for _ in range(1000):
    faker = random.choice(fakers)
    tc = random.choice(trainer_classes).strip()
    print(tc + ' ' + faker.first_name())
