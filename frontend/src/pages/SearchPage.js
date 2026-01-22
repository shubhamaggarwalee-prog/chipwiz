import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { newsApi } from '../lib/api';
import { Button } from '../components/ui/button';
import { 
  Search as SearchIcon, 
  ChevronRight,
  BookOpen,
  Newspaper,
  Loader2
} from 'lucide-react';

const SearchPage = () => {
  const navigate = useNavigate();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;
    
    setLoading(true);
    try {
      const response = await newsApi.globalSearch(query);
      setResults(response.data);
    } catch (error) {
      console.error('Search error:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const debounce = setTimeout(() => {
      if (query.trim().length >= 2) {
        handleSearch();
      } else {
        setResults([]);
      }
    }, 300);
    
    return () => clearTimeout(debounce);
  }, [query]);

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="search-page">
      <div className="container-app py-12">
        {/* Search Header */}
        <div className="max-w-2xl mx-auto text-center mb-12">
          <h1 className="text-3xl font-semibold mb-4">Search</h1>
          <p className="text-slate-600 dark:text-slate-400 mb-8">
            Search across encyclopedia topics, news articles, and reports
          </p>
          
          {/* Search Input */}
          <div className="relative">
            <SearchIcon className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-slate-400" />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Search semiconductors, EUV, TSMC, FinFET..."
              className="w-full pl-12 pr-4 py-4 bg-white border border-slate-200 rounded-xl text-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 outline-none shadow-sm dark:bg-slate-800 dark:border-slate-700"
              autoFocus
              data-testid="search-input"
            />
            {loading && (
              <Loader2 className="absolute right-4 top-1/2 -translate-y-1/2 h-5 w-5 text-slate-400 animate-spin" />
            )}
          </div>
        </div>

        {/* Results */}
        {results.length > 0 && (
          <div className="max-w-2xl mx-auto">
            <p className="text-sm text-slate-500 mb-4">
              {results.length} result{results.length !== 1 ? 's' : ''} found
            </p>
            
            <div className="space-y-4">
              {results.map((result, index) => (
                <Link
                  key={`${result.type}-${result.id}`}
                  to={result.url}
                  className="card-base p-6 block hover:border-blue-300 transition-colors"
                  data-testid={`result-${index}`}
                >
                  <div className="flex items-start gap-4">
                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                      result.type === 'encyclopedia' 
                        ? 'bg-blue-50 dark:bg-blue-900/30' 
                        : 'bg-green-50 dark:bg-green-900/30'
                    }`}>
                      {result.type === 'encyclopedia' ? (
                        <BookOpen className="h-5 w-5 text-blue-600 dark:text-blue-400" />
                      ) : (
                        <Newspaper className="h-5 w-5 text-green-600 dark:text-green-400" />
                      )}
                    </div>
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <span className={`text-xs px-2 py-0.5 rounded capitalize ${
                          result.type === 'encyclopedia'
                            ? 'bg-blue-100 text-blue-600 dark:bg-blue-900/30 dark:text-blue-400'
                            : 'bg-green-100 text-green-600 dark:bg-green-900/30 dark:text-green-400'
                        }`}>
                          {result.type}
                        </span>
                        {result.category && (
                          <span className="text-xs text-slate-500">{result.category}</span>
                        )}
                      </div>
                      <h3 className="font-medium mb-1">{result.title}</h3>
                      <p className="text-sm text-slate-600 dark:text-slate-400 line-clamp-2">
                        {result.excerpt}
                      </p>
                    </div>
                    <ChevronRight className="h-5 w-5 text-slate-400 flex-shrink-0" />
                  </div>
                </Link>
              ))}
            </div>
          </div>
        )}

        {/* Empty State */}
        {query.length >= 2 && !loading && results.length === 0 && (
          <div className="max-w-2xl mx-auto text-center py-12">
            <SearchIcon className="h-16 w-16 text-slate-300 mx-auto mb-4" />
            <h3 className="text-lg font-medium mb-2">No results found</h3>
            <p className="text-slate-600 dark:text-slate-400">
              Try different keywords or browse the encyclopedia
            </p>
            <Link to="/encyclopedia" className="mt-4 inline-block">
              <Button variant="outline">Browse Encyclopedia</Button>
            </Link>
          </div>
        )}

        {/* Suggestions when empty */}
        {query.length < 2 && (
          <div className="max-w-2xl mx-auto">
            <h3 className="text-sm font-medium text-slate-500 mb-4">Popular Searches</h3>
            <div className="flex flex-wrap gap-2">
              {['EUV', 'FinFET', 'GAAFET', 'TSMC', 'CoWoS', '3nm', 'HBM', 'Chiplet'].map((term) => (
                <button
                  key={term}
                  onClick={() => setQuery(term)}
                  className="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm hover:bg-slate-50 transition-colors dark:bg-slate-800 dark:border-slate-700 dark:hover:bg-slate-700"
                >
                  {term}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SearchPage;
