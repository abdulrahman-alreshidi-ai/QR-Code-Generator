import qrcode
import os


def generate_qr():

    print("=" * 40)
    print("      QR CODE GENERATOR")
    print("=" * 40)

    data = input("Enter text or URL: ").strip()

    if data == "":
        print("Input cannot be empty.")
        return

    filename = input("Enter file name: ").strip()

    if filename == "":
        filename = "qrcode"

    image = qrcode.make(data)

    output_file = f"{filename}.png"

    image.save(output_file)

    print("\nQR Code generated successfully.")
    print(f"Saved as: {os.path.abspath(output_file)}")

def main():

    while True:

        generate_qr()

        again = input("\nGenerate another QR Code? (Y/N): ").strip().upper()

        if again != "Y":
            print("Thank you for using QR Code Generator.")
            break


if __name__ == "__main__":
    main()
