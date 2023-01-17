import csv
from faker import Faker
fake = Faker()

def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("Data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            email = Fname +"."+ Lname + domain_name
            username = Fname +"."+ Lname

            writer.writerow({
               "Email" : email,
               "Username" : username,
               "First Name" : Fname, 
               "Last Name" : Lname,
               "Password" : fake.password()
            })

if __name__ == '__main__':
    records = 100
    headers = ["Email", "Username", "First Name", "Last Name", "Password"]
    datagenerate(records, headers)
    print("CSV generation complete!")