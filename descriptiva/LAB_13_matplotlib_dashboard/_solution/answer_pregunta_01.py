# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import shutil

    if not os.path.exists("docs"):
        os.makedirs("docs")

    files = [
        ("_index.html", "index.html"),
        ("_average_customer_rating.png", "average_customer_rating.png"),
        ("_mode_of_shipment.png", "mode_of_shipment.png"),
        ("_shipping_per_warehouse.png", "shipping_per_warehouse.png"),
        ("_weight_distribution.png", "weight_distribution.png"),
    ]
    for source, target in files:
        shutil.copyfile(source, f"docs/{target}")


if __name__ == "__main__":
    pregunta_01()
