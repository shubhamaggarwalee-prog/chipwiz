import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import { preferencesApi } from '../lib/api';

const ThemeContext = createContext({
  theme: 'light',
  difficulty: 'intermediate',
  setTheme: () => {},
  setDifficulty: () => {},
  toggleTheme: () => {},
  syncPreferences: () => {}
});

export const useTheme = () => useContext(ThemeContext);

export const ThemeProvider = ({ children }) => {
  const [theme, setThemeState] = useState('light');
  const [difficulty, setDifficultyState] = useState('intermediate');
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Load preferences on mount
  useEffect(() => {
    const loadPreferences = async () => {
      // First check localStorage for immediate UX
      const savedTheme = localStorage.getItem('theme');
      const savedDifficulty = localStorage.getItem('difficulty');
      
      if (savedTheme) setThemeState(savedTheme);
      if (savedDifficulty) setDifficultyState(savedDifficulty);
      
      // Then try to sync with server for authenticated users
      try {
        const response = await preferencesApi.get();
        if (response.data.is_authenticated) {
          setIsAuthenticated(true);
          if (response.data.theme) setThemeState(response.data.theme);
          if (response.data.difficulty) setDifficultyState(response.data.difficulty);
          // Update localStorage with server values
          localStorage.setItem('theme', response.data.theme || 'light');
          localStorage.setItem('difficulty', response.data.difficulty || 'intermediate');
        }
      } catch (error) {
        // Server sync failed, use localStorage values
        console.log('Using local preferences');
      }
    };
    
    loadPreferences();
  }, []);

  // Apply theme to document
  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  // Save difficulty to localStorage
  useEffect(() => {
    localStorage.setItem('difficulty', difficulty);
  }, [difficulty]);

  // Set theme with server sync
  const setTheme = useCallback(async (newTheme) => {
    setThemeState(newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Sync to server if authenticated
    if (isAuthenticated) {
      try {
        await preferencesApi.patch('theme', newTheme);
      } catch (error) {
        console.log('Failed to sync theme to server');
      }
    }
  }, [isAuthenticated]);

  // Set difficulty with server sync
  const setDifficulty = useCallback(async (newDifficulty) => {
    setDifficultyState(newDifficulty);
    localStorage.setItem('difficulty', newDifficulty);
    
    // Sync to server if authenticated
    if (isAuthenticated) {
      try {
        await preferencesApi.patch('difficulty', newDifficulty);
      } catch (error) {
        console.log('Failed to sync difficulty to server');
      }
    }
  }, [isAuthenticated]);

  const toggleTheme = useCallback(() => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
  }, [theme, setTheme]);

  // Manual sync function
  const syncPreferences = useCallback(async () => {
    try {
      const response = await preferencesApi.sync();
      if (response.data.synced && response.data.preferences) {
        const prefs = response.data.preferences;
        if (prefs.theme) setThemeState(prefs.theme);
        if (prefs.difficulty) setDifficultyState(prefs.difficulty);
        return true;
      }
    } catch (error) {
      console.error('Sync failed:', error);
    }
    return false;
  }, []);

  return (
    <ThemeContext.Provider value={{ 
      theme, 
      difficulty,
      setTheme, 
      setDifficulty,
      toggleTheme,
      syncPreferences,
      isAuthenticated
    }}>
      {children}
    </ThemeContext.Provider>
  );
};
