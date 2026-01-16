import os
import base64
from pathlib import Path


def get_template_path(lang_code):
    """Get the path to the template file based on language code."""
    module_dir = Path(__file__).parent
    template_file = f"template_{lang_code}.md"
    return module_dir / "resources" / template_file


def image_to_base64(image_path):
    """Convert image file to base64 data URI."""
    with open(image_path, 'rb') as img_file:
        img_data = base64.b64encode(img_file.read()).decode('utf-8')
    return f"data:image/png;base64,{img_data}"


def calculate_statistics(data):
    """Calculate additional statistics needed for the report."""
    total_creds = data['general'][0] + data['general'][1]
    recovered_creds = data['general'][0]
    recovered_percentage = f"{(recovered_creds / total_creds * 100):.1f}%"
    
    # Find highest and second highest password lengths
    lengths_with_counts = list(zip(data['lengths_x'], data['lengths_y']))
    sorted_lengths = sorted(lengths_with_counts, key=lambda x: x[1], reverse=True)
    
    highest_length = sorted_lengths[0][0] if len(sorted_lengths) > 0 else "N/A"
    second_highest_length = sorted_lengths[1][0] if len(sorted_lengths) > 1 else "N/A"
    
    # Calculate compliance percentage
    total_recovered = data['general'][0]
    compliant_count = data['compliance'][0]
    compliance_percentage = f"{(compliant_count / total_recovered * 100):.1f}%" if total_recovered > 0 else "0%"
    
    return {
        'TOTAL_AMOUNT_OF_CREDS': str(total_creds),
        'RECOVERED_AMOUNT_OF_CREDS': str(recovered_creds),
        'RECOVERED_AMOUNT_OF_CREDS_PERCENTAGE': recovered_percentage,
        'HIGHEST_PASSWORD_LENGTH_DISTRIBUTION': highest_length,
        'SECOND_HIGHEST_PASSWORD_LENGTH_DISTRIBUTION': second_highest_length,
        'COMPLIANCE_PASSWORD_PERCENTAGE': compliance_percentage
    }


def generate_report(data, outdir, lang_code, template_path=None):
    """Generate markdown report with embedded images.
    
    Args:
        data: Parsed analytics data
        outdir: Output directory for report and images
        lang_code: Language code (EN/ES) for default templates
        template_path: Optional custom template file path
    """
    # Use custom template if provided, otherwise use default
    if template_path:
        template_file = Path(template_path)
        if not template_file.exists():
            raise FileNotFoundError(f"Template file not found: {template_path}")
    else:
        template_file = get_template_path(lang_code)
    
    # Read template
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Calculate statistics
    stats = calculate_statistics(data)
    
    # Replace placeholders with actual values
    report_content = template_content
    for key, value in stats.items():
        report_content = report_content.replace(f"{{{{{key}}}}}", value)
    
    # Embed images as base64
    image_mappings = {
        "![Passwords Recovery Statistics](base64/imagedata)": "general_stats.png",
        "![Estadísticas de Contraseñas Recuperadas](base64/imagedata)": "general_stats.png",
        "![Password Length Distribution](base64/imagedata)": "length_distribution.png",
        "![Distribución de Longitud de Contraseñas](base64/imagedata)": "length_distribution.png",
        "![Password Policy Compliance Statistics](base64/imagedata)": "compliance_analysis.png",
        "![Análisis de Cumplimiento de Políticas](base64/imagedata)": "compliance_analysis.png",
        "![Top 10 Most Used Passwords](base64/imagedata)": "top_10_passwords.png",
        "![Top 10 Contraseñas Más Usadas](base64/imagedata)": "top_10_passwords.png"
    }
    
    for placeholder, image_file in image_mappings.items():
        image_path = os.path.join(outdir, image_file)
        if os.path.exists(image_path):
            base64_data = image_to_base64(image_path)
            # Extract alt text from placeholder
            alt_text = placeholder.split('](')[0][2:]
            replacement = f"![{alt_text}]({base64_data})"
            report_content = report_content.replace(placeholder, replacement)
    
    # Save report
    output_file = os.path.join(outdir, f"password_statistics_{lang_code}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return output_file
