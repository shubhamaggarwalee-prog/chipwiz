import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { encyclopediaApi, newsApi, assistantApi, subscriptionsApi } from '../lib/api';
import { Button } from '../components/ui/button';
import { 
  BookOpen, 
  Newspaper, 
  MessageSquare, 
  Bell,
  ChevronRight,
  TrendingUp,
  Clock,
  Zap
} from 'lucide-react';

const Dashboard = () => {
  const { user } = useAuth();
  const [recentTopics, setRecentTopics] = useState([]);
  const [latestNews, setLatestNews] = useState([]);
  const [chatSessions, setChatSessions] = useState([]);
  const [subscriptions, setSubscriptions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [topicsRes, newsRes, sessionsRes, subsRes] = await Promise.all([
          encyclopediaApi.getTopics({ limit: 4 }),
          newsApi.getNews({ limit: 5 }),
          assistantApi.getSessions().catch(() => ({ data: [] })),
          subscriptionsApi.getSubscriptions().catch(() => ({ data: [] }))
        ]);

        setRecentTopics(topicsRes.data);
        setLatestNews(newsRes.data);
        setChatSessions(sessionsRes.data?.slice(0, 3) || []);
        setSubscriptions(subsRes.data || []);
      } catch (error) {
        console.error('Dashboard data fetch error:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const quickActions = [
    { icon: BookOpen, label: 'Encyclopedia', href: '/encyclopedia', color: 'bg-blue-500' },
    { icon: Newspaper, label: 'News', href: '/news', color: 'bg-green-500' },
    { icon: MessageSquare, label: 'AI Assistant', href: '/assistant', color: 'bg-purple-500' },
    { icon: Bell, label: 'Subscriptions', href: '/subscriptions', color: 'bg-orange-500' },
  ];

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="dashboard-page">
      <div className="container-app py-8">
        {/* Welcome Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-semibold mb-2">
            Welcome back, {user?.name?.split(' ')[0] || 'Researcher'}
          </h1>
          <p className="text-slate-600 dark:text-slate-400">
            Your semiconductor intelligence hub
          </p>
        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {quickActions.map((action) => (
            <Link
              key={action.href}
              to={action.href}
              className="card-base p-4 flex items-center gap-4 hover:-translate-y-1 transition-all duration-300"
              data-testid={`quick-action-${action.label.toLowerCase()}`}
            >
              <div className={`w-12 h-12 ${action.color} rounded-xl flex items-center justify-center`}>
                <action.icon className="h-6 w-6 text-white" />
              </div>
              <span className="font-medium">{action.label}</span>
            </Link>
          ))}
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Main Content Area */}
          <div className="lg:col-span-2 space-y-8">
            {/* Latest News */}
            <section className="card-base p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-xl font-semibold flex items-center gap-2">
                  <Newspaper className="h-5 w-5 text-green-500" />
                  Latest News
                </h2>
                <Link to="/news" className="text-sm text-blue-600 hover:text-blue-700 flex items-center gap-1">
                  View All <ChevronRight className="h-4 w-4" />
                </Link>
              </div>

              {latestNews.length > 0 ? (
                <div className="space-y-4">
                  {latestNews.map((article) => (
                    <Link
                      key={article.article_id}
                      to={`/news/${article.article_id}`}
                      className="block p-4 rounded-lg hover:bg-slate-50 transition-colors dark:hover:bg-slate-800"
                      data-testid={`news-item-${article.article_id}`}
                    >
                      <div className="flex items-start justify-between gap-4">
                        <div className="flex-1">
                          <h3 className="font-medium mb-1 line-clamp-2">{article.title}</h3>
                          <p className="text-sm text-slate-600 dark:text-slate-400 line-clamp-2">
                            {article.summary}
                          </p>
                          <div className="flex items-center gap-3 mt-2 text-xs text-slate-500">
                            <span className="flex items-center gap-1">
                              <Clock className="h-3 w-3" />
                              {new Date(article.published_at).toLocaleDateString()}
                            </span>
                            <span className="px-2 py-0.5 bg-slate-100 rounded dark:bg-slate-700">
                              {article.category}
                            </span>
                          </div>
                        </div>
                      </div>
                    </Link>
                  ))}
                </div>
              ) : (
                <p className="text-slate-500 text-center py-8">No news available yet</p>
              )}
            </section>

            {/* Recent Encyclopedia Topics */}
            <section className="card-base p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-xl font-semibold flex items-center gap-2">
                  <BookOpen className="h-5 w-5 text-blue-500" />
                  Encyclopedia Topics
                </h2>
                <Link to="/encyclopedia" className="text-sm text-blue-600 hover:text-blue-700 flex items-center gap-1">
                  View All <ChevronRight className="h-4 w-4" />
                </Link>
              </div>

              <div className="grid sm:grid-cols-2 gap-4">
                {recentTopics.map((topic) => (
                  <Link
                    key={topic.topic_id}
                    to={`/encyclopedia/${topic.slug}`}
                    className="p-4 rounded-lg border border-slate-200 hover:border-blue-300 hover:bg-blue-50/50 transition-all dark:border-slate-700 dark:hover:border-blue-700 dark:hover:bg-blue-900/20"
                    data-testid={`topic-${topic.slug}`}
                  >
                    <h3 className="font-medium mb-1">{topic.title}</h3>
                    <p className="text-sm text-slate-600 dark:text-slate-400 line-clamp-2">
                      {topic.overview}
                    </p>
                    <div className="mt-2">
                      <span className={`text-xs px-2 py-0.5 rounded badge-${topic.difficulty}`}>
                        {topic.difficulty}
                      </span>
                    </div>
                  </Link>
                ))}
              </div>
            </section>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* AI Chat Sessions */}
            <section className="card-base p-6">
              <div className="flex items-center justify-between mb-4">
                <h2 className="font-semibold flex items-center gap-2">
                  <MessageSquare className="h-5 w-5 text-purple-500" />
                  Recent Chats
                </h2>
                <Link to="/assistant" className="text-sm text-blue-600 hover:text-blue-700">
                  New Chat
                </Link>
              </div>

              {chatSessions.length > 0 ? (
                <div className="space-y-2">
                  {chatSessions.map((session) => (
                    <Link
                      key={session.session_id}
                      to={`/assistant?session=${session.session_id}`}
                      className="block p-3 rounded-lg hover:bg-slate-50 transition-colors dark:hover:bg-slate-800"
                    >
                      <p className="text-sm font-medium truncate">{session.title}</p>
                      <p className="text-xs text-slate-500">
                        {new Date(session.updated_at).toLocaleDateString()}
                      </p>
                    </Link>
                  ))}
                </div>
              ) : (
                <div className="text-center py-6">
                  <p className="text-sm text-slate-500 mb-3">No chat sessions yet</p>
                  <Link to="/assistant">
                    <Button size="sm" data-testid="start-chat-btn">Start a Chat</Button>
                  </Link>
                </div>
              )}
            </section>

            {/* Subscriptions */}
            <section className="card-base p-6">
              <div className="flex items-center justify-between mb-4">
                <h2 className="font-semibold flex items-center gap-2">
                  <Bell className="h-5 w-5 text-orange-500" />
                  Subscriptions
                </h2>
                <Link to="/subscriptions" className="text-sm text-blue-600 hover:text-blue-700">
                  Manage
                </Link>
              </div>

              {subscriptions.length > 0 ? (
                <div className="space-y-2">
                  {subscriptions.slice(0, 5).map((sub) => (
                    <div
                      key={sub.subscription_id}
                      className="flex items-center justify-between p-2 rounded-lg bg-slate-50 dark:bg-slate-800"
                    >
                      <span className="text-sm font-medium">{sub.topic_name || sub.topic}</span>
                      <span className="text-xs text-slate-500 capitalize">{sub.frequency}</span>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-6">
                  <p className="text-sm text-slate-500 mb-3">No subscriptions yet</p>
                  <Link to="/subscriptions">
                    <Button size="sm" variant="outline" data-testid="add-subscription-btn">
                      Add Topics
                    </Button>
                  </Link>
                </div>
              )}
            </section>

            {/* Quick Stats */}
            <section className="card-base p-6">
              <h2 className="font-semibold mb-4 flex items-center gap-2">
                <TrendingUp className="h-5 w-5 text-green-500" />
                Platform Stats
              </h2>
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-sm text-slate-600 dark:text-slate-400">Encyclopedia Topics</span>
                  <span className="font-medium">5+</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-slate-600 dark:text-slate-400">News Articles</span>
                  <span className="font-medium">{latestNews.length}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-slate-600 dark:text-slate-400">Your Chats</span>
                  <span className="font-medium">{chatSessions.length}</span>
                </div>
              </div>
            </section>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
