import pandas as pd
import os

def check_orphans():
    csv_path = "PRODUCTO_FINAL_CSV"
    benef_df = pd.read_csv(os.path.join(csv_path, "tb_beneficiario.csv"))
    antro_df = pd.read_csv(os.path.join(csv_path, "tb_antropometrica.csv"))
    pesotalla_df = pd.read_csv(os.path.join(csv_path, "tb_pesotallamenores5x.csv"))

    # Convert everything to string and strip just in case
    benef_df['CEDULA_BEF'] = benef_df['CEDULA_BEF'].astype(str).str.strip()
    antro_df['CEDULA'] = antro_df['CEDULA'].astype(str).str.strip()
    
    # Check orphans in antropometrica
    orphans = antro_df[~antro_df['CEDULA'].isin(benef_df['CEDULA_BEF'])]
    print(f"Registros en Antropometría: {len(antro_df)}")
    print(f"Registros Huérfanos en Antropometría (CEDULA not in CEDULA_BEF): {len(orphans)}")
    if len(orphans) > 0:
        print("Muestra de Huérfanos (CEDULA):")
        print(orphans['CEDULA'].unique()[:10])

    # Check pesotallamenores5x columns
    print("\nColumnas en pesotallamenores5x:", pesotalla_df.columns.tolist())
    # Identify if there is a CEDULA or ID there
    # Usually it's linked to something.
    
if __name__ == "__main__":
    check_orphans()
