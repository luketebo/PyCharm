from os import error
import PyPDF2


def encrypt(old_path, new_path):
    """

    :param old_path:
    :param new_path:
    :return:
    """
    pass


def decrypt(old_path):
    """
    解密
    :param old_path:
    :return:
    """
    with open(old_path, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        if pdfReader.isEncrypted:
            for i in range(10000):
                pwd = str(i).zfill(4).replace(" ", "")
                print(pwd)
                try:
                    pdfReader.decrypt(pwd)
                except:
                    print("no")
                else:
                    print("success: " + pwd)
                    break
        else:
            print("no crypt")


if __name__ == "__main__":
    decrypt("D:\\Desktop\\1.pptx")

    pass



