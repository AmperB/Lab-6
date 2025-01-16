class Firearm:
    def __init__(self, ammo_capacity, fire_rate, range):
        # Количество патронов в магазине
        self.ammo_capacity = ammo_capacity
        # Скорострельность (выстрелов в секунду)
        self.fire_rate = fire_rate
        # Дальность стрельбы (в метрах)
        self.range = range

    def time_to_empty_magazine(self):
        """Метод 1: За сколько секунд магазин опустеет."""
        if self.fire_rate > 0:
            return self.ammo_capacity / self.fire_rate
        return float('inf')  # Если скорострельность равна нулю, магазин не опустеет

    def fire_rate_to_range_ratio(self):
        """Метод 2: Соотношение скорострельности к дальности стрельбы."""
        if self.range > 0:
            return self.fire_rate / self.range
        return float('inf')  # Если дальность равна нулю, возвращаем бесконечность

# Класс "Штурмовая винтовка"
class AssaultRifle(Firearm):
    def __init__(self, ammo_capacity, fire_rate, range, burst_mode):
        # Вызываем конструктор базового класса
        super().__init__(ammo_capacity, fire_rate, range)
        # Дополнительное поле: режим стрельбы очередями (True/False)
        self.burst_mode = burst_mode

    def fire_rate_to_range_ratio(self):
        """Переопределённый метод 2: соотношение скорострельности к дальности стрельбы."""
        ratio = super().fire_rate_to_range_ratio()
        # Уменьшаем коэффициент, если включён режим стрельбы очередями
        return ratio * 0.9 if self.burst_mode else ratio

# Класс "Снайперская винтовка"
class SniperRifle(Firearm):
    def __init__(self, ammo_capacity, fire_rate, range, zoom_level):
        # Вызываем конструктор базового класса
        super().__init__(ammo_capacity, fire_rate, range)
        # Дополнительное поле: уровень увеличения оптического прицела
        self.zoom_level = zoom_level

    def fire_rate_to_range_ratio(self):
        """Переопределённый метод 2: соотношение скорострельности к дальности стрельбы."""
        ratio = super().fire_rate_to_range_ratio()
        # Увеличиваем коэффициент в зависимости от уровня увеличения
        return ratio / (self.zoom_level if self.zoom_level > 0 else 1)

# Пример использования
if __name__ == "__main__":
    ak47 = AssaultRifle(ammo_capacity=30, fire_rate=10, range=300, burst_mode=True)
    print(f"Штурмовая винтовка (AK-47):")
    print(f"  Время опустошения магазина: {ak47.time_to_empty_magazine()} сек.")
    print(f"  Соотношение скорострельности к дальности: {ak47.fire_rate_to_range_ratio()}")

    awp = SniperRifle(ammo_capacity=10, fire_rate=1, range=1000, zoom_level=4)
    print(f"Снайперская винтовка (AWP):")
    print(f"  Время опустошения магазина: {awp.time_to_empty_magazine()} сек.")
    print(f"  Соотношение скорострельности к дальности: {awp.fire_rate_to_range_ratio()}")
