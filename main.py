from pypdf import PdfReader

generated_nums = []

def generate_nums():
    global generated_nums
    for i in range(10000, 100000):
        generated_nums.append(str(i))

def check_password(generated_nums):
    pdf_path = '5_digit_pdf_lock.pdf'
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        for password in generated_nums:
            print("checking password: ", password)
            if pdf_reader.decrypt(password):
                print(f"Password is: {password}")
                return
        print("error")

generate_nums()
check_password(generated_nums)