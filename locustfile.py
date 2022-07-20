import os
import random

from locust import HttpUser, task, between

USERNAME = os.environ["LOCUST_EMAIL"]
PASSWORD = os.environ["LOCUST_PASSWORD"]


class AutomationPracticeRequester(HttpUser):
    wait_time = between(1, 10)

    def on_start(self):
        self.login()

    def login(self):
        self.client.post("index.php?controller=authentication",
                         json={"email": USERNAME,
                               "passwd": PASSWORD}
                         )

    def on_stop(self):
        self.logout()

    def logout(self):
        self.client.get("index.php?controller=authentication&back=my-account")

    @task(4)
    def select_category(self):
        category_number = random.randint(3, 8)
        self.client.get(f"index.php?id_category={category_number}&controller=category")

    @task(7)
    def filter_available_products(self):
        category_number = random.randint(1, 8)
        size = random.choice(["s", "m", "l"])
        self.client.get(f"index.php?id_category={category_number}&controller=category#/size-{size}/"
                        "availability-in_stock")

    @task(2)
    def send_a_message(self):
        self.client.post(f"index.php?controller=contact",
                         json={"id_contact": 1,
                               "from": USERNAME,
                               "id_order": "1234",
                               "message": "Hello"})
