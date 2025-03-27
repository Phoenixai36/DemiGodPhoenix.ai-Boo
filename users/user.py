class User:
    def __init__(self, user_id, username, email, affiliate_link):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.affiliate_link = affiliate_link
        self.clicks = 0
        self.income = 0.0
        self.costs = 0.0

    def add_clicks(self, clicks):
        self.clicks += clicks
        self.income = self.clicks * 0.50  # $0.50 por clic

    def add_costs(self, costs):
        self.costs += costs

    def get_roi(self):
        return self.income - self.costs

    def get_commission(self, commission_rate=0.20):
        roi = self.get_roi()
        return roi * commission_rate