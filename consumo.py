# Simulação de consumo de energia - Análise de dados reais — Consumo energético da Amazon
# Exemplo de código Python para simular consumo de energia de data centers, baseado em alguns parâmetros simplificados (número de servidores, potência por servidor, eficiência de PUE, horas de operação, mix energia renovável).

import numpy as np


class DataCenterEnergySim:
    def __init__(self, num_serv, power_kw, power, horas_ano=8760):
        """
        num_serv: número de servidores no data center
        power_kw: consumo médio de cada servidor em kW
        power: Eficiência no uso de energia
        horas_ano: horas ativas por ano (padrão 8760 = 24h * 365d)
        """
        self.num_serv = num_serv
        self.power_kw = power_kw
        self.power = power
        self.horas = horas_ano

    def consumo_anual(self):
        """
        Calcula o consumo anual de energia (em kWh)
        """
        # energia usada pelos servidores (IT)
        it_power_total_kw = self.num_serv * self.power_kw
        # energia total no data center considerando overhead
        total_power_kw = it_power_total_kw * self.power
        # energia anual (kWh)
        energy_kwh = total_power_kw * self.horas
        return energy_kwh

    def renewable_matched_energy(self, renewable_fraction):
        """
        renewable_fraction: fração (0 a 1) da energia que é “match” com energia renovável
        Retorna a energia renovável “associada (match)”
        """
        total = self.consumo_anual()
        return total * renewable_fraction

    def emissions_estimate(self, carbon_intensidade_grid):
        """
        Estima emissões de CO2 baseado na intensidade de carbono da rede elétrica
        carbon_intensidade_grid: kgCO2 por kWh (intensidade média da rede)
        Retorna emissões em toneladas de CO2 por ano.
        """
        energy = self.consumo_anual()
        emissions_kg = energy * carbon_intensidade_grid
        emissions_tons = emissions_kg / 1000.0
        return emissions_tons


# Exemplo de uso:
if __name__ == "__main__":
    # Parâmetros hipotéticos
    num_serv = 10000  # por exemplo, 10 mil servidores
    power_kw = 0.5  # cada servidor consome em média 500 W (0.5 kW)
    power = 1.15  # eficiência do data center

    sim = DataCenterEnergySim(num_serv, power_kw, power)
    annual_kwh = sim.consumo_anual()
    print(f"Consumo anual total: {annual_kwh / 1e6:.2f} milhões de kWh")

    # Supomos que 100% da energia é “matched” com renovável (Amazon-style)
    renewable_fraction = 1.0
    renew_energy = sim.renewable_matched_energy(renewable_fraction)
    print(f"Energia renovável associada: {renew_energy / 1e6:.2f} milhões de kWh")

    # Estimativa de emissões assumindo uma intensidade de carbono da rede
    # Suponha 0,4 kg CO2 por kWh (depende do país/rede)
    carbon_intensidade = 0.4
    emissions = sim.emissions_estimate(carbon_intensidade)
    print(f"Estimativa de emissões: {emissions:.2f} toneladas de CO2 por ano")




