import pandas as pd
import os

# 1. Load data
file_path = r"C:\Users\HP\OneDrive\Dokumen\prak mesin L\1227050036_Materi-3-Mengenal-Pengolahan-Data-dan-Eksplorasi-DataURL-main\Modul1-2-3_Materi3\DatasetForCoffeeSales2.csv"


if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    print("Dataset berhasil dibaca. Berikut 10 baris pertama:")
    print(data.head(10))
    
    # 2. Tampilkan informasi dataset
    print("\nInformasi dataset:")
    print(data.info())
    
    # 3. Cek missing values
    print("\nJumlah missing values per fitur:")
    print(data.isna().sum())
    
    # 4. Handling missing values (Modus untuk 'lunch')
    data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)
    
    # 5. Handling missing values (Mean untuk 'reading score')
    data['reading score'].fillna(data['reading score'].mean(), inplace=True)
    
    # 6. Handling missing values (Median untuk 'grade')
    data['grade'].fillna(data['grade'].median(), inplace=True)
    
    # 7. Cek kembali apakah masih ada missing values
    print("\nInformasi dataset setelah handling missing values:")
    print(data.info())
    
    # 8. Alternatif lain handling missing values
    # Interpolasi linear
    # data['nama_fitur'].interpolate(method='linear', inplace=True)
    
    # Backward Fill
    # data['nama_fitur'].fillna(method='bfill', inplace=True)
    
    # Forward Fill
    # data['nama_fitur'].fillna(method='ffill', inplace=True)
    
    # Drop rows dengan missing values
    # data.dropna(axis=0, inplace=True)
    
    # Drop kolom dengan lebih dari 50% missing values
    # data.dropna(axis=1, inplace=True)
    
    print("\nProses handling missing values selesai.")
else:
    print(f"Error: File '{file_path}' tidak ditemukan.")