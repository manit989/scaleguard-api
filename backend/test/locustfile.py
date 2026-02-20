from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(0.09, 0.1) 

    def on_start(self):
        response = self.client.post("/auth/token", data={
            "username": "johndoe",
            "password": "secret"
        })
        
        token = response.json()["access_token"]
        self.client.headers.update({"Authorization": f"Bearer {token}"})

    @task
    def access_protected_route(self):
        with self.client.get("/users/me/items/", catch_response=True) as response:
            if response.status_code == 429:
                response.success()
            elif response.status_code == 200:
                response.success()
