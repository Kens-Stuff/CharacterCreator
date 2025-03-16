import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_character_sheet(character_data, pdf_path):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    header_style = styles["Heading2"]
    body_style = styles["Normal"]
    attribute_style = ParagraphStyle(name='AttributeStyle', parent=body_style, textColor=colors.black, fontSize=12)

    content = []

    content.append(Paragraph("D&D Character Sheet", title_style))
    content.append(Paragraph("<b>Character Information:</b>", header_style))
    
    for key, value in character_data.items():
        if isinstance(value, dict):
            content.append(Paragraph("<b>" + key.capitalize() + ":</b>", header_style))
            for sub_key, sub_value in value.items():
                content.append(Paragraph(f"{sub_key.capitalize()}: {sub_value}", attribute_style))
        elif isinstance(value, list):
            content.append(Paragraph("<b>" + key.capitalize() + ":</b>", header_style))
            for item in value:
                content.append(Paragraph("- " + item, attribute_style))
        else:
            content.append(Paragraph(f"<b>{key.capitalize()}:</b> {value}", attribute_style))
        
        content.append(Paragraph("", body_style)) # Add an empty paragraph for spacing

    doc.build(content)


def create_from_json(char):
    # JSON string of the D&D character
    character_json = char

    # Parse JSON string to Python dictionary
    character_data = json.loads(character_json)

    # Generate PDF
    create_character_sheet(character_data, "character_sheet.pdf")
    
    #communicate
    print(f"Character sheet created successfully: {file_name}")

