import json
from users.user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open("users/user_data.json", "r") as f:
                data = json.load(f)
                for user_id, user_data in data.items():
                    user = User(
                        user_id=user_id,
                        username=user_data["username"],
                        email=user_data["email"],
                        affiliate_link=user_data["affiliate_link"]
                    )
                    user.clicks = user_data["clicks"]
                    user.income = user_data["income"]
                    user.costs = user_data["costs"]
                    self.users[user_id] = user
        except FileNotFoundError:
            with open("users/user_data.json", "w") as f:
                json.dump({}, f)

    def save_users(self):
        data = {}
        for user_id, user in self.users.items():
            data[user_id] = {
                "username": user.username,
                "email": user.email,
                "affiliate_link": user.affiliate_link,
                "clicks": user.clicks,
                "income": user.income,
                "costs": user.costs
            }
        with open("users/user_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def add_user(self, user_id, username, email, affiliate_link):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, username, email, affiliate_link)
            self.save_users()
            return True
        return False

    def update_user_stats(self, user_id, clicks, costs):
        if user_id in self.users:
            self.users[user_id].add_clicks(clicks)
            self.users[user_id].add_costs(costs)
            self.save_users()

    def get_user_commission(self, user_id, commission_rate=0.20):
        if user_id in self.users:
            return self.users[user_id].get_commission(commission_rate)
        return 0.0

    def get_total_commission(self, commission_rate=0.20):
        total = 0.0
        for user in self.users.values():
            total += user.get_commission(commission_rate)
        return total