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
- ✅ News Module: Scraping from public sources, categorization
- ✅ AI Assistant: GPT-5.2 powered chat with citations
- ✅ Reports Module: TechInsights-style research reports
- ✅ Subscriptions: Topic-based email subscriptions with Resend

### Frontend (React + Tailwind + Shadcn)
- ✅ Landing Page: Hero section, features, CTAs
- ✅ Encyclopedia: 3-column IDE-style layout (tree | content | context)
- ✅ News Page: Category filters, impact analysis
- ✅ AI Assistant: Chat interface with example queries, difficulty selection
- ✅ Reports Page: Report listings and detail views
- ✅ Subscriptions: Topic management, frequency settings
- ✅ Dashboard: User overview, quick actions
- ✅ Settings: Theme toggle, preferences
- ✅ Search: Global search across encyclopedia and news

### Seed Data
- 5 Encyclopedia Topics: EUV Lithography, FinFET, GAAFET, CoWoS, TSMC
- 10 Encyclopedia Categories: Fundamentals, Devices, Manufacturing, Materials, Packaging, Design & EDA, Nodes & Scaling, Foundries, Reliability, Testing
- 2 Research Reports: 3nm Process Node Analysis, AI Chip Packaging

### Integrations
- ✅ OpenAI GPT-5.2 via Emergent LLM Key
- ✅ Emergent Google OAuth for authentication
- ⏳ Resend email integration (configured, needs API key for production)

## Prioritized Backlog

### P0 - Critical (Next Steps)
1. Add Resend API key for production email delivery
2. Expand encyclopedia content (more topics per category)
3. Schedule news scraping (background job)

### P1 - High Priority
1. PDF export for research reports
2. User preferences persistence
3. News notification system (instant alerts)
4. More research report types

### P2 - Medium Priority
1. Advanced search with filters
2. User-contributed content moderation
3. Report generation UI for admins
4. Analytics dashboard

### P3 - Future Enhancements
1. Mobile app (React Native)
2. Premium tier with advanced features
3. Team/Enterprise accounts
4. API access for developers

## Tech Stack
- **Frontend**: React 19, Tailwind CSS, Shadcn UI, React Router
- **Backend**: FastAPI, Motor (async MongoDB)
- **Database**: MongoDB
- **AI**: OpenAI GPT-5.2 via Emergent LLM Key
- **Auth**: Emergent Google OAuth
- **Email**: Resend (configured)
- **Fonts**: IBM Plex Sans (headings), Inter (body), JetBrains Mono (code)

## API Endpoints
- `GET /api/` - Health check
- `POST /api/auth/session` - OAuth session exchange
- `GET /api/auth/me` - Current user
- `GET /api/encyclopedia/tree` - Knowledge tree
- `GET /api/encyclopedia/topics` - Topics with filtering
- `GET /api/encyclopedia/topics/{slug}` - Single topic
- `GET /api/news` - News articles
- `GET /api/news/categories` - News categories
- `POST /api/assistant/chat` - AI chat
- `GET /api/reports` - Research reports
- `GET /api/subscriptions/topics` - Available topics
- `GET /api/subscriptions` - User subscriptions
