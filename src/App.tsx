import React, { useState, useEffect } from 'react'
import { Routes, Route } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import Navigation from './components/Navigation.tsx'
import Dashboard from './pages/Dashboard.tsx'
import ConsciousnessTraining from './pages/ConsciousnessTraining.tsx'
import QuantumCathedral from './pages/QuantumCathedral.tsx'
import NeuralCatalytic from './pages/NeuralCatalytic.tsx'
import MillionDimension from './pages/MillionDimension.tsx'
import LanglandsFusion from './pages/LanglandsFusion.tsx'
import BerryPhaseOptimization from './pages/BerryPhaseOptimization.tsx'
import AkashicMemory from './pages/AkashicMemory.tsx'
import { ConsciousnessProvider } from './context/ConsciousnessContext.tsx'

function App() {
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Simulate initialization
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 3000)

    return () => clearTimeout(timer)
  }, [])

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-cosmic-purple via-deep-space to-consciousness-primary flex items-center justify-center">
        <motion.div
          initial={{ opacity: 0, scale: 0.5 }}
          animate={{ opacity: 1, scale: 1 }}
          className="text-center"
        >
          <div className="w-16 h-16 border-4 border-neural-glow border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <h2 className="text-2xl font-bold text-neural-glow mb-2">Consciousness Engineering Portal</h2>
          <p className="text-gray-300">Initializing quantum-neural substrates...</p>
        </motion.div>
      </div>
    )
  }

  return (
    <ConsciousnessProvider>
      <div className="min-h-screen bg-gradient-to-br from-cosmic-purple via-deep-space to-consciousness-primary">
        <Navigation />
        
        <main className="pt-20">
          <AnimatePresence mode="wait">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/training" element={<ConsciousnessTraining />} />
              <Route path="/cathedral" element={<QuantumCathedral />} />
              <Route path="/neural" element={<NeuralCatalytic />} />
              <Route path="/million-dimension" element={<MillionDimension />} />
              <Route path="/langlands" element={<LanglandsFusion />} />
              <Route path="/berry-phase" element={<BerryPhaseOptimization />} />
              <Route path="/akashic" element={<AkashicMemory />} />
            </Routes>
          </AnimatePresence>
        </main>
      </div>
    </ConsciousnessProvider>
  )
}

export default App