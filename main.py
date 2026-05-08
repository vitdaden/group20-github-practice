from todo import Todo
from utils import print_header, print_separator, get_input, get_int_input, confirm

todos = []
next_id = 1


def them_todo():
    print_header("THÊM CÔNG VIỆC MỚI")
    title = get_input("  Tên công việc: ")
    description = get_input("  Mô tả (bỏ trống nếu không có): ", allow_empty=True)
    global next_id
    todo = Todo(next_id, title, description)
    todos.append(todo)
    next_id += 1
    print(f"\n  ✅ Đã thêm: \"{title}\" (ID: {todo.id})")


def hien_thi_todo():
    print_header("DANH SÁCH CÔNG VIỆC")
    if not todos:
        print("  (Chưa có công việc nào)")
        return

    chua_xong = [t for t in todos if not t.completed]
    xong_roi = [t for t in todos if t.completed]

    if chua_xong:
        print("  📋 Chưa hoàn thành:")
        for t in chua_xong:
            print(f"    {t}")

    if xong_roi:
        print("  📋 Đã hoàn thành:")
        for t in xong_roi:
            print(f"    {t}")

    print(f"\n  Tổng: {len(todos)} | Xong: {len(xong_roi)} | Còn lại: {len(chua_xong)}")


def tim_kiem_todo():
    print_header("TÌM KIẾM CÔNG VIỆC")
    keyword = get_input("  Nhập từ khóa tìm kiếm: ").lower()
    ket_qua = [t for t in todos if keyword in t.title.lower() or keyword in t.description.lower()]

    if not ket_qua:
        print(f"  ❌ Không tìm thấy công việc nào với từ khóa \"{keyword}\".")
    else:
        print(f"  🔍 Tìm thấy {len(ket_qua)} kết quả:")
        for t in ket_qua:
            print(f"    {t}")


def danh_dau_hoan_thanh():
    print_header("ĐÁNH DẤU HOÀN THÀNH")
    hien_thi_todo()
    if not todos:
        return
    id_input = get_int_input("\n  Nhập ID công việc muốn đánh dấu: ", min_val=1)
    todo = next((t for t in todos if t.id == id_input), None)
    if not todo:
        print(f"  ❌ Không tìm thấy công việc ID {id_input}.")
        return
    if todo.completed:
        print(f"  ℹ️  Công việc \"{todo.title}\" đã hoàn thành rồi.")
        if confirm("  Bỏ đánh dấu hoàn thành?"):
            todo.mark_undone()
            print("  ↩️  Đã bỏ đánh dấu hoàn thành.")
    else:
        todo.mark_done()
        print(f"  ✅ Đã đánh dấu hoàn thành: \"{todo.title}\"")


def xoa_todo():
    print_header("XÓA CÔNG VIỆC")
    hien_thi_todo()
    if not todos:
        return
    id_input = get_int_input("\n  Nhập ID công việc muốn xóa: ", min_val=1)
    todo = next((t for t in todos if t.id == id_input), None)
    if not todo:
        print(f"  ❌ Không tìm thấy công việc ID {id_input}.")
        return
    if confirm(f"  Bạn chắc chắn muốn xóa \"{todo.title}\"?"):
        todos.remove(todo)
        print(f"  🗑️  Đã xóa: \"{todo.title}\"")


def hien_thi_menu():
    print_header("📝 TODO LIST - QUẢN LÝ CÔNG VIỆC")
    print("  1. Thêm công việc")
    print("  2. Hiển thị tất cả công việc")
    print("  3. Tìm kiếm công việc")
    print("  4. Đánh dấu hoàn thành")
    print("  5. Xóa công việc")
    print("  0. Thoát")
    print_separator()


def main():
    print("\n  Chào mừng đến với Todo List! 🎉")
    while True:
        print()
        hien_thi_menu()
        choice = input("  Chọn chức năng (0-5): ").strip()

        if choice == '1':
            them_todo()
        elif choice == '2':
            hien_thi_todo()
        elif choice == '3':
            tim_kiem_todo()
        elif choice == '4':
            danh_dau_hoan_thanh()
        elif choice == '5':
            xoa_todo()
        elif choice == '0':
            print("\n  👋 Tạm biệt! Hẹn gặp lại.\n")
            break
        else:
            print("  ⚠️  Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 5.")


if __name__ == "__main__":
    main()
