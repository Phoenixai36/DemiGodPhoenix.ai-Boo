from users.user_manager import UserManager

class SystemCore:
    def __init__(self, month=1):
        self.month = month
        self.affiliate_link = "https://tu-enlace-de-afiliado.com"  # Reemplaza con tu enlace real
        self.user_manager = UserManager()
        self.clicks_per_day = 2200  # Clics base del sistema principal
        self.total_clicks = 0
        self.income = 0.0
        self.costs = 40.40  # Costos del administrador (dominio, Bitly, EC2)

    def run_cycle(self):
        # Simulación de clics del sistema principal
        self.total_clicks = self.clicks_per_day * 30  # 30 días
        self.income = self.total_clicks * 0.50  # $0.50 por clic

        # Simulación de usuarios (5 usuarios de ejemplo)
        for i in range(1, 6):
            user_id = f"user_{i}"
            if user_id not in self.user_manager.users:
                self.user_manager.add_user(
                    user_id=user_id,
                    username=f"User{i}",
                    email=f"user{i}@example.com",
                    affiliate_link=f"https://tu-enlace-de-afiliado.com/user{i}"  # Reemplaza con tu enlace real
                )
            # Cada usuario genera 500 clics/día (15,000 clics/mes)
            user_clicks = 500 * 30
            user_costs = 10.0  # Costos simulados por usuario
            self.user_manager.update_user_stats(user_id, user_clicks, user_costs)

        # Calcular comisiones
        total_commission = self.user_manager.get_total_commission(commission_rate=0.20)
        print(f"Total commission from users: ${total_commission:.2f}")

        # Ingresos totales del administrador
        total_income = self.income + total_commission
        print(f"Admin total income: ${total_income:.2f}")
        print(f"Admin net profit: ${total_income - self.costs:.2f}")