from fpdf import FPDF
from datetime import datetime

class IncomeCertificatePDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "", 12)
        self.cell(0, 10, "INCOME CERTIFICATE (Urban)", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.cell(0, 10, f"Generated on {datetime.today().strftime('%Y-%m-%d')}", 0, 0, "C")

pdf = IncomeCertificatePDF()
pdf.add_page()

# 1️⃣ Register the font
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)

# 2️⃣ Set it as active font
pdf.set_font("DejaVu", "", 12)

content = """
File No./Sl.No.: ___________
Date: 8th August 2025

This is to certify that the annual income from all sources of Sri Aktar e Aadil Khan,
S/o Ziaulhaqu Khan,
Resident of H.No 15/12, Shanti Nagar, Salt Pan Road, Near Rehaan Medical,
Antop Hill, Wadala East, Mumbai – 400037, District Mumbai,
is ₹ 6,00,000/- (Rupees Six Lakhs only).

The Aadhaar Card Number of the applicant is ————————————————

This certificate is issued for the purpose of filing application for scholarship/fee reimbursement,
and to avail benefits under any Government Welfare Scheme as requested by the applicant.
This certificate will be valid for a period of four (4) years from the date of issue.

Date: 8th August 2025

Office Seal                  Signature of the Tahsildar / Deputy Tahsildar

Name (in block letters): ____________________
Emp. Code: ____________________
Urban Area: Mumbai
District: Mumbai
"""

for line in content.strip().split("\n"):
    pdf.cell(0, 10, line.strip(), ln=True)

pdf.output("Income_Certificate_Urban_Aktar_Aadil_Khan.pdf")
