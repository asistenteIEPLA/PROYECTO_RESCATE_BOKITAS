import pandas as pd
from dbfread import DBF
import os

def clean_dataframe(df):
    # Clean FoxPro noise: strip strings
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
    
    # Normalize Dates
    for col in df.columns:
        if 'fec' in col.lower() or 'date' in col.lower() or 'fecha' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
            except Exception:
                pass
    return df

def rescue_data():
    base_path = "RESCATE_BOKITAS_FINAL/BasedeDatos"
    output_path = "PRODUCTO_FINAL_CSV"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Directorio creado: {output_path}")

    files_to_rescue = [
        "tb_beneficiario.DBF",
        "tb_antropometrica.DBF",
        "tb_pesotallamenores5x.dbf"
    ]
    
    results = {}

    for file_name in files_to_rescue:
        full_path = os.path.join(base_path, file_name)
        file_key = file_name.split('.')[0].lower()
        
        print(f"Procesando {file_name}...")
        try:
            # Read DBF with cp850 to preserve special characters
            table = DBF(full_path, encoding='cp850', load=True, ignore_missing_memofile=True)
            df = pd.DataFrame(iter(table))
            
            # Clean and Normalize
            df = clean_dataframe(df)
            
            # Export to CSV
            output_file = os.path.join(output_path, f"{file_key}.csv")
            df.to_csv(output_file, index=False, encoding='utf-8')
            
            results[file_key] = len(df)
            print(f"Rescatados {len(df)} registros de {file_name} -> {output_file}")
            
        except Exception as e:
            print(f"Error procesando {file_name}: {e}")
            # Try lowercase if not found (though OS might be case insensitive, best to be safe)
            if "not found" in str(e).lower():
                 print(f"Reintentando con variaciones de nombre...")
                 # list files in dir to match
                 files = os.listdir(base_path)
                 match = [f for f in files if f.lower() == file_name.lower()]
                 if match:
                     try:
                         table = DBF(os.path.join(base_path, match[0]), encoding='cp850', load=True, ignore_missing_memofile=True)
                         df = pd.DataFrame(iter(table))
                         df = clean_dataframe(df)
                         output_file = os.path.join(output_path, f"{file_key}.csv")
                         df.to_csv(output_file, index=False, encoding='utf-8')
                         results[file_key] = len(df)
                         print(f"Rescatados {len(df)} registros de {match[0]} -> {output_file}")
                     except Exception as e2:
                         print(f"Error fatal en reintento: {e2}")

    print("\n--- RESUMEN DE RESCATE ---")
    for table, count in results.items():
        print(f"{table}: {count} registros")

if __name__ == "__main__":
    rescue_data()
