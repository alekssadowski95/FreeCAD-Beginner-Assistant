from fpdf import FPDF
from fpdf.fonts import FontFace
import os
import subprocess
import platform
import sys


from fba_config import addon_work_dir

Path = os.path.join(os.path.dirname(__file__))
PathImages = os.path.join(Path, "model_images")
PathIcons = os.path.join(Path, "icons")
PathScreenshots = os.path.join(Path, "Screenshots")
PathDocs = os.path.join(Path, "Docs")
PathReports = os.path.join(Path, "reports_pdf")
sys.path.append(Path)
sys.path.append(PathImages)
sys.path.append(PathIcons)
sys.path.append(PathScreenshots)
sys.path.append(PathDocs)
sys.path.append(PathReports)

ONE_INCH = 25.4  # millimeters


def freecad_assistant_pdf_report_header(freecad_report_pdf):
    freecad_report_pdf.set_font("Arial", style="B", size=21)
    freecad_report_pdf.cell(200, 10, txt="Report", ln=True, align="L")

    freecad_report_pdf.set_font("Arial", style="", size=8.5)
    freecad_report_pdf.set_text_color(128, 128, 128)
    freecad_report_pdf.cell(200, 5, txt="FreeCAD Beginner Assistant", ln=True, align="L")

    return freecad_report_pdf


def freecad_assistant_pdf_report_summary_text(freecad_report_pdf, filename, run_date, rank, points_got, points_max):
    freecad_report_pdf.set_text_color(0, 0, 0)
    freecad_report_pdf.set_font("Arial", style="", size=13.5)
    freecad_report_pdf.cell(200, 8, txt="Points: " + points_got + " / " + points_max, ln=True, align="L")
    freecad_report_pdf.cell(200, 8, txt="Rank: " + rank, ln=True, align="L")

    freecad_report_pdf.set_font("Arial", style="", size=8.5)
    freecad_report_pdf.cell(200, 6, txt="Date: " + run_date, ln=True, align="L")
    freecad_report_pdf.cell(200, 6, txt="File: " + filename, ln=True, align="L")

    return freecad_report_pdf


def freecad_assistant_convert_dict_data_to_array_data(freecad_best_practices_dict):
    freecad_report_table_array = [
        (  # Header
            "ID",
            "What the user has done",
            "What negative (and positive) effect that has",
            "How to resolve the issue",
            "Status",
        ),
    ]

    for item in freecad_best_practices_dict:
        freecad_report_table_array.append(
            (str(item["id"]), item["action"], item["effect"], item["solution"], item["status"])
        )

    return freecad_report_table_array


def freecad_assistant_pdf_report_table(freecad_report_pdf, freecad_report_table_array):
    table_width = freecad_report_pdf.w - (2 * ONE_INCH)
    num_cols = 5
    row_height = 10
    all_equal_col_width = table_width / num_cols

    # Custom column variables
    id_col_width = all_equal_col_width * (1 / 3)
    id_col_neg_space = all_equal_col_width - id_col_width
    status_col_width = all_equal_col_width * (2 / 3)
    status_col_neg_space = all_equal_col_width - status_col_width
    total_neg_space = id_col_neg_space + status_col_neg_space
    custom_col_width_count = 2

    # Text column variables
    equal_col_count = num_cols - custom_col_width_count
    text_col_width = all_equal_col_width + total_neg_space / equal_col_count

    freecad_report_pdf.set_font("Arial", size=10)
    freecad_report_pdf.set_line_width(0.2)
    light_blue = (216, 226, 243)
    dark_blue = (68, 113, 196)
    white = (255, 255, 255)
    headings_style = FontFace(emphasis="BOLD", color=white, fill_color=dark_blue)

    with freecad_report_pdf.table(
        headings_style=headings_style,
        repeat_headings=0,
        text_align="LEFT",
        line_height=6,
        cell_fill_color=light_blue,
        cell_fill_mode="ROWS",
        width=table_width,
        col_widths=(id_col_width, text_col_width, text_col_width, text_col_width, status_col_width),
    ) as table:
        for data_row in freecad_report_table_array:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    return freecad_report_pdf


def freecad_assistant_pdf_report_footer(freecad_report_pdf):
    screenshot = os.path.join(PathIcons, "owl-2.png")
    freecad_report_pdf.image(
        screenshot,
        x=ONE_INCH,
        y=freecad_report_pdf.y,
        w=20,
    )

    freecad_report_pdf.ln(50)  # Add Space in millimeters

    freecad_report_pdf.set_font("Arial", style="", size=8.5)

    # Define text with hyperlinks
    text1 = "This report was auto-generated with the "
    link_text1 = "FreeCAD Beginner Assistant"
    text2 = "."
    link1 = "https://github.com/alekssadowski95/FreeCAD-Beginner-Assistant/tree/main"

    # Add text with hyperlink for the first line
    freecad_report_pdf.write(6, text1)
    freecad_report_pdf.set_text_color(0, 0, 255)  # Blue color for the link text
    link1_id = freecad_report_pdf.add_link()
    freecad_report_pdf.write(6, link_text1, link1)
    freecad_report_pdf.set_text_color(0, 0, 0)  # Reset color to black
    freecad_report_pdf.write(6, text2)
    freecad_report_pdf.ln(6)

    freecad_report_pdf.cell(
        200,
        6,
        txt="Do you like getting automatic feedback while working with FreeCAD? Help us improve the project.",
        ln=True,
        align="L",
    )

    return freecad_report_pdf


# Takes in a formatted dict to generate a FreeCAD assistant PDF report.
def freecad_assistant_pdf_report(freecad_report_dict, pdf_path):
    run_date = freecad_report_dict["date"]
    filename = freecad_report_dict["file"]
    model_image_name = freecad_report_dict["screenshot"]
    points_got = freecad_report_dict["pts-reached"]
    points_max = freecad_report_dict["pts-available"]
    rank = freecad_report_dict["rank"]
    freecad_report_table_array = freecad_assistant_convert_dict_data_to_array_data(
        freecad_report_dict["best-practices"]
    )

    pdf = FPDF()

    pdf.set_left_margin(ONE_INCH)
    pdf.set_right_margin(ONE_INCH)
    pdf.set_top_margin(ONE_INCH)
    pdf.set_auto_page_break(auto=True, margin=ONE_INCH)

    pdf.add_page()

    pdf = freecad_assistant_pdf_report_header(pdf)  # Header
    pdf.ln(10)  # Add Space in millimeters
    pdf.image(model_image_name, x=ONE_INCH, y=pdf.y, w=(pdf.w - (2 * ONE_INCH)))
    pdf.ln(90)  # Add Space in millimeters
    pdf = freecad_assistant_pdf_report_summary_text(pdf, filename, run_date, rank, points_got, points_max)
    pdf.ln(10)  # Add Space in millimeters
    pdf = freecad_assistant_pdf_report_table(pdf, freecad_report_table_array)  # Table
    pdf.ln(10)  # Add Space in millimeters
    pdf = freecad_assistant_pdf_report_footer(pdf)  # Footer

    pdf.output(pdf_path)  # Save the PDF


def run_report(result_dict):
    PDF_PATH = os.path.join(PathReports, "example.pdf")
    freecad_assistant_pdf_report(result_dict, PDF_PATH)

    if platform.system() == "Darwin":  # macOS
        subprocess.call(("open", PDF_PATH))
    elif platform.system() == "Windows":  # Windows
        os.startfile(PDF_PATH)
    else:  # Linux
        subprocess.call(("xdg-open", PDF_PATH))
