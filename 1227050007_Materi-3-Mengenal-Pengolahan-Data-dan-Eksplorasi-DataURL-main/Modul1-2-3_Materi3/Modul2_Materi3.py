import pandas as pd
import os

# 1. Load data
# Tentukan path file CSV
file_path = r"C:\Users\HP\OneDrive\Dokumen\prak mesin L\1227050036_Materi-3-Mengenal-Pengolahan-Data-dan-Eksplorasi-DataURL-main\Modul1-2-3_Materi3\DatasetForCoffeeSales2.csv"

# Periksa apakah file ada sebelum membaca
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    print("Dataset berhasil dibaca. Berikut 10 baris pertama:")
    print(data.head(10))
    
    # 2. Filter data hanya menampilkan kolom City, Category, Product, dan Quantity
    filtered_data = data.filter(["City", "Category", "Product", "Quantity"], axis=1)
    print("\nData yang difilter:")
    print(filtered_data.head())
    
    # 3. Sorting berdasarkan Quantity dari terbesar ke terkecil
    data.sort_values("Quantity", axis=0, ascending=False, inplace=True, na_position="last")
    print("\nData setelah diurutkan berdasarkan Quantity (terbesar ke terkecil):")
    print(data.head())
    
    # 4. Group Total Sales by City
    if "Final Sales" in data.columns:
        grp1 = data.groupby("City")
        result = grp1["Final Sales"].aggregate("sum")
        print("\nTotal Sales per City:")
        print(result)
    else:
        print("\nError: Kolom 'Final Sales' tidak ditemukan dalam dataset.")
else:
    print(f"Error: File '{file_path}' tidak ditemukan. Pastikan file berada di direktori yang benar.")
