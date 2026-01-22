import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { Button } from '../components/ui/button';
import { Switch } from '../components/ui/switch';
import { 
  User, 
  Sun, 
  Moon, 
  Bell,
  Shield,
  LogOut
} from 'lucide-react';
import { toast } from 'sonner';

const SettingsPage = () => {
  const { user, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const [preferences, setPreferences] = useState({
    difficulty_default: 'intermediate',
    email_notifications: true
  });

  useEffect(() => {
    if (user?.preferences) {
      setPreferences(user.preferences);
    }
  }, [user]);

  const handleLogout = async () => {
    await logout();
    window.location.href = '/';
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="settings-page">
      <div className="container-app py-8 max-w-2xl">
        <h1 className="text-3xl font-semibold mb-8">Settings</h1>

        {/* Profile Section */}
        <section className="card-base p-6 mb-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <User className="h-5 w-5 text-slate-500" />
            Profile
          </h2>
          
          {user ? (
            <div className="flex items-center gap-4">
              <div className="w-16 h-16 rounded-full bg-slate-200 flex items-center justify-center overflow-hidden dark:bg-slate-700">
                {user.picture ? (
                  <img src={user.picture} alt={user.name} className="w-full h-full object-cover" />
                ) : (
                  <User className="h-8 w-8 text-slate-400" />
                )}
              </div>
              <div>
                <p className="font-medium text-lg">{user.name}</p>
                <p className="text-slate-600 dark:text-slate-400">{user.email}</p>
                <p className="text-xs text-slate-500 mt-1 capitalize">
                  Account type: {user.role || 'Free'}
                </p>
              </div>
            </div>
          ) : (
            <p className="text-slate-600 dark:text-slate-400">Not signed in</p>
          )}
        </section>

        {/* Appearance */}
        <section className="card-base p-6 mb-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            {theme === 'light' ? <Sun className="h-5 w-5 text-yellow-500" /> : <Moon className="h-5 w-5 text-blue-500" />}
            Appearance
          </h2>
          
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium">Dark Mode</p>
              <p className="text-sm text-slate-600 dark:text-slate-400">
                Switch between light and dark themes
              </p>
            </div>
            <Switch
              checked={theme === 'dark'}
              onCheckedChange={toggleTheme}
              data-testid="theme-switch"
            />
          </div>
        </section>

        {/* Preferences */}
        <section className="card-base p-6 mb-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Bell className="h-5 w-5 text-slate-500" />
            Preferences
          </h2>
          
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Default Difficulty</p>
                <p className="text-sm text-slate-600 dark:text-slate-400">
                  Set your preferred content difficulty level
                </p>
              </div>
              <select
                value={preferences.difficulty_default}
                onChange={(e) => setPreferences(prev => ({ ...prev, difficulty_default: e.target.value }))}
                className="px-3 py-2 bg-slate-50 border border-slate-200 rounded-md text-sm dark:bg-slate-800 dark:border-slate-700"
                data-testid="difficulty-select"
              >
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>

            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Email Notifications</p>
                <p className="text-sm text-slate-600 dark:text-slate-400">
                  Receive subscription updates via email
                </p>
              </div>
              <Switch
                checked={preferences.email_notifications}
                onCheckedChange={(checked) => setPreferences(prev => ({ ...prev, email_notifications: checked }))}
                data-testid="email-notifications-switch"
              />
            </div>
          </div>
        </section>

        {/* Data & Privacy */}
        <section className="card-base p-6 mb-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Shield className="h-5 w-5 text-slate-500" />
            Data & Privacy
          </h2>
          
          <div className="space-y-3 text-sm text-slate-600 dark:text-slate-400">
            <p>
              Your data is securely stored and never shared with third parties without consent.
            </p>
            <p>
              Chat sessions and preferences are stored to improve your experience.
            </p>
            <Button variant="outline" size="sm" className="mt-2">
              Download My Data
            </Button>
          </div>
        </section>

        {/* Logout */}
        {user && (
          <section className="card-base p-6">
            <Button 
              variant="destructive" 
              onClick={handleLogout}
              className="w-full gap-2"
              data-testid="logout-btn"
            >
              <LogOut className="h-4 w-4" />
              Sign Out
            </Button>
          </section>
        )}
      </div>
    </div>
  );
};

export default SettingsPage;
