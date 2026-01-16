import re
import argparse
from hashtocrack_report.image_generation import generate_all_charts
from hashtocrack_report.report_writer import generate_report

LANGS = {
    "EN": {
        "gen_title": "Passwords Recovery Statistics",
        "gen_labels": ["Cracked", "Not Cracked"],
        "len_title": "Password Length Distribution",
        "len_ylabel": "Count",
        "top_title": "Top 10 Most Used Passwords",
        "top_xlabel": "Count",
        "comp_title": "Password Policy Compliance",
        "comp_labels": ["Compliant", "Non-compliant"]
    },
    "ES": {
        "gen_title": "Estadísticas de Contraseñas Recuperadas",
        "gen_labels": ["Descifradas", "No Descifradas"],
        "len_title": "Distribución de Longitud de Contraseñas",
        "len_ylabel": "Cantidad",
        "top_title": "Top 10 Contraseñas Más Usadas",
        "top_xlabel": "Cantidad",
        "comp_title": "Análisis de Cumplimiento de Políticas",
        "comp_labels": ["Cumple", "No Cumple"]
    }
}

def parse_analytics(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {}
    
    # 1. General Stats
    cracked = re.search(r"Cracked:\s+(\d+)", content)
    not_cracked = re.search(r"Not Cracked:\s+(\d+)", content)
    data['general'] = [int(cracked.group(1)), int(not_cracked.group(1))]

    # 2. Length Distribution
    lengths = re.findall(r"(\d+)\s+chars:.*?\s+(\d+)\s+\(", content)
    data['lengths_x'] = [f"{x[0]} chars" for x in lengths]
    data['lengths_y'] = [int(x[1]) for x in lengths]

    # 3. Top 10 Most Used
    top_10 = re.findall(r"#\d+\s+(\S+)\s+(\d+)", content)
    data['top_x'] = [x[0] for x in top_10]
    data['top_y'] = [int(x[1]) for x in top_10]

    # 4. Compliance
    compliant = re.search(r"Compliant passwords:\s+(\d+)", content)
    non_compliant = re.search(r"Non-compliant passwords:\s+(\d+)", content)
    data['compliance'] = [int(compliant.group(1)), int(non_compliant.group(1))]

    return data

def generate_charts_legacy(data, outdir, lang_code):
    l = LANGS[lang_code]
    os.makedirs(outdir, exist_ok=True)

    # Chart 1: General Stats (Pie)
    fig = plt.figure(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    fig.patch.set_edgecolor('#cccccc')
    fig.patch.set_linewidth(1)
    
    ax = fig.add_subplot(111)
    colors = ['#ff9999','#66b3ff']
    explode = (0.02, 0.02)
    wedges, texts, autotexts = ax.pie(
        data['general'], 
        autopct='%1.1f%%', 
        colors=colors,
        explode=explode,
        wedgeprops={'edgecolor': 'none'}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontfamily('DejaVu Sans')
    
    ax.legend(l['gen_labels'], loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False, handlelength=1, handleheight=1, fontsize=14)
    fig.suptitle(l['gen_title'], fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    plt.subplots_adjust(left=0.1, right=0.75, top=0.88, bottom=0.05)
    
    plt.savefig(os.path.join(outdir, "general_stats.png"), facecolor='white', edgecolor='#cccccc', dpi=100)

    # Chart 2: Length (Bar)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(True, axis='y', color='#cccccc', linestyle='-', linewidth=0.5)  # Grey horizontal grid lines
    ax.set_axisbelow(True)  # Put grid behind bars
    colors_bar = plt.cm.tab10(range(len(data['lengths_x'])))  # Different color for each bar
    ax.bar(data['lengths_x'], data['lengths_y'], color=colors_bar, width=0.3)  # Narrower bars
    fig.suptitle(l['len_title'], fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    # Remove tick marks but keep labels
    ax.tick_params(axis='both', length=0)
    # Remove chart frame borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)  # Show bottom axis at 0
    ax.spines['bottom'].set_color('#cccccc')
    ax.spines['bottom'].set_linewidth(0.5)
    # Add light grey border to image
    fig.patch.set_edgecolor('#cccccc')
    fig.patch.set_linewidth(1)
    plt.subplots_adjust(left=0.08, right=0.95, top=0.92, bottom=0.08)
    # Remove ylabel (count label)
    plt.savefig(os.path.join(outdir, "length_distribution.png"), facecolor='white', edgecolor='#cccccc', dpi=100)

    # Chart 3: Top 10 (Horizontal Bar)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(True, axis='x', color='#cccccc', linestyle='-', linewidth=0.5)  # Grey vertical grid lines
    ax.set_axisbelow(True)  # Put grid behind bars
    colors_top = plt.cm.tab10(range(len(data['top_x'])))  # Different color for each bar
    ax.barh(data['top_x'][::-1], data['top_y'][::-1], color=colors_top[::-1], height=0.3)  # Narrower bars
    fig.suptitle(l['top_title'], fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    # Remove tick marks but keep labels
    ax.tick_params(axis='both', length=0)
    # Remove chart frame borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)  # Show left axis at 0
    ax.spines['left'].set_color('#cccccc')
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_visible(False)
    # Add light grey border to image
    fig.patch.set_edgecolor('#cccccc')
    fig.patch.set_linewidth(1)
    plt.subplots_adjust(left=0.15, right=0.95, top=0.92, bottom=0.08)
    # Remove xlabel (count label)
    plt.savefig(os.path.join(outdir, "top_10_passwords.png"), facecolor='white', edgecolor='#cccccc', dpi=100)

    # Chart 4: Compliance (Pie)
    fig = plt.figure(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    fig.patch.set_edgecolor('#cccccc')
    fig.patch.set_linewidth(1)
    
    ax = fig.add_subplot(111)
    colors = ['#99ff99','#ffcc99']
    explode = (0.02, 0.02)
    wedges, texts, autotexts = ax.pie(
        data['compliance'], 
        autopct='%1.1f%%', 
        colors=colors,
        explode=explode,
        wedgeprops={'edgecolor': 'none'}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontfamily('DejaVu Sans')
    
    ax.legend(l['comp_labels'], loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False, handlelength=1, handleheight=1, fontsize=14)
    fig.suptitle(l['comp_title'], fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    plt.subplots_adjust(left=0.1, right=0.75, top=0.88, bottom=0.05)
    
    plt.savefig(os.path.join(outdir, "compliance_analysis.png"), facecolor='white', edgecolor='#cccccc', dpi=100)

def main():
    parser = argparse.ArgumentParser(description="Process password analytics into charts and generate report.")
    parser.add_argument("file", help="Path to the analytics report file")
    parser.add_argument("-l", "--language", choices=["EN", "ES"], default="EN", help="Report language (for default templates)")
    parser.add_argument("-o", "--outdir", default="./data", help="Output directory")
    parser.add_argument("-t", "--template", help="Path to custom template file (overrides -l/--language)")
    parser.add_argument("--charts-only", action="store_true", help="Generate only charts without report")
    
    args = parser.parse_args()
    
    try:
        data = parse_analytics(args.file)
        
        # Generate charts
        generate_all_charts(data, args.outdir, args.language)
        print(f"✓ Generated charts in {args.outdir}")
        
        # Generate report unless charts-only mode
        if not args.charts_only:
            report_path = generate_report(data, args.outdir, args.language, args.template)
            print(f"✓ Generated report: {report_path}")
        
    except Exception as e:
        print(f"Error: {e}")
