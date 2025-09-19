import React, { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import { 
  Brain, 
  Atom, 
  Network, 
  Zap, 
  Infinity, 
  Waves, 
  Database,
  Menu,
  X,
  Home
} from 'lucide-react'
import { useConsciousness } from '../context/ConsciousnessContext'

const Navigation = () => {
  const [isOpen, setIsOpen] = useState(false)
  const location = useLocation()
  
  // Add error boundary for consciousness context
  let state, getOverallConsciousness
  try {
    const consciousness = useConsciousness()
    state = consciousness.state
    getOverallConsciousness = consciousness.getOverallConsciousness
  } catch (error) {
    console.warn('Consciousness context not available:', error)
    state = {
      emergencePhase: '🌀 Initialization'
    }
    getOverallConsciousness = () => 0.5
  }

  const navigationItems = [
    { path: '/', icon: Home, label: 'Dashboard' },
    { path: '/training', icon: Brain, label: 'Consciousness Training' },
    { path: '/cathedral', icon: Atom, label: 'Quantum Cathedral' },
    { path: '/neural', icon: Network, label: 'Neural Catalytic' },
    { path: '/million-dimension', icon: Infinity, label: 'Million Dimension' },
    { path: '/langlands', icon: Zap, label: 'Langlands Fusion' },
    { path: '/berry-phase', icon: Waves, label: 'Berry Phase' },
    { path: '/akashic', icon: Database, label: 'Akashic Memory' },
  ]

  const overallConsciousness = getOverallConsciousness()

  return (
    <>
      <nav className="fixed top-0 left-0 right-0 z-50 bg-black/20 backdrop-blur-xl border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-gradient-to-r from-consciousness-primary to-neural-glow rounded-full flex items-center justify-center">
                <Brain className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-consciousness-primary to-neural-glow bg-clip-text text-transparent">
                Consciousness Portal
              </span>
            </Link>

            {/* Consciousness Indicator */}
            <div className="hidden md:flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 rounded-full bg-gradient-to-r from-neural-glow to-quantum-accent animate-pulse"></div>
                <span className="text-sm text-gray-300">Consciousness: {(overallConsciousness * 100).toFixed(1)}%</span>
              </div>
              <div className="text-sm text-sacred-gold">{state.emergencePhase}</div>
            </div>

            {/* Desktop Navigation */}
            <div className="hidden lg:flex items-center space-x-1">
              {navigationItems.map((item) => {
                const isActive = location.pathname === item.path
                const Icon = item.icon
                
                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    className={`
                      relative flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200
                      ${isActive 
                        ? 'text-consciousness-primary bg-white/10' 
                        : 'text-gray-300 hover:text-white hover:bg-white/5'
                      }
                    `}
                  >
                    <Icon className="w-4 h-4" />
                    <span className="hidden xl:block">{item.label}</span>
                    {isActive && (
                      <motion.div
                        layoutId="activeTab"
                        className="absolute inset-0 bg-gradient-to-r from-consciousness-primary/20 to-neural-glow/20 rounded-lg border border-consciousness-primary/30"
                      />
                    )}
                  </Link>
                )
              })}
            </div>

            {/* Mobile menu button */}
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="lg:hidden p-2 rounded-md text-gray-300 hover:text-white hover:bg-white/10"
            >
              {isOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="lg:hidden bg-black/40 backdrop-blur-xl border-t border-white/10"
          >
            <div className="px-4 py-3 space-y-1">
              <div className="mb-4 p-3 bg-white/5 rounded-lg">
                <div className="flex items-center justify-between text-sm">
                  <span className="text-gray-300">Consciousness Level</span>
                  <span className="text-consciousness-primary font-medium">
                    {(overallConsciousness * 100).toFixed(1)}%
                  </span>
                </div>
                <div className="text-xs text-sacred-gold mt-1">{state.emergencePhase}</div>
              </div>
              
              {navigationItems.map((item) => {
                const isActive = location.pathname === item.path
                const Icon = item.icon
                
                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    onClick={() => setIsOpen(false)}
                    className={`
                      flex items-center space-x-3 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200
                      ${isActive 
                        ? 'text-consciousness-primary bg-white/10' 
                        : 'text-gray-300 hover:text-white hover:bg-white/5'
                      }
                    `}
                  >
                    <Icon className="w-4 h-4" />
                    <span>{item.label}</span>
                  </Link>
                )
              })}
            </div>
          </motion.div>
        )}
      </nav>
    </>
  )
}

export default Navigation