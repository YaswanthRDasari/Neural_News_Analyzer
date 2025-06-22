# Neural News Analyzer

A futuristic AI-powered news analysis tool that fetches and analyzes news articles from CNN and Fox News, providing summaries and bias detection with a modern React frontend.

## Features

- 🤖 **AI-Powered Analysis**: Neural network-based news summarization and bias detection
- 📰 **Multi-Source News**: Fetches articles from CNN and Fox News
- 🎨 **Futuristic UI**: Modern React frontend with neon colors and glassmorphism
- 🌙 **Dark/Light Mode**: Toggle between themes with smooth transitions
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎯 **First-Time Tutorial**: Interactive tutorial for new users

## Tech Stack

### Backend
- **Flask**: Python web framework
- **SerpAPI**: News article fetching
- **Azure OpenAI**: AI-powered summarization and bias analysis
- **BeautifulSoup**: Web scraping utilities

### Frontend
- **React**: Modern UI framework
- **CSS3**: Custom styling with animations
- **Axios**: HTTP client for API calls
- **Lucide React**: Icon library

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Azure OpenAI API key and endpoint
- SerpAPI key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yash-prof/Neural_News_Analyzer.git
   cd Neural_News_Analyzer
   ```

2. **Backend Setup**
   ```bash
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Environment Configuration**
   
   **Option A: Using .env file (Recommended for development)**
   
   Create a `.env` file in the root directory:
   ```env
   AZURE_OPENAI_KEY=your_azure_openai_key_here
   AZURE_ENDPOINT=your_azure_endpoint_here
   AZURE_WEB_APP_NAME=your_web_app_name_here
   AZURE_DEPLOYMENT_NAME=your_deployment_name_here
   SERPAPI_KEY=your_serpapi_key_here
   ```
   
   **Option B: Using config.py (Legacy method)**
   
   Copy `config.example.py` to `config.py` and fill in your actual API keys:
   ```bash
   cp config.example.py config.py
   # Edit config.py with your actual API keys
   ```

5. **Run the Application**
   ```bash
   # Terminal 1 - Backend
   python app.py
   
   # Terminal 2 - Frontend
   cd frontend
   npm start
   ```

## Git Deployment Setup

### Before Pushing to Git

1. **Ensure .env is in .gitignore**
   The `.gitignore` file should already include `.env` to prevent sensitive data from being committed.

2. **Verify your configuration**
   - If using `.env` file: Make sure it's not tracked by Git
   - If using `config.py`: Consider switching to `.env` for better security

3. **Check Git status**
   ```bash
   git status
   ```
   Make sure `.env` is not showing as a file to be committed.

### Initial Git Setup

```bash
# Initialize Git repository (if not already done)
git init

# Add all files (except those in .gitignore)
git add .

# Make initial commit
git commit -m "Initial commit: Neural News Analyzer"

# Add remote repository
git remote add origin <your-repo-url>

# Push to GitHub
git push -u origin main
```

## Deployment Options

### Option 1: Vercel (Recommended)

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy Frontend**
   ```bash
   cd frontend
   vercel
   ```

3. **Deploy Backend**
   ```bash
   vercel --prod
   ```

4. **Set Environment Variables in Vercel Dashboard**
   - Go to your project settings in Vercel
   - Add all environment variables from your `.env` file

### Option 2: Railway

1. **Connect your GitHub repository to Railway**
2. **Set environment variables** in Railway dashboard using the variables from your `.env` file
3. **Deploy automatically** on push to main branch

### Option 3: Render

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**
3. **Set build command**: `pip install -r requirements.txt`
4. **Set start command**: `python app.py`
5. **Add environment variables** from your `.env` file in the Render dashboard

### Option 4: Heroku

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login and create app**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Set environment variables**
   ```bash
   heroku config:set AZURE_OPENAI_KEY=your_key
   heroku config:set AZURE_ENDPOINT=your_endpoint
   heroku config:set AZURE_WEB_APP_NAME=your_app_name
   heroku config:set AZURE_DEPLOYMENT_NAME=your_deployment_name
   heroku config:set SERPAPI_KEY=your_serpapi_key
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

## Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `AZURE_OPENAI_KEY` | Azure OpenAI API key | Yes | `sk-...` |
| `AZURE_ENDPOINT` | Azure OpenAI endpoint URL | Yes | `https://...openai/deployments/...` |
| `AZURE_WEB_APP_NAME` | Azure web app name | Yes | `my-app-name` |
| `AZURE_DEPLOYMENT_NAME` | Azure deployment name | Yes | `gpt-4-deployment` |
| `SERPAPI_KEY` | SerpAPI key for news fetching | Yes | `your_serpapi_key` |

## Security Best Practices

1. **Never commit API keys to Git**
   - Use `.env` files for local development
   - Set environment variables in deployment platforms
   - Keep `config.example.py` as a template only

2. **Use environment variables in production**
   - All deployment platforms support environment variable configuration
   - Never hardcode sensitive data in production code

3. **Regular key rotation**
   - Rotate API keys periodically
   - Monitor API usage for security

## API Endpoints

- `POST /api/analyze` - Analyze news for a given topic
  - Body: `{"topic": "your_topic_here"}`
  - Returns: Summaries and bias analysis

## Project Structure

```
Neural_News_Analyzer/
├── app.py                 # Flask backend
├── config.py             # Configuration settings (loads from .env)
├── config.example.py     # Example configuration template
├── .env                  # Environment variables (not in Git)
├── .gitignore           # Git ignore rules
├── requirements.txt      # Python dependencies
├── frontend/            # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
└── utils/               # Utility modules
    ├── serpapi_fetcher.py
    ├── summarizer.py
    ├── bias_analyzer.py
    └── generic_scraper.py
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'dotenv'**
   ```bash
   pip install python-dotenv
   ```

2. **Environment variables not loading**
   - Ensure `.env` file is in the root directory
   - Check that `python-dotenv` is installed
   - Verify environment variable names match exactly

3. **API key errors**
   - Verify API keys are correct
   - Check Azure OpenAI endpoint URL format
   - Ensure proper permissions for Azure resources

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please open an issue on GitHub or contact the development team. 