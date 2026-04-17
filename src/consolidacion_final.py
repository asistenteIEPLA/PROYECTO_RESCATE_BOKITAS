import pandas as pd
import os

def consolidate():
    csv_path = "PRODUCTO_FINAL_CSV"
    
    # Load all tables
    print("Cargando tablas...")
    antro_df = pd.read_csv(os.path.join(csv_path, "tb_antropometrica.csv"))
    menores_df = pd.read_csv(os.path.join(csv_path, "tb_menores.csv"))
    benef_df = pd.read_csv(os.path.join(csv_path, "tb_beneficiario.csv"))
    
    # Clean IDs to ensure match (strip and convert to string)
    antro_df['CEDULA'] = antro_df['CEDULA'].astype(str).str.strip()
    menores_df['CEDULA'] = menores_df['CEDULA'].astype(str).str.strip()
    menores_df['CEDULA_REP'] = menores_df['CEDULA_REP'].astype(str).str.strip()
    benef_df['CEDULA_BEF'] = benef_df['CEDULA_BEF'].astype(str).str.strip()
    
    # Deduplicate tables to avoid multiplying measurements during merge
    print("Deduplicando tablas...")
    menores_df = menores_df.drop_duplicates(subset=['CEDULA'], keep='first')
    benef_df = benef_df.drop_duplicates(subset=['CEDULA_BEF'], keep='first')
    
    # First Merge: Antropometrica + Menores
    print("Uniendo Antropometría con Menores...")
    merged_a_m = pd.merge(
        antro_df, 
        menores_df[['CEDULA', 'NOMBRE', 'APELLIDO', 'SEXO', 'FECHA_NAC', 'CEDULA_REP']], 
        on='CEDULA', 
        how='left'
    )
    
    # Second Merge: result + Beneficiarios (parents)
    print("Uniendo con Beneficiarios (representantes)...")
    final_df = pd.merge(
        merged_a_m,
        benef_df[['CEDULA_BEF', 'NOMBRE_CEN', 'PROYECTO']],
        left_on='CEDULA_REP',
        right_on='CEDULA_BEF',
        how='left',
        suffixes=('', '_benef')
    )
    
    # Convert dates to datetime
    final_df['FECHA_NAC'] = pd.to_datetime(final_df['FECHA_NAC'], errors='coerce')
    final_df['FECHA_PESAJE'] = pd.to_datetime(final_df['FECHA_INI'], errors='coerce')
    
    # Calculate Age in Months
    print("Calculando edad en meses...")
    # Primary logic: dates
    final_df['edad_meses_al_pesaje'] = (final_df['FECHA_PESAJE'] - final_df['FECHA_NAC']).dt.days / 30.4375
    
    # Secondary logic: fallback to EDAD/MESES from original measurement if dates missing
    fallback_age = final_df['EDAD'] * 12 + final_df['MESES']
    final_df['edad_meses_al_pesaje'] = final_df['edad_meses_al_pesaje'].fillna(fallback_age)
    
    # Format Children Name
    final_df['nombre_completo_niño'] = final_df['NOMBRE'].fillna('') + ' ' + final_df['APELLIDO'].fillna('')
    final_df['nombre_completo_niño'] = final_df['nombre_completo_niño'].str.strip()
    # If still empty, use ID
    final_df.loc[final_df['nombre_completo_niño'] == '', 'nombre_completo_niño'] = 'ORFANATO ID: ' + final_df['CEDULA']
    
    # Selection of final columns
    project_col = 'PROYECTO_benef' if 'PROYECTO_benef' in final_df.columns else 'PROYECTO'
    master_columns = [
        'CEDULA', 'nombre_completo_niño', 'SEXO', 'FECHA_NAC',
        'PESO', 'TALLA', 'FECHA_PESAJE', 'edad_meses_al_pesaje',
        'CEDULA_REP', 'NOMBRE_CEN', project_col
    ]
    
    master_data = final_df[master_columns].copy()
    master_data.rename(columns={project_col: 'PROYECTO'}, inplace=True)
    
    # Validation
    total_antro = len(antro_df)
    final_rows = len(master_data)
    with_name = len(final_df[final_df['NOMBRE'].notna()])
    print(f"\n--- VALIDACIÓN FINAL ---")
    print(f"Total mediciones originales: {total_antro}")
    print(f"Mediciones en archivo maestro: {final_rows}")
    print(f"Mediciones con datos de identidad (Name/Sex/DOB): {with_name}")
    print(f"Mediciones huérfanas (solo ID + Peso/Talla + Edad auto): {final_rows - with_name}")
    
    # Export
    output_file = "MASTER_DATA_ANTROPOMETRICA.csv"
    master_data.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\nArchivo maestro generado: {output_file}")
    
    # Export
    output_file = "MASTER_DATA_ANTROPOMETRICA.csv"
    master_data.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\nArchivo maestro generado: {output_file}")

if __name__ == "__main__":
    consolidate()
