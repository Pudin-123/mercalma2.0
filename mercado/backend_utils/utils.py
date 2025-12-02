# Helpers / ejemplos para optimizar consultas
def optimized_products_qs(qs):
    return qs.select_related('seller','category')
