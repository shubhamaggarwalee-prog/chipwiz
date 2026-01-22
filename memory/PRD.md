# Semiconductor Intelligence Platform - PRD

## Overview
AI-powered semiconductor knowledge and research platform for engineers, researchers, students, analysts, and industry professionals.

## Original Problem Statement
Build a world-class, production-ready AI-powered Semiconductor Intelligence Platform featuring:
- Latest Semiconductor News Engine
- Deep, Structured Semiconductor Encyclopedia
- AI Research Assistant with Citations
- Topic-based Email & Push Subscriptions
- TechInsights-style Research Reports (OSINT-based)
- Modern, premium-grade Web UX

## User Personas
1. **Semiconductor Engineers** - Need deep technical content on manufacturing, devices, processes
2. **Researchers** - Require citation-backed information, academic-level content
3. **Students** - Need beginner-friendly explanations with progressive difficulty
4. **Industry Analysts** - Want competitive intelligence, market analysis, reports
5. **Professionals** - Need quick access to structured knowledge, news updates

## Core Requirements (Static)
- Legal compliance: Only public sources, no copyrighted material
- Source transparency: All content cited and traceable
- Multiple difficulty levels: Beginner, Intermediate, Advanced
- Light mode default with dark mode toggle
- WCAG-compliant accessibility
- Mobile-responsive design

## What's Been Implemented (January 22, 2026)

### Backend (FastAPI + MongoDB)
- ✅ Authentication: Emergent Google OAuth integration
- ✅ Encyclopedia Module: Categories, topics, search, tree structure
- ✅ News Module: Real web scraping from public sources (RSS feeds)
- ✅ AI Assistant: GPT-5.2 powered chat with citations
- ✅ Reports Module: TechInsights-style research reports
- ✅ Subscriptions: Topic-based email subscriptions with Resend
- ✅ Background Scheduler: Automated news scraping every 6 hours
- ✅ PDF Export: Professional PDF generation for reports and topics

### Frontend (React + Tailwind + Shadcn)
- ✅ Landing Page: Hero section, features, CTAs
- ✅ Encyclopedia: 3-column IDE-style layout (tree | content | context)
- ✅ News Page: Category filters, impact analysis
- ✅ AI Assistant: Chat interface with example queries, difficulty selection
- ✅ Reports Page: Report listings and detail views with PDF download
- ✅ Subscriptions: Topic management, frequency settings
- ✅ Dashboard: User overview, quick actions
- ✅ Settings: Theme toggle, preferences
- ✅ Search: Global search across encyclopedia and news

### Encyclopedia Content (19 Topics)
**Manufacturing (5 topics):**
- DUV Lithography, EUV Lithography, Photoresist Technology
- Plasma Etching, Thin Film Deposition

**Devices (2 topics):**
- FinFET Technology, GAAFET/Nanosheet Transistors

**Materials (3 topics):**
- Silicon (Si) Substrates, Silicon Carbide (SiC), Gallium Nitride (GaN)

**Packaging (4 topics):**
- CoWoS Packaging, Chiplet Architecture, Hybrid Bonding, HBM

**Nodes & Scaling (3 topics):**
- 2nm Process Node, 3nm Process Node, Backside Power Delivery

**Foundries (1 topic):**
- TSMC

**Reliability (1 topic):**
- Semiconductor Yield

### Research Reports (2 Reports)
- 3nm Process Node Analysis: TSMC vs Samsung vs Intel
- Advanced Packaging for AI Accelerators: The CoWoS Capacity Challenge

### Integrations
- ✅ OpenAI GPT-5.2 via Emergent LLM Key
- ✅ Emergent Google OAuth for authentication
- ✅ Resend email integration (configured with placeholder key)
- ✅ Background scheduler with news scraping (21 articles scraped)
- ✅ PDF export via ReportLab

## Prioritized Backlog

### P0 - Critical (Next Steps)
1. Replace placeholder Resend API key with production key
2. Deploy to production environment (resolves mixed content issues)
3. Add more encyclopedia topics (memory, testing/metrology categories)

### P1 - High Priority
1. User preference persistence to database
2. News instant alert notifications
3. Report scheduling/auto-generation
4. Encyclopedia content expansion (100+ topics)

### P2 - Medium Priority
1. Advanced search with faceted filters
2. User bookmarks and reading history
3. Report comparison tools
4. Analytics dashboard

### P3 - Future Enhancements
1. Mobile app (React Native)
2. Premium tier with advanced features
3. Team/Enterprise accounts with roles
4. API access for developers
5. Content contribution system

## Tech Stack
- **Frontend**: React 19, Tailwind CSS, Shadcn UI, React Router
- **Backend**: FastAPI, Motor (async MongoDB)
- **Database**: MongoDB
- **AI**: OpenAI GPT-5.2 via Emergent LLM Key
- **Auth**: Emergent Google OAuth
- **Email**: Resend (configured)
- **PDF**: ReportLab
- **Scheduler**: APScheduler (asyncio)
- **Fonts**: IBM Plex Sans (headings), Inter (body), JetBrains Mono (code)

## API Endpoints
- `GET /api/` - Health check with scheduler status
- `POST /api/auth/session` - OAuth session exchange
- `GET /api/auth/me` - Current user
- `GET /api/encyclopedia/tree` - Knowledge tree (19 topics)
- `GET /api/encyclopedia/topics` - Topics with filtering
- `GET /api/encyclopedia/topics/{slug}` - Single topic
- `GET /api/encyclopedia/topics/{slug}/pdf` - PDF export
- `GET /api/news` - News articles
- `GET /api/news/categories` - News categories
- `POST /api/news/scrape` - Trigger manual scrape
- `POST /api/assistant/chat` - AI chat with citations
- `GET /api/reports` - Research reports
- `GET /api/reports/{slug}/pdf` - PDF export
- `GET /api/subscriptions/topics` - Available topics (10)
- `GET /api/subscriptions` - User subscriptions

## Known Issues
1. Mixed content warning in Emergent preview environment (dev server config)
   - Workaround: Direct API calls work correctly
   - Resolution: Production deployment with HTTPS throughout
