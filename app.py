import uuid
import flet as ft


def main(page: ft.Page):
    format_mac = []
    mac_addr = hex(uuid.getnode())[2:]
    print(mac_addr)  # 68b599fb9283
    for i in range(0, len(mac_addr), 2):
        format_mac.append(mac_addr[i:i+2])

    formated_mac = f"Your MAC adress is {'-'.join(format_mac)}"
   
    page.add(
        ft.Text(formated_mac)
    )


if __name__ == "__main__":
    ft.app(main)
