import pandas as pd
import os

def audit_data():
    csv_path = "PRODUCTO_FINAL_CSV"
    files = ["tb_beneficiario.csv", "tb_antropometrica.csv", "tb_pesotallamenores5x.csv"]
    
    dataframes = {}
    
    for f in files:
        full_path = os.path.join(csv_path, f)
        if os.path.exists(full_path):
            df = pd.read_csv(full_path)
            dataframes[f] = df
            print(f"\n--- Auditoría de {f} ---")
            print(df.head(5))
            
            # Check names if applicable
            name_cols = [c for c in df.columns if 'nom' in c.lower() or 'ape' in c.lower()]
            if name_cols:
                print(f"Muestra de nombres ({name_cols}):")
                print(df[name_cols].head(5))
            
            # Check weight/height in antropometrica
            if 'antropometrica' in f:
                weight_cols = [c for c in df.columns if 'peso' in c.lower()]
                height_cols = [c for c in df.columns if 'talla' in c.lower()]
                print(f"Muestra de peso/talla: {df[weight_cols + height_cols].head(5)}")
                # Check types
                print(f"Tipos de datos weight/height: {df[weight_cols + height_cols].dtypes}")

    # Orphan IDs Check
    if "tb_beneficiario.csv" in dataframes and "tb_antropometrica.csv" in dataframes:
        # Identify beneficiary ID column. Usually something like 'id_benef' or 'id'
        # Let's find common columns
        benef_df = dataframes["tb_beneficiario.csv"]
        antro_df = dataframes["tb_antropometrica.csv"]
        
        # Look for columns like 'ID' or 'CEDULA' or 'CODIGO'
        # Assuming there is a common ID. Let's list columns first to be sure.
        print("\nColumnas en beneficiario:", benef_df.columns.tolist())
        print("Columnas en antropometrica:", antro_df.columns.tolist())
        
        # Often ID is the first column or 'cedula'
        # Let's try to match by 'id_benef' or common names
        common = set(benef_df.columns).intersection(set(antro_df.columns))
        print("Columnas comunes:", common)
        
        if common:
            # Pick an ID column
            id_col = list(common)[0] # Just a guess for now, will refine
            # Actually, let's look for 'id' string in columns
            potential_ids = [c for c in common if 'id' in c.lower() or 'ced' in c.lower() or 'cod' in c.lower()]
            if potential_ids:
                id_col = potential_ids[0]
                print(f"Usando '{id_col}' para chequeo de huérfanos.")
                orphans = antro_df[~antro_df[id_col].isin(benef_df[id_col])]
                print(f"Registros huérfanos en antropométrica: {len(orphans)}")
                if len(orphans) > 0:
                    print("Primeros 5 huérfanos:")
                    print(orphans.head(5))
            else:
                print("No se encontró columna de ID común clara.")
        else:
            print("No hay columnas comunes para cruzar.")

if __name__ == "__main__":
    audit_data()
