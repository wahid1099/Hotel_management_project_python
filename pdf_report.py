# pdf_report.py
from fpdf import FPDF

class PDFReport:
    def __init__(self, title):
        self.title = title
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def header(self):
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, self.title, 0, 1, "C")
        self.pdf.ln(10)

    def add_table(self, header, data):
        self.pdf.set_font("Arial", "B", 12)
        col_widths = [30, 30, 40, 50, 30, 30, 30]  # Custom column widths
        row_height = self.pdf.font_size * 1.5

        for i, col in enumerate(header):
            self.pdf.cell(col_widths[i], row_height, col, border=1)
        self.pdf.ln(row_height)

        self.pdf.set_font("Arial", size=12)
        for row in data:
            for i, item in enumerate(row):
                self.pdf.cell(col_widths[i], row_height, str(item), border=1)
            self.pdf.ln(row_height)

    def output(self, filename):
        self.pdf.output(filename)

def generate_bookings_report(bookings, filename):
    report = PDFReport("Bookings Report")
    report.header()
    header = ["Booking ID", "Room Number", "Customer Name", "User Email", "Check-in Date", "Check-out Date", "Total Bill"]
    data = bookings
    report.add_table(header, data)
    report.output(filename)
