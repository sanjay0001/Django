from .models import *
def create_data():
    logging.info("Cron job executed successfully.")
    p=Product(name="TV"+str(c),price=1000+c,description="Demo Cron")
    p.save()
    c+=1
