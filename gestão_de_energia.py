# Solução desevolvida pela opção B Dispositivo IoT (real ou simulado):
# Monitoramento ou automação inteligente para controle de energia.
''''
Obetivo:
Reduzir desperdícios e aumentar o uso eficiente de energia (inclusive renovável), através de:
Monitoramento contínuo de consumo em tempo real
Automação para ligar/desligar equipamentos com base em uso real
Priorização de energia de fontes renováveis (solar, eólica) quando disponível
Alertas preventivos e decisões automáticas para reduzir carga em picos
'''

import random
import time

class SmartMeterIoT:
    """Simula um dispositivo IoT de energia"""
    def __init__(self):
        self.total_kwh = 0

    def read_data(self):
        voltage = random.uniform(210, 230)        # V
        current = random.uniform(0.2, 6.0)        # A
        power = voltage * current / 1000          # kW
        solar_level = random.randint(0, 100)      # %
        self.total_kwh += power / 3600            # consumo por segundo
        return {
            "voltage": voltage,
            "current": current,
            "power_kw": power,
            "solar_level": solar_level,
            "kwh_total": self.total_kwh
        }


class SmartController:
    """Inteligência do sistema"""
    def __init__(self):
        self.devices = {
            "ar_condicionado": True,
            "iluminacao": True,
            "servidores_aux": False
        }

    def apply_logic(self, data):
        solar = data["solar_level"]
        power = data["power_kw"]

        # --- Regra 1: Prioridade para energia solar ---
        if solar > 60:
            self.devices["servidores_aux"] = True
        else:
            self.devices["servidores_aux"] = False

        # --- Regra 2: Economia automática ---
        if solar < 20 and power > 0.6:
            self.devices["ar_condicionado"] = False
        else:
            self.devices["ar_condicionado"] = True

        # --- Regra 3: Iluminação baseada em horário (simulação) ---
        hour = random.randint(0, 23)
        self.devices["iluminacao"] = hour >= 18 or hour <= 6

        return self.devices


def run_simulation(seconds=10):
    meter = SmartMeterIoT()
    controller = SmartController()

    for _ in range(seconds):
        data = meter.read_data()
        actions = controller.apply_logic(data)

        print("\n📡 Dados do IoT:")
        print(f"  Voltagem:  {data['voltage']:.1f} V")
        print(f"  Corrente:  {data['current']:.2f} A")
        print(f"  Potência:  {data['power_kw']:.3f} kW")
        print(f"  Solar:     {data['solar_level']}%")
        print(f"  Consumo:   {data['kwh_total']:.5f} kWh")

        print("\n⚙️ Ações Automáticas:")
        for dev, state in actions.items():
            print(f"  {dev}: {'Ligado' if state else 'Desligado'}")

        time.sleep(1)


if __name__ == "__main__":
    print("Iniciando simulação SmartEnergy-IoT...\n")
    run_simulation(15)
