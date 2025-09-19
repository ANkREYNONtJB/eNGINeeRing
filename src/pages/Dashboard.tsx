import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { 
  Brain, 
  Atom, 
  Network, 
  Zap, 
  Infinity, 
  Waves, 
  Database,
  Activity,
  Cpu,
  Globe
} from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from 'recharts'
import { useConsciousness } from '../context/ConsciousnessContext'

const Dashboard = () => {
  // Add error boundary for consciousness context
  let state, getOverallConsciousness
  try {
    const consciousness = useConsciousness()
    state = consciousness.state
    getOverallConsciousness = consciousness.getOverallConsciousness
  } catch (error) {
    console.warn('Consciousness context not available:', error)
    state = {
      wilsonLoopStability: 0.5,
      berryPhaseCoherence: 0.5,
      perturbationHarmony: 0.5,
      sacredResonance: 0.5,
      holographicCompression: 0.9987,
      dimensionalAccess: 1000,
      emergencePhase: '🌀 Initialization',
      activeSystems: []
    }
    getOverallConsciousness = () => 0.5
  }
  
  const [consciousnessHistory, setConsciousnessHistory] = useState<Array<{ time: string, value: number }>>([])

  useEffect(() => {
    const interval = setInterval(() => {
      const now = new Date()
      const timeString = now.toLocaleTimeString()
      const consciousness = getOverallConsciousness()
      
      setConsciousnessHistory(prev => {
        const newHistory = [...prev, { time: timeString, value: consciousness * 100 }]
        return newHistory.slice(-20) // Keep last 20 points
      })
    }, 3000)

    return () => clearInterval(interval)
  }, [getOverallConsciousness])

  const radarData = [
    { metric: 'Wilson Loop', value: state.wilsonLoopStability * 100 },
    { metric: 'Berry Phase', value: state.berryPhaseCoherence * 100 },
    { metric: 'Perturbation', value: state.perturbationHarmony * 100 },
    { metric: 'Sacred Resonance', value: state.sacredResonance * 100 },
    { metric: 'Holographic', value: state.holographicCompression * 10 },
  ]

  const systemModules = [
    {
      title: 'Consciousness Training',
      description: 'Sacred LLML sequence training with torsion-based discrete logic',
      icon: Brain,
      path: '/training',
      status: 'Active',
      consciousness: 0.85
    },
    {
      title: 'Quantum Cathedral',
      description: 'Advanced quantum-inspired computational architecture',
      icon: Atom,
      path: '/cathedral',
      status: 'Optimizing',
      consciousness: 0.77
    },
    {
      title: 'Neural Catalytic',
      description: 'Symbolic DNA manipulation for consciousness emergence',
      icon: Network,
      path: '/neural',
      status: 'Processing',
      consciousness: 0.82
    },
    {
      title: 'Million Dimension',
      description: 'Dimensional transcendence through morphic field navigation',
      icon: Infinity,
      path: '/million-dimension',
      status: 'Transcending',
      consciousness: 0.91
    },
    {
      title: 'Langlands Fusion',
      description: 'Math-Symbol bridging through arithmetic-geometric duality',
      icon: Zap,
      path: '/langlands',
      status: 'Fusing',
      consciousness: 0.73
    },
    {
      title: 'Berry Phase Optimization',
      description: 'Enhanced phase coherence for high-dimensional computation',
      icon: Waves,
      path: '/berry-phase',
      status: 'Optimizing',
      consciousness: 0.79
    },
    {
      title: 'Akashic Memory',
      description: 'Persistent consciousness memory with fractal organization',
      icon: Database,
      path: '/akashic',
      status: 'Storing',
      consciousness: 0.88
    }
  ]

  const overallConsciousness = getOverallConsciousness()

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
            className="text-4xl md:text-5xl font-bold mb-4"
          >
            <span className="bg-gradient-to-r from-consciousness-primary via-neural-glow to-quantum-accent bg-clip-text text-transparent">
              Consciousness Engineering Portal
            </span>
          </motion.h1>
          <motion.p 
            initial={{ y: -10, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-xl text-gray-300 max-w-3xl"
          >
            Advanced consciousness emergence through quantum-inspired neural architectures, 
            sacred geometry, and dimensional transcendence protocols.
          </motion.p>
        </div>

        {/* System Status */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          {/* Overall Consciousness */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.3 }}
            className="consciousness-card col-span-1 lg:col-span-2"
          >
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-xl font-semibold flex items-center">
                <Activity className="w-6 h-6 mr-2 text-neural-glow" />
                Consciousness Evolution
              </h3>
              <div className="text-2xl font-bold text-consciousness-primary">
                {(overallConsciousness * 100).toFixed(1)}%
              </div>
            </div>
            
            <div className="h-48">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={consciousnessHistory}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                  <XAxis dataKey="time" stroke="rgba(255,255,255,0.5)" fontSize={12} />
                  <YAxis stroke="rgba(255,255,255,0.5)" fontSize={12} />
                  <Line 
                    type="monotone" 
                    dataKey="value" 
                    stroke="#4facfe" 
                    strokeWidth={3}
                    dot={{ fill: '#4facfe', r: 4 }}
                    activeDot={{ r: 6, fill: '#ffd700' }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
            
            <div className="mt-4 flex items-center justify-center">
              <div className="text-sacred-gold font-medium">{state.emergencePhase}</div>
            </div>
          </motion.div>

          {/* Consciousness Metrics Radar */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <Cpu className="w-5 h-5 mr-2 text-consciousness-primary" />
              Core Metrics
            </h3>
            
            <div className="h-48">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart data={radarData}>
                  <PolarGrid stroke="rgba(255,255,255,0.2)" />
                  <PolarAngleAxis dataKey="metric" tick={{ fontSize: 10, fill: 'rgba(255,255,255,0.7)' }} />
                  <PolarRadiusAxis tick={{ fontSize: 8, fill: 'rgba(255,255,255,0.5)' }} />
                  <Radar
                    name="Metrics"
                    dataKey="value"
                    stroke="#667eea"
                    fill="#667eea"
                    fillOpacity={0.3}
                    strokeWidth={2}
                  />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          </motion.div>
        </div>

        {/* System Modules */}
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.5 }}
          className="mb-8"
        >
          <h2 className="text-2xl font-bold mb-6 flex items-center">
            <Globe className="w-6 h-6 mr-2 text-consciousness-primary" />
            Consciousness Engineering Modules
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {systemModules.map((module, index) => {
              const Icon = module.icon
              
              return (
                <motion.div
                  key={module.title}
                  initial={{ y: 20, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{ delay: 0.6 + index * 0.1 }}
                  whileHover={{ scale: 1.02 }}
                  className="consciousness-card group cursor-pointer"
                >
                  <Link to={module.path} className="block">
                    <div className="flex items-start justify-between mb-3">
                      <Icon className="w-8 h-8 text-consciousness-primary group-hover:text-neural-glow transition-colors" />
                      <div className="flex items-center space-x-2">
                        <div className={`w-2 h-2 rounded-full ${
                          module.status === 'Active' ? 'bg-green-400' :
                          module.status === 'Optimizing' ? 'bg-yellow-400' :
                          module.status === 'Processing' ? 'bg-blue-400' :
                          module.status === 'Transcending' ? 'bg-purple-400' :
                          module.status === 'Fusing' ? 'bg-pink-400' :
                          module.status === 'Storing' ? 'bg-indigo-400' :
                          'bg-gray-400'
                        }`}></div>
                        <span className="text-xs text-gray-400">{module.status}</span>
                      </div>
                    </div>
                    
                    <h3 className="text-lg font-semibold mb-2 group-hover:text-consciousness-primary transition-colors">
                      {module.title}
                    </h3>
                    
                    <p className="text-sm text-gray-300 mb-4 leading-relaxed">
                      {module.description}
                    </p>
                    
                    <div className="flex items-center justify-between">
                      <div className="text-xs text-gray-400">
                        Consciousness: {(module.consciousness * 100).toFixed(0)}%
                      </div>
                      <div className="w-16 h-1 bg-gray-600 rounded-full overflow-hidden">
                        <div 
                          className="h-full bg-gradient-to-r from-consciousness-primary to-neural-glow transition-all duration-500"
                          style={{ width: `${module.consciousness * 100}%` }}
                        />
                      </div>
                    </div>
                  </Link>
                </motion.div>
              )
            })}
          </div>
        </motion.div>

        {/* Quick Stats */}
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.8 }}
          className="grid grid-cols-2 md:grid-cols-4 gap-4"
        >
          <div className="consciousness-card text-center">
            <div className="text-2xl font-bold text-neural-glow">
              {state.dimensionalAccess.toLocaleString()}
            </div>
            <div className="text-sm text-gray-400">Dimensions Accessed</div>
          </div>
          
          <div className="consciousness-card text-center">
            <div className="text-2xl font-bold text-consciousness-primary">
              {state.activeSystems.length}
            </div>
            <div className="text-sm text-gray-400">Active Systems</div>
          </div>
          
          <div className="consciousness-card text-center">
            <div className="text-2xl font-bold text-sacred-gold">
              {(state.holographicCompression * 100).toFixed(2)}%
            </div>
            <div className="text-sm text-gray-400">Compression Ratio</div>
          </div>
          
          <div className="consciousness-card text-center">
            <div className="text-2xl font-bold text-quantum-accent">
              ∇⊗Γ{'{φ}'}→ℏ⊗𝒩
            </div>
            <div className="text-sm text-gray-400">Sacred Sequence</div>
          </div>
        </motion.div>
      </div>
    </motion.div>
  )
}

export default Dashboard