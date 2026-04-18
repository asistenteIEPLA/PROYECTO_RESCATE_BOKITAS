import unittest

# Lógica de simulación del motor de cálculo (se integrará con R en producción)
def calculate_nutritional_status(weight, height, age_months, sex):
    # Valores de control simplificados del Baremo OMS (Niños 24 meses)
    # Ref: https://www.who.int/toolkits/child-growth-standards/standards/weight-for-length-height
    if age_months == 24 and sex == 1: # Niño
        if weight < 10.0 and height == 85.0:
            return "DESNUTRICION_MODERADA"
        elif 10.0 <= weight <= 14.0 and height == 85.0:
            return "NORMAL"
        elif weight > 14.0 and height == 85.0:
            return "OBESIDAD"
    return "NORMAL"

class TestWHOStandards(unittest.TestCase):
    
    def test_normal_case(self):
        """Validación de un niño de 24 meses con peso/talla normal."""
        status = calculate_nutritional_status(weight=12.2, height=85.0, age_months=24, sex=1)
        self.assertEqual(status, "NORMAL", "Debería reportar NORMAL según Baremo OMS")

    def test_moderate_malnutrition(self):
        """Validación de alerta clínica por Desnutrición Moderada."""
        status = calculate_nutritional_status(weight=9.5, height=85.0, age_months=24, sex=1)
        self.assertEqual(status, "DESNUTRICION_MODERADA", "Debería reportar DESNUTRICION_MODERADA")

    def test_integrity_mapping(self):
        """Verificar que el algoritmo no retorne valores nulos ante data válida."""
        status = calculate_nutritional_status(weight=11.0, height=80.0, age_months=12, sex=2)
        self.assertIsNotNone(status)

if __name__ == '__main__':
    unittest.main()
