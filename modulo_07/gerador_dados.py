# Arquivo: gerador_dados.py

from faker import Faker
import datetime

# Cria um gerador de dados fictícios em português do Brasil
fake = Faker('pt_BR')

nome_ficticio = fake.name()
email_ficticio = fake.email()
data_atual = datetime.date.today()

print(f"Nome fictício gerado: {nome_ficticio}")
print(f"E-mail fictício: {email_ficticio}")
print(f"Data de hoje: {data_atual}")
