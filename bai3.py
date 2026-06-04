
patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
	["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def display_patients(list):
    print('----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----')
    print()
    for i,pat in enumerate(list,1):
        print(f"{i}. MÃ: {pat[0]} | Tên: {pat[1]:<17} | Giới tính: {pat[2]:<15} | Bệnh: {pat[3]}")
    print()
    if patients == []:
        print("Hiện không có bệnh nhân nào đang điều trị. !!! ")
        print()



def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ.
    """
    gender_input = gender_input.strip().lower()

    if gender_input in ["nam", "nu"]:
        return True

    return False

def find_patient_index(patient_list, patient_id):

    patient_id = patient_id.strip().upper()

    for index in range(len(patient_list)):
        if patient_list[index][0] == patient_id:
            return index

    return -1



def add_patient(patient_list):
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if patient_name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender = input("Nhập giới tính Nam/Nu: ").strip()

        if validate_gender(gender):
            gender = gender.title()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    disease = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    patient = [patient_id,patient_name,gender,disease]

    patient_list.append(patient)

    print("Tiếp nhận bệnh nhân thành công!")



def update_diagnosis(patient_list):

    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, patient_id)

    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")

    new_disease = input("Nhập chẩn đoán mới: ").strip().capitalize()

    if new_disease == "":
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = new_disease

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
 
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input("Nhập từ khóa tên bệnh: ").strip()

    if keyword == "":
        print("Từ khóa tìm kiếm không được để trống!")
        return

    print("Kết quả tìm kiếm:")

    count = 0

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1
            print(f"{count}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


while True:
    choice = int(input("""===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====
Hiển thị danh sách bệnh nhân
Tiếp nhận bệnh nhân mới
Cập nhật chẩn đoán bệnh theo mã BN
Tìm kiếm và thống kê theo tên bệnh
Thoát chương trình
===========================================
Nhập lựa chọn của bạn:"""))


    if choice == 1:
        display_patients(patients)

    elif choice == 2:
        add_patient(patients)

    elif choice == 3:
        update_diagnosis(patients)

    elif choice == 4:
        search_by_disease(patients)

    elif choice == 5:
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")