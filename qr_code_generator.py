import qrcode
from PIL import Image, ImageDraw

def create_qr_code(data: str, box_size: int = 10, border: int = 4, error_correction=qrcode.constants.ERROR_CORRECT_L) -> qrcode.QRCode:
    """
    Create a QR code object with the specified parameters.
    
    Args:
    data (str): The data to encode in the QR code (URL, local file path, text, etc.).
    box_size (int): The size of each box in the QR code grid.
    border (int): The width of the border (in boxes).
    error_correction: The error correction level for the QR code.
    
    Returns:
    qrcode.QRCode: A QRCode object with the encoded data.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr

def save_qr_code_image(qr: qrcode.QRCode, file_name: str, fill_color: str = 'black', back_color: str = 'white', add_frame: bool = True) -> None:
    """
    Generate and save the QR code image from the given QRCode object, with an optional frame around it.
    
    Args:
    qr (qrcode.QRCode): The QR code object to convert to an image.
    file_name (str): The file name to save the image.
    fill_color (str): The color of the QR code itself.
    back_color (str): The background color of the QR code.
    add_frame (bool): Whether to add a frame around the QR code.
    """
    img = qr.make_image(fill=fill_color, back_color=back_color)

    if add_frame:
        # Add a frame around the QR code
        frame_thickness = 20  # Adjust this for frame thickness
        frame_color = 'black'  # Color of the frame
        img_with_frame = Image.new('RGB', (img.size[0] + frame_thickness * 2, img.size[1] + frame_thickness * 2), frame_color)
        img_with_frame.paste(img, (frame_thickness, frame_thickness))
        img = img_with_frame

    img.save(file_name)
    print(f"QR code saved as {file_name}")

def generate_qr_code_for_website(url: str, file_name: str) -> None:
    """
    Generate a QR code for a website URL and save it as an image.
    
    Args:
    url (str): The website URL to encode.
    file_name (str): The name of the file where the QR code will be saved.
    """
    qr = create_qr_code(url)
    save_qr_code_image(qr, file_name)

def generate_qr_code_for_pdf(pdf_url: str, file_name: str) -> None:
    """
    Generate a QR code for a PDF link and save it as an image.
    
    Args:
    pdf_url (str): The URL to the PDF file to encode.
    file_name (str): The name of the file where the QR code will be saved.
    """
    qr = create_qr_code(pdf_url)
    save_qr_code_image(qr, file_name)

def generate_qr_code_for_social_media(profile_url: str, file_name: str) -> None:
    """
    Generate a QR code for a social media profile link and save it as an image.
    
    Args:
    profile_url (str): The URL of the social media profile.
    file_name (str): The name of the file where the QR code will be saved.
    """
    qr = create_qr_code(profile_url)
    save_qr_code_image(qr, file_name)

def generate_qr_code_for_local_pdf(local_file_path: str, file_name: str) -> None:
    """
    Generate a QR code for a locally saved PDF file.
    
    Args:
    local_file_path (str): The local file path to the PDF.
    file_name (str): The name of the file where the QR code will be saved.
    """
    # Encode the local file path in the QR code
    file_path_data = f'file://{local_file_path}'
    qr = create_qr_code(file_path_data)
    save_qr_code_image(qr, file_name)

def generate_qr_code(data_type: str, data: str, file_name: str) -> None:
    """
    Generate a QR code based on the data type (website, PDF, local PDF, or social media link).
    
    Args:
    data_type (str): The type of data ('website', 'pdf', 'local_pdf', or 'social_media').
    data (str): The actual data to encode (URL, local path, or file link).
    file_name (str): The name of the file where the QR code will be saved.
    """
    if data_type == 'website':
        generate_qr_code_for_website(data, file_name)
    elif data_type == 'pdf':
        generate_qr_code_for_pdf(data, file_name)
    elif data_type == 'social_media':
        generate_qr_code_for_social_media(data, file_name)
    elif data_type == 'local_pdf':
        generate_qr_code_for_local_pdf(data, file_name)
    else:
        print(f"Error: Unsupported data type '{data_type}'")

# Example usage
if __name__ == '__main__':
    # Options: website, pdf, social_media, local_pdf
    data_type = 'local_pdf'
    
    # Provide the relevant data for each type
    if data_type == 'website':
        data = 'https://msamprovalaki.github.io'
    elif data_type == 'pdf':
        data = 'https://example.com/file.pdf'
    elif data_type == 'social_media':
        data = 'https://twitter.com/username'
    elif data_type == 'local_pdf':
        # Local file path to the PDF
        data = '/content/marina-samprovalaki.pdf'  # Replace with actual local path

    output_file = 'qr_code_with_frame1.png'
    generate_qr_code(data_type, data, output_file)
