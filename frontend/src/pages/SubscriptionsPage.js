import React, { useState, useEffect } from 'react';
import { subscriptionsApi } from '../lib/api';
import { useAuth } from '../context/AuthContext';
import { Button } from '../components/ui/button';
import { 
  Bell, 
  Check, 
  Plus,
  Trash2,
  Sun,
  Package,
  Factory,
  Layers,
  Cpu,
  Brain,
  GitBranch,
  Database,
  Atom
} from 'lucide-react';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '../components/ui/select';
import { toast } from 'sonner';

const iconMap = {
  euv: Sun,
  packaging: Package,
  foundry: Factory,
  materials: Layers,
  design: Cpu,
  ai_chips: Brain,
  nodes: GitBranch,
  memory: Database,
  gaafet: Atom
};

const SubscriptionsPage = () => {
  const { isAuthenticated, login } = useAuth();
  const [topics, setTopics] = useState([]);
  const [subscriptions, setSubscriptions] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch topics and subscriptions
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [topicsRes, subsRes] = await Promise.all([
          subscriptionsApi.getTopics(),
          isAuthenticated ? subscriptionsApi.getSubscriptions() : Promise.resolve({ data: [] })
        ]);
        setTopics(topicsRes.data);
        setSubscriptions(subsRes.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [isAuthenticated]);

  const handleSubscribe = async (topicId) => {
    if (!isAuthenticated) {
      toast.error('Please sign in to subscribe');
      return;
    }

    try {
      await subscriptionsApi.subscribe(topicId, 'daily');
      // Refresh subscriptions
      const response = await subscriptionsApi.getSubscriptions();
      setSubscriptions(response.data);
      toast.success('Subscribed successfully!');
    } catch (error) {
      if (error.response?.status === 400) {
        toast.error('Already subscribed to this topic');
      } else {
        toast.error('Failed to subscribe');
      }
    }
  };

  const handleUnsubscribe = async (subscriptionId) => {
    try {
      await subscriptionsApi.unsubscribe(subscriptionId);
      setSubscriptions(prev => prev.filter(s => s.subscription_id !== subscriptionId));
      toast.success('Unsubscribed successfully');
    } catch (error) {
      toast.error('Failed to unsubscribe');
    }
  };

  const handleUpdateFrequency = async (subscriptionId, frequency) => {
    try {
      await subscriptionsApi.updateSubscription(subscriptionId, { frequency });
      setSubscriptions(prev => prev.map(s => 
        s.subscription_id === subscriptionId ? { ...s, frequency } : s
      ));
      toast.success('Frequency updated');
    } catch (error) {
      toast.error('Failed to update');
    }
  };

  const isSubscribed = (topicId) => {
    return subscriptions.some(s => s.topic === topicId);
  };

  const getSubscription = (topicId) => {
    return subscriptions.find(s => s.topic === topicId);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="subscriptions-page">
      <div className="container-app py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-semibold mb-2">Topic Subscriptions</h1>
          <p className="text-slate-600 dark:text-slate-400">
            Subscribe to topics and receive updates at your preferred frequency
          </p>
        </div>

        {!isAuthenticated && (
          <div className="card-base p-6 mb-8 text-center">
            <Bell className="h-12 w-12 text-slate-300 mx-auto mb-4" />
            <h2 className="text-xl font-semibold mb-2">Sign in to Subscribe</h2>
            <p className="text-slate-600 dark:text-slate-400 mb-4">
              Create an account to receive topic-based updates via email
            </p>
            <Button onClick={login} data-testid="login-to-subscribe-btn">
              Sign In with Google
            </Button>
          </div>
        )}

        {/* Active Subscriptions */}
        {isAuthenticated && subscriptions.length > 0 && (
          <section className="mb-12">
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <Check className="h-5 w-5 text-green-500" />
              Your Subscriptions ({subscriptions.length})
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
              {subscriptions.map((sub) => {
                const topicInfo = topics.find(t => t.id === sub.topic);
                const IconComponent = iconMap[sub.topic] || Bell;
                
                return (
                  <div
                    key={sub.subscription_id}
                    className="card-base p-4 border-l-4 border-green-500"
                    data-testid={`subscription-${sub.topic}`}
                  >
                    <div className="flex items-start justify-between gap-3">
                      <div className="flex items-center gap-3">
                        <div className="w-10 h-10 bg-green-50 rounded-lg flex items-center justify-center dark:bg-green-900/30">
                          <IconComponent className="h-5 w-5 text-green-600 dark:text-green-400" />
                        </div>
                        <div>
                          <h3 className="font-medium">{topicInfo?.name || sub.topic}</h3>
                          <p className="text-xs text-slate-500">{topicInfo?.description}</p>
                        </div>
                      </div>
                      <button
                        onClick={() => handleUnsubscribe(sub.subscription_id)}
                        className="p-2 hover:bg-slate-100 rounded-lg transition-colors dark:hover:bg-slate-800"
                        data-testid={`unsubscribe-${sub.topic}`}
                      >
                        <Trash2 className="h-4 w-4 text-slate-400" />
                      </button>
                    </div>
                    
                    <div className="mt-4 flex items-center gap-2">
                      <span className="text-xs text-slate-500">Frequency:</span>
                      <Select
                        value={sub.frequency}
                        onValueChange={(value) => handleUpdateFrequency(sub.subscription_id, value)}
                      >
                        <SelectTrigger className="w-32 h-8 text-xs">
                          <SelectValue />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="instant">Instant</SelectItem>
                          <SelectItem value="daily">Daily</SelectItem>
                          <SelectItem value="weekly">Weekly</SelectItem>
                          <SelectItem value="monthly">Monthly</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        )}

        {/* Available Topics */}
        <section>
          <h2 className="text-xl font-semibold mb-4">
            {isAuthenticated && subscriptions.length > 0 ? 'More Topics' : 'Available Topics'}
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {topics.filter(t => !isSubscribed(t.id)).map((topic) => {
              const IconComponent = iconMap[topic.id] || Bell;
              
              return (
                <div
                  key={topic.id}
                  className="card-base p-6 hover:border-blue-300 transition-colors"
                  data-testid={`topic-${topic.id}`}
                >
                  <div className="flex items-start gap-4">
                    <div className="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center dark:bg-blue-900/30">
                      <IconComponent className="h-6 w-6 text-blue-600 dark:text-blue-400" />
                    </div>
                    <div className="flex-1">
                      <h3 className="font-medium mb-1">{topic.name}</h3>
                      <p className="text-sm text-slate-600 dark:text-slate-400 mb-4">
                        {topic.description}
                      </p>
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => handleSubscribe(topic.id)}
                        className="gap-2"
                        data-testid={`subscribe-${topic.id}`}
                      >
                        <Plus className="h-4 w-4" />
                        Subscribe
                      </Button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        {/* Delivery Info */}
        <section className="mt-12 card-base p-6">
          <h2 className="text-lg font-semibold mb-4">Delivery Options</h2>
          <div className="grid md:grid-cols-4 gap-6">
            {[
              { freq: 'Instant', desc: 'Get notified immediately when news breaks' },
              { freq: 'Daily', desc: 'Daily digest of updates in the morning' },
              { freq: 'Weekly', desc: 'Weekly summary every Monday' },
              { freq: 'Monthly', desc: 'Monthly research brief' }
            ].map((option) => (
              <div key={option.freq} className="text-center">
                <div className="font-medium mb-1">{option.freq}</div>
                <p className="text-xs text-slate-500">{option.desc}</p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
};

export default SubscriptionsPage;
