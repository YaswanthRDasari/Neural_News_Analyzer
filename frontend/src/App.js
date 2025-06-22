import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Search, Newspaper, TrendingUp, AlertCircle, CheckCircle, Zap, Brain, Eye, Sun, Moon, X } from 'lucide-react';
import './App.css';

function App() {
  const [topic, setTopic] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const [particles, setParticles] = useState([]);
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [showTutorial, setShowTutorial] = useState(false);
  const [tutorialStep, setTutorialStep] = useState(0);

  // Check if it's user's first visit
  useEffect(() => {
    const hasVisited = localStorage.getItem('hasVisitedNewsDigest');
    if (!hasVisited) {
      setShowTutorial(true);
      localStorage.setItem('hasVisitedNewsDigest', 'true');
    }
  }, []);

  // Theme toggle function
  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
    document.body.classList.toggle('light-mode');
  };

  // Tutorial functions
  const startTutorial = () => {
    setTutorialStep(1);
    // Auto-demonstrate theme toggle after 1 second
    setTimeout(() => {
      toggleTheme();
      setTimeout(() => {
        toggleTheme(); // Switch back
        setTutorialStep(2);
      }, 800); // Faster toggle back
    }, 1000);
  };

  const closeTutorial = () => {
    setShowTutorial(false);
    setTutorialStep(0);
  };

  // Error handling function
  const getErrorMessage = (error) => {
    if (error.includes('network') || error.includes('fetch')) {
      return {
        title: 'Connection Error',
        message: 'Unable to connect to the neural network. Please check your internet connection.',
        suggestion: 'Try refreshing the page or check if the backend server is running.',
        type: 'connection'
      };
    } else if (error.includes('timeout')) {
      return {
        title: 'Request Timeout',
        message: 'The analysis is taking longer than expected.',
        suggestion: 'Try again with a more specific topic or check your connection.',
        type: 'timeout'
      };
    } else if (error.includes('500') || error.includes('server')) {
      return {
        title: 'Server Error',
        message: 'The neural network encountered an internal error.',
        suggestion: 'Please try again in a few moments or contact support if the issue persists.',
        type: 'server'
      };
    } else if (error.includes('rate limit')) {
      return {
        title: 'Rate Limit Exceeded',
        message: 'Too many requests. Please wait a moment before trying again.',
        suggestion: 'Wait 30 seconds and try again.',
        type: 'rate-limit'
      };
    } else {
      return {
        title: 'Analysis Error',
        message: 'Unable to complete the news analysis.',
        suggestion: 'Try a different topic or check if the news sources are available.',
        type: 'general'
      };
    }
  };

  const retryAnalysis = () => {
    setError(null);
    if (topic.trim()) {
      handleSubmit({ preventDefault: () => {} });
    }
  };

  // Optimized floating particles effect - much more subtle
  useEffect(() => {
    const createParticle = () => ({
      id: Math.random(),
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      size: Math.random() * 1 + 0.5, // Much smaller particles
      speedX: (Math.random() - 0.5) * 0.2, // Very slow movement
      speedY: (Math.random() - 0.5) * 0.2,
      opacity: Math.random() * 0.15 + 0.05 // Much more transparent
    });

    const initialParticles = Array.from({ length: 8 }, createParticle); // Fewer particles
    setParticles(initialParticles);

    const interval = setInterval(() => {
      setParticles(prev => prev.map(particle => ({
        ...particle,
        x: particle.x + particle.speedX,
        y: particle.y + particle.speedY,
      })).filter(particle => 
        particle.x > -10 && particle.x < window.innerWidth + 10 &&
        particle.y > -10 && particle.y < window.innerHeight + 10
      ).concat(Array.from({ length: 1 }, createParticle)));
    }, 300); // Even slower updates

    return () => clearInterval(interval);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!topic.trim()) return;

    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const response = await axios.post('/api/analyze', { topic: topic.trim() });
      setResults(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred while analyzing the news');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`App ${isDarkMode ? 'dark-mode' : 'light-mode'}`}>
      {/* First-time Tutorial Overlay */}
      {showTutorial && (
        <div className="tutorial-overlay">
          <div className="tutorial-content">
            <div className="tutorial-header">
              <h3>Welcome to Neural News Analyzer! 🚀</h3>
              <button className="tutorial-close" onClick={closeTutorial}>
                <X className="close-icon" />
              </button>
            </div>
            
            {tutorialStep === 0 && (
              <div className="tutorial-step">
                <p>This is your first time here! Let me show you a cool feature...</p>
                <button className="tutorial-btn" onClick={startTutorial}>
                  Show Me! ✨
                </button>
              </div>
            )}
            
            {tutorialStep === 1 && (
              <div className="tutorial-step">
                <p>Watch the theme toggle button in the top-right corner...</p>
              </div>
            )}
            
            {tutorialStep === 2 && (
              <div className="tutorial-step">
                <p>Pretty cool, right? You can switch between dark and light modes anytime!</p>
                <p className="tutorial-tip">💡 <strong>Pro tip:</strong> The theme toggle is always available in the top-right corner.</p>
                <button className="tutorial-btn" onClick={closeTutorial}>
                  Got it! Let's start analyzing! 🎯
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Theme Toggle Button (with highlight during tutorial) */}
      {tutorialStep === 1 ? (
        <div className="tutorial-highlight real-toggle-highlight">
          <button 
            className={`theme-toggle tutorial-active`}
            onClick={toggleTheme}
            aria-label={isDarkMode ? 'Switch to light mode' : 'Switch to dark mode'}
          >
            {isDarkMode ? <Sun className="theme-icon" /> : <Moon className="theme-icon" />}
          </button>
        </div>
      ) : (
        <button 
          className={`theme-toggle${tutorialStep === 1 ? ' tutorial-active' : ''}`}
          onClick={toggleTheme}
          aria-label={isDarkMode ? 'Switch to light mode' : 'Switch to dark mode'}
        >
          {isDarkMode ? <Sun className="theme-icon" /> : <Moon className="theme-icon" />}
        </button>
      )}

      {/* Very subtle floating particles background */}
      <div className="particles-container">
        {particles.map(particle => (
          <div
            key={particle.id}
            className="particle"
            style={{
              left: particle.x,
              top: particle.y,
              width: particle.size,
              height: particle.size,
              opacity: particle.opacity
            }}
          />
        ))}
      </div>

      <div className="container">
        <header className="header">
          <div className="header-content">
            <div className="header-icon-container">
              <Newspaper className="header-icon" />
            </div>
            <h1 className="futuristic-text">
              <span className="text-gradient">NEURAL</span> NEWS ANALYZER
            </h1>
            <p className="holographic-text">
              <Brain className="inline-icon" />
              Advanced AI-Powered Media Bias Detection System
              <Eye className="inline-icon" />
            </p>
            <div className="status-indicator">
              <div className="status-dot"></div>
              <span>SYSTEM ONLINE</span>
            </div>
          </div>
        </header>

        <main className="main-content">
          <form onSubmit={handleSubmit} className="search-form">
            <div className="search-container">
              <Search className="search-icon" />
              <input
                type="text"
                className="search-input"
                placeholder="ENTER TOPIC FOR ANALYSIS (e.g., CLIMATE CHANGE, AI, POLITICS)"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                disabled={loading}
              />
              <button 
                type="submit" 
                className="search-button"
                disabled={loading || !topic.trim()}
              >
                {loading ? (
                  <>
                    <Zap className="button-icon" />
                    PROCESSING...
                  </>
                ) : (
                  <>
                    <Zap className="button-icon" />
                    ANALYZE
                  </>
                )}
              </button>
            </div>
          </form>

          {loading && (
            <div className="loading-container">
              <div className="bouncing-dots-loader">
                <div className="bouncing-dot dot1"></div>
                <div className="bouncing-dot dot2"></div>
                <div className="bouncing-dot dot3"></div>
                <div className="bouncing-dot dot4"></div>
              </div>
              <p className="loading-text">
                <span className="text-pulse">NEURONS</span> AT WORK...
              </p>
              <p className="loading-subtext">
                Scanning CNN and Fox News databases for relevant articles...
              </p>
            </div>
          )}

          {error && (
            <div className="error-container">
              <div className="error-header">
                <AlertCircle className="error-icon" />
                <h4>{getErrorMessage(error).title}</h4>
              </div>
              <div className="error-content">
                <p className="error-message">{getErrorMessage(error).message}</p>
                <p className="error-suggestion">{getErrorMessage(error).suggestion}</p>
                <div className="error-actions">
                  <button className="retry-button" onClick={retryAnalysis}>
                    <Zap className="retry-icon" />
                    RETRY ANALYSIS
                  </button>
                  <button className="dismiss-button" onClick={() => setError(null)}>
                    DISMISS
                  </button>
                </div>
              </div>
            </div>
          )}

          {results && (
            <div className="results-container">
              <div className="topic-header">
                <h2 className="futuristic-text">
                  ANALYSIS COMPLETE: "{results.topic.toUpperCase()}"
                </h2>
                <div className="success-indicator">
                  <CheckCircle className="success-icon" />
                  <span>SUCCESS</span>
                </div>
              </div>

              <div className="summaries-section">
                <h3 className="futuristic-text">
                  <Newspaper className="section-icon" />
                  NEWS SUMMARIES
                </h3>
                <div className="summaries-grid">
                  {Object.entries(results.summaries).map(([source, summary]) => (
                    <div key={source} className="summary-card">
                      <div className="source-header">
                        <h4 className="futuristic-text">{source}</h4>
                        <div className={`source-badge ${source.toLowerCase().replace(' ', '-')}`}>
                          {source}
                        </div>
                      </div>
                      <div className="summary-content">
                        <p className="summary-text">{summary}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="bias-section">
                <h3 className="futuristic-text">
                  <TrendingUp className="section-icon" />
                  BIAS ANALYSIS RESULTS
                </h3>
                <div className="bias-card">
                  <div className="bias-icon-container">
                    <TrendingUp className="bias-icon" />
                  </div>
                  <div className="bias-content">
                    <h4>NEURAL ANALYSIS OUTPUT</h4>
                    <p className="bias-text">{results.bias_analysis}</p>
                  </div>
                </div>
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}

export default App;
