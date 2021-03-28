import pandas as pd

df_autonomous_community = pd.DataFrame(
    {
        "Community": [
            "Andalucia",
            "Aragon",
            "Asturias",
            "Baleares",
            "Canarias",
            "Cantabria",
            "Castilla y Leon",
            "Castilla-La Mancha",
            "Cataluña",
            "Comunitat Valenciana",
            "Extremadura",
            "Galicia",
            "Madrid",
            "Murcia",
            "Navarra",
            "Pais Vasco",
            "Rioja",
            "Ceuta",
            "Melilla"
        ]
    }
)

df_autonomous_community.index += 1