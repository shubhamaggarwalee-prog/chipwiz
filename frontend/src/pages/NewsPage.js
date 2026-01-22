import React, { useState, useEffect } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import { newsApi } from '../lib/api';
import { Button } from '../components/ui/button';
import { 
  Newspaper, 
  Clock, 
  ExternalLink, 
  Filter,
  ChevronRight,
  TrendingUp,
  Sun,
  Package,
  Factory,
  Layers,
  Cpu,
  Brain,
  GitBranch,
  Database,
  RefreshCw
} from 'lucide-react';

const iconMap = {
  sun: Sun,
  package: Package,
  factory: Factory,
  layers: Layers,
  cpu: Cpu,
  brain: Brain,
  'git-branch': GitBranch,
  database: Database,
  newspaper: Newspaper
};

const NewsPage = () => {
  const { articleId } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const [articles, setArticles] = useState([]);
  const [categories, setCategories] = useState([]);
  const [featuredNews, setFeaturedNews] = useState([]);
  const [selectedArticle, setSelectedArticle] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState(searchParams.get('category') || '');
  const [dailyBrief, setDailyBrief] = useState(null);
  const [loading, setLoading] = useState(true);
  const [scraping, setScraping] = useState(false);

  // Fetch categories and featured news
  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const [catsRes, featuredRes] = await Promise.all([
          newsApi.getCategories(),
          newsApi.getFeatured()
        ]);
        setCategories(catsRes.data);
        setFeaturedNews(featuredRes.data);
      } catch (error) {
        console.error('Error fetching initial data:', error);
      }
    };
    fetchInitialData();
  }, []);

  // Fetch articles
  useEffect(() => {
    const fetchArticles = async () => {
      setLoading(true);
      try {
        const params = {};
        if (selectedCategory) params.category = selectedCategory;
        
        const response = await newsApi.getNews(params);
        setArticles(response.data);
      } catch (error) {
        console.error('Error fetching news:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchArticles();
  }, [selectedCategory]);

  // Fetch single article
  useEffect(() => {
    const fetchArticle = async () => {
      if (!articleId) {
        setSelectedArticle(null);
        return;
      }
      
      try {
        const response = await newsApi.getArticle(articleId);
        setSelectedArticle(response.data);
      } catch (error) {
        console.error('Error fetching article:', error);
      }
    };
    fetchArticle();
  }, [articleId]);

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    if (category) {
      setSearchParams({ category });
    } else {
      setSearchParams({});
    }
  };

  const handleScrapeNews = async () => {
    setScraping(true);
    try {
      await newsApi.triggerScrape();
      // Refresh articles after scrape
      setTimeout(async () => {
        const response = await newsApi.getNews({});
        setArticles(response.data);
        setScraping(false);
      }, 3000);
    } catch (error) {
      console.error('Scrape error:', error);
      setScraping(false);
    }
  };

  const fetchDailyBrief = async () => {
    try {
      const response = await newsApi.getDailyBrief();
      setDailyBrief(response.data);
    } catch (error) {
      console.error('Error fetching daily brief:', error);
    }
  };

  // Article detail view
  if (selectedArticle) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="article-detail-page">
        <div className="container-app py-8">
          <Link 
            to="/news" 
            className="inline-flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900 mb-6 dark:text-slate-400 dark:hover:text-white"
          >
            <ChevronRight className="h-4 w-4 rotate-180" />
            Back to News
          </Link>

          <article className="card-base p-6 lg:p-10 max-w-4xl mx-auto">
            {/* Category Badge */}
            <div className="flex items-center gap-3 mb-4">
              <span className="px-3 py-1 bg-blue-50 text-blue-600 rounded-full text-sm font-medium capitalize dark:bg-blue-900/30 dark:text-blue-400">
                {selectedArticle.category}
              </span>
              {selectedArticle.is_breaking && (
                <span className="px-3 py-1 bg-red-50 text-red-600 rounded-full text-sm font-medium dark:bg-red-900/30 dark:text-red-400">
                  Breaking
                </span>
              )}
            </div>

            <h1 className="text-3xl lg:text-4xl font-semibold mb-4">{selectedArticle.title}</h1>
            
            <div className="flex flex-wrap items-center gap-4 text-sm text-slate-500 mb-8 pb-6 border-b border-slate-200 dark:border-slate-700">
              <span className="flex items-center gap-1">
                <Clock className="h-4 w-4" />
                {new Date(selectedArticle.published_at).toLocaleDateString()}
              </span>
              <a 
                href={selectedArticle.source_url} 
                target="_blank" 
                rel="noopener noreferrer"
                className="flex items-center gap-1 text-blue-600 hover:text-blue-700"
              >
                {selectedArticle.source}
                <ExternalLink className="h-4 w-4" />
              </a>
            </div>

            {/* Summary */}
            <div className="prose-semi">
              <p className="text-lg leading-relaxed mb-6">{selectedArticle.summary}</p>
              
              {selectedArticle.content && (
                <div className="mb-8">
                  <p className="leading-relaxed">{selectedArticle.content}</p>
                </div>
              )}

              {/* Impact Analysis */}
              {selectedArticle.impact_analysis && (
                <div className="p-6 bg-blue-50 rounded-xl mb-6 dark:bg-blue-900/20">
                  <h3 className="font-medium text-blue-700 mb-2 flex items-center gap-2 dark:text-blue-400">
                    <TrendingUp className="h-5 w-5" />
                    Impact Analysis
                  </h3>
                  <p className="text-slate-700 dark:text-slate-300">{selectedArticle.impact_analysis}</p>
                </div>
              )}

              {/* Why It Matters */}
              {selectedArticle.why_it_matters && (
                <div className="p-6 bg-slate-100 rounded-xl mb-6 dark:bg-slate-800">
                  <h3 className="font-medium mb-2">Why This Matters</h3>
                  <p className="text-slate-600 dark:text-slate-400">{selectedArticle.why_it_matters}</p>
                </div>
              )}

              {/* Tags */}
              {selectedArticle.tags?.length > 0 && (
                <div className="flex flex-wrap gap-2 mt-6">
                  {selectedArticle.tags.map((tag, i) => (
                    <span key={i} className="px-3 py-1 bg-slate-100 rounded-full text-sm dark:bg-slate-800">
                      {tag}
                    </span>
                  ))}
                </div>
              )}
            </div>
          </article>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="news-page">
      <div className="container-app py-8">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
          <div>
            <h1 className="text-3xl font-semibold mb-2">Semiconductor News</h1>
            <p className="text-slate-600 dark:text-slate-400">
              Curated updates from official sources with AI-powered analysis
            </p>
          </div>
          <div className="flex gap-2">
            <Button 
              variant="outline" 
              onClick={fetchDailyBrief}
              data-testid="daily-brief-btn"
            >
              Daily Brief
            </Button>
            <Button 
              onClick={handleScrapeNews}
              disabled={scraping}
              data-testid="refresh-news-btn"
            >
              <RefreshCw className={`h-4 w-4 mr-2 ${scraping ? 'animate-spin' : ''}`} />
              {scraping ? 'Updating...' : 'Refresh'}
            </Button>
          </div>
        </div>

        {/* Daily Brief Modal */}
        {dailyBrief && (
          <div className="card-base p-6 mb-8 border-l-4 border-blue-500">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold">Daily Brief</h2>
              <button 
                onClick={() => setDailyBrief(null)}
                className="text-slate-400 hover:text-slate-600"
              >
                ✕
              </button>
            </div>
            <p className="text-slate-600 dark:text-slate-400 leading-relaxed whitespace-pre-wrap">
              {dailyBrief.brief}
            </p>
          </div>
        )}

        {/* Categories */}
        <div className="flex flex-wrap gap-2 mb-8">
          <Button
            variant={selectedCategory === '' ? 'default' : 'outline'}
            size="sm"
            onClick={() => handleCategoryChange('')}
            data-testid="category-all"
          >
            All
          </Button>
          {categories.map((cat) => {
            const IconComponent = iconMap[cat.icon] || Newspaper;
            return (
              <Button
                key={cat.id}
                variant={selectedCategory === cat.id ? 'default' : 'outline'}
                size="sm"
                onClick={() => handleCategoryChange(cat.id)}
                className="gap-2"
                data-testid={`category-${cat.id}`}
              >
                <IconComponent className="h-4 w-4" />
                {cat.name}
                {cat.count > 0 && (
                  <span className="ml-1 text-xs opacity-70">({cat.count})</span>
                )}
              </Button>
            );
          })}
        </div>

        {/* Featured News */}
        {!selectedCategory && featuredNews.length > 0 && (
          <section className="mb-8">
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <TrendingUp className="h-5 w-5 text-orange-500" />
              Featured
            </h2>
            <div className="grid md:grid-cols-2 gap-4">
              {featuredNews.slice(0, 2).map((article) => (
                <Link
                  key={article.article_id}
                  to={`/news/${article.article_id}`}
                  className="card-base p-6 hover:-translate-y-1 transition-all duration-300"
                  data-testid={`featured-${article.article_id}`}
                >
                  <div className="flex items-center gap-2 mb-3">
                    <span className="px-2 py-0.5 bg-orange-100 text-orange-600 text-xs rounded dark:bg-orange-900/30 dark:text-orange-400">
                      Featured
                    </span>
                    <span className="text-xs text-slate-500 capitalize">{article.category}</span>
                  </div>
                  <h3 className="text-lg font-medium mb-2 line-clamp-2">{article.title}</h3>
                  <p className="text-sm text-slate-600 dark:text-slate-400 line-clamp-2">{article.summary}</p>
                </Link>
              ))}
            </div>
          </section>
        )}

        {/* News List */}
        <section>
          <h2 className="text-lg font-semibold mb-4">
            {selectedCategory ? `${selectedCategory.toUpperCase()} News` : 'Latest News'}
          </h2>

          {loading ? (
            <div className="flex items-center justify-center h-64">
              <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
            </div>
          ) : articles.length > 0 ? (
            <div className="space-y-4">
              {articles.map((article) => (
                <Link
                  key={article.article_id}
                  to={`/news/${article.article_id}`}
                  className="card-base p-6 block hover:border-blue-300 transition-colors"
                  data-testid={`article-${article.article_id}`}
                >
                  <div className="flex flex-col md:flex-row md:items-start gap-4">
                    <div className="flex-1">
                      <div className="flex flex-wrap items-center gap-2 mb-2">
                        <span className="px-2 py-0.5 bg-slate-100 text-slate-600 text-xs rounded capitalize dark:bg-slate-700 dark:text-slate-300">
                          {article.category}
                        </span>
                        {article.is_breaking && (
                          <span className="px-2 py-0.5 bg-red-100 text-red-600 text-xs rounded dark:bg-red-900/30 dark:text-red-400">
                            Breaking
                          </span>
                        )}
                      </div>
                      <h3 className="text-lg font-medium mb-2">{article.title}</h3>
                      <p className="text-slate-600 dark:text-slate-400 line-clamp-2 mb-3">
                        {article.summary}
                      </p>
                      <div className="flex flex-wrap items-center gap-4 text-sm text-slate-500">
                        <span className="flex items-center gap-1">
                          <Clock className="h-4 w-4" />
                          {new Date(article.published_at).toLocaleDateString()}
                        </span>
                        <span>{article.source}</span>
                        {article.tags?.slice(0, 3).map((tag, i) => (
                          <span key={i} className="px-2 py-0.5 bg-slate-50 rounded text-xs dark:bg-slate-800">
                            {tag}
                          </span>
                        ))}
                      </div>
                    </div>
                    <ChevronRight className="h-5 w-5 text-slate-400 hidden md:block" />
                  </div>
                </Link>
              ))}
            </div>
          ) : (
            <div className="text-center py-16">
              <Newspaper className="h-16 w-16 text-slate-300 mx-auto mb-4" />
              <h3 className="text-lg font-medium mb-2">No news available</h3>
              <p className="text-slate-600 dark:text-slate-400 mb-4">
                Click "Refresh" to fetch the latest semiconductor news
              </p>
              <Button onClick={handleScrapeNews} disabled={scraping}>
                <RefreshCw className={`h-4 w-4 mr-2 ${scraping ? 'animate-spin' : ''}`} />
                Fetch News
              </Button>
            </div>
          )}
        </section>
      </div>
    </div>
  );
};

export default NewsPage;
