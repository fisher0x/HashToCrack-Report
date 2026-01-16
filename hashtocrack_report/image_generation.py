import os
import matplotlib.pyplot as plt


def generate_general_stats_chart(data, outdir, labels, title):
    """Generate pie chart for general crack statistics."""
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
    
    ax.legend(labels, loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False, handlelength=1, handleheight=1, fontsize=14)
    fig.suptitle(title, fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    plt.subplots_adjust(left=0.1, right=0.75, top=0.88, bottom=0.05)
    
    plt.savefig(os.path.join(outdir, "general_stats.png"), facecolor='white', edgecolor='#cccccc', dpi=100)
    plt.close()


def generate_length_distribution_chart(data, outdir, title):
    """Generate bar chart for password length distribution."""
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(True, axis='y', color='#cccccc', linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)
    colors_bar = plt.cm.tab10(range(len(data['lengths_x'])))
    ax.bar(data['lengths_x'], data['lengths_y'], color=colors_bar, width=0.3)
    fig.suptitle(title, fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    ax.tick_params(axis='both', length=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_color('#cccccc')
    ax.spines['bottom'].set_linewidth(0.5)
    fig.patch.set_edgecolor('#cccccc')
    fig.patch.set_linewidth(1)
    plt.subplots_adjust(left=0.08, right=0.95, top=0.92, bottom=0.08)
    
    plt.savefig(os.path.join(outdir, "length_distribution.png"), facecolor='white', edgecolor='#cccccc', dpi=100)
    plt.close()


def generate_top_passwords_chart(data, outdir, title):
    """Generate horizontal bar chart for top 10 passwords."""
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(True, axis='x', color='#cccccc', linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)
    colors_top = plt.cm.tab10(range(len(data['top_x'])))
    ax.barh(data['top_x'][::-1], data['top_y'][::-1], color=colors_top[::-1], height=0.3)
    fig.suptitle(title, fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    ax.tick_params(axis='both', length=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_visible(False)
    fig.patch.set_edgecolor('#cccccc')
    fig.patch.set_linewidth(1)
    plt.subplots_adjust(left=0.15, right=0.95, top=0.92, bottom=0.08)
    
    plt.savefig(os.path.join(outdir, "top_10_passwords.png"), facecolor='white', edgecolor='#cccccc', dpi=100)
    plt.close()


def generate_compliance_chart(data, outdir, labels, title):
    """Generate pie chart for password policy compliance."""
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
    
    ax.legend(labels, loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False, handlelength=1, handleheight=1, fontsize=14)
    fig.suptitle(title, fontsize=20, fontfamily='DejaVu Sans', color='#4a4a4a')
    plt.subplots_adjust(left=0.1, right=0.75, top=0.88, bottom=0.05)
    
    plt.savefig(os.path.join(outdir, "compliance_analysis.png"), facecolor='white', edgecolor='#cccccc', dpi=100)
    plt.close()


def generate_all_charts(data, outdir, lang_code):
    """Generate all charts for the given data and language."""
    from hashtocrack_report.main import LANGS
    
    l = LANGS[lang_code]
    os.makedirs(outdir, exist_ok=True)
    
    generate_general_stats_chart(data, outdir, l['gen_labels'], l['gen_title'])
    generate_length_distribution_chart(data, outdir, l['len_title'])
    generate_top_passwords_chart(data, outdir, l['top_title'])
    generate_compliance_chart(data, outdir, l['comp_labels'], l['comp_title'])
