class SystemCoreSub:
    def __init__(self, month=1):
        self.month = month
    def run_cycle(self):
        print(f"Running subsystem cycle for month {self.month}")