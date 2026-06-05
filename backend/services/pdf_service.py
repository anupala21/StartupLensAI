from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    validation,
    competitors,
    market,
    blueprint,
    filename="StartupLens_Report.pdf"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(
        Paragraph(
            "StartupLens AI Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Validation
    content.append(
        Paragraph(
            "Validation Results",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(validation),
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    # Competitors
    content.append(
        Paragraph(
            "Competitor Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(competitors),
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    # Market Research
    content.append(
        Paragraph(
            "Market Research",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(market),
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    # Blueprint
    content.append(
        Paragraph(
            "Startup Blueprint",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(blueprint),
            styles["BodyText"]
        )
    )

    doc.build(content)

    return filename