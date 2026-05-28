"""
Enhanced Summary Report Generator for Marketing Campaign Analysis
Author: Data Analytics Team | Date: May 28, 2026
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import pandas as pd

# ==================== SETUP ====================
pdf_file = "Summary_Report_Enhanced.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Style definitions
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#1F4788'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#2E5C8A'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['BodyText'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    leading=14
)

# ==================== CONTENT BUILDING ====================
story = []

# ==================== PAGE 1: TITLE PAGE ====================
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("📊 MARKETING CAMPAIGN", title_style))
story.append(Paragraph("BUSINESS INSIGHTS REPORT", title_style))
story.append(Spacer(1, 0.3*inch))

subtitle = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor('#555555'),
    alignment=TA_CENTER,
    spaceAfter=6
)
story.append(Paragraph("Exploratory Data Analysis (EDA) & Strategic Recommendations", subtitle))
story.append(Spacer(1, 0.2*inch))

meta_style = ParagraphStyle(
    'Meta',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#777777'),
    alignment=TA_CENTER,
    spaceAfter=4
)
story.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%B %d, %Y')}", meta_style))
story.append(Paragraph("<b>Organization:</b> SkillCraft Technology — Data Analytics Internship", meta_style))
story.append(Paragraph("<b>Domain:</b> Marketing Analytics | <b>Task:</b> 04", meta_style))
story.append(Spacer(1, 0.4*inch))

# Quick metrics box
metrics_data = [
    ['📈 Total Customers', '2,236'],
    ['💰 Total Revenue', '$1.35M'],
    ['✅ Campaign Responses', '1,000'],
    ['🎯 Store Purchases', '12,959']
]
metrics_table = Table(metrics_data, colWidths=[2.5*inch, 2*inch])
metrics_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F0F4F8')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1F4788')),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
]))
story.append(metrics_table)
story.append(PageBreak())

# ==================== PAGE 2: EXECUTIVE SUMMARY ====================
story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

exec_summary = """
This report presents a comprehensive Exploratory Data Analysis of 2,236 customers from 5 marketing campaigns. 
The analysis focuses on understanding customer behavior, identifying high-value segments, and optimizing marketing 
channel allocation for maximum ROI.

<b>Key Takeaways:</b><br/>
• <b>Wine & Meat dominate revenue:</b> These two product categories account for 77% of total revenue ($680K + $373K out of $1.35M)<br/>
• <b>Store channel leads:</b> Physical store purchases represent 39% of all transactions (12,959 purchases)<br/>
• <b>Campaign 5 outperforms:</b> The final campaign achieved 334 responses, 11x better than Campaign 2's performance<br/>
• <b>High-income customers drive growth:</b> Premium and High segments account for 85%+ of revenue despite being smaller customer groups<br/>
"""
story.append(Paragraph(exec_summary, normal_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("REPORT STRUCTURE", heading_style))
report_structure = """
<b>1. Data Overview:</b> Dataset composition, cleaning methodology, and quality assurance<br/>
<b>2. Key Findings:</b> Detailed insights with data-backed conclusions<br/>
<b>3. Channel Performance:</b> ROI analysis across web, catalog, store, and deals<br/>
<b>4. Customer Segmentation:</b> High-value vs. low-value customer profiles<br/>
<b>5. Campaign Performance:</b> Response rates, acceptance trends, and optimization strategies<br/>
<b>6. Recommendations:</b> Actionable next steps for marketing strategy optimization<br/>
"""
story.append(Paragraph(report_structure, normal_style))
story.append(PageBreak())

# ==================== PAGE 3: DATA OVERVIEW ====================
story.append(Paragraph("DATA OVERVIEW & CLEANING", heading_style))

data_overview = """
<b>Dataset Source:</b> Marketing Campaign Dataset (Kaggle)<br/>
<b>Size After Cleaning:</b> 2,236 customers | 35 features | 5 campaigns<br/>
<b>Time Period:</b> 2012-2014 customer acquisition window<br/>
<br/>
<b>Cleaning Steps Performed:</b><br/>
1. <b>Missing Values:</b> 24 missing income values filled with median ($51,381)<br/>
2. <b>Outlier Detection:</b> Removed 4 records with impossible ages (>100 years) and extreme income values (>$200K)<br/>
3. <b>Feature Engineering:</b> Created 6 new calculated fields including Age, Total_Spent, Total_Purchases, Income_Segment<br/>
4. <b>Data Validation:</b> Verified data types and consistency across all 35 columns<br/>
<br/>
<b>Quality Metrics:</b> ✅ 100% data completeness | ✅ 0 remaining null values | ✅ No data integrity issues
"""
story.append(Paragraph(data_overview, normal_style))
story.append(PageBreak())

# ==================== PAGE 4: KEY FINDINGS ====================
story.append(Paragraph("KEY FINDINGS & INSIGHTS", heading_style))

# Finding 1
story.append(Paragraph("Finding 1: Store Channel Dominance", ParagraphStyle(
    'Finding', parent=styles['Heading3'], fontSize=12, textColor=colors.HexColor('#2E5C8A'),
    spaceBefore=8, spaceAfter=4, fontName='Helvetica-Bold')))
story.append(Paragraph(
    "<b>12,959 purchases through store channel (39% of total)</b> — Physical retail remains the strongest sales channel. "
    "This suggests customers prefer in-person shopping experiences and personal consultation for marketing products.",
    normal_style))
story.append(Spacer(1, 0.1*inch))

# Finding 2
story.append(Paragraph("Finding 2: Product Category Revenue", ParagraphStyle(
    'Finding', parent=styles['Heading3'], fontSize=12, textColor=colors.HexColor('#2E5C8A'),
    spaceBefore=8, spaceAfter=4, fontName='Helvetica-Bold')))
finding2_data = [
    ['Category', 'Revenue', '% of Total'],
    ['Wine', '$680,000', '50.2%'],
    ['Meat Products', '$373,000', '27.6%'],
    ['Gold Products', '$138,000', '10.2%'],
    ['Fish Products', '$97,000', '7.2%'],
    ['Fruits & Sweets', '$67,000', '4.9%'],
]
finding2_table = Table(finding2_data, colWidths=[1.8*inch, 1.5*inch, 1.5*inch])
finding2_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E5C8A')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('TOPPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F9F9F9')),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#DDDDDD')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(finding2_table)
story.append(Spacer(1, 0.1*inch))

# Finding 3
story.append(Paragraph("Finding 3: Campaign Performance Trajectory", ParagraphStyle(
    'Finding', parent=styles['Heading3'], fontSize=12, textColor=colors.HexColor('#2E5C8A'),
    spaceBefore=8, spaceAfter=4, fontName='Helvetica-Bold')))
story.append(Paragraph(
    "<b>Campaign 5 achieved 334 responses (11x better than Campaign 2's 30 responses)</b> — Shows significant "
    "improvement in campaign targeting and messaging over time. Suggests learnings from earlier campaigns were successfully applied.",
    normal_style))
story.append(Spacer(1, 0.1*inch))

# Finding 4
story.append(Paragraph("Finding 4: Premium Customer Value", ParagraphStyle(
    'Finding', parent=styles['Heading3'], fontSize=12, textColor=colors.HexColor('#2E5C8A'),
    spaceBefore=8, spaceAfter=4, fontName='Helvetica-Bold')))
story.append(Paragraph(
    "<b>Premium & High income segments = 85%+ of revenue</b> despite comprising only ~43% of customer base. "
    "This indicates strong revenue concentration and opportunity for premium customer expansion.",
    normal_style))
story.append(PageBreak())

# ==================== PAGE 5: RECOMMENDATIONS ====================
story.append(Paragraph("STRATEGIC RECOMMENDATIONS", heading_style))

rec_style = ParagraphStyle(
    'Recommendation',
    parent=styles['Normal'],
    fontSize=9.5,
    spaceAfter=8,
    leading=12,
    leftIndent=20,
    bulletIndent=10
)

recommendations = """
<b>1. BUDGET ALLOCATION OPTIMIZATION</b><br/>
   → Increase store channel investment by 25-30% (currently delivering 39% of purchases)<br/>
   → Maintain web & catalog channels at current levels; they serve niche demographics<br/>
   → Expected ROI Impact: +$180K-200K annual revenue<br/>
<br/>
<b>2. PRODUCT STRATEGY</b><br/>
   → Expand Wine & Meat product portfolios (driving 77% of revenue)<br/>
   → Create premium bundled offerings targeting High/Premium income segments<br/>
   → Evaluate profitability of Fruits/Sweets category (<5% revenue contribution)<br/>
<br/>
<b>3. CAMPAIGN OPTIMIZATION</b><br/>
   → Apply Campaign 5 winning strategies (messaging, timing, targeting) to future campaigns<br/>
   → Implement A/B testing framework to replicate the 11x improvement seen in Campaign 5<br/>
   → Target campaigns specifically at Premium segment customers (highest response rates)<br/>
<br/>
<b>4. CUSTOMER SEGMENTATION</b><br/>
   → Develop premium tier retention programs for High/Premium customers<br/>
   → Create growth initiatives to upgrade Mid-tier customers into Premium segment<br/>
   → Implement targeted re-engagement campaigns for Low-tier customers<br/>
<br/>
<b>5. DATA & MEASUREMENT</b><br/>
   → Establish monthly KPI dashboard tracking channel performance and ROI<br/>
   → Implement customer lifetime value (CLV) tracking by segment<br/>
   → Create early warning system for churn identification<br/>
"""
story.append(Paragraph(recommendations, normal_style))
story.append(PageBreak())

# ==================== PAGE 6: INTERACTIVE DASHBOARD ====================
story.append(Paragraph("INTERACTIVE DASHBOARD", heading_style))

dashboard_info = """
<b>Live Tableau Dashboard Available:</b><br/>
🔗 https://public.tableau.com/app/profile/mneddula.reena/viz/task4_17799486193580/MARKETINGCAMPAIGNBUSINESSINSIGHTSREPORT<br/>
<br/>
<b>Dashboard Features:</b><br/>
✓ <b>Purchases by Channel</b> — Bar chart comparing Web, Catalog, Store, and Deals channels<br/>
✓ <b>Revenue by Product Category</b> — Pie chart showing contribution breakdown<br/>
✓ <b>Campaign Acceptance Rates</b> — Performance trending across 5 campaigns<br/>
✓ <b>Income vs. Total Spending Relationship</b> — Scatter plot with trend line analysis<br/>
✓ <b>Product Spending by Customer Segment</b> — Stacked bar visualization<br/>
✓ <b>Interactive Filters:</b> Marital Status, Education Level, Income Segment<br/>
<br/>
<b>How to Use:</b> Visit the Tableau link above to filter data by customer demographics and explore patterns specific to your target segments.
"""
story.append(Paragraph(dashboard_info, normal_style))
story.append(Spacer(1, 0.2*inch))

# ==================== PAGE 7: CONCLUSION ====================
story.append(PageBreak())
story.append(Paragraph("CONCLUSION", heading_style))

conclusion = """
The analysis of 2,236 marketing campaign customers reveals clear opportunities for revenue optimization through:<br/>
<br/>
<b>1. Channel Strategy:</b> Store channel investment should be prioritized as the primary revenue driver<br/>
<b>2. Product Focus:</b> Wine and Meat categories represent core revenue pillars requiring continued innovation<br/>
<b>3. Customer Value:</b> Premium customers generate disproportionate value and warrant dedicated retention strategies<br/>
<b>4. Campaign Effectiveness:</b> Demonstrated ability to improve response rates 11x (Campaign 2→5) shows potential for continued optimization<br/>
<br/>
By implementing these recommendations, the marketing team can expect <b>15-25% revenue growth</b> within 12 months 
while maintaining operational efficiency.<br/>
<br/>
<b>Next Steps:</b> Schedule strategy alignment meeting to prioritize recommendations and establish implementation timeline.
"""
story.append(Paragraph(conclusion, normal_style))
story.append(Spacer(1, 0.3*inch))

# Footer
footer_style = ParagraphStyle(
    'Footer',
    parent=styles['Normal'],
    fontSize=8,
    textColor=colors.HexColor('#999999'),
    alignment=TA_CENTER,
    spaceAfter=4
)
story.append(Paragraph("___", footer_style))
story.append(Paragraph(
    f"Report Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')} | "
    "Data Source: Marketing Campaign Dataset | SkillCraft Technology",
    footer_style))

# ==================== BUILD PDF ====================
doc.build(story)
print(f"✅ Enhanced PDF Report Generated: {pdf_file}")
print(f"📄 Location: Current working directory")
print(f"📊 Report includes: Executive Summary, Data Analysis, Key Findings, Recommendations, and Dashboard Link")
