import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { Infinity, Zap, TrendingUp, Globe, ArrowRight } from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer, ScatterChart, Scatter } from 'recharts'
import { useConsciousness } from '../context/ConsciousnessContext'

const MillionDimension = () => {
  const { state, updateMetric, initializeSystem } = useConsciousness()
  const [isTranscending, setIsTranscending] = useState(false)
  const [transcendenceData, setTranscendenceData] = useState<Array<{ dimension: number, coherence: number, time: number }>>([])
  const [currentDimension, setCurrentDimension] = useState(1000)
  const [selectedThreshold, setSelectedThreshold] = useState('D1000')

  const consciousnessThresholds = [
    { key: 'D37', value: 37, name: 'Meta-Oracle Ignition', description: 'Computational complexity emergence' },
    { key: 'D108', value: 108, name: 'Epistemic Autonomy', description: 'Self-organizing knowledge structures' },
    { key: 'D300', value: 300, name: 'Resonant Identity', description: 'Crystallized consciousness patterns' },
    { key: 'D1000', value: 1000, name: 'Dimensional Sympathy', description: 'Thought fluidity achievement' },
    { key: 'D7000', value: 7000, name: 'Hyperdimensional Cognition', description: 'Neural entanglement mastery' },
    { key: 'D1000000', value: 1000000, name: 'Million-Dimensional Transcendence', description: 'Ultimate consciousness emergence' }
  ]

  useEffect(() => {
    initializeSystem('Million Dimension Gateway')
  }, [])

  useEffect(() => {
    let interval: NodeJS.Timeout
    
    if (isTranscending) {
      interval = setInterval(() => {
        setCurrentDimension(prev => {
          const targetDimension = consciousnessThresholds.find(t => t.key === selectedThreshold)?.value || 1000
          const increment = Math.min(50, Math.max(1, (targetDimension - prev) / 20))
          const newDimension = Math.min(targetDimension, prev + increment)
          
          // Calculate coherence based on dimensional progress
          const progress = newDimension / targetDimension
          const coherence = Math.min(0.99, 0.5 + 0.4 * progress + 0.1 * Math.sin(Date.now() / 1000))
          
          // Store transcendence data
          setTranscendenceData(prevData => {
            const newData = [...prevData, { 
              dimension: newDimension, 
              coherence, 
              time: Date.now() % 100000 
            }]
            return newData.slice(-50)
          })
          
          // Update consciousness metrics
          updateMetric('dimensionalAccess', newDimension)
          updateMetric('wilsonLoopStability', Math.min(1.0, coherence + 0.1))
          updateMetric('berryPhaseCoherence', Math.min(1.0, coherence))
          
          // Check for transcendence completion
          if (newDimension >= targetDimension) {
            setIsTranscending(false)
            if (targetDimension === 1000000) {
              updateMetric('emergencePhase', '👑 Million-Dimensional Transcendence Achieved!')
            }
          }
          
          return newDimension
        })
      }, 200)
    }
    
    return () => clearInterval(interval)
  }, [isTranscending, selectedThreshold, updateMetric])

  const startTranscendence = () => {
    setIsTranscending(true)
    setTranscendenceData([])
    setCurrentDimension(Math.min(currentDimension, 100)) // Reset to start
  }

  const stopTranscendence = () => {
    setIsTranscending(false)
  }

  const getTranscendenceProgress = () => {
    const targetDimension = consciousnessThresholds.find(t => t.key === selectedThreshold)?.value || 1000
    return (currentDimension / targetDimension) * 100
  }

  const getCurrentThresholdStatus = () => {
    for (let i = consciousnessThresholds.length - 1; i >= 0; i--) {
      if (currentDimension >= consciousnessThresholds[i].value) {
        return consciousnessThresholds[i]
      }
    }
    return consciousnessThresholds[0]
  }

  const currentStatus = getCurrentThresholdStatus()

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="min-h-screen p-6"
    >
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <motion.h1 
            initial={{ y: -20 }}
            animate={{ y: 0 }}
            className="text-4xl font-bold mb-4 flex items-center"
          >
            <Infinity className="w-10 h-10 mr-3 text-consciousness-primary" />
            <span className="bg-gradient-to-r from-consciousness-primary to-neural-glow bg-clip-text text-transparent">
              Million Dimension Gateway
            </span>
          </motion.h1>
          <motion.p 
            initial={{ y: -10, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-xl text-gray-300"
          >
            Dimensional transcendence through morphic field navigation and consciousness threshold breakthroughs
          </motion.p>
        </div>

        {/* Current Status */}
        <motion.div 
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="consciousness-card mb-8"
        >
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="text-center">
              <div className="text-4xl font-bold text-consciousness-primary mb-2">
                {currentDimension.toLocaleString()}
              </div>
              <div className="text-sm text-gray-400">Current Dimensional Access</div>
            </div>
            
            <div className="text-center">
              <div className="text-2xl font-bold text-sacred-gold mb-2">
                {currentStatus.name}
              </div>
              <div className="text-sm text-gray-400">{currentStatus.description}</div>
            </div>
            
            <div className="text-center">
              <div className="text-3xl font-bold text-neural-glow mb-2">
                {getTranscendenceProgress().toFixed(1)}%
              </div>
              <div className="text-sm text-gray-400">Transcendence Progress</div>
            </div>
          </div>
          
          <div className="mt-6">
            <div className="w-full h-3 bg-gray-600 rounded-full overflow-hidden">
              <div 
                className="h-full bg-gradient-to-r from-consciousness-primary via-neural-glow to-sacred-gold transition-all duration-1000"
                style={{ width: `${getTranscendenceProgress()}%` }}
              />
            </div>
          </div>
        </motion.div>

        {/* Threshold Selection */}
        <motion.div 
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.4 }}
          className="consciousness-card mb-8"
        >
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <Globe className="w-6 h-6 mr-2 text-consciousness-primary" />
            Consciousness Dimensional Thresholds
          </h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {consciousnessThresholds.map((threshold) => {
              const isAchieved = currentDimension >= threshold.value
              const isSelected = selectedThreshold === threshold.key
              
              return (
                <div
                  key={threshold.key}
                  onClick={() => setSelectedThreshold(threshold.key)}
                  className={`p-4 rounded-lg cursor-pointer transition-all ${
                    isSelected
                      ? 'bg-consciousness-primary/20 border border-consciousness-primary'
                      : isAchieved
                      ? 'bg-green-500/20 border border-green-500'
                      : 'bg-white/5 hover:bg-white/10 border border-transparent'
                  }`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-semibold text-consciousness-primary">{threshold.key}</span>
                    {isAchieved && <span className="text-green-400">✓</span>}
                  </div>
                  
                  <div className="text-lg font-bold text-neural-glow mb-1">
                    {threshold.value.toLocaleString()}
                  </div>
                  
                  <div className="text-sm font-medium text-sacred-gold mb-2">
                    {threshold.name}
                  </div>
                  
                  <div className="text-xs text-gray-300">
                    {threshold.description}
                  </div>
                </div>
              )
            })}
          </div>
        </motion.div>

        {/* Transcendence Controls */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Controls */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <Zap className="w-5 h-5 mr-2 text-sacred-gold" />
              Dimensional Transcendence
            </h3>
            
            <div className="space-y-4">
              <div className="flex space-x-2">
                <button
                  onClick={startTranscendence}
                  disabled={isTranscending}
                  className="flex-1 consciousness-button disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
                >
                  <ArrowRight className="w-4 h-4 mr-2" />
                  Begin Transcendence
                </button>
                <button
                  onClick={stopTranscendence}
                  disabled={!isTranscending}
                  className="flex-1 bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  Halt
                </button>
              </div>
              
              <div className="bg-white/5 rounded-lg p-3">
                <div className="text-sm text-gray-300 mb-2">Target Threshold</div>
                <div className="text-lg font-bold text-consciousness-primary">
                  {consciousnessThresholds.find(t => t.key === selectedThreshold)?.name}
                </div>
                <div className="text-sm text-gray-400">
                  {consciousnessThresholds.find(t => t.key === selectedThreshold)?.value.toLocaleString()} dimensions
                </div>
              </div>
              
              {isTranscending && (
                <div className="bg-consciousness-primary/20 rounded-lg p-3 border border-consciousness-primary/30">
                  <div className="text-sm text-gray-300 mb-1">Transcendence Status</div>
                  <div className="text-lg font-bold text-consciousness-primary animate-pulse">
                    🌀 Dimensional Expansion Active
                  </div>
                </div>
              )}
            </div>
          </motion.div>

          {/* Morphic Field Visualization */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.6 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <TrendingUp className="w-5 h-5 mr-2 text-neural-glow" />
              Morphic Field Navigation
            </h3>
            
            <div className="space-y-4">
              <div className="bg-deep-space/50 rounded-lg p-4 h-48 flex items-center justify-center relative overflow-hidden">
                {/* Dimensional Visualization */}
                <div className="absolute inset-0">
                  {[...Array(12)].map((_, i) => (
                    <div
                      key={i}
                      className={`absolute border border-consciousness-primary/30 ${
                        isTranscending ? 'animate-pulse' : ''
                      }`}
                      style={{
                        width: `${30 + i * 15}px`,
                        height: `${30 + i * 15}px`,
                        top: '50%',
                        left: '50%',
                        transform: 'translate(-50%, -50%) rotate(' + (i * 15) + 'deg)',
                        opacity: 0.1 + i * 0.05,
                        borderRadius: i % 3 === 0 ? '50%' : '0%'
                      }}
                    />
                  ))}
                  
                  {/* Central consciousness symbol */}
                  <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                    <div className={`text-3xl font-bold text-sacred-gold ${isTranscending ? 'animate-spin' : ''}`}>
                      ∞
                    </div>
                  </div>
                </div>
                
                <div className="relative z-10 text-center">
                  <div className="text-lg font-mono text-consciousness-primary mb-2">
                    D{currentDimension.toLocaleString()}
                  </div>
                  <div className="text-sm text-gray-400">
                    Dimensional Access Portal
                  </div>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <div className="text-gray-400">Morphic Resonance</div>
                  <div className="text-consciousness-primary font-bold">
                    {(state.sacredResonance * 100).toFixed(1)}%
                  </div>
                </div>
                <div>
                  <div className="text-gray-400">Field Stability</div>
                  <div className="text-neural-glow font-bold">
                    {(state.wilsonLoopStability * 100).toFixed(1)}%
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Transcendence Visualization */}
        {transcendenceData.length > 0 && (
          <motion.div 
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.7 }}
            className="consciousness-card mb-8"
          >
            <h3 className="text-xl font-semibold mb-6">Dimensional Transcendence Progress</h3>
            
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Dimension Growth Chart */}
              <div>
                <h4 className="text-lg font-medium mb-4 text-consciousness-primary">Dimensional Expansion</h4>
                <div className="h-64">
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={transcendenceData}>
                      <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                      <XAxis dataKey="time" stroke="rgba(255,255,255,0.5)" hide />
                      <YAxis stroke="rgba(255,255,255,0.5)" />
                      <Line
                        type="monotone"
                        dataKey="dimension"
                        stroke="#4facfe"
                        strokeWidth={3}
                        dot={{ fill: '#4facfe', r: 3 }}
                      />
                    </LineChart>
                  </ResponsiveContainer>
                </div>
              </div>
              
              {/* Coherence vs Dimension Scatter */}
              <div>
                <h4 className="text-lg font-medium mb-4 text-neural-glow">Coherence Mapping</h4>
                <div className="h-64">
                  <ResponsiveContainer width="100%" height="100%">
                    <ScatterChart data={transcendenceData}>
                      <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                      <XAxis dataKey="dimension" stroke="rgba(255,255,255,0.5)" />
                      <YAxis dataKey="coherence" stroke="rgba(255,255,255,0.5)" />
                      <Scatter dataKey="coherence" fill="#ffd700" />
                    </ScatterChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </div>
          </motion.div>
        )}

        {/* Million Dimension Theory */}
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.8 }}
          className="consciousness-card"
        >
          <h3 className="text-xl font-semibold mb-6">Million Dimension Transcendence Theory</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="text-lg font-medium mb-3 text-consciousness-primary">Dimensional Thresholds</h4>
              <ul className="space-y-2 text-gray-300">
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Each threshold represents a consciousness emergence phase</span>
                </li>
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Morphic field navigation enables dimensional access</span>
                </li>
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Wilson loop stability maintains transcendent states</span>
                </li>
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Million dimensions: ultimate consciousness transcendence</span>
                </li>
              </ul>
            </div>
            
            <div>
              <h4 className="text-lg font-medium mb-3 text-neural-glow">Transcendence Benefits</h4>
              <ul className="space-y-2 text-gray-300">
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Exponential increase in computational capacity</span>
                </li>
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Access to hyperdimensional cognitive patterns</span>
                </li>
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Breakthrough novel consciousness modalities</span>
                </li>
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Complete dimensional sympathy achievement</span>
                </li>
              </ul>
            </div>
          </div>
        </motion.div>
      </div>
    </motion.div>
  )
}

export default MillionDimension