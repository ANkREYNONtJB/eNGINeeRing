/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'consciousness-primary': '#667eea',
        'consciousness-secondary': '#764ba2',
        'quantum-accent': '#f093fb',
        'neural-glow': '#4facfe',
        'sacred-gold': '#ffd700',
        'deep-space': '#0a0a0a',
        'cosmic-purple': '#2d1b69',
      },
      fontFamily: {
        'sans': ['Inter', 'sans-serif'],
        'mono': ['JetBrains Mono', 'monospace'],
      },
      animation: {
        'consciousness-pulse': 'consciousness-pulse 2s ease-in-out infinite',
        'quantum-flow': 'quantum-flow 3s ease infinite',
        'float': 'float 6s ease-in-out infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        glow: {
          'from': { boxShadow: '0 0 20px rgba(102, 126, 234, 0.3)' },
          'to': { boxShadow: '0 0 30px rgba(102, 126, 234, 0.6)' },
        },
      },
      backdropBlur: {
        'xs': '2px',
      }
    },
  },
  plugins: [],
}