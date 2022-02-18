import pyqrcode 
from pyqrcode import QRCode
import png

contact_tracing = """          --- CONTACT TRACING INFORMATION ---

Name: Angela E. Corpuz
Age: 19
Birthday: December 14, 2002
Address: Blk 47 Lot 6 Phase 2-E Mabuhay Homes, Brgy. Dila, Santa Rosa City, Laguna
Email: angelaescariocorpuz@gmail.com
Phone Number: 09451426999

Vaccination Details (as of Febraury 18, 2022):

First Dose:
     Date taken: October 25, 2021
     Vaccine Brand: Pfizer-BioNTech
     Place taken: Santa Rosa Sports Complex

Second Dose:
     Date taken: November 15, 2021
     Vaccine Brand: Pfizer-BioNTech
     Place taken: Santa Rosa Sports Complex

Booster Shot:
    *Haven't taken yet*
"""

CT_file = pyqrcode.create (contact_tracing)

CT_file.png ('Contact Tracing Details.png', scale = 6)