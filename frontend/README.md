# News Digest Bot Frontend

A modern React frontend for the News Digest Bot that analyzes news coverage and detects bias across different sources.

## Features

- 🎨 Modern, responsive UI with beautiful gradients and animations
- 📱 Mobile-friendly design
- ⚡ Real-time news analysis
- 🔍 Compare coverage from CNN and Fox News
- 🎯 Bias detection and analysis
- 📊 Clean, organized results display

## Prerequisites

- Node.js (version 14 or higher)
- npm or yarn
- The Flask backend running on `http://localhost:5000`

## Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The React app will open in your browser at `http://localhost:3000`.

## Usage

1. Make sure your Flask backend is running on `http://localhost:5000`
2. Open the React app in your browser
3. Enter a topic you want to analyze (e.g., "Climate Change", "AI", "Politics")
4. Click "Analyze News" to get results
5. View the summaries from both CNN and Fox News
6. Read the bias analysis comparison

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── App.js          # Main application component
│   ├── App.css         # Component-specific styles
│   ├── index.js        # Application entry point
│   └── index.css       # Global styles
├── package.json        # Dependencies and scripts
└── README.md          # This file
```

## API Integration

The frontend communicates with the Flask backend through the `/api/analyze` endpoint:

- **Method**: POST
- **URL**: `http://localhost:5000/api/analyze`
- **Body**: `{ "topic": "your topic here" }`
- **Response**: JSON with summaries and bias analysis

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm eject` - Ejects from Create React App (one-way operation)

## Technologies Used

- **React 18** - UI library
- **Axios** - HTTP client for API calls
- **Lucide React** - Beautiful icons
- **CSS3** - Modern styling with gradients and animations

## Development

The app uses a proxy configuration to forward API requests to the Flask backend during development. This is configured in `package.json`:

```json
{
  "proxy": "http://localhost:5000"
}
```

## Production Build

To create a production build:

```bash
npm run build
```

This creates an optimized build in the `build/` folder that can be served by any static file server. 