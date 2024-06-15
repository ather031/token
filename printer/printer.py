from datetime import datetime
from this import d
import MSWinPrint
from PIL import Image, ImageFont, ImageDraw
import qrcode
from api.util import generate_qr
from api.util import generate_appointment_receipt
import json



class Printer:
    _instance = None

    @staticmethod
    def get_instance():
        if not Printer._instance:
            if not Printer._instance:
                Printer._instance = Printer()
        return Printer._instance

    def __init__(self):
        self.x = 0
        self.y = 0
        self.th = 20
        self.center = 90
        

    def print_qr(self,data):
        
        mr_number = data['patient']['mr_number']
        qr = generate_qr(mr_number = mr_number, size=10)
        name = data['patient']['patient_name']
        
        doc = MSWinPrint.document()
        doc.begin_document()
        doc.setfont("Ariel", 12, bold=True)
        doc.text((self.center - 30, self.y), 'CMH Rawalpindi')
        self.y += self.th + 5
        doc.text((self.center - 30, self.y), 'Smart Hospitals')
        self.y += self.th
        doc.setfont("Ariel", 12, bold=False)
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        doc.text((self.x + 5, self.y), f'Name:     {name}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'MR # :     {mr_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        img = qr
        scale = 0.40
        neww = int(img.size[0] * scale)
        newh = int(img.size[1] * scale)
        page_width, _ = doc.getsize()
        page_center = int(page_width/2)
        doc.image((page_center - int(neww/2), self.y), img, (neww, newh))
        self.y += newh
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 2
        doc.text((self.x + 40, self.y), 'Powered By: AG Branch.')
        doc.end_document()
        self.reset()
    
    def print_create_appointment_receipt(self, data):
        qr = generate_qr(consumer_number = data['consumer_number'], size = 10)
        name = data['patient_name']
        mr_number = data['mr_number']
        consumer_number = data['consumer_number']
        fee = data["fee"]
        type = data['type']
        status = data['status']
        scheduled_date = data['scheduled_date']
        doc = MSWinPrint.document()
        doc.begin_document()
        doc.setfont("Ariel", 12, bold=True)
        doc.text((self.center - 30, self.y), 'CMH Rawalpindi')
        self.y += self.th + 5
        doc.text((self.center - 30, self.y), 'Military Hospitals')
        self.y += self.th
        doc.setfont("Ariel", 12, bold=False)
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        doc.text((self.x + 5, self.y), f'Name:')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{name}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'MR # :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{mr_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Consumer #')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{consumer_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Type :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{type}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Scheduled Date :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{scheduled_date}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Amount :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'Rs {fee}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Status :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{status}')  # 2 tabs
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        scale = 0.40
        neww = int(qr.size[0] * scale)
        newh = int(qr.size[1] * scale)
        doc.image((self.x + neww // 2 - 30, self.y), qr, (neww, newh))
        self.y += newh
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 2
        doc.text((self.x + 40, self.y), "Powered By: AG's Branch.")
        self.y += self.th + 5
        doc.setfont("Ariel", 10, bold=False)
        doc.text((self.x + 40, self.y), str( datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        doc.end_document()
        self.reset()
    
    def print_appointment_receipt(self, data):
        
        data = generate_appointment_receipt(data)
        qr = generate_qr(consumer_number = data['consumer_number'], size = 10)
        name = data['patient_name']
        mr_number = data['mr_number']
        consumer_number = data['consumer_number']
        fee = data["fee"]
        appointment_type = data['appointment_type']
        status = data['status']
        scheduled_date = data['scheduled_date']
        
        doc = MSWinPrint.document()
        doc.begin_document()
        doc.setfont("Ariel", 12, bold=True)
        doc.text((self.center - 30, self.y), 'CMH Rawalpindi')
        self.y += self.th + 5
        doc.text((self.center - 30, self.y), 'Military Hospitals')
        self.y += self.th
        doc.setfont("Ariel", 12, bold=False)
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        doc.text((self.x + 5, self.y), f'Name:')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{name}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'MR # :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{mr_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Consumer #')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{consumer_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Type :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{appointment_type}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Scheduled Date :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{scheduled_date}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Amount :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'Rs {fee}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Status :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{status}')  # 2 tabs
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        scale = 0.40
        neww = int(qr.size[0] * scale)
        newh = int(qr.size[1] * scale)
        # center qr
        # page_width, _ = doc.getsize()
        # page_center = int(page_width/2)
        # doc.image((page_center - int(neww/2), self.y), qr, (neww, newh))
        doc.image((self.x + neww // 2 - 30, self.y), qr, (neww, newh))
        self.y += newh
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 2
        doc.text((self.x + 40, self.y), "Powered By: AG's Branch.")
        self.y += self.th + 5
        doc.setfont("Ariel", 10, bold=False)
        doc.text((self.x + 40, self.y), str( datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        doc.end_document()
        self.reset()



    def print_topup_receipt(self, data):
        
        
        qr = generate_qr(consumer_number = data['consumer_number'], size = 10)
        name = data['patient_name']
        mr_number = data['mr_number']
        consumer_number = data['consumer_number']
        fee = data["fee"]
        type = data['type']
        status = data['status']
        
        doc = MSWinPrint.document()
        doc.begin_document()
        doc.setfont("Ariel", 12, bold=True)
        doc.text((self.center - 30, self.y), 'CMH Rawalpindi')
        self.y += self.th + 5
        doc.text((self.center - 30, self.y), 'Military Hospitals')
        self.y += self.th
        doc.setfont("Ariel", 12, bold=False)
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        doc.text((self.x + 5, self.y), f'Name:')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{name}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'MR # :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{mr_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Consumer #')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{consumer_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Type :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{type}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Amount :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'Rs {fee}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Status :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{status}')  # 2 tabs
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        scale = 0.40
        neww = int(qr.size[0] * scale)
        newh = int(qr.size[1] * scale)
        doc.image((self.x + neww // 2 - 30, self.y), qr, (neww, newh))
        self.y += newh
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 2
        doc.text((self.x + 40, self.y), "Powered By: AG's Branch.")
        self.y += self.th + 5
        doc.setfont("Ariel", 10, bold=False)
        doc.text((self.x + 40, self.y), str( datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        doc.end_document()
        self.reset()


    def print_advance_amount_receipt(self, data):
        qr = generate_qr(consumer_number = data['consumer_number'], size = 10)
        name = data['patient_name']
        mr_number = data['mr_number']
        consumer_number = data['consumer_number']
        fee = data["fee"]
        type = data['type']
        status = data['status']
        admission_number = data['admission_number']
        doc = MSWinPrint.document()
        doc.begin_document()
        doc.setfont("Ariel", 12, bold=True)
        doc.text((self.center - 30, self.y), 'CMH Rawalpindi')
        self.y += self.th + 5
        doc.text((self.center - 30, self.y), 'Military Hospitals')
        self.y += self.th
        doc.setfont("Ariel", 12, bold=False)
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        doc.text((self.x + 5, self.y), f'Name:')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{name}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'MR # :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{mr_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Consumer #')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{consumer_number}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Type :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{type}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Admission Number :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{admission_number}')  # 2 tabs
        self.y += self.th    
        doc.text((self.x + 5, self.y), f'Amount :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'Rs {fee}')  # 2 tabs
        self.y += self.th
        doc.text((self.x + 5, self.y), f'Status :')  # 2 tabs
        doc.text((self.x + 100, self.y), f'{status}')  # 2 tabs
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 5
        scale = 0.40
        neww = int(qr.size[0] * scale)
        newh = int(qr.size[1] * scale)
        doc.image((self.x + neww // 2 - 30, self.y), qr, (neww, newh))
        self.y += newh
        self.y += self.th
        doc.text((self.x, self.y), '______________________________________')
        self.y += self.th + 2
        doc.text((self.x + 40, self.y), "Powered By: AG's Branch.")
        self.y += self.th + 5
        doc.setfont("Ariel", 10, bold=False)
        doc.text((self.x + 40, self.y), str( datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        doc.end_document()
        self.reset()

    
        
    def print_letter(self, letter, letter2):
        doc = MSWinPrint.document()
        doc.begin_document()
        img = letter
        width, height = doc.getsize()
        doc.image((self.x, self.y), img, (int(width),int(height)))
        doc.end_page()
        self.reset()
        img2 = letter2
        width, height = doc.getsize()
        doc.image((self.x, self.y), img2, (int(width),int(height)))
        doc.end_document()
        self.reset()

    def print_card(self, front_side, back_side):
        doc = MSWinPrint.document()
        doc.begin_document()
        img = front_side
        width, height = doc.getsize()
        doc.image((self.x, self.y), img, (int(width),int(height)))
        doc.end_page()
        self.reset()
        img2 = back_side
        width, height = doc.getsize()
        doc.image((self.x, self.y), img2, (int(width),int(height)))
        doc.end_document()
        self.reset()



    def reset(self):
        self.x = 0
        self.y = 0
        self.th = 12
        self.center = 90



def generate_letter_head(appointment):
    try:
        doctor = appointment.doctor
        patient = appointment.patient
        doctor_name = "Dr."
        doctor_name += doctor.first_name + " " + doctor.last_name
        doctor_specialization = doctor.expertise
        doctor_qualification = doctor.qualification
        doctor_data = doctor_specialization + '\n' + doctor_qualification
        letter_date = str(datetime.now().strftime("%d-%m-%Y"))  
        patient_name = patient.first_name + " " + patient.last_name
        patient_age = str(patient.age)
        qr = generate_qr(doctor_name = doctor_name, patient_name = patient_name, time= datetime.now(), size = 9)
        img = Image.open("./media/letterhead_1.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("bahnschrift.ttf", 110)
        draw.text((208, 128),doctor_name,(0,0,0), font=font)
        font = ImageFont.truetype("bahnschrift.ttf", 60)
        draw.multiline_text((208,300), doctor_data,(0,0,0), font=font,spacing=30)
        font = ImageFont.truetype("arial.ttf", 50)
        draw.text((414,630), letter_date,(0,0,0), font=font,spacing=30)
        draw.text((1024,630), patient_name,(0,0,0), font=font,spacing=30)
        draw.text((2200,630), patient_age,(0,0,0), font=font,spacing=30)
        img.paste(qr, (2000, 3150))  
        img.show()
        
        return img
    except Exception as e:
        print(e) 
        
        
def generate_qr(**kwargs):
    size = kwargs["size"]
    qr = qrcode.QRCode(box_size=size)
    data = json.dumps(kwargs)
    qr.make(data)
    img = qr.make_image()
    
    return img