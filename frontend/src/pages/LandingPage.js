import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Button } from '../components/ui/button';
import { 
  BookOpen, 
  Newspaper, 
  MessageSquare, 
  FileText, 
  Bell, 
  ChevronRight,
  Cpu,
  Layers,
  Zap,
  Shield,
  ArrowRight
} from 'lucide-react';

const LandingPage = () => {
  const { login, isAuthenticated } = useAuth();

  const features = [
    {
      icon: BookOpen,
      title: 'Semiconductor Encyclopedia',
      description: 'Deep, structured knowledge base with technical explanations, diagrams, and equations.'
    },
    {
      icon: Newspaper,
      title: 'Curated News Engine',
      description: 'AI-powered news aggregation from official sources with impact analysis.'
    },
    {
      icon: MessageSquare,
      title: 'AI Research Assistant',
      description: 'GPT-5.2 powered assistant with citation-backed answers for technical queries.'
    },
    {
      icon: FileText,
      title: 'Research Reports',
      description: 'TechInsights-style analysis reports based on public sources.'
    },
    {
      icon: Bell,
      title: 'Topic Subscriptions',
      description: 'Stay informed with topic-based alerts and digests.'
    },
    {
      icon: Shield,
      title: 'Source Transparency',
      description: 'Every piece of information is cited and verified from public sources.'
    }
  ];

  const topics = [
    { name: 'EUV Lithography', slug: 'euv-lithography', icon: Zap },
    { name: 'FinFET Technology', slug: 'finfet-technology', icon: Cpu },
    { name: 'GAAFET/Nanosheet', slug: 'gaafet-nanosheet', icon: Layers },
    { name: 'CoWoS Packaging', slug: 'cowos-packaging', icon: Layers },
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-b from-slate-50 to-white dark:from-slate-900 dark:to-slate-800 overflow-hidden">
        {/* Background Pattern */}
        <div className="absolute inset-0 opacity-5">
          <div className="absolute inset-0" style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`
          }} />
        </div>

        <div className="container-app relative">
          <div className="py-24 md:py-32 lg:py-40">
            <div className="max-w-4xl mx-auto text-center">
              {/* Badge */}
              <div className="inline-flex items-center gap-2 px-4 py-2 bg-blue-50 text-blue-600 rounded-full text-sm font-medium mb-8 dark:bg-blue-900/30 dark:text-blue-400">
                <Cpu className="h-4 w-4" />
                AI-Powered Semiconductor Research
              </div>

              {/* Main Headline */}
              <h1 className="text-4xl sm:text-5xl lg:text-6xl font-semibold tracking-tight text-slate-900 dark:text-white mb-6">
                The Intelligence Platform for{' '}
                <span className="text-gradient">Semiconductor Professionals</span>
              </h1>

              {/* Subheadline */}
              <p className="text-lg md:text-xl text-slate-600 dark:text-slate-300 mb-10 max-w-2xl mx-auto leading-relaxed">
                Structured knowledge, curated news, and AI-powered research assistance. 
                Built for engineers, researchers, and industry analysts.
              </p>

              {/* CTA Buttons */}
              <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                {isAuthenticated ? (
                  <Link to="/dashboard">
                    <Button className="btn-primary text-lg px-8 py-4" data-testid="get-started-btn">
                      Go to Dashboard
                      <ArrowRight className="ml-2 h-5 w-5" />
                    </Button>
                  </Link>
                ) : (
                  <Button 
                    onClick={login} 
                    className="btn-primary text-lg px-8 py-4"
                    data-testid="get-started-btn"
                  >
                    Get Started Free
                    <ArrowRight className="ml-2 h-5 w-5" />
                  </Button>
                )}
                <Link to="/encyclopedia">
                  <Button variant="outline" className="text-lg px-8 py-4" data-testid="explore-btn">
                    Explore Encyclopedia
                  </Button>
                </Link>
              </div>

              {/* Trust Indicators */}
              <div className="mt-12 flex flex-wrap items-center justify-center gap-8 text-sm text-slate-500">
                <div className="flex items-center gap-2">
                  <Shield className="h-4 w-4 text-green-500" />
                  Public Sources Only
                </div>
                <div className="flex items-center gap-2">
                  <FileText className="h-4 w-4 text-blue-500" />
                  Citation-Backed
                </div>
                <div className="flex items-center gap-2">
                  <Zap className="h-4 w-4 text-yellow-500" />
                  GPT-5.2 Powered
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Topics */}
      <section className="py-16 bg-white dark:bg-slate-900">
        <div className="container-app">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-semibold mb-4">Explore Semiconductor Topics</h2>
            <p className="text-slate-600 dark:text-slate-400">
              Deep technical content with multiple difficulty levels
            </p>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {topics.map((topic) => (
              <Link
                key={topic.slug}
                to={`/encyclopedia/${topic.slug}`}
                className="group card-base p-6 hover:-translate-y-1 transition-all duration-300"
                data-testid={`topic-${topic.slug}`}
              >
                <topic.icon className="h-8 w-8 text-blue-500 mb-4" />
                <h3 className="font-medium mb-2 group-hover:text-blue-600 transition-colors">
                  {topic.name}
                </h3>
                <ChevronRight className="h-4 w-4 text-slate-400 group-hover:translate-x-1 transition-transform" />
              </Link>
            ))}
          </div>

          <div className="text-center mt-8">
            <Link to="/encyclopedia" className="text-blue-600 hover:text-blue-700 font-medium inline-flex items-center gap-1">
              View All Topics
              <ChevronRight className="h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="section-padding bg-slate-50 dark:bg-slate-800">
        <div className="container-app">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-semibold mb-4">
              Everything You Need for Semiconductor Research
            </h2>
            <p className="text-lg text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
              A comprehensive platform built for semiconductor professionals who demand accuracy and depth.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="card-base p-8 animate-fade-in"
                style={{ animationDelay: `${index * 100}ms` }}
                data-testid={`feature-${index}`}
              >
                <div className="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center mb-6 dark:bg-blue-900/30">
                  <feature.icon className="h-6 w-6 text-blue-600 dark:text-blue-400" />
                </div>
                <h3 className="text-xl font-medium mb-3">{feature.title}</h3>
                <p className="text-slate-600 dark:text-slate-400 leading-relaxed">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* AI Assistant Preview */}
      <section className="section-padding bg-white dark:bg-slate-900">
        <div className="container-app">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1.5 bg-blue-50 text-blue-600 rounded-full text-sm font-medium mb-6 dark:bg-blue-900/30 dark:text-blue-400">
                <MessageSquare className="h-4 w-4" />
                AI Research Assistant
              </div>
              <h2 className="text-3xl md:text-4xl font-semibold mb-6">
                Ask Complex Technical Questions
              </h2>
              <p className="text-lg text-slate-600 dark:text-slate-400 mb-8 leading-relaxed">
                Our GPT-5.2 powered assistant understands semiconductor terminology and provides 
                citation-backed answers at your chosen difficulty level.
              </p>
              <ul className="space-y-4 mb-8">
                {[
                  'Explain EUV stochastic defects at 2nm',
                  'Compare FinFET vs GAAFET yield challenges',
                  'Impact of CoWoS on AI accelerators'
                ].map((query, i) => (
                  <li key={i} className="flex items-start gap-3">
                    <div className="w-6 h-6 rounded-full bg-green-100 flex items-center justify-center flex-shrink-0 mt-0.5 dark:bg-green-900/30">
                      <ChevronRight className="h-4 w-4 text-green-600 dark:text-green-400" />
                    </div>
                    <span className="text-slate-700 dark:text-slate-300">{query}</span>
                  </li>
                ))}
              </ul>
              <Link to="/assistant">
                <Button className="btn-primary" data-testid="try-assistant-btn">
                  Try AI Assistant
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              </Link>
            </div>
            
            {/* Chat Preview */}
            <div className="card-base p-6 lg:p-8">
              <div className="space-y-4">
                <div className="chat-message user">
                  Explain how high-NA EUV improves resolution
                </div>
                <div className="chat-message assistant">
                  <p className="mb-3">
                    High-NA EUV lithography uses a larger numerical aperture (0.55 NA vs 0.33 NA) 
                    to improve resolution according to the Rayleigh criterion:
                  </p>
                  <div className="bg-slate-50 dark:bg-slate-900 rounded-lg p-3 font-mono text-sm mb-3">
                    R = k₁ × λ/NA
                  </div>
                  <p className="text-sm text-slate-600 dark:text-slate-400">
                    [Source: ASML Technology Overview]
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-padding bg-slate-900 text-white dark:bg-slate-950">
        <div className="container-app text-center">
          <h2 className="text-3xl md:text-4xl font-semibold mb-6">
            Ready to Accelerate Your Research?
          </h2>
          <p className="text-lg text-slate-400 mb-10 max-w-2xl mx-auto">
            Join engineers, researchers, and analysts using Semiconductor Intelligence 
            to stay ahead in the semiconductor industry.
          </p>
          {isAuthenticated ? (
            <Link to="/dashboard">
              <Button className="bg-white text-slate-900 hover:bg-slate-100 text-lg px-8 py-4" data-testid="cta-dashboard-btn">
                Go to Dashboard
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
            </Link>
          ) : (
            <Button 
              onClick={login}
              className="bg-white text-slate-900 hover:bg-slate-100 text-lg px-8 py-4"
              data-testid="cta-signup-btn"
            >
              Get Started Free
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
          )}
        </div>
      </section>
    </div>
  );
};

export default LandingPage;
