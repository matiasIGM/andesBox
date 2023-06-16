from django.test import TestCase

# Create your tests here.
import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "andes_b.settings")
django.setup()


from andesRestApi.models import Envio

fake = Faker()

def create_envios(num_envios):
    for _ in range(num_envios):
        envio = Envio.objects.create(
            numero_seguimiento=fake.random_number(digits=7),
            amountPieces=fake.random_int(min=0, max=100),
            customerName=fake.name(),
            creationDate=fake.date_time(),
            baseOrigin=fake.address(),
            receiverName=fake.name(),
            receiveMail=fake.email(),
            receiverPhone=fake.phone_number(),
            receiverAddress=fake.address(),
            receiverDistrict=fake.city(),
            receiverCity=fake.city(),
            receiverRegion=fake.state(),
            locationName=fake.company(),
            patent=fake.random_element(elements=('ABC123', 'XYZ789')),
            courierName=fake.name(),
            receiver=fake.name()
        )
        print(f"Envío creado: {envio}")

if __name__ == "__main__":
    num_envios = int(input("Ingrese la cantidad de envíos a crear: "))
    create_envios(num_envios)
