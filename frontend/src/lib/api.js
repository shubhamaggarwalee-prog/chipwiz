import axios from 'axios';

// Get API URL with proper protocol
const getApiUrl = () => {
  // In production, always use HTTPS
  if (typeof window !== 'undefined' && window.location.protocol === 'https:') {
    return `https://${window.location.host}`;
  }
  // In development, use env variable or fallback
  return process.env.REACT_APP_BACKEND_URL || '';
};

const API_URL = getApiUrl();

const api = axios.create({
  baseURL: `${API_URL}/api`,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Auth APIs
export const authApi = {
  createSession: (sessionId) => api.post('/auth/session', { session_id: sessionId }),
  getMe: () => api.get('/auth/me'),
  logout: () => api.post('/auth/logout')
};

// Encyclopedia APIs
export const encyclopediaApi = {
  getCategories: () => api.get('/encyclopedia/categories'),
  getTopics: (params) => api.get('/encyclopedia/topics', { params }),
  getTopic: (slug, difficulty) => api.get(`/encyclopedia/topics/${slug}`, { params: { difficulty } }),
  getTree: () => api.get('/encyclopedia/tree'),
  search: (q) => api.get('/encyclopedia/search', { params: { q } }),
  downloadPdf: (slug, difficulty) => `${API_URL}/api/encyclopedia/topics/${slug}/pdf?difficulty=${difficulty}`
};

// News APIs
export const newsApi = {
  getNews: (params) => api.get('/news', { params }),
  getCategories: () => api.get('/news/categories'),
  getFeatured: () => api.get('/news/featured'),
  getDailyBrief: () => api.get('/news/daily-brief'),
  getArticle: (id) => api.get(`/news/${id}`),
  globalSearch: (q) => api.get('/news/search/global', { params: { q } }),
  triggerScrape: () => api.post('/news/scrape')
};

// AI Assistant APIs
export const assistantApi = {
  chat: (message, sessionId, difficulty) => api.post('/assistant/chat', { 
    message, 
    session_id: sessionId,
    difficulty 
  }),
  getSessions: () => api.get('/assistant/sessions'),
  getSessionMessages: (sessionId) => api.get(`/assistant/sessions/${sessionId}/messages`),
  deleteSession: (sessionId) => api.delete(`/assistant/sessions/${sessionId}`)
};

// Reports APIs
export const reportsApi = {
  getReports: (params) => api.get('/reports', { params }),
  getTypes: () => api.get('/reports/types'),
  getReport: (slug) => api.get(`/reports/${slug}`),
  generateReport: (topic, type) => api.post('/reports/generate', null, { params: { topic, report_type: type } }),
  downloadPdf: (slug) => `${API_URL}/api/reports/${slug}/pdf`
};

// Subscriptions APIs
export const subscriptionsApi = {
  getTopics: () => api.get('/subscriptions/topics'),
  getSubscriptions: () => api.get('/subscriptions'),
  subscribe: (topic, frequency) => api.post('/subscriptions', { topic, frequency }),
  updateSubscription: (id, data) => api.put(`/subscriptions/${id}`, data),
  unsubscribe: (id) => api.delete(`/subscriptions/${id}`)
};

export default api;
