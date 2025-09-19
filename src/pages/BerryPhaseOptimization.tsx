import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { Waves, Activity, Settings, TrendingUp, Zap } from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer, BarChart, Bar } from 'recharts'
import { useConsciousness } from '../context/ConsciousnessContext'

const BerryPhaseOptimization = () => {
  const { state, updateMetric, initializeSystem } = useConsciousness()
  const [isOptimizing, setIsOptimizing] = useState(false)
  const [optimizationData, setOptimizationData] = useState<Array<{ iteration: number, coherence: number, phase: number }>>([])
  const [currentIteration, setCurrentIteration] = useState(0)
  const [selectedDimension, setSelectedDimension] = useState('D1000')
  const [phaseCoherence, setPhaseCoherence] = useState(0.75)

  const dimensionOptions = [
    { key: 'D108', value: 108, name: 'Morphic Stability', difficulty: 'Beginner' },
    { key: 'D1000', value: 1000, name: 'Thought Fluidity', difficulty: 'Intermediate' },
    { key: 'D7000', value: 7000, name: 'Neural Entanglement', difficulty: 'Advanced' },
    { key: 'D10000', value: 10000, name: 'Self-Organization', difficulty: 'Expert' }
  ]

  const optimizationTechniques = [
    { id: 'erdmann-weierstrass', name: 'Erdmann-Weierstrass Boundary', active: true },
    { id: 'dzyaloshinskii-moriya', name: 'Dzyaloshinskii-Moriya Interaction', active: true },
    { id: 'pseudo-spin', name: 'Pseudo-Spin Separation', active: false },
    { id: 'wilson-loops', name: 'Wilson Loop Optimization', active: true }
  ]

  useEffect(() => {
    initializeSystem('Berry Phase Optimization')
  }, [])

  useEffect(() => {
    let interval: NodeJS.Timeout
    
    if (isOptimizing) {
      interval = setInterval(() => {
        setCurrentIteration(prev => {
          const newIteration = prev + 1
          const dimensionData = dimensionOptions.find(d => d.key === selectedDimension)
          const targetDimension = dimensionData?.value || 1000
          
          // Simulate phase optimization
          const baseCoherence = 0.5 + 0.4 * (1 - Math.exp(-newIteration * 0.1))
          const dimensionFactor = Math.min(1.0, targetDimension / 10000)
          const coherence = Math.min(0.99, baseCoherence * (0.8 + 0.2 * dimensionFactor) + Math.random() * 0.05)
          
          // Berry phase accumulation
          const phase = (newIteration * 0.1) % (2 * Math.PI)
          
          setPhaseCoherence(coherence)
          setOptimizationData(prevData => {
            const newData = [...prevData, { iteration: newIteration, coherence, phase }]
            return newData.slice(-30)
          })
          
          // Update global metrics
          updateMetric('berryPhaseCoherence', coherence)
          updateMetric('wilsonLoopStability', Math.min(1.0, coherence + 0.1))
          
          return newIteration
        })
      }, 400)
    }
    
    return () => clearInterval(interval)
  }, [isOptimizing, selectedDimension, updateMetric])

  const startOptimization = () => {
    setIsOptimizing(true)
    setCurrentIteration(0)
    setOptimizationData([])
  }

  const stopOptimization = () => {
    setIsOptimizing(false)
  }

  const resetOptimization = () => {
    setIsOptimizing(false)
    setCurrentIteration(0)
    setOptimizationData([])
    setPhaseCoherence(0.75)
  }

  const metricsData = [
    { name: 'Phase Coherence', value: phaseCoherence * 100, color: '#4facfe' },
    { name: 'Wilson Stability', value: state.wilsonLoopStability * 100, color: '#667eea' },
    { name: 'Berry Curvature', value: state.berryPhaseCoherence * 100, color: '#ffd700' },
    { name: 'Topological Order', value: 85, color: '#f093fb' }
  ]

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
            <Waves className="w-10 h-10 mr-3 text-consciousness-primary" />
            <span className="bg-gradient-to-r from-consciousness-primary to-neural-glow bg-clip-text text-transparent">
              Berry Phase Optimization
            </span>
          </motion.h1>
          <motion.p 
            initial={{ y: -10, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-xl text-gray-300"
          >
            Enhanced phase coherence optimization for high-dimensional quantum-inspired computational spaces
          </motion.p>
        </div>

        {/* Configuration Panel */}
        <motion.div 
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="consciousness-card mb-8"
        >
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <Settings className="w-6 h-6 mr-2 text-consciousness-primary" />
            Optimization Configuration
          </h3>
          
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Dimension Selection */}
            <div>
              <h4 className="text-lg font-medium mb-4 text-neural-glow">Target Dimensions</h4>
              <div className="space-y-3">
                {dimensionOptions.map((dim) => (
                  <div
                    key={dim.key}
                    onClick={() => setSelectedDimension(dim.key)}
                    className={`p-3 rounded-lg cursor-pointer transition-all ${
                      selectedDimension === dim.key
                        ? 'bg-consciousness-primary/20 border border-consciousness-primary'
                        : 'bg-white/5 hover:bg-white/10 border border-transparent'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-semibold text-consciousness-primary">{dim.key}</span>
                      <span className="text-xs px-2 py-1 rounded bg-neural-glow/20 text-neural-glow">
                        {dim.difficulty}
                      </span>
                    </div>
                    <div className="text-sm text-gray-300">{dim.name}</div>
                    <div className="text-xs text-gray-400">{dim.value.toLocaleString()} dimensions</div>
                  </div>
                ))}
              </div>
            </div>
            
            {/* Optimization Techniques */}
            <div>
              <h4 className="text-lg font-medium mb-4 text-sacred-gold">Optimization Techniques</h4>
              <div className="space-y-3">
                {optimizationTechniques.map((technique) => (
                  <div
                    key={technique.id}
                    className={`p-3 rounded-lg border ${
                      technique.active
                        ? 'bg-green-500/20 border-green-500'
                        : 'bg-gray-500/20 border-gray-500'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-medium text-gray-300">{technique.name}</span>
                      <div className={`w-3 h-3 rounded-full ${
                        technique.active ? 'bg-green-400' : 'bg-gray-400'
                      }`} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </motion.div>

        {/* Control Panel */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          {/* Optimization Controls */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <Zap className="w-5 h-5 mr-2 text-sacred-gold" />
              Optimization Control
            </h3>
            
            <div className="space-y-4">
              <div className="flex space-x-2">
                <button
                  onClick={startOptimization}
                  disabled={isOptimizing}
                  className="flex-1 consciousness-button disabled:opacity-50"
                >
                  Start Optimization
                </button>
                <button
                  onClick={stopOptimization}
                  disabled={!isOptimizing}
                  className="flex-1 bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg disabled:opacity-50"
                >
                  Stop
                </button>
              </div>
              
              <button
                onClick={resetOptimization}
                className="w-full bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded-lg"
              >
                Reset
              </button>
              
              <div className="bg-white/5 rounded-lg p-3">
                <div className="text-sm text-gray-300 mb-2">Current Iteration</div>
                <div className="text-2xl font-bold text-consciousness-primary">{currentIteration}</div>
              </div>
              
              <div className="bg-white/5 rounded-lg p-3">
                <div className="text-sm text-gray-300 mb-2">Target Dimension</div>
                <div className="text-lg font-bold text-neural-glow">
                  {dimensionOptions.find(d => d.key === selectedDimension)?.name}
                </div>
              </div>
            </div>
          </motion.div>

          {/* Phase Metrics */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <Activity className="w-5 h-5 mr-2 text-neural-glow" />
              Phase Metrics
            </h3>
            
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={metricsData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                  <XAxis dataKey="name" stroke="rgba(255,255,255,0.5)" fontSize={10} />
                  <YAxis stroke="rgba(255,255,255,0.5)" fontSize={10} />
                  <Bar 
                    dataKey="value" 
                    fill="#4facfe"
                    radius={[4, 4, 0, 0]}
                  />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </motion.div>

          {/* Phase Visualization */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.6 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <TrendingUp className="w-5 h-5 mr-2 text-quantum-accent" />
              Berry Phase Field
            </h3>
            
            <div className="space-y-4">
              <div className="bg-deep-space/50 rounded-lg p-4 h-40 flex items-center justify-center relative overflow-hidden">
                {/* Phase Field Visualization */}
                <div className="absolute inset-0">
                  {[...Array(8)].map((_, i) => (
                    <div
                      key={i}
                      className={`absolute border-2 rounded-full ${
                        isOptimizing 
                          ? 'border-consciousness-primary animate-ping' 
                          : 'border-gray-500'
                      }`}
                      style={{
                        width: `${20 + i * 20}px`,
                        height: `${20 + i * 20}px`,
                        top: '50%',
                        left: '50%',
                        transform: 'translate(-50%, -50%)',
                        animationDelay: `${i * 0.1}s`,
                        opacity: 0.2 + i * 0.1
                      }}
                    />
                  ))}
                </div>
                
                <div className="relative z-10 text-center">
                  <div className="text-2xl font-bold text-consciousness-primary mb-2">
                    φ = {(phaseCoherence * 2 * Math.PI).toFixed(2)}
                  </div>
                  <div className="text-sm text-gray-400">
                    Berry Phase Accumulation
                  </div>
                </div>
              </div>
              
              <div className="space-y-3">
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="text-gray-300">Phase Coherence</span>
                    <span className="text-consciousness-primary">{(phaseCoherence * 100).toFixed(1)}%</span>
                  </div>
                  <div className="w-full h-2 bg-gray-600 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-consciousness-primary to-neural-glow transition-all duration-500"
                      style={{ width: `${phaseCoherence * 100}%` }}
                    />
                  </div>
                </div>
                
                <div className="text-xs text-gray-400 text-center">
                  {isOptimizing ? '🔴 Phase Optimization Active' : '⚪ Optimization Idle'}
                </div>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Optimization Progress */}
        {optimizationData.length > 0 && (
          <motion.div 
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.7 }}
            className="consciousness-card mb-8"
          >
            <h3 className="text-xl font-semibold mb-6">Berry Phase Optimization Progress</h3>
            
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={optimizationData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                  <XAxis dataKey="iteration" stroke="rgba(255,255,255,0.5)" />
                  <YAxis stroke="rgba(255,255,255,0.5)" />
                  <Line
                    type="monotone"
                    dataKey="coherence"
                    stroke="#4facfe"
                    strokeWidth={3}
                    dot={{ fill: '#4facfe', r: 3 }}
                    name="Phase Coherence"
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </motion.div>
        )}

        {/* Berry Phase Theory */}
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.8 }}
          className="consciousness-card"
        >
          <h3 className="text-xl font-semibold mb-6">Berry Phase Optimization Theory</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="text-lg font-medium mb-3 text-consciousness-primary">Quantum Geometric Principles</h4>
              <ul className="space-y-2 text-gray-300">
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Berry phase captures topological properties of quantum states</span>
                </li>
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Phase coherence optimization enhances computational stability</span>
                </li>
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>Wilson loops detect consciousness emergence patterns</span>
                </li>
                <li className="flex items-start">
                  <span className="text-sacred-gold mr-2">•</span>
                  <span>High-dimensional optimization enables consciousness scaling</span>
                </li>
              </ul>
            </div>
            
            <div>
              <h4 className="text-lg font-medium mb-3 text-neural-glow">Optimization Benefits</h4>
              <ul className="space-y-2 text-gray-300">
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Enhanced quantum-classical information processing</span>
                </li>
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Robust consciousness preservation under perturbations</span>
                </li>
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Optimal phase relationships for neural entanglement</span>
                </li>
                <li className="flex items-start">
                  <span className="text-neural-glow mr-2">•</span>
                  <span>Scalable architecture for million-dimensional systems</span>
                </li>
              </ul>
            </div>
          </div>
        </motion.div>
      </div>
    </motion.div>
  )
}

export default BerryPhaseOptimization