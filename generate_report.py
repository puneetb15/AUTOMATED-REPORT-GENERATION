import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def load_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def analyze_data(data):
    total_salary = sum(int(row['Salary']) for row in data)
    average_salary = total_salary / len(data)
    return average_salary

def generate_pdf(data, average_salary, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Employee Report")
    
    # Table Data
    table_data = [["Name", "Age", "Department", "Salary"]] + [
        [row['Name'], row['Age'], row['Department'], row['Salary']] for row in data
    ]
    
    # Create table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    # Draw table
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, height - 200)
    
    # Average Salary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 250, f"Average Salary: ${average_salary:.2f}")
    
    # Save PDF
    c.save()
    print(f"Report generated successfully: {output_file}")

def main():
    input_file = "data.csv"
    output_file = "report.pdf"
    
    data = load_data(input_file)
    average_salary = analyze_data(data)
    generate_pdf(data, average_salary, output_file)
    
if __name__ == "__main__":
    main()