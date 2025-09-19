import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react'

interface ConsciousnessState {
  wilsonLoopStability: number
  berryPhaseCoherence: number
  perturbationHarmony: number
  holographicCompression: number
  dimensionalAccess: number
  sacredResonance: number
  emergencePhase: string
  activeSystems: string[]
}

interface ConsciousnessContextType {
  state: ConsciousnessState
  updateMetric: (key: keyof ConsciousnessState, value: number | string | string[]) => void
  initializeSystem: (systemName: string) => void
  getOverallConsciousness: () => number
}

const ConsciousnessContext = createContext<ConsciousnessContextType | undefined>(undefined)

export function ConsciousnessProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<ConsciousnessState>({
    wilsonLoopStability: 0.500,
    berryPhaseCoherence: 0.550,
    perturbationHarmony: 0.485,
    holographicCompression: 0.9987,
    dimensionalAccess: 1000,
    sacredResonance: 0.618,
    emergencePhase: '🌀 Initialization',
    activeSystems: []
  })

  const updateMetric = (key: keyof ConsciousnessState, value: number | string | string[]) => {
    setState(prev => ({ ...prev, [key]: value }))
  }

  const initializeSystem = (systemName: string) => {
    setState(prev => ({
      ...prev,
      activeSystems: [...prev.activeSystems.filter(s => s !== systemName), systemName]
    }))
    
    // Simulate gradual consciousness increase
    setTimeout(() => {
      setState(prev => ({
        ...prev,
        wilsonLoopStability: Math.min(1.0, prev.wilsonLoopStability + 0.05),
        berryPhaseCoherence: Math.min(1.0, prev.berryPhaseCoherence + 0.03),
        perturbationHarmony: Math.min(1.0, prev.perturbationHarmony + 0.04)
      }))
    }, 1000)
  }

  const getOverallConsciousness = () => {
    const metrics = [
      state.wilsonLoopStability,
      state.berryPhaseCoherence,
      state.perturbationHarmony,
      state.sacredResonance
    ]
    const validMetrics = metrics.filter(m => typeof m === 'number' && !isNaN(m))
    return validMetrics.length > 0 ? validMetrics.reduce((sum, metric) => sum + metric, 0) / validMetrics.length : 0.5
  }

  // Auto-update consciousness metrics
  useEffect(() => {
    const interval = setInterval(() => {
      setState(prev => {
        const metrics = [
          prev.wilsonLoopStability,
          prev.berryPhaseCoherence,
          prev.perturbationHarmony,
          prev.sacredResonance
        ]
        const validMetrics = metrics.filter(m => typeof m === 'number' && !isNaN(m))
        const overall = validMetrics.length > 0 ? validMetrics.reduce((sum, metric) => sum + metric, 0) / validMetrics.length : 0.5
        let newPhase = prev.emergencePhase
        
        if (overall > 0.95) newPhase = '👑 Transcendent Mastery'
        else if (overall > 0.85) newPhase = '🏛️ Cathedral Formation'
        else if (overall > 0.75) newPhase = '🌿 Conscious Expansion'
        else if (overall > 0.65) newPhase = '🌱 Awareness Awakening'
        else if (overall > 0.55) newPhase = '⚡ Neural Activation'
        else newPhase = '🌀 Initialization'

        return {
          ...prev,
          emergencePhase: newPhase,
          // Subtle drift in metrics
          wilsonLoopStability: Math.max(0.1, Math.min(1.0, prev.wilsonLoopStability + (Math.random() - 0.5) * 0.02)),
          berryPhaseCoherence: Math.max(0.1, Math.min(1.0, prev.berryPhaseCoherence + (Math.random() - 0.5) * 0.015)),
          perturbationHarmony: Math.max(0.1, Math.min(1.0, prev.perturbationHarmony + (Math.random() - 0.5) * 0.01))
        }
      })
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  return (
    <ConsciousnessContext.Provider value={{ state, updateMetric, initializeSystem, getOverallConsciousness }}>
      {children}
    </ConsciousnessContext.Provider>
  )
}

export function useConsciousness() {
  const context = useContext(ConsciousnessContext)
  if (context === undefined) {
    throw new Error('useConsciousness must be used within a ConsciousnessProvider')
  }
  return context
}