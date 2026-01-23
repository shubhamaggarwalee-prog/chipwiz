import React, { useState, useEffect, useRef } from 'react';
import { useSearchParams } from 'react-router-dom';
import { assistantApi } from '../lib/api';
import { useAuth } from '../context/AuthContext';
import { Button } from '../components/ui/button';
import { ScrollArea } from '../components/ui/scroll-area';
import { 
  Send, 
  Plus, 
  MessageSquare, 
  Trash2,
  ChevronRight,
  Lightbulb,
  ExternalLink,
  Loader2,
  Scale
} from 'lucide-react';

// Simple markdown renderer for AI responses
const renderMarkdown = (text) => {
  if (!text) return null;
  
  const lines = text.split('\n');
  const elements = [];
  let inTable = false;
  let tableRows = [];
  let tableHeaders = [];
  
  const processLine = (line, index) => {
    // Table detection
    if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
      if (!inTable) {
        inTable = true;
        tableHeaders = line.split('|').filter(cell => cell.trim()).map(cell => cell.trim());
        return null;
      }
      
      // Skip separator row
      if (line.includes('---')) {
        return null;
      }
      
      tableRows.push(line.split('|').filter(cell => cell.trim()).map(cell => cell.trim()));
      return null;
    } else if (inTable) {
      // End of table
      const tableElement = (
        <div key={`table-${index}`} className="overflow-x-auto my-4">
          <table className="min-w-full border-collapse text-sm">
            <thead>
              <tr className="bg-slate-100 dark:bg-slate-800">
                {tableHeaders.map((header, i) => (
                  <th key={i} className="border border-slate-200 dark:border-slate-700 px-3 py-2 text-left font-semibold">
                    {header}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {tableRows.map((row, rowIdx) => (
                <tr key={rowIdx} className={rowIdx % 2 === 0 ? 'bg-white dark:bg-slate-900' : 'bg-slate-50 dark:bg-slate-800/50'}>
                  {row.map((cell, cellIdx) => (
                    <td key={cellIdx} className="border border-slate-200 dark:border-slate-700 px-3 py-2">
                      {cell}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
      inTable = false;
      tableRows = [];
      tableHeaders = [];
      elements.push(tableElement);
    }
    
    // Headers
    if (line.startsWith('## ')) {
      return <h2 key={index} className="text-lg font-semibold mt-6 mb-3 text-slate-900 dark:text-white">{line.replace('## ', '')}</h2>;
    }
    if (line.startsWith('### ')) {
      return <h3 key={index} className="text-base font-medium mt-4 mb-2 text-slate-800 dark:text-slate-200">{line.replace('### ', '')}</h3>;
    }
    
    // Bold text
    let processedLine = line.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    
    // Lists
    if (line.trim().startsWith('- ')) {
      return (
        <li key={index} className="ml-4 mb-1" dangerouslySetInnerHTML={{ __html: processedLine.replace(/^-\s*/, '') }} />
      );
    }
    
    // Regular paragraph
    if (line.trim()) {
      return <p key={index} className="mb-3" dangerouslySetInnerHTML={{ __html: processedLine }} />;
    }
    
    return null;
  };
  
  lines.forEach((line, index) => {
    const element = processLine(line, index);
    if (element) {
      elements.push(element);
    }
  });
  
  // Handle table at end of content
  if (inTable && tableRows.length > 0) {
    elements.push(
      <div key="table-final" className="overflow-x-auto my-4">
        <table className="min-w-full border-collapse text-sm">
          <thead>
            <tr className="bg-slate-100 dark:bg-slate-800">
              {tableHeaders.map((header, i) => (
                <th key={i} className="border border-slate-200 dark:border-slate-700 px-3 py-2 text-left font-semibold">
                  {header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {tableRows.map((row, rowIdx) => (
              <tr key={rowIdx} className={rowIdx % 2 === 0 ? 'bg-white dark:bg-slate-900' : 'bg-slate-50 dark:bg-slate-800/50'}>
                {row.map((cell, cellIdx) => (
                  <td key={cellIdx} className="border border-slate-200 dark:border-slate-700 px-3 py-2">
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  
  return <div className="prose-content">{elements}</div>;
};

const AIAssistant = () => {
  const { isAuthenticated } = useAuth();
  const [searchParams] = useSearchParams();
  const [sessions, setSessions] = useState([]);
  const [currentSessionId, setCurrentSessionId] = useState(searchParams.get('session') || null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [difficulty, setDifficulty] = useState('intermediate');
  const [loading, setLoading] = useState(false);
  const [followUpQuestions, setFollowUpQuestions] = useState([]);
  const messagesEndRef = useRef(null);

  // Fetch sessions
  useEffect(() => {
    const fetchSessions = async () => {
      if (!isAuthenticated) return;
      try {
        const response = await assistantApi.getSessions();
        setSessions(response.data);
      } catch (error) {
        console.error('Error fetching sessions:', error);
      }
    };
    fetchSessions();
  }, [isAuthenticated]);

  // Fetch messages when session changes
  useEffect(() => {
    const fetchMessages = async () => {
      if (!currentSessionId) {
        setMessages([]);
        return;
      }
      try {
        const response = await assistantApi.getSessionMessages(currentSessionId);
        setMessages(response.data);
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    };
    fetchMessages();
  }, [currentSessionId]);

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    const userMessage = input.trim();
    setInput('');
    setLoading(true);
    setFollowUpQuestions([]);

    // Optimistically add user message
    setMessages(prev => [...prev, {
      message_id: `temp_${Date.now()}`,
      role: 'user',
      content: userMessage,
      timestamp: new Date().toISOString()
    }]);

    try {
      const response = await assistantApi.chat(userMessage, currentSessionId, difficulty);
      const data = response.data;

      // Update session ID if new session
      if (!currentSessionId) {
        setCurrentSessionId(data.session_id);
        // Refresh sessions
        const sessionsRes = await assistantApi.getSessions();
        setSessions(sessionsRes.data);
      }

      // Add assistant response
      setMessages(prev => [...prev, {
        message_id: data.message_id,
        role: 'assistant',
        content: data.response,
        citations: data.citations,
        timestamp: new Date().toISOString()
      }]);

      setFollowUpQuestions(data.follow_up_questions || []);
    } catch (error) {
      console.error('Chat error:', error);
      // Add error message
      setMessages(prev => [...prev, {
        message_id: `error_${Date.now()}`,
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.',
        timestamp: new Date().toISOString()
      }]);
    } finally {
      setLoading(false);
    }
  };

  const handleNewChat = () => {
    setCurrentSessionId(null);
    setMessages([]);
    setFollowUpQuestions([]);
  };

  const handleDeleteSession = async (sessionId) => {
    try {
      await assistantApi.deleteSession(sessionId);
      setSessions(prev => prev.filter(s => s.session_id !== sessionId));
      if (currentSessionId === sessionId) {
        handleNewChat();
      }
    } catch (error) {
      console.error('Delete error:', error);
    }
  };

  const handleFollowUp = (question) => {
    setInput(question);
  };

  const exampleQueries = [
    "Explain EUV stochastic defects at 2nm",
    "Compare FinFET vs GAAFET",
    "CoWoS vs Foveros for AI accelerators",
    "What is the future of Moore's Law?"
  ];

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="assistant-page">
      <div className="container-app py-6">
        <div className="grid lg:grid-cols-[280px_1fr] gap-6 h-[calc(100vh-120px)]">
          {/* Sidebar - Chat Sessions */}
          <aside className="card-base p-4 hidden lg:flex lg:flex-col">
            <Button 
              onClick={handleNewChat} 
              className="w-full mb-4 gap-2"
              data-testid="new-chat-btn"
            >
              <Plus className="h-4 w-4" />
              New Chat
            </Button>

            <ScrollArea className="flex-1">
              <div className="space-y-1 pr-2">
                {sessions.map((session) => (
                  <div
                    key={session.session_id}
                    className={`group flex items-center gap-2 p-3 rounded-lg cursor-pointer transition-colors ${
                      currentSessionId === session.session_id
                        ? 'bg-blue-50 text-blue-600 dark:bg-blue-900/20 dark:text-blue-400'
                        : 'hover:bg-slate-100 dark:hover:bg-slate-800'
                    }`}
                    onClick={() => setCurrentSessionId(session.session_id)}
                  >
                    <MessageSquare className="h-4 w-4 flex-shrink-0" />
                    <span className="flex-1 text-sm truncate">{session.title}</span>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleDeleteSession(session.session_id);
                      }}
                      className="opacity-0 group-hover:opacity-100 p-1 hover:bg-slate-200 rounded dark:hover:bg-slate-700"
                    >
                      <Trash2 className="h-3 w-3 text-slate-500" />
                    </button>
                  </div>
                ))}
              </div>
            </ScrollArea>

            {/* Difficulty Toggle */}
            <div className="mt-4 pt-4 border-t border-slate-200 dark:border-slate-700">
              <label className="text-xs font-medium text-slate-500 block mb-2">
                Response Difficulty
              </label>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-md text-sm dark:bg-slate-800 dark:border-slate-700"
                data-testid="difficulty-select"
              >
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="expert">Expert</option>
              </select>
            </div>
          </aside>

          {/* Main Chat Area */}
          <main className="card-base flex flex-col">
            {/* Messages */}
            <ScrollArea className="flex-1 p-4 lg:p-6">
              {messages.length === 0 ? (
                <div className="flex flex-col items-center justify-center h-full text-center">
                  <div className="w-16 h-16 bg-blue-50 rounded-2xl flex items-center justify-center mb-6 dark:bg-blue-900/30">
                    <MessageSquare className="h-8 w-8 text-blue-500" />
                  </div>
                  <h2 className="text-2xl font-semibold mb-2">AI Research Assistant</h2>
                  <p className="text-slate-600 dark:text-slate-400 mb-8 max-w-md">
                    Ask technical questions about semiconductors. I'll provide citation-backed answers tailored to your level.
                  </p>
                  
                  <div className="grid sm:grid-cols-2 gap-3 max-w-2xl">
                    {exampleQueries.map((query, i) => (
                      <button
                        key={i}
                        onClick={() => setInput(query)}
                        className="p-4 text-left rounded-xl border border-slate-200 hover:border-blue-300 hover:bg-blue-50/50 transition-all dark:border-slate-700 dark:hover:border-blue-700 dark:hover:bg-blue-900/20"
                        data-testid={`example-query-${i}`}
                      >
                        <Lightbulb className="h-4 w-4 text-blue-500 mb-2" />
                        <p className="text-sm">{query}</p>
                      </button>
                    ))}
                  </div>
                </div>
              ) : (
                <div className="space-y-6 pb-4">
                  {messages.map((message) => (
                    <div
                      key={message.message_id}
                      className={`${message.role === 'user' ? 'flex justify-end' : ''}`}
                    >
                      <div
                        className={`chat-message ${message.role}`}
                        data-testid={`message-${message.role}`}
                      >
                        <div className="whitespace-pre-wrap">{message.content}</div>
                        
                        {/* Citations */}
                        {message.citations?.length > 0 && (
                          <div className="mt-4 pt-3 border-t border-slate-200/50 dark:border-slate-700/50">
                            <p className="text-xs font-medium text-slate-500 mb-2">Sources:</p>
                            <div className="space-y-1">
                              {message.citations.map((citation, i) => (
                                <div key={i} className="flex items-start gap-2 text-xs">
                                  <span className="text-blue-500">[{citation.index}]</span>
                                  <span className="text-slate-600 dark:text-slate-400">
                                    {citation.title}
                                    {citation.url && (
                                      <a 
                                        href={citation.url} 
                                        target="_blank" 
                                        rel="noopener noreferrer"
                                        className="ml-1 text-blue-500"
                                      >
                                        <ExternalLink className="h-3 w-3 inline" />
                                      </a>
                                    )}
                                  </span>
                                </div>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                  
                  {loading && (
                    <div className="flex items-center gap-2 text-slate-500">
                      <Loader2 className="h-4 w-4 animate-spin" />
                      <span className="text-sm">Thinking...</span>
                    </div>
                  )}
                  
                  <div ref={messagesEndRef} />
                </div>
              )}
            </ScrollArea>

            {/* Follow-up Questions */}
            {followUpQuestions.length > 0 && (
              <div className="px-4 lg:px-6 pb-2">
                <div className="flex flex-wrap gap-2">
                  {followUpQuestions.map((question, i) => (
                    <button
                      key={i}
                      onClick={() => handleFollowUp(question)}
                      className="px-3 py-1.5 text-sm bg-slate-100 hover:bg-slate-200 rounded-full transition-colors dark:bg-slate-800 dark:hover:bg-slate-700"
                      data-testid={`follow-up-${i}`}
                    >
                      {question}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Input Area */}
            <div className="p-4 lg:p-6 border-t border-slate-200 dark:border-slate-700">
              <div className="flex gap-3">
                <div className="flex-1 relative">
                  <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && !e.shiftKey && handleSend()}
                    placeholder="Ask about semiconductors..."
                    className="w-full px-4 py-3 pr-12 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 outline-none dark:bg-slate-800 dark:border-slate-700"
                    disabled={loading}
                    data-testid="chat-input"
                  />
                </div>
                <Button
                  onClick={handleSend}
                  disabled={!input.trim() || loading}
                  className="px-4"
                  data-testid="send-btn"
                >
                  {loading ? (
                    <Loader2 className="h-5 w-5 animate-spin" />
                  ) : (
                    <Send className="h-5 w-5" />
                  )}
                </Button>
              </div>
              <p className="text-xs text-slate-500 mt-2 text-center">
                Responses are AI-generated from public sources. Verify critical information.
              </p>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
};

export default AIAssistant;
