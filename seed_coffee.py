import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jyzcool.settings')
django.setup()

from api.models import Coffee

def seed_data():
    coffee_items = [
        {'name': 'Espresso', 'description': 'Strong and rich coffee.', 'price': 2.50, 'category': 'HOT'},
        {'name': 'Cappuccino', 'description': 'Espresso with steamed milk foam.', 'price': 3.00, 'category': 'HOT'},
        {'name': 'Iced Latte', 'description': 'Cold milk with a shot of espresso.', 'price': 3.75, 'category': 'ICED'},
        {'name': 'Caramel Frappuccino', 'description': 'Blended coffee with caramel syrup.', 'price': 4.50, 'category': 'SPECIAL'},
    ]

    for item in coffee_items:
        Coffee.objects.get_or_create(
            name=item['name'],
            description=item['description'],
            price=item['price'],
            category=item['category']
        )

if __name__ == '__main__':
    print("Seeding data...")
    seed_data()
    print("Data seeded successfully.")
