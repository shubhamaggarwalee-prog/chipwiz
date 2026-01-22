"""
PDF Export Module - Generate professional PDF reports
Clean layout suitable for analyst presentations and offline reading
"""
from io import BytesIO
from datetime import datetime, timezone
from typing import Dict, Any, List
import logging
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

logger = logging.getLogger(__name__)


def create_styles():
    """Create custom styles for the PDF"""
    styles = getSampleStyleSheet()
    
    # Title page styles
    styles.add(ParagraphStyle(
        name='MainTitle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A')
    ))
    
    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#64748B')
    ))
    
    # Section styles
    styles.add(ParagraphStyle(
        name='SectionTitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceBefore=20,
        spaceAfter=12,
        textColor=colors.HexColor('#0F172A'),
        borderPadding=5,
        borderWidth=0,
        borderColor=colors.HexColor('#006FEE'),
        leftIndent=0
    ))
    
    styles.add(ParagraphStyle(
        name='SubsectionTitle',
        parent=styles['Heading3'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=8,
        textColor=colors.HexColor('#334155')
    ))
    
    # Body text styles - use custom name to avoid conflict
    styles.add(ParagraphStyle(
        name='ReportBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#334155')
    ))
    
    styles.add(ParagraphStyle(
        name='Caption',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#64748B'),
        alignment=TA_CENTER
    ))
    
    # Special styles
    styles.add(ParagraphStyle(
        name='Disclaimer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#94A3B8'),
        alignment=TA_CENTER,
        spaceBefore=20
    ))
    
    styles.add(ParagraphStyle(
        name='Reference',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#006FEE'),
        leftIndent=20
    ))
    
    return styles


def generate_report_pdf(report: Dict[str, Any]) -> BytesIO:
    """
    Generate a professional PDF from a research report
    
    Args:
        report: Report data dictionary
        
    Returns:
        BytesIO buffer containing the PDF
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = create_styles()
    story = []
    
    # ==================== TITLE PAGE ====================
    story.append(Spacer(1, 2*inch))
    
    # Logo placeholder
    story.append(Paragraph("SEMICONDUCTOR INTELLIGENCE", styles['Subtitle']))
    story.append(Spacer(1, 0.5*inch))
    
    # Main title
    story.append(Paragraph(report.get('title', 'Research Report'), styles['MainTitle']))
    
    # Report type badge
    report_type = report.get('report_type', 'analysis').replace('_', ' ').title()
    story.append(Paragraph(f"<b>{report_type}</b>", styles['Subtitle']))
    story.append(Spacer(1, inch))
    
    # Author and date
    author = report.get('author', 'AI Research Team')
    created_at = report.get('created_at', datetime.now(timezone.utc).isoformat())
    if isinstance(created_at, str):
        try:
            created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        except:
            created_at = datetime.now(timezone.utc)
    
    story.append(Paragraph(f"<b>Author:</b> {author}", styles['ReportBody']))
    story.append(Paragraph(f"<b>Date:</b> {created_at.strftime('%B %d, %Y')}", styles['ReportBody']))
    story.append(Spacer(1, 2*inch))
    
    # Disclaimer on title page
    disclaimer = """
    <b>DISCLAIMER</b><br/>
    This report is based on publicly available information and AI-assisted analysis.
    It does not constitute investment, financial, or professional advice.
    All data should be independently verified before making decisions.
    """
    story.append(Paragraph(disclaimer, styles['Disclaimer']))
    
    story.append(PageBreak())
    
    # ==================== EXECUTIVE SUMMARY ====================
    story.append(Paragraph("Executive Summary", styles['SectionTitle']))
    
    exec_summary = report.get('executive_summary', '')
    if exec_summary:
        # Split by paragraphs and add each
        for para in exec_summary.split('\n\n'):
            if para.strip():
                story.append(Paragraph(para.strip(), styles['BodyText']))
    
    story.append(Spacer(1, 0.3*inch))
    
    # ==================== MAIN CONTENT SECTIONS ====================
    content_sections = report.get('content_sections', [])
    for section in content_sections:
        story.append(Paragraph(section.get('title', 'Section'), styles['SectionTitle']))
        
        content = section.get('content', '')
        if content:
            # Process markdown-like formatting
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                # Handle headers
                if line.startswith('## '):
                    story.append(Paragraph(line[3:], styles['SubsectionTitle']))
                elif line.startswith('### '):
                    story.append(Paragraph(line[4:], styles['SubsectionTitle']))
                # Handle bullet points
                elif line.startswith('- '):
                    story.append(Paragraph(f"• {line[2:]}", styles['BodyText']))
                # Handle tables (simplified)
                elif line.startswith('| '):
                    # Skip table formatting for now, just show as text
                    story.append(Paragraph(line.replace('|', ' | '), styles['BodyText']))
                # Regular paragraph
                elif line.startswith('**') and line.endswith('**'):
                    story.append(Paragraph(f"<b>{line[2:-2]}</b>", styles['BodyText']))
                else:
                    story.append(Paragraph(line, styles['BodyText']))
        
        story.append(Spacer(1, 0.2*inch))
    
    # ==================== DATA SOURCES ====================
    data_sources = report.get('data_sources', [])
    if data_sources:
        story.append(PageBreak())
        story.append(Paragraph("Data Sources", styles['SectionTitle']))
        
        for source in data_sources:
            story.append(Paragraph(f"• {source}", styles['BodyText']))
        
        story.append(Spacer(1, 0.3*inch))
    
    # ==================== ASSUMPTIONS ====================
    assumptions = report.get('assumptions', [])
    if assumptions:
        story.append(Paragraph("Key Assumptions", styles['SectionTitle']))
        
        for assumption in assumptions:
            story.append(Paragraph(f"• {assumption}", styles['BodyText']))
        
        story.append(Spacer(1, 0.3*inch))
    
    # ==================== RISKS & UNKNOWNS ====================
    risks = report.get('risks_unknowns', [])
    if risks:
        story.append(Paragraph("Risks & Unknowns", styles['SectionTitle']))
        
        for risk in risks:
            story.append(Paragraph(f"• {risk}", styles['BodyText']))
        
        story.append(Spacer(1, 0.3*inch))
    
    # ==================== REFERENCES ====================
    references = report.get('references', [])
    if references:
        story.append(PageBreak())
        story.append(Paragraph("References", styles['SectionTitle']))
        
        for i, ref in enumerate(references, 1):
            title = ref.get('title', 'Unknown')
            source = ref.get('source', '')
            url = ref.get('url', '')
            
            ref_text = f"[{i}] {title}"
            if source:
                ref_text += f" - {source}"
            story.append(Paragraph(ref_text, styles['Reference']))
        
        story.append(Spacer(1, 0.3*inch))
    
    # ==================== FINAL DISCLAIMER ====================
    story.append(Spacer(1, inch))
    
    final_disclaimer = f"""
    <b>About This Report</b><br/><br/>
    
    This report was generated by Semiconductor Intelligence Platform on {datetime.now(timezone.utc).strftime('%B %d, %Y at %H:%M UTC')}.
    
    <br/><br/>
    
    <b>Source Methodology:</b> This analysis is based exclusively on publicly available information 
    including company press releases, earnings transcripts, patent filings, academic publications, 
    and official announcements. No proprietary or confidential information was used.
    
    <br/><br/>
    
    <b>AI-Assisted Analysis:</b> Portions of this report were generated with AI assistance using 
    GPT-5.2. All content has been structured to provide educational and informational value. 
    Readers should verify critical information with primary sources.
    
    <br/><br/>
    
    © {datetime.now().year} Semiconductor Intelligence Platform. All rights reserved.
    """
    story.append(Paragraph(final_disclaimer, styles['Disclaimer']))
    
    # Build the PDF
    doc.build(story)
    buffer.seek(0)
    
    return buffer


def generate_encyclopedia_pdf(topic: Dict[str, Any], difficulty: str = "intermediate") -> BytesIO:
    """
    Generate a PDF from an encyclopedia topic
    
    Args:
        topic: Topic data dictionary
        difficulty: Content difficulty level
        
    Returns:
        BytesIO buffer containing the PDF
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = create_styles()
    story = []
    
    # Title
    story.append(Paragraph(topic.get('title', 'Topic'), styles['MainTitle']))
    story.append(Paragraph(f"Difficulty: {difficulty.title()}", styles['Subtitle']))
    story.append(Spacer(1, 0.5*inch))
    
    # Overview
    story.append(Paragraph("Overview", styles['SectionTitle']))
    story.append(Paragraph(topic.get('overview', ''), styles['BodyText']))
    story.append(Spacer(1, 0.3*inch))
    
    # Content based on difficulty
    content_key = f"content_{difficulty}" if difficulty != "intermediate" else "content_advanced"
    content = topic.get(content_key, topic.get('content_advanced', ''))
    
    if content:
        story.append(Paragraph("Technical Content", styles['SectionTitle']))
        for para in content.split('\n\n'):
            if para.strip():
                # Handle formatting
                if para.strip().startswith('**') and para.strip().endswith('**'):
                    story.append(Paragraph(f"<b>{para.strip()[2:-2]}</b>", styles['SubsectionTitle']))
                else:
                    story.append(Paragraph(para.strip(), styles['BodyText']))
    
    # Applications
    applications = topic.get('applications', [])
    if applications:
        story.append(Paragraph("Applications", styles['SectionTitle']))
        for app in applications:
            story.append(Paragraph(f"• {app}", styles['BodyText']))
    
    # Advantages & Limitations
    advantages = topic.get('advantages', [])
    limitations = topic.get('limitations', [])
    
    if advantages:
        story.append(Paragraph("Advantages", styles['SectionTitle']))
        for adv in advantages:
            story.append(Paragraph(f"• {adv}", styles['BodyText']))
    
    if limitations:
        story.append(Paragraph("Limitations", styles['SectionTitle']))
        for lim in limitations:
            story.append(Paragraph(f"• {lim}", styles['BodyText']))
    
    # References
    references = topic.get('references', [])
    if references:
        story.append(PageBreak())
        story.append(Paragraph("References", styles['SectionTitle']))
        for i, ref in enumerate(references, 1):
            ref_text = f"[{i}] {ref.get('title', '')} - {ref.get('source', '')}"
            story.append(Paragraph(ref_text, styles['Reference']))
    
    # Footer disclaimer
    story.append(Spacer(1, inch))
    disclaimer = f"""
    Generated from Semiconductor Intelligence Encyclopedia on {datetime.now(timezone.utc).strftime('%B %d, %Y')}.
    Content sourced from public information. Verify with primary sources for critical applications.
    """
    story.append(Paragraph(disclaimer, styles['Disclaimer']))
    
    doc.build(story)
    buffer.seek(0)
    
    return buffer
