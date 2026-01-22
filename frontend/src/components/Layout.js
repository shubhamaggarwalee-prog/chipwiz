import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { Button } from './ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from './ui/dropdown-menu';
import { 
  Sun, 
  Moon, 
  Search, 
  Menu, 
  User, 
  LogOut, 
  Settings, 
  BookOpen,
  Bell,
  ChevronDown
} from 'lucide-react';

export const Header = () => {
  const { user, isAuthenticated, login, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = React.useState(false);

  const navItems = [
    { href: '/encyclopedia', label: 'Encyclopedia', icon: BookOpen },
    { href: '/news', label: 'News' },
    { href: '/assistant', label: 'AI Assistant' },
    { href: '/reports', label: 'Reports' },
  ];

  const isActive = (path) => location.pathname.startsWith(path);

  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-xl border-b border-slate-200 dark:bg-slate-900/80 dark:border-slate-800">
      <div className="container-app">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-3" data-testid="logo-link">
            <div className="w-8 h-8 bg-slate-900 rounded-lg flex items-center justify-center dark:bg-white">
              <span className="text-white text-sm font-bold dark:text-slate-900">SI</span>
            </div>
            <span className="font-semibold text-lg hidden sm:block">
              Semiconductor Intelligence
            </span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-1">
            {navItems.map((item) => (
              <Link
                key={item.href}
                to={item.href}
                data-testid={`nav-${item.label.toLowerCase().replace(' ', '-')}`}
                className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                  isActive(item.href)
                    ? 'bg-slate-100 text-slate-900 dark:bg-slate-800 dark:text-white'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50 dark:text-slate-400 dark:hover:text-white dark:hover:bg-slate-800'
                }`}
              >
                {item.label}
              </Link>
            ))}
          </nav>

          {/* Right Side Actions */}
          <div className="flex items-center gap-2">
            {/* Search Button */}
            <Link to="/search">
              <Button variant="ghost" size="icon" data-testid="search-btn">
                <Search className="h-5 w-5" />
              </Button>
            </Link>

            {/* Theme Toggle */}
            <Button 
              variant="ghost" 
              size="icon" 
              onClick={toggleTheme}
              data-testid="theme-toggle"
            >
              {theme === 'light' ? (
                <Moon className="h-5 w-5" />
              ) : (
                <Sun className="h-5 w-5" />
              )}
            </Button>

            {/* Auth Section */}
            {isAuthenticated ? (
              <>
                {/* Notifications */}
                <Link to="/subscriptions">
                  <Button variant="ghost" size="icon" data-testid="notifications-btn">
                    <Bell className="h-5 w-5" />
                  </Button>
                </Link>

                {/* User Menu */}
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <Button variant="ghost" className="gap-2" data-testid="user-menu-trigger">
                      <div className="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center overflow-hidden dark:bg-slate-700">
                        {user?.picture ? (
                          <img src={user.picture} alt={user.name} className="w-full h-full object-cover" />
                        ) : (
                          <User className="h-4 w-4" />
                        )}
                      </div>
                      <ChevronDown className="h-4 w-4 hidden sm:block" />
                    </Button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent align="end" className="w-56">
                    <div className="px-3 py-2">
                      <p className="font-medium">{user?.name}</p>
                      <p className="text-sm text-slate-500">{user?.email}</p>
                    </div>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem asChild>
                      <Link to="/dashboard" className="cursor-pointer" data-testid="menu-dashboard">
                        <User className="mr-2 h-4 w-4" />
                        Dashboard
                      </Link>
                    </DropdownMenuItem>
                    <DropdownMenuItem asChild>
                      <Link to="/subscriptions" className="cursor-pointer" data-testid="menu-subscriptions">
                        <Bell className="mr-2 h-4 w-4" />
                        Subscriptions
                      </Link>
                    </DropdownMenuItem>
                    <DropdownMenuItem asChild>
                      <Link to="/settings" className="cursor-pointer" data-testid="menu-settings">
                        <Settings className="mr-2 h-4 w-4" />
                        Settings
                      </Link>
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem onClick={logout} className="cursor-pointer text-red-600" data-testid="menu-logout">
                      <LogOut className="mr-2 h-4 w-4" />
                      Log out
                    </DropdownMenuItem>
                  </DropdownMenuContent>
                </DropdownMenu>
              </>
            ) : (
              <Button onClick={login} className="btn-primary" data-testid="login-btn">
                Sign In
              </Button>
            )}

            {/* Mobile Menu Toggle */}
            <Button 
              variant="ghost" 
              size="icon" 
              className="md:hidden"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              data-testid="mobile-menu-toggle"
            >
              <Menu className="h-5 w-5" />
            </Button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <nav className="md:hidden py-4 border-t border-slate-200 dark:border-slate-800">
            {navItems.map((item) => (
              <Link
                key={item.href}
                to={item.href}
                onClick={() => setMobileMenuOpen(false)}
                className={`block px-4 py-3 text-sm font-medium transition-colors ${
                  isActive(item.href)
                    ? 'bg-slate-100 text-slate-900 dark:bg-slate-800 dark:text-white'
                    : 'text-slate-600 hover:bg-slate-50 dark:text-slate-400 dark:hover:bg-slate-800'
                }`}
              >
                {item.label}
              </Link>
            ))}
          </nav>
        )}
      </div>
    </header>
  );
};

export const Footer = () => {
  return (
    <footer className="bg-slate-50 border-t border-slate-200 dark:bg-slate-900 dark:border-slate-800">
      <div className="container-app py-12">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div className="col-span-2 md:col-span-1">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-8 h-8 bg-slate-900 rounded-lg flex items-center justify-center dark:bg-white">
                <span className="text-white text-sm font-bold dark:text-slate-900">SI</span>
              </div>
              <span className="font-semibold">Semiconductor Intelligence</span>
            </div>
            <p className="text-sm text-slate-600 dark:text-slate-400">
              AI-powered semiconductor knowledge and research platform for engineers, researchers, and analysts.
            </p>
          </div>

          <div>
            <h4 className="font-medium mb-4">Platform</h4>
            <ul className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
              <li><Link to="/encyclopedia" className="hover:text-slate-900 dark:hover:text-white">Encyclopedia</Link></li>
              <li><Link to="/news" className="hover:text-slate-900 dark:hover:text-white">News</Link></li>
              <li><Link to="/assistant" className="hover:text-slate-900 dark:hover:text-white">AI Assistant</Link></li>
              <li><Link to="/reports" className="hover:text-slate-900 dark:hover:text-white">Reports</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-medium mb-4">Topics</h4>
            <ul className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
              <li><Link to="/encyclopedia/euv-lithography" className="hover:text-slate-900 dark:hover:text-white">EUV Lithography</Link></li>
              <li><Link to="/encyclopedia/finfet-technology" className="hover:text-slate-900 dark:hover:text-white">FinFET</Link></li>
              <li><Link to="/encyclopedia/gaafet-nanosheet" className="hover:text-slate-900 dark:hover:text-white">GAAFET</Link></li>
              <li><Link to="/encyclopedia/cowos-packaging" className="hover:text-slate-900 dark:hover:text-white">CoWoS</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-medium mb-4">Legal</h4>
            <ul className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
              <li><Link to="/privacy" className="hover:text-slate-900 dark:hover:text-white">Privacy Policy</Link></li>
              <li><Link to="/terms" className="hover:text-slate-900 dark:hover:text-white">Terms of Service</Link></li>
              <li><Link to="/sources" className="hover:text-slate-900 dark:hover:text-white">Data Sources</Link></li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-slate-200 dark:border-slate-800">
          <p className="text-sm text-slate-500 text-center">
            © {new Date().getFullYear()} Semiconductor Intelligence Platform. All content is sourced from public information and transformed for educational purposes.
          </p>
        </div>
      </div>
    </footer>
  );
};
