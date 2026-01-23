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

---

## CHANGELOG

### January 23, 2026 - P1 Features Complete

#### AI Assistant Compare Feature ✅
- Detects comparison queries (patterns: "Compare X vs Y", "X versus Y", "difference between X and Y")
- Returns structured output: Summary → Comparison Table → Advantages → Manufacturing Implications → Recommendation
- Citations for both technologies being compared
- Comparison-specific follow-up questions

#### Encyclopedia Expansion ✅
- Expanded from 19 → 37 topics
- Added 2 new categories:
  - **Memory Technologies** (4 topics): DRAM, NAND Flash, SRAM, Emerging Memory
  - **Applications** (2 topics): AI Accelerator Chips, Automotive Semiconductors
- New topics also added to: Testing & Metrology, Manufacturing, Nodes & Scaling, Foundries

#### Semantic Search ✅
- AI-powered search using GPT-5.2
- Natural language queries like "which packaging is best for AI chips"
- Returns ranked results with relevance scores (0.0-1.0)
- Each result includes reason for relevance
- Fallback to keyword search for short queries

#### User Preference Persistence ✅
- Backend `/api/preferences/` endpoint
- Stores: theme, difficulty, email_frequency, subscribed_topics, notification settings
- Server sync for authenticated users
- localStorage fallback for anonymous users

#### Resend Email Integration ✅
- Real API key configured (re_SiXJEn9m_Kgpx8PxVycdgFuryG1TJ42Gg)
- Using onboarding@resend.dev sender (no domain verification required for testing)
- Subscription endpoints functional

#### Mixed Content Error Fixed ✅
- Changed axios baseURL to relative `/api` instead of absolute URLs
- Eliminated http:// calls in https:// environment

### January 22, 2026 - Initial Implementation
- Google OAuth authentication
- Encyclopedia with 19 topics across 10 categories
- News scraping from public RSS feeds
- AI Assistant with GPT-5.2 and citations
- Research Reports with PDF export
- Background scheduler for news (6-hour intervals)
- Full frontend with React + Tailwind + Shadcn

---

## Current State

### Backend APIs
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/google/login` | GET | Initiate Google OAuth |
| `/api/auth/me` | GET | Get current user |
| `/api/encyclopedia/tree` | GET | Knowledge tree |
| `/api/encyclopedia/semantic-search` | GET | AI-powered search |
| `/api/encyclopedia/topics/{slug}/pdf` | GET | Download topic PDF |
| `/api/assistant/chat` | POST | AI chat with compare support |
| `/api/reports/` | GET | List reports |
| `/api/reports/{slug}/pdf` | GET | Download report PDF |
| `/api/news/` | GET | List news articles |
| `/api/subscriptions/` | GET/POST | Manage subscriptions |
| `/api/preferences/` | GET/PUT/PATCH | User preferences |

### Encyclopedia Statistics
- **Categories:** 12
- **Topics:** 37
- **Categories:** Fundamentals, Devices, Manufacturing, Materials, Packaging, Design & EDA, Nodes & Scaling, Foundries & Companies, Reliability & Yield, Testing & Metrology, Memory Technologies, Applications

### Test Results
- **Backend:** 100% (15/15 tests passed)
- **Frontend:** 100%
- **Test file:** `/app/test_reports/iteration_4.json`

---

## Remaining Backlog

### P1 - High Priority
1. **Expand Encyclopedia to 100+ topics** - Currently at 37, add ~65 more
   - Focus areas: Manufacturing processes, Advanced packaging, Materials, Nodes & scaling
2. **Real email delivery testing** - Test actual inbox delivery with user email
3. **AI Session continuity** - Persist last AI session for authenticated users

### P2 - Medium Priority
1. **Advanced search filters** - Filter by category, difficulty, date
2. **Bookmarking system** - Save favorite topics/reports
3. **Reading history** - Track user's viewed content
4. **Offline support** - PWA capabilities

### P3 - Future
1. **Mobile app** - React Native
2. **Premium tier** - Advanced features, API access
3. **Team/Enterprise accounts** - Shared workspaces
4. **Interactive diagrams** - SVG visualizations for processes
5. **Video content** - Manufacturing process videos

---

## Tech Stack
- **Backend:** FastAPI, MongoDB (Motor async driver), Python 3.11
- **Frontend:** React 18, TailwindCSS, Shadcn/UI
- **AI:** OpenAI GPT-5.2 via Emergent LLM Key
- **Email:** Resend
- **Auth:** Emergent-managed Google OAuth

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
**All previously known issues have been resolved.**

## Changelog

### January 23, 2026
- ✅ **FIXED: Mixed Content Error** - Resolved frontend API blocking by switching to relative URLs in axios configuration (`baseURL: '/api'`)
- ✅ **VERIFIED: PDF Export** - Both report and encyclopedia topic PDF exports working correctly
- ✅ **VERIFIED: Encyclopedia Seeding** - 10 categories with 19 topics loaded from expanded_content.py
- ✅ **VERIFIED: News Scheduler** - Background job running every 6 hours, last successful run logged
- ✅ **VERIFIED: AI Assistant** - Chat endpoint returning detailed responses with citations
- ✅ **VERIFIED: Theme Toggle** - Dark/Light mode switching correctly

### January 22, 2026
- Initial implementation of all core features
- Backend API with FastAPI + MongoDB
- Frontend with React + Tailwind + Shadcn
- Google OAuth authentication
- Encyclopedia with 19 topics across 10 categories
- News scraping from public RSS feeds
- AI Assistant with GPT-5.2 integration
- Research reports with PDF export
