#!/bin/bash

echo "🚀 Neural News Analyzer Deployment Script"
echo "=========================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit"
fi

echo ""
echo "Choose your deployment platform:"
echo "1. Vercel (Recommended)"
echo "2. Railway"
echo "3. Render"
echo "4. Heroku"
echo "5. Exit"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🚀 Deploying to Vercel..."
        echo "Installing Vercel CLI..."
        npm install -g vercel
        
        echo "Deploying frontend..."
        cd frontend
        vercel --yes
        
        echo "Deploying backend..."
        cd ..
        vercel --prod --yes
        
        echo "✅ Vercel deployment complete!"
        ;;
    2)
        echo "🚀 Deploying to Railway..."
        echo "Please follow these steps:"
        echo "1. Go to https://railway.app"
        echo "2. Connect your GitHub repository"
        echo "3. Set environment variables:"
        echo "   - SERPAPI_KEY"
        echo "   - OPENAI_API_KEY"
        echo "4. Deploy automatically"
        ;;
    3)
        echo "🚀 Deploying to Render..."
        echo "Please follow these steps:"
        echo "1. Go to https://render.com"
        echo "2. Create a new Web Service"
        echo "3. Connect your GitHub repository"
        echo "4. Set build command: pip install -r requirements.txt"
        echo "5. Set start command: python app.py"
        echo "6. Add environment variables"
        ;;
    4)
        echo "🚀 Deploying to Heroku..."
        if ! command -v heroku &> /dev/null; then
            echo "Please install Heroku CLI first:"
            echo "https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi
        
        echo "Creating Heroku app..."
        heroku create neural-news-analyzer-$(date +%s)
        
        echo "Setting environment variables..."
        read -p "Enter your SERPAPI_KEY: " serpapi_key
        read -p "Enter your OPENAI_API_KEY: " openai_key
        
        heroku config:set SERPAPI_KEY=$serpapi_key
        heroku config:set OPENAI_API_KEY=$openai_key
        
        echo "Deploying to Heroku..."
        git add .
        git commit -m "Deploy to Heroku"
        git push heroku main
        
        echo "✅ Heroku deployment complete!"
        ;;
    5)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment setup complete!"
echo "Don't forget to:"
echo "1. Set your environment variables"
echo "2. Test your deployed application"
echo "3. Share your app URL with others!" 