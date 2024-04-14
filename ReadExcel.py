import pandas as pd
import os

def add_id_column(file_path, id_column_name, id_value):
    df = pd.read_excel(file_path)
    df[id_column_name] = id_value
    df.to_excel(file_path, index=False)
def main():
    folder_path = "C:/Users/begam/OneDrive/Desktop/New folder (2)"
    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(folder_path, filename)
            name = filename.split("_")[0]
            id_value = input("Nhập ID cho {}: ".format(name))     
            if os.path.exists(file_path):
                df = pd.read_excel(file_path)
                if 'ID' in df.columns:
                    if id_value in df['ID'].values:
                        print("ID đã tồn tại. Vui lòng nhập ID khác.")
                        continue
            # Thêm cột ID vào file Excel
            add_id_column(file_path, 'ID', id_value)
            print("Đã thêm ID thành công vào file {}.".format(filename))

if __name__ == "__main__":
    main()
