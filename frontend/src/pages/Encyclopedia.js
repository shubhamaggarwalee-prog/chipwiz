import React, { useState, useEffect } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import { encyclopediaApi } from '../lib/api';
import { Button } from '../components/ui/button';
import { ScrollArea } from '../components/ui/scroll-area';
import { 
  ChevronRight, 
  ChevronDown, 
  Search, 
  BookOpen,
  Atom,
  Cpu,
  Factory,
  Layers,
  Package,
  PencilRuler,
  TrendingDown,
  Building,
  ShieldCheck,
  Microscope,
  ExternalLink,
  Download
} from 'lucide-react';

const iconMap = {
  atom: Atom,
  cpu: Cpu,
  factory: Factory,
  layers: Layers,
  package: Package,
  'pencil-ruler': PencilRuler,
  'trending-down': TrendingDown,
  building: Building,
  'shield-check': ShieldCheck,
  microscope: Microscope
};

const Encyclopedia = () => {
  const { slug } = useParams();
  const [searchParams] = useSearchParams();
  const [tree, setTree] = useState([]);
  const [topic, setTopic] = useState(null);
  const [expandedCategories, setExpandedCategories] = useState({});
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [difficulty, setDifficulty] = useState('intermediate');
  const [loading, setLoading] = useState(true);

  // Fetch knowledge tree
  useEffect(() => {
    const fetchTree = async () => {
      try {
        const response = await encyclopediaApi.getTree();
        setTree(response.data);
        // Expand first category by default
        if (response.data.length > 0) {
          setExpandedCategories({ [response.data[0].category_id]: true });
        }
      } catch (error) {
        console.error('Error fetching tree:', error);
      }
    };
    fetchTree();
  }, []);

  // Fetch topic when slug changes
  useEffect(() => {
    const fetchTopic = async () => {
      if (!slug) {
        setTopic(null);
        setLoading(false);
        return;
      }

      setLoading(true);
      try {
        const response = await encyclopediaApi.getTopic(slug, difficulty);
        setTopic(response.data);
        // Expand parent category
        const parentCat = tree.find(cat => 
          cat.topics?.some(t => t.slug === slug)
        );
        if (parentCat) {
          setExpandedCategories(prev => ({ ...prev, [parentCat.category_id]: true }));
        }
      } catch (error) {
        console.error('Error fetching topic:', error);
        setTopic(null);
      } finally {
        setLoading(false);
      }
    };
    fetchTopic();
  }, [slug, difficulty, tree]);

  // Search
  useEffect(() => {
    const search = async () => {
      if (!searchQuery.trim()) {
        setSearchResults([]);
        return;
      }
      try {
        const response = await encyclopediaApi.search(searchQuery);
        setSearchResults(response.data);
      } catch (error) {
        console.error('Search error:', error);
      }
    };

    const debounce = setTimeout(search, 300);
    return () => clearTimeout(debounce);
  }, [searchQuery]);

  const toggleCategory = (categoryId) => {
    setExpandedCategories(prev => ({
      ...prev,
      [categoryId]: !prev[categoryId]
    }));
  };

  const getContent = () => {
    if (difficulty === 'beginner') return topic?.content_beginner;
    return topic?.content_advanced;
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="encyclopedia-page">
      <div className="container-app py-6">
        <div className="grid lg:grid-cols-[280px_1fr_320px] gap-6">
          {/* Left Sidebar - Knowledge Tree */}
          <aside className="card-base p-4 h-[calc(100vh-120px)] sticky top-24">
            {/* Search */}
            <div className="relative mb-4">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400" />
              <input
                type="text"
                placeholder="Search topics..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-10 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 outline-none dark:bg-slate-800 dark:border-slate-700"
                data-testid="encyclopedia-search"
              />
            </div>

            {/* Search Results */}
            {searchResults.length > 0 && (
              <div className="mb-4 p-2 bg-blue-50 rounded-lg dark:bg-blue-900/20">
                <p className="text-xs text-blue-600 mb-2 dark:text-blue-400">Search Results</p>
                {searchResults.slice(0, 5).map(result => (
                  <Link
                    key={result.id}
                    to={`/encyclopedia/${result.slug}`}
                    className="block p-2 text-sm hover:bg-blue-100 rounded dark:hover:bg-blue-900/40"
                    onClick={() => setSearchQuery('')}
                  >
                    {result.title}
                  </Link>
                ))}
              </div>
            )}

            {/* Tree */}
            <ScrollArea className="h-[calc(100%-60px)]">
              <div className="knowledge-tree pr-2">
                {tree.map((category) => {
                  const IconComponent = iconMap[category.icon] || BookOpen;
                  const isExpanded = expandedCategories[category.category_id];
                  
                  return (
                    <div key={category.category_id} className="mb-1">
                      <button
                        onClick={() => toggleCategory(category.category_id)}
                        className="w-full flex items-center gap-2 px-3 py-2 rounded-md text-sm font-medium hover:bg-slate-100 transition-colors dark:hover:bg-slate-800"
                        data-testid={`category-${category.slug}`}
                      >
                        {isExpanded ? (
                          <ChevronDown className="h-4 w-4 text-slate-400" />
                        ) : (
                          <ChevronRight className="h-4 w-4 text-slate-400" />
                        )}
                        <IconComponent className="h-4 w-4 text-slate-500" />
                        <span className="flex-1 text-left">{category.name}</span>
                        <span className="text-xs text-slate-400">
                          {category.topics?.length || 0}
                        </span>
                      </button>
                      
                      {isExpanded && category.topics?.length > 0 && (
                        <div className="ml-6 mt-1 space-y-0.5">
                          {category.topics.map((topicItem) => (
                            <Link
                              key={topicItem.topic_id}
                              to={`/encyclopedia/${topicItem.slug}`}
                              className={`knowledge-tree-item ${slug === topicItem.slug ? 'active' : ''}`}
                              data-testid={`topic-link-${topicItem.slug}`}
                            >
                              {topicItem.title}
                            </Link>
                          ))}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </ScrollArea>
          </aside>

          {/* Main Content */}
          <main className="card-base p-6 lg:p-8 min-h-[calc(100vh-120px)]">
            {loading ? (
              <div className="flex items-center justify-center h-64">
                <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
              </div>
            ) : topic ? (
              <article className="prose-semi" data-testid="topic-content">
                {/* Topic Header */}
                <div className="mb-8 pb-6 border-b border-slate-200 dark:border-slate-700">
                  <div className="flex items-center gap-2 text-sm text-slate-500 mb-3">
                    <Link to="/encyclopedia" className="hover:text-slate-700">Encyclopedia</Link>
                    <ChevronRight className="h-4 w-4" />
                    <span>{topic.title}</span>
                  </div>
                  
                  <h1 className="text-3xl lg:text-4xl font-semibold mb-4">{topic.title}</h1>
                  
                  <p className="text-lg text-slate-600 dark:text-slate-400 leading-relaxed">
                    {topic.overview}
                  </p>

                  {/* Difficulty Toggle */}
                  <div className="flex items-center gap-2 mt-6">
                    <span className="text-sm text-slate-500">Difficulty:</span>
                    <div className="flex gap-1 bg-slate-100 p-1 rounded-lg dark:bg-slate-800">
                      {['beginner', 'intermediate', 'advanced'].map((level) => (
                        <button
                          key={level}
                          onClick={() => setDifficulty(level)}
                          className={`px-3 py-1 text-sm rounded-md transition-colors capitalize ${
                            difficulty === level
                              ? 'bg-white shadow-sm dark:bg-slate-700'
                              : 'hover:bg-slate-200 dark:hover:bg-slate-700'
                          }`}
                          data-testid={`difficulty-${level}`}
                        >
                          {level}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Content */}
                <div className="whitespace-pre-wrap">
                  {getContent()?.split('\n').map((line, i) => {
                    if (line.startsWith('**') && line.endsWith('**')) {
                      return <h3 key={i} className="text-xl font-medium mt-6 mb-3">{line.replace(/\*\*/g, '')}</h3>;
                    }
                    if (line.startsWith('## ')) {
                      return <h2 key={i} className="text-2xl font-semibold mt-8 mb-4">{line.replace('## ', '')}</h2>;
                    }
                    if (line.startsWith('### ')) {
                      return <h3 key={i} className="text-xl font-medium mt-6 mb-3">{line.replace('### ', '')}</h3>;
                    }
                    if (line.startsWith('- ')) {
                      return <li key={i} className="ml-4">{line.replace('- ', '')}</li>;
                    }
                    if (line.startsWith('| ')) {
                      return <div key={i} className="font-mono text-sm bg-slate-50 p-2 dark:bg-slate-800">{line}</div>;
                    }
                    if (line.trim()) {
                      return <p key={i} className="mb-4">{line}</p>;
                    }
                    return null;
                  })}
                </div>

                {/* Manufacturing Challenges */}
                {topic.manufacturing_challenges?.length > 0 && (
                  <section className="mt-8">
                    <h2 className="text-2xl font-semibold mb-4">Manufacturing Challenges</h2>
                    <ul className="list-disc pl-6 space-y-2">
                      {topic.manufacturing_challenges.map((challenge, i) => (
                        <li key={i}>{challenge}</li>
                      ))}
                    </ul>
                  </section>
                )}

                {/* Applications */}
                {topic.applications?.length > 0 && (
                  <section className="mt-8">
                    <h2 className="text-2xl font-semibold mb-4">Applications</h2>
                    <div className="flex flex-wrap gap-2">
                      {topic.applications.map((app, i) => (
                        <span key={i} className="px-3 py-1 bg-blue-50 text-blue-700 rounded-full text-sm dark:bg-blue-900/30 dark:text-blue-400">
                          {app}
                        </span>
                      ))}
                    </div>
                  </section>
                )}

                {/* Advantages & Limitations */}
                <div className="grid md:grid-cols-2 gap-6 mt-8">
                  {topic.advantages?.length > 0 && (
                    <div className="p-4 bg-green-50 rounded-xl dark:bg-green-900/20">
                      <h3 className="font-medium text-green-700 mb-3 dark:text-green-400">Advantages</h3>
                      <ul className="space-y-2">
                        {topic.advantages.map((adv, i) => (
                          <li key={i} className="text-sm text-green-800 dark:text-green-300">• {adv}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  {topic.limitations?.length > 0 && (
                    <div className="p-4 bg-red-50 rounded-xl dark:bg-red-900/20">
                      <h3 className="font-medium text-red-700 mb-3 dark:text-red-400">Limitations</h3>
                      <ul className="space-y-2">
                        {topic.limitations.map((lim, i) => (
                          <li key={i} className="text-sm text-red-800 dark:text-red-300">• {lim}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              </article>
            ) : (
              <div className="flex flex-col items-center justify-center h-64 text-center">
                <BookOpen className="h-16 w-16 text-slate-300 mb-4" />
                <h2 className="text-xl font-semibold mb-2">Semiconductor Encyclopedia</h2>
                <p className="text-slate-600 dark:text-slate-400 mb-6">
                  Select a topic from the knowledge tree to start exploring
                </p>
                <Link to="/encyclopedia/euv-lithography">
                  <Button data-testid="explore-euv-btn">Start with EUV Lithography</Button>
                </Link>
              </div>
            )}
          </main>

          {/* Right Sidebar - Context Panel */}
          <aside className="hidden lg:block card-base p-4 h-[calc(100vh-120px)] sticky top-24">
            <ScrollArea className="h-full">
              {topic ? (
                <div className="space-y-6 pr-2">
                  {/* Equations */}
                  {topic.equations?.length > 0 && (
                    <section>
                      <h3 className="font-medium mb-3 text-sm uppercase tracking-wider text-slate-500">
                        Key Equations
                      </h3>
                      <div className="space-y-3">
                        {topic.equations.map((eq, i) => (
                          <div key={i} className="p-3 bg-slate-50 rounded-lg dark:bg-slate-800">
                            <code className="block text-sm font-mono mb-1">{eq.latex}</code>
                            <p className="text-xs text-slate-500">{eq.description}</p>
                          </div>
                        ))}
                      </div>
                    </section>
                  )}

                  {/* Diagrams */}
                  {topic.diagrams?.length > 0 && (
                    <section>
                      <h3 className="font-medium mb-3 text-sm uppercase tracking-wider text-slate-500">
                        Diagrams
                      </h3>
                      <div className="space-y-3">
                        {topic.diagrams.map((diagram, i) => (
                          <div key={i} className="p-3 bg-slate-50 rounded-lg dark:bg-slate-800">
                            <pre className="text-xs overflow-x-auto">{diagram.content}</pre>
                            <p className="text-xs text-slate-500 mt-2">{diagram.caption}</p>
                          </div>
                        ))}
                      </div>
                    </section>
                  )}

                  {/* Related Topics */}
                  {topic.related_topics_data?.length > 0 && (
                    <section>
                      <h3 className="font-medium mb-3 text-sm uppercase tracking-wider text-slate-500">
                        Related Topics
                      </h3>
                      <div className="space-y-2">
                        {topic.related_topics_data.map((related) => (
                          <Link
                            key={related.topic_id}
                            to={`/encyclopedia/${related.slug}`}
                            className="block p-3 rounded-lg hover:bg-slate-50 transition-colors dark:hover:bg-slate-800"
                          >
                            <p className="font-medium text-sm">{related.title}</p>
                            <p className="text-xs text-slate-500 line-clamp-2">{related.overview}</p>
                          </Link>
                        ))}
                      </div>
                    </section>
                  )}

                  {/* References */}
                  {topic.references?.length > 0 && (
                    <section>
                      <h3 className="font-medium mb-3 text-sm uppercase tracking-wider text-slate-500">
                        References
                      </h3>
                      <div className="space-y-2">
                        {topic.references.map((ref, i) => (
                          <a
                            key={i}
                            href={ref.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-start gap-2 p-2 rounded-lg hover:bg-slate-50 text-sm group dark:hover:bg-slate-800"
                          >
                            <ExternalLink className="h-4 w-4 mt-0.5 text-slate-400 group-hover:text-blue-500" />
                            <div>
                              <p className="text-blue-600 group-hover:text-blue-700">{ref.title}</p>
                              <p className="text-xs text-slate-500">{ref.source}</p>
                            </div>
                          </a>
                        ))}
                      </div>
                    </section>
                  )}

                  {/* Meta Info */}
                  <section className="text-xs text-slate-500 pt-4 border-t border-slate-200 dark:border-slate-700">
                    <p>Views: {topic.views}</p>
                    <p>Updated: {new Date(topic.updated_at).toLocaleDateString()}</p>
                  </section>
                </div>
              ) : (
                <div className="flex items-center justify-center h-full text-slate-400">
                  <p className="text-sm">Select a topic to view details</p>
                </div>
              )}
            </ScrollArea>
          </aside>
        </div>
      </div>
    </div>
  );
};

export default Encyclopedia;
